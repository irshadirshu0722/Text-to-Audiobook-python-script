import requests

# Define the URL and headers
url = "https://play.ht/api/v2/tts"
headers = {
    "AUTHORIZATION": "Bearer 1a9ec063fb1c4281b2510acd6d4055af",
    "X-USER-ID": "iWSCBLGQzUhZIrYe3O9CpiZ6Ovj1",
    "accept": "text/event-stream",
    "content-type": "application/json",
}

# Define the request data as a dictionary
data = {
    "text": "hi i am irshad  ",
    "voice": "larry"
}

# Make the POST request
response = requests.post(url, headers=headers, json=data)

# Check the response
if response.status_code == 200:
    print("Request was successful")

    data = response.content
    data_str = data.decode('utf-8')
    start_index = data_str.find('"url":"') + len('"url":"')
    end_index = data_str.find('"}', start_index)
    audio_url = data_str[start_index:end_index][:-36]

    response = requests.get(audio_url)

    if response.status_code == 200:
        # Save the audio content to a file named "output.mp3"
        with open("output.mp3", "wb") as audio_file:
            audio_file.write(response.content)
        print("Audio file downloaded and saved as output.mp3")
    else:
        print(f"Failed to download audio with status code {response.status_code}")
else:
    print(f"Request failed with status code {response.status_code}")
    print(response.text)
