```python
import requests

def get_ip_info(ip_address):
    """
    Fetches IP information from an external API.
    
    Args:
        ip_address (str): The IP address to lookup.
    
    Returns:
        dict: Information about the IP address.
    """
    try:
        # Use the ipinfo.io API to get information about the IP
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return JSON data as a dictionary
    except requests.RequestException as e:
        print(f"Error fetching data for {ip_address}: {e}")
        return None

def display_ip_info(ip_info):
    """
    Displays the IP information in a formatted manner.
    
    Args:
        ip_info (dict): The IP address information.
    """
    if ip_info:
        print(f"IP Address: {ip_info.get('ip', 'N/A')}")
        print(f"Hostname: {ip_info.get('hostname', 'N/A')}")
        print(f"City: {ip_info.get('city', 'N/A')}")
        print(f"Region: {ip_info.get('region', 'N/A')}")
        print(f"Country: {ip_info.get('country', 'N/A')}")
        print(f"Location: {ip_info.get('loc', 'N/A')}")
        print(f"Organization: {ip_info.get('org', 'N/A')}")
    else:
        print("No information available.")

def main():
    """
    Main function to execute the script's functionality.
    """
    ip_address = input("Enter an IP address to look up: ")
    ip_info = get_ip_info(ip_address)
    display_ip_info(ip_info)

if __name__ == "__main__":
    main()
```