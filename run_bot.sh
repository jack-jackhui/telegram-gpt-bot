#!/bin/bash

# Navigate to the directory where the script is located
cd "$(dirname "$0")"

# Activate the virtual environment
source venv/bin/activate

# Run the Telegram bot
python main.py

# Deactivate the virtual environment (optional)
deactivate