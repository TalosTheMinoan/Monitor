try:
    from bs4 import BeautifulSoup
except ImportError:
    print("Beautiful Soup is not installed. Attempting to download and install...")

    try:
        import pip
        from subprocess import call
        call("pip install beautifulsoup4", shell=True)
        print("Beautiful Soup has been successfully installed. You're all set!")
        from bs4 import BeautifulSoup  # Check if Beautiful Soup is now installed
    except ImportError:
        print("Failed to install Beautiful Soup. Please install it manually using 'pip install beautifulsoup4'.")
        exit()

import config
import requests
import time
from datetime import datetime
from bs4 import BeautifulSoup  # Import Beautiful Soup again

# Log file setup
import logging

log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(filename='monitor.log', level=logging.INFO, format=log_format)

# Function to send notifications to Discord
def send_discord_notification(message):
    discord_data = {
        "content": message
    }

    try:
        response = requests.post(config.DISCORD_WEBHOOK_URL, json=discord_data)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error sending Discord notification: {e}")

def check_url(url, categories, resolutions, http_status_alerts):
    try:
        response = requests.get(url)
        response.raise_for_status()
        page_content = response.text
        soup = BeautifulSoup(page_content, 'html.parser')

        # Apply automatic content resolution
        if url in resolutions:
            for selector in resolutions[url]:
                for tag in soup.select(selector):
                    tag.decompose()

        # Check for updates
        current_content = str(soup)
        if url in categories:
            if current_content != categories[url]:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"[{timestamp}] Web Page Updated: {url}")
                categories[url] = current_content
                # Log update events
                logging.info(f"Web Page Updated: {url}")
                # Send Discord notification for updates
                send_discord_notification(f"Web Page Updated: {url}")
        else:
            categories[url] = current_content

        # HTTP status code monitoring
        if url in http_status_alerts and response.status_code in http_status_alerts[url]:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{timestamp}] Unusual HTTP Status Code ({response.status_code}) for: {url}")
            # Log status code alerts
            logging.warning(f"Unusual HTTP Status Code ({response.status_code}) for: {url}")
            # Send Discord notification for status code alerts
            send_discord_notification(f"Unusual HTTP Status Code ({response.status_code}) for: {url}")

        # Check if the website service is up
        if response.status_code == 200:
            print(f"{url} is up")
        else:
            print(f"{url} is down")
            # Log service status
            logging.warning(f"{url} is down")
            # Send Discord notification for service status changes
            send_discord_notification(f"{url} is down")

        # Display the ping time
        ping_time = response.elapsed.total_seconds()
        print(f"Ping time for {url}: {ping_time:.2f} seconds")
        # Log ping times
        logging.info(f"Ping time for {url}: {ping_time:.2f} seconds")

    except requests.exceptions.RequestException as e:
        print(f"Error checking {url}: {e}")
        print(f"{url} is down")
        # Log errors and service status
        logging.error(f"Error checking {url}: {e}")
        logging.warning(f"{url} is down")
        # Send Discord notification for errors and service status changes
        send_discord_notification(f"Error checking {url}: {e}\n{url} is down")

def display_setup_message():
    print("URL Monitoring Service (Under Development)")
    print("Setting up some things... (This may take a moment)")
    time.sleep(10)  # Add a 10-second delay for setup
    print("Simulating setup tasks...")
    time.sleep(5)  # Simulate additional setup tasks
    print("Monitoring the following URLs:")
    for category, urls in config.URLs.items():
        print(f"{category}:")
        for url in urls:
            print(f"- {url}")
    print(f"Checking every {config.CHECK_INTERVAL / 60} minutes")
    print("Feel free to improve and customize this system for your needs.")

display_setup_message()

categories = {}  # Store the last retrieved content for each URL

while True:
    for category, urls in config.URLs.items():
        for url in urls:
            check_url(url, categories, config.AUTOMATIC_RESOLUTION, config.HTTP_STATUS_ALERTS)
    time.sleep(config.CHECK_INTERVAL)
