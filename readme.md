# URL Monitoring Service

![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)

URL Monitoring Service is a Python-based tool that allows you to monitor multiple websites for updates, unusual HTTP status codes, and service availability. It provides notifications through Discord and logs all events for your reference.

## Features

- **Website Monitoring**: Monitor multiple websites simultaneously.
- **Automatic Content Resolution**: Remove dynamic elements for accurate change detection.
- **HTTP Status Code Monitoring**: Get alerts for unusual HTTP status codes.
- **Discord Notifications**: Receive notifications through Discord webhooks.
- **Logging**: Log events to a file for future analysis.
- **Easy Setup**: Configure URLs, check intervals, and other settings in `config.py`.
- **Ping Time Display**: View response times of monitored websites.

## Upcoming Features

- **Custom Logging Configuration**: Configure log file name, logging level, and enable/disable logging.
- **Customizable Check Interval**: Set check intervals for different URLs or categories.
- **Security Measures**: Implement SSL certificate checks, certificate validation, or IP address filtering.
- **Web Service Status Monitoring**: Check if the website services (HTTP, FTP, etc.) are up or down.
- **Staggered Monitoring**: Distribute checks over time to reduce network/server load.

## Prerequisites

- Python 3.x

**You can automatically check and install the required modules by running the programm but if you want to do it mannuall just do this:**
**pip install beautifulsoup4** 


