# telegram-gpt-bot
This project implements a Telegram bot that integrates with GPT-3 to provide intelligent responses to user queries. The bot can handle natural language queries, display typing indicators, and manage large responses by splitting them into smaller messages.

## Features

	•	Responds to user queries using GPT-3.
	•	Displays a typing indicator while processing requests.
	•	Splits large responses into manageable chunks for better readability.
	•	Configuration through environment variables.

## Getting Started

### Prerequisites

	•	Python 3.7+
	•	Telegram Bot API key
	•	GPT-3 API key
	•	python-telegram-bot library
	•	requests library
	•	python-dotenv library

### Installation

	1.	Clone the repository:
git clone https://github.com/jack-jackhui/telegram-gpt-bot.git
    
    2. Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

    3.	Install the required dependencies:

	4.	Set up environment variables:
Create a .env file in the root directory of the project with the following content:

### Usage

	1.	Run the bot:
	2.	Interact with the bot on Telegram by sending messages and receiving responses.

## Project Structure
	•	main.py: Entry point of the bot application.
	•	gpt_bot.py: Contains the bot logic and handlers.
	•	requirements.txt: Lists the Python dependencies.
	•	.env: Environment variables configuration file.
	•	README.md: Project documentation.

## Contributing

We welcome contributions to improve the Galapago GPT Telegram Bot. Please follow these steps to contribute:

	1.	Fork the repository.
	2.	Create a new branch (git checkout -b feature/your-feature-name).
	3.	Make your changes.
	4.	Commit your changes (git commit -am 'Add new feature').
	5.	Push to the branch (git push origin feature/your-feature-name).
	6.	Create a new Pull Request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgements

	•	python-telegram-bot
	•	requests
	•	python-dotenv
