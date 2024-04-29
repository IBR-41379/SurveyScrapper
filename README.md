
# Survey Information Scraper

This Python script is used to scrape land survey information from the Dharani Telangana website.

## Requirements

- Python 3.7 or higher
- BeautifulSoup4
- requests

## Installation

1. Install Python 3.7 or higher if you haven't already. You can download it from the official website: https://www.python.org/downloads/

2. Install the required Python packages using pip. Open a terminal and run the following command:

```bash
pip install beautifulsoup4 requests
```

## Usage

1. Run the script using Python:

```bash
python sc.py
```

2. Follow the prompts in the terminal to select the district, mandal, and village for which you want to get the land survey information.

3. The script will print the survey numbers for the selected location.

## Code Explanation

The script first sends a GET request to the Dharani Telangana website to get the list of districts. It then prompts the user to select a district, and sends another GET request to get the list of mandals in that district. The user is then prompted to select a mandal, and another GET request is sent to get the list of villages in that mandal. Finally, the user is prompted to select a village, and a final GET request is sent to get the list of survey numbers in that village.

The script uses the BeautifulSoup library to parse the HTML content of the responses and extract the required information. The requests library is used to send the HTTP requests.

## Note

This script is intended for educational purposes only. Please use it responsibly and respect the terms of use of the Dharani Telangana website.
