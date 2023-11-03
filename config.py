# config.py
# URLs to monitor organized into categories
URLs = {
    'Category 1': [
        "https://example.com",
        "https://example.com",
    ],
    'Category 2': [
        "https://example.com",
    ],
    # Add more categories and URLs to monitor
}

# Check interval (in seconds)
CHECK_INTERVAL = 3600  # Every hour

# Customizable Check Interval for specific URLs or categories
CUSTOM_CHECK_INTERVAL = {
    "https://example.com": 1800,  # 30 minutes
    "Category 1": 7200,  # 2 hours
}

# Automatic content resolution for dynamic elements (CSS selectors)
AUTOMATIC_RESOLUTION = {
    "https://example.com": [
        ".ad-container",
        ".timestamp",
    ],
    "https://example.com": [
        ".sidebar",
    ],
    # Add more resolutions as needed
}

# HTTP status code monitoring
HTTP_STATUS_ALERTS = {
    "https://example.com": [404, 500],
    # Add more URLs and status codes for monitoring
}

# Display website service status
DISPLAY_SERVICE_STATUS = True

# Display website ping times
DISPLAY_PING_TIMES = True

# Custom Logging Configuration
LOGGING_ENABLED = True  # Set to False to disable logging
LOGGING_FILE = "monitor.log"  # Log file name
LOGGING_LEVEL = "INFO"  # Logging level (e.g., "INFO", "WARNING", "ERROR")
