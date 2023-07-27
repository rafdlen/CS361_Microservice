import requests


def send_max_value_to_microservice(max_val):
    url = "http://localhost:5000/generate"
    payload = {
        "max": str(max_val)
    }
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        return response.json()['random_number']
    else:
        return "Failed to generate random number: ", response.json()['error']


if __name__ == "__main__":
    max_val = 100000
    print(send_max_value_to_microservice(max_val))
