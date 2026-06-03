import src.settings
from src.settings import settings, SSHAuthType
import asyncssh
from src.models.host import Host
from .exceptions import SSHConnectionError, SSHError
from typing import Optional, Any
from dataclasses import dataclass
from os import environ

@dataclass
class SSHOperationResult:
    success: bool
    result: Optional[str] = None


class SSHConnection:
    def __init__(self, host: Host):
        self._host: Host = host
        self._conn: Optional[asyncssh.SSHClientConnection] = None

    async def __aenter__(self) -> SSHConnection:
        conn_kwargs: dict[str, Any] = {
            "host": self._host.hostname,
            "port": self._host.port,
            "username": self._host.username,
            "known_hosts": None
        }

        auth_specified: bool = False
        if self._host.password:
            conn_kwargs['password'] = self._host.password
        else:
            for auth_type in settings.SSH_AUTH_METHODS:
                match auth_type:
                    case SSHAuthType.SSH_AGENT:
                        if settings.SSH_AGENT_PATH is None: continue
                        conn_kwargs['agent_path'] = settings.SSH_AGENT_PATH
                        conn_kwargs['client_keys'] = []
                        auth_specified = True
                        break

                    case SSHAuthType.SSH_AGENT_ENVIRONMENT:
                        if environ.get('SSH_AUTH_SOCK') is None: continue
                        auth_specified = True
                        break

                    case SSHAuthType.SSH_KEYS:
                        if settings.SSH_KEYS_PATH is None: continue
                        conn_kwargs['agent_path'] = None
                        conn_kwargs['client_keys'] = settings.SSH_KEYS_PATH
                        auth_specified = True
                        break
                        
        if not auth_specified:
            raise SSHConnectionError("You must specify either a password, or SSH_AGENT_PATH, or SSH_KEYS_PATH")
        
        try:
            self._conn = await asyncssh.connect(**conn_kwargs)
            return self
                    
        except asyncssh.Error as e:
            raise SSHConnectionError(f"failed to connect to {self._host.label}: {e}")

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self._conn is not None:
            self._conn.close()
            
            await self._conn.wait_closed()
            
            self._conn = None

    async def execute_command(self, command: str) -> str:
        if self._conn is None:
            raise RuntimeError("execute_command must be called inside 'async with SSHConnection(...)'")

        try:
            result = await self._conn.run(command)

            if result.exit_status != 0:
                raise SSHError(f"Command failed: {result.stderr}")

            if result.stdout is None: 
                return ""
            elif isinstance(result.stdout, bytes):
                return result.stdout.decode("utf-8")
            elif isinstance(result.stdout, str):
                return result.stdout
                
        except asyncssh.Error as e:
            raise SSHConnectionError(f"error while executing command: {e}")

    @staticmethod
    async def check_connection(ssh_conn: SSHConnection) -> SSHOperationResult:
        try:
            await ssh_conn.execute_command("echo 1")
            return SSHOperationResult(True)
        except (SSHConnectionError, SSHError, Exception) as e:
            return SSHOperationResult(False, str(e))