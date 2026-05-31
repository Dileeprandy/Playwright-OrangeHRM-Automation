import requests
from requests.exceptions import RequestException

def check_application_health(url):
    """Checks the HTTP status code of a given URL to determine application health."""
    print(f"Target Application: {url}")
    print("-" * 50)
    
    try:
        # Send a GET request to the application with a 10-second timeout
        response = requests.get(url, timeout=10)
        
        # A 200 HTTP status code means "OK"
        if response.status_code == 200:
            print(f"[STATUS: UP] The application is functioning correctly.")
            print(f"[DETAILS] HTTP Status Code returned: {response.status_code}")
        else:
            print(f"[STATUS: DOWN] The application returned an unexpected response.")
            print(f"[DETAILS] HTTP Status Code returned: {response.status_code}")
            
    except RequestException as e:
        # This catches connection errors, timeouts, or DNS failures
        print(f"[STATUS: DOWN] The application is unavailable or not responding.")
        print(f"[ERROR] {e}")

if _name_ == "_main_":
    # Using the OrangeHRM URL provided in the assessment instructions
    app_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    check_application_health(app_url)