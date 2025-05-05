import requests


def check_request(url):
    try:
        response = requests.get(url, timeout=5)

        if response.status_code // 100 in (1, 2, 3):
            print(f"Successful response from {url}:")
            print(f"Status-Code: {response.status_code}")
            print(f"Body: {response.text}\n")
        elif response.status_code // 100 in (4, 5):
            raise Exception(f"Error response {response.status_code} from {url}: {response.text}\n")
        return response

    except Exception as e:
        print(f"Error: {e}\n")


endpoints = [
    'https://httpstat.us/101',
    'https://httpstat.us/200',
    'https://httpstat.us/301',
    'https://httpstat.us/404',
    'https://httpstat.us/500'
]

print("Starting requests to https://httpstat.us")

for endpoint in endpoints:
    print(f"Making request to: {endpoint}")
    check_request(endpoint)

print("Program completed.")