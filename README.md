# remoBot

A Telegram bot designed for remote server management and monitoring via SSH. It allows you to execute commands, monitor system status, and manage multiple connections directly from your Telegram client.

Docker images available both from [GitHub](https://github.com/SileboxUnderfined/remoBot/pkgs/container/remobot) and [Gitlab](https://gitlab.com/SileboxUnderfined/remobot/container_registry)

## Main development at [Gitlab](https://gitlab.com/SileboxUnderfined/remoBot)

## Features
- **SSH Management:** Execute commands on remote servers securely.
- **Authentication Methods:** Support for Password, SSH Agent, and Private Keys.
- **Multi-host Support:** Manage multiple SSH connections.
- **Interactive UI:** Built with `aiogram-dialog` for a seamless user experience.
- **Fast and Efficient:** Powered by `asyncssh` and `uv` package manager.
- **Proxy Support:** Supports HTTP(S) and SOCKS5 Proxy.

---

## Configuration

Before running the bot, you must provide your environment variables. Create a `.env` file in the root directory:

```env
BOT_TOKEN=your_telegram_bot_token_here
ALLOWED_IDS=12345678,87654321
PROXY_URL="socks5://user:password@ip:port" # or "http://user:password@ip:port" (even for https!!)

# --- SSH Authentication Settings (Optional) ---
# Comma-separated list of preferred auth methods order if authenticating without password: ssh_agent, ssh_agent_environment, ssh_keys
SSH_AUTH_METHODS=ssh_agent,ssh_agent_environment,ssh_keys
# Path to the SSH agent socket (required if using ssh_agent)
SSH_AGENT_PATH="/run/ssh-agent"
# Comma-separated list of paths to private keys (required if using ssh_keys)
SSH_KEYS_PATH="/app/keys/id_rsa,/app/keys/id_ed25519"
```

- `BOT_TOKEN`: The API token you received from [@Botfather](https://t.me/BotFather).
- `ALLOWED_IDS`: A comma-separated list of Telegram User IDs allowed to access the bot. 
- `PROXY_URL`: SOCKS5 or HTTP(S) proxy URL. For HTTPS proxy url, use `http://` instead of `https://`.
- `SSH_AUTH_METHODS`: Priority order for authentication methods. Default: `ssh_agent,ssh_agent_environment`.
- `SSH_AGENT_PATH`: Explicit path to the SSH agent socket.
- `SSH_KEYS_PATH`: List of paths to private keys to use for authentication.

---

## SSH Authentication & Docker

### Using SSH Agent
To use your host's SSH agent inside the Docker container, you need to mount the socket and set the environment variable.

**Docker Run:**
```bash
docker run -d \
  --name remobot_app \
  -v $SSH_AUTH_SOCK:/run/ssh-agent \
  -e SSH_AUTH_SOCK=/run/ssh-agent \
  --env-file .env \
  -v $(pwd)/data:/app/data \
  ghcr.io/sileboxunderfined/remobot:main
```
*Note: In this case, you can use `SSH_AUTH_METHODS=ssh_agent_environment` in your `.env`.*

**Docker Compose:**
```yaml
services:
  remobot:
    # ...
    volumes:
      - ${SSH_AUTH_SOCK}:/run/ssh-agent
      - ./data:/app/data
    environment:
      - SSH_AUTH_SOCK=/run/ssh-agent
```

### Using Private Keys
To use specific private keys, mount them as files (preferably read-only) and specify their paths.

**Docker Run:**
```bash
docker run -d \
  --name remobot_app \
  -v ~/.ssh/id_rsa:/app/keys/id_rsa:ro \
  --env-file .env \
  -e SSH_KEYS_PATH=/app/keys/id_rsa \
  -v $(pwd)/data:/app/data \
  ghcr.io/sileboxunderfined/remobot:main
```

**Docker Compose:**
```yaml
services:
  remobot:
    # ...
    volumes:
      - ~/.ssh/id_rsa:/app/keys/id_rsa:ro
      - ./data:/app/data
    environment:
      - SSH_KEYS_PATH=/app/keys/id_rsa
      - SSH_AUTH_METHODS=ssh_keys
```

---

## Installation Methods

### 1. Using Docker (Recommended)
This is the easiest way to get started.

1. **Install [Docker](https://docs.docker.com/engine/install/)**

2. **Create .env file and fill it as described in Configuration**

3. **Run the container**
    using image from github registry:
    ```bash
    docker run -d \
    --name remobot_app \
    --env-file .env \
    -v $(pwd)/data:/app/data \
    ghcr.io/sileboxunderfined/remobot:main
    ```

    Or using image from gitlab registry:
    ```bash
    docker run -d \
    --name remobot_app \
    --env-file .env \
    -v $(pwd)/data:/app/data \
    registry.gitlab.com/sileboxunderfined/remobot
    ```

    Or using `docker-compose.yml`:
    ```yaml
    services:
        remobot:
            image: ghcr.io/sileboxunderfined/remobot:main
            container_name: remobot_app
            restart: unless-stopped
            env_file:
                - .env
            volumes:
                - ./data:/app/data
    ```

### 2. Building Docker from Source

1. **Install [Docker](https://docs.docker.com/engine/install/)**

2. **[Download](https://gitlab.com/SileboxUnderfined/remobot/-/archive/main/remobot-main.zip?ref_type=heads) or clone repository**
  ```bash
  git clone https://gitlab.com/SileboxUnderfined/remobot.git
  ```

3. **Build and run manually:**
    ```bash
    docker build -t remobot:latest .
    
    docker run -d \
    --name remobot_app \
    --env-file .env \
    -v $(pwd)/data:/app/data \
    remobot:latest
    ```

    Or using [docker-compose.yml](docker-compose.yml):
    ```bash
    docker compose up -d --build
    ```

### 3. From Source
1. **Install [Python 3.14](https://www.python.org)**

2. **Install [uv](https://docs.astral.sh/uv/getting-started/installation/)**

3. **[Download](https://gitlab.com/SileboxUnderfined/remobot/-/archive/main/remobot-main.zip?ref_type=heads) or clone repository**
  ```bash
  git clone https://gitlab.com/SileboxUnderfined/remobot.git
  ```

4. **Create .env file and fill it as described in Configuration**

5. **Sync dependencies**
  ```bash
  uv sync
  ```

6. **Run**
  ```bash
  uv run python -m src.main
  ```

---

## Persistent Data
The bot uses a SQLite database located in `/app/data/db.sqlite3` (inside the container). When using Docker or Docker Compose, ensure the `./data` directory is mounted to preserve your host connections and settings across restarts.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
