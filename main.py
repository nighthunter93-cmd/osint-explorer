```python
import requests
from bs4 import BeautifulSoup

def fetch_ip_info(ip_address):
    """
    Fetches IP information from an online service.

    Args:
        ip_address (str): The IP address to look up.

    Returns:
        dict: Parsed JSON response containing IP information.
    """
    try:
        # API endpoint for IP information
        url = f"https://ipinfo.io/{ip_address}/json"
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data for {ip_address}: {e}")
        return None

def display_ip_info(ip_info):
    """
    Displays the IP information in a readable format.

    Args:
        ip_info (dict): The IP information to display.
    """
    if ip_info:
        print("IP Information:")
        for key, value in ip_info.items():
            print(f"{key.capitalize()}: {value}")
    else:
        print("No information available.")

def main():
    """
    Main function to execute the script.
    """
    ip_address = input("Enter an IP address to look up: ")
    ip_info = fetch_ip_info(ip_address)
    display_ip_info(ip_info)

if __name__ == "__main__":
    main()
```
