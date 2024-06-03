## dracobot2

### System Requirements

1. Python (>= 3.8.10)
1. Pip (>= 21.2.4)
1. MariaDB (>= 10.3.9) (or MySQL)
1. virtualenv (>= 20.8.1) (if setting up project in virtual environment)

### Setting up in Virtual Environment

 1. Setup virtual environment
    ```
    $ python -m venv venv
    ```

 2. Activate virtual environment
    ```
    $ source venv/bin/activate
    ```

 3. Update pip to latest version
    ```
    $ python -m pip install --upgrade pip
    ```

 4. Repeat the above steps to set up the project in the virtual environment
    Run the following code to deactivate the virtual environment
    ```
    $ deactivate
    ```

 Note: Run all future commands after activating virtual environment to ensure consistencies

### Getting Started

 1. Install Python dependencies

    ```
    $ pip install -r requirements.txt
    ```

 2. Install additional Python Telegram Bot dependency (for job queue)

    ```
    $ pip install python-telegram-bot[job-queue]
    ```

 3. Create the environment file (make a copy of `env.sample` and rename it to `.env`).
    Add the details for each environment variable.

    ```
    TELEGRAM_BOT_TOKEN=<put_your_telegram_bot_token_here>
    ```

 4. Create database
    ```
    $ python setup.py
    ```

 5. Run the python telegram server
    ```
    $ python main.py
    ```
