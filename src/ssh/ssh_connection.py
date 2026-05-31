import asyncssh
from src.models.host import Host
from .exceptions import SSHConnectionError, SSHError
from typing import Optional
from dataclasses import dataclass

@dataclass
class SSHOperationResult:
    success: bool
    result: Optional[str] = None


class SSHConnection:
    def __init__(self, host: Host):
        self._host: Host = host
        self._conn: Optional[asyncssh.SSHClientConnection] = None

    async def __aenter__(self) -> SSHConnection:
        try:
            self._conn = await asyncssh.connect(
                host=self._host.hostname,
                port=self._host.port,
                username=self._host.username,
                password=self._host.password,
                known_hosts=None
            )
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

    async def check_connection(self) -> SSHOperationResult:
        try:
            async with self:
                await self.execute_command("echo 1")
        except (SSHError,SSHConnectionError,Exception) as e:
            return SSHOperationResult(False,str(e))

        return SSHOperationResult(True)