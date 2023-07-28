import requests
import json

def translate_text(text, target_language, api_key):
    url = "https://translation.googleapis.com/language/translate/v2"

    data = {
        'q': text,
        'target': target_language,
        'format': 'text',
        'key': api_key
    }

    response = requests.post(url, data=data)

    if response.status_code == 200:
        return response.json()['data']['translations'][0]['translatedText']
    else:
        print("Translation failed. Check your API key and quota.")


# Replace 'YOUR_API_KEY' with your actual API key
api_key = ""
translated_text = translate_text("Hello, World!", "es", api_key)
print(translated_text)

