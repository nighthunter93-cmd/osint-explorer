```python
import requests
import json

# Function to get WHOIS information from a public WHOIS API
def get_whois_info(domain):
    # WHOIS API endpoint
    whois_api_url = f"https://jsonwhoisapi.com/api/v1/whois?identifier={domain}"
    
    # Make a request to the WHOIS API
    response = requests.get(whois_api_url, headers={"Authorization": "Token YOUR_API_TOKEN"})
    
    # Check if the request was successful
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching WHOIS data for {domain}: {response.status_code}")
        return None

# Function to extract and display relevant information from the WHOIS data
def display_whois_info(domain_info):
    if domain_info:
        print(f"Domain: {domain_info.get('domain', 'N/A')}")
        print(f"Registrar: {domain_info.get('registrar', 'N/A')}")
        print(f"Creation Date: {domain_info.get('created', 'N/A')}")
        print(f"Expiration Date: {domain_info.get('expires', 'N/A')}")
        print(f"Name Servers: {', '.join(domain_info.get('name_servers', [])) if domain_info.get('name_servers') else 'N/A'}")
    else:
        print("No information available.")

# Main function to run the OSINT project
def main():
    # Example domain for analysis
    domain = "example.com"
    
    print(f"Fetching WHOIS information for {domain}...\n")
    
    # Get WHOIS information
    whois_info = get_whois_info(domain)
    
    # Display the extracted information
    display_whois_info(whois_info)

# Entry point for the script
if __name__ == "__main__":
    main()
```
