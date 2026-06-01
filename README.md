# remoBot

A Telegram bot designed for remote server management and monitoring via SSH. It allows you to execute commands, monitor system status, and manage multiple connections directly from your Telegram client.

## Features
- **SSH Management:** Execute commands on remote servers securely.
- **Multi-host Support:** Manage multiple SSH connections.
- **Interactive UI:** Built with `aiogram-dialog` for a seamless user experience.
- **Fast and Efficient:** Powered by `asyncssh` and `uv` package manager.

---

## Configuration

Before running the bot, you must provide your environment variables. Create a `.env` file in the root directory:

```env
BOT_TOKEN=your_telegram_bot_token_here
ALLOWED_IDS=12345678,87654321
```

- `BOT_TOKEN`: The API token you received from @BotFather.
- `ALLOWED_IDS`: A comma-separated list of Telegram User IDs allowed to access the bot.

---

## Installation Methods

### 1. From Source (using uv)
If you want to run the bot directly on your machine:

1.  **Install uv** (if not already installed):
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```
2.  **Sync dependencies:**
    ```bash
    uv sync
    ```
3.  **Run the bot:**
    ```bash
    uv run python -m src.main
    ```

### 2. Using Docker (Dockerfile)
To build and run the container manually:

1.  **Build the image:**
    ```bash
    docker build -t remobot:latest .
    ```
2.  **Run the container:**
    ```bash
    docker run -d \
      --name remobot_app \
      --env-file .env \
      -v $(pwd)/data:/app/data \
      remobot:latest
    ```

### 3. Using Docker Compose (Recommended)
This is the easiest way to manage the bot and its persistent data.

1.  **Start the bot:**
    ```bash
    docker-compose up -d
    ```
2.  **To rebuild and update:**
    ```bash
    docker-compose up -d --build
    ```

---

## Persistent Data
The bot uses a SQLite database located in `/app/data/db.sqlite3` (inside the container). When using Docker or Docker Compose, ensure the `./data` directory is mounted to preserve your host connections and settings across restarts.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
