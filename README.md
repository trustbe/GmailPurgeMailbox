# Gmail Email Deletion Scripts

## Overview
This repository contains two Python scripts designed to automate the deletion of emails from a Gmail account. One script uses the Selenium WebDriver for automation via a browser interface, and the other employs the POP3 protocol for direct server interaction.

## Scripts Description

1. **Selenium-based Email Deletion Script**
   - **Language**: Python
   - **Dependencies**: Selenium, webdriver_manager
   - **Functionality**: Automates a browser to log into Gmail, select all emails, and delete them, mimicking the manual process of email deletion through a web browser interface.

2. **POP3-based Email Deletion Script**
   - **Language**: Python
   - **Dependencies**: poplib
   - **Functionality**: Connects to the Gmail server using the Post Office Protocol version 3 (POP3) and deletes all emails in the mailbox. It is a direct and efficient method to clear emails from the server.

## Usage

### Selenium Script

1. Ensure Python is installed on your system.
2. Install required libraries: `pip install selenium webdriver_manager`.
3. Replace the placeholder username and password in the script with your actual Gmail credentials.
4. Run the script: `python purge_selenium.py --username "XYZ" --password "XYZ"`.

**Note**: Google 2FA should be disabled for this script to work.

### POP3 Script

1. Ensure Python is installed on your system.
2. Replace the placeholder email and password in the script with your actual Gmail credentials.
3. Run the script: `python pop3_gmail_deletion.py`.

**Important**: This script will delete all emails in the specified account. Use it with caution.

## Disclaimer

These scripts are provided for educational purposes. Please use them responsibly and at your own risk. Ensure you comply with Gmail's terms of service and understand the implications of bulk email deletion, especially since these actions are irreversible.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
