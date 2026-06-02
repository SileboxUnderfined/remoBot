# remoBot

A Telegram bot designed for remote server management and monitoring via SSH. It allows you to execute commands, monitor system status, and manage multiple connections directly from your Telegram client.

Docker images available both from [GitHub](https://github.com/SileboxUnderfined/remoBot/pkgs/container/remobot) and [Gitlab](https://gitlab.com/SileboxUnderfined/remobot/container_registry)

## Main development at [Gitlab](https://gitlab.com/SileboxUnderfined/remoBot)

## Features
- **SSH Management:** Execute commands on remote servers securely.
- **Multi-host Support:** Manage multiple SSH connections.
- **Interactive UI:** Built with `aiogram-dialog` for a seamless user experience.
- **Fast and Efficient:** Powered by `asyncssh` and `uv` package manager.
- **Proxy Support** Supports HTTP(S) and SOCKS5 Proxy.

---

## Configuration

Before running the bot, you must provide your environment variables. Create a `.env` file in the root directory:

```env
BOT_TOKEN=your_telegram_bot_token_here
ALLOWED_IDS=12345678,87654321
PROXY_URL="socks5://user:password@ip:port" # or "http://user:password@ip:port" (even for https!!)
```

- `BOT_TOKEN`: The API token you received from [@Botfather](https://t.me/BotFather).
- `ALLOWED_IDS`: A comma-separated list of Telegram User IDs allowed to access the bot. **(NOW SUPPORT ONLY FOR 1 ALLOWED_ID!!!! DO NOT SEPARATE WITH COMMA)**
- `PROXY_URL`: SOCKS5 or HTTP(S) proxy URL. for HTTPS proxy url, use `http://` instead of `https://`
---

## Installation Methods

### 1. Using Docker (Recommended)
This is the easiest way to get started

1. **Install [Docker](https://docs.docker.com/engine/install/)**

2. **Create .env file and fill it as described in Configuration**

2. **Run the container**
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

    Or using `docker-compose.yml` and image from github registry:
    ```bash
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

    Or using `docker-compose.yml` and image from gitlab registry:
    ```bash
    services:
        remobot:
            image: registry.gitlab.com/sileboxunderfined/remobot
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
    --env-file .env
    -v $(pwd)/data:/app/data
    remobot:latest
    ```

    Or using [docker-compose.yml](docker-compose.yml):
    ```bash
    docker compose up -d --build
    ```

### 3. From Source
1. **Install [Python3.14](https://www.python.org)**

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
  uv run python -c src.main
  ```

---

## Persistent Data
The bot uses a SQLite database located in `/app/data/db.sqlite3` (inside the container). When using Docker or Docker Compose, ensure the `./data` directory is mounted to preserve your host connections and settings across restarts.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
