# University Payment Slip Generation and Sending Project

## Description

This project is a Python application designed to automate the process of generating and sending payment slips to university students. The system accesses the university's student portal online using the appropriate credentials, performs the necessary authentication, generates the upcoming payment slip, and then sends the generated slip to the payer's responsible party via Telegram, using the Chat ID and bot Token.

### Features

- **Access to the Student Portal:** The system connects to the university's student portal, logging in with provided credentials and accessing the specific section for generating payment slips.
- **Slip Generation:** After authentication, the system locates the upcoming payment slip and either downloads or generates it in PDF format.
- **Sending via Telegram:** Using the Telegram API, the system sends the generated payment slip to the Chat ID of the responsible payer through the bot configured with the provided Token.

### Technologies Used

- **Python:** The main programming language used to develop the application.
- **Selenium:** A library used for automating web navigation and interacting with the university portal.
- **PDF:** The file format used for the generated payment slip.
- **Telegram API:** Used to send the generated payment slip to the responsible payer via Telegram.

### Prerequisites

Before running the project, make sure you have the following:

- Python 3.12.4 installed
- Necessary Python libraries installed. Use the command `pip install -r requirements.txt` to install all dependencies.
- Valid credentials for the university's student portal.
- Chat ID and Telegram bot Token configured for sending messages.
