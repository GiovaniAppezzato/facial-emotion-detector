import requests
import threading

# Environment variables
workspace_id = 1
api_url = "http://127.0.0.1:8001/api/v1/emotion"

def send_emotion_to_api(emotion):
    try:
        payload = {"workspace_id": workspace_id, "emotion": emotion}
        response = requests.post(api_url, json=payload)

        if response.status_code == 200:
            print(f"Emotion sent successfully: {emotion}")
        else:
            print(f"Error sending emotion: {response.text}")
            
    except Exception as e:
        print(f"Error sending emotion2 wadasdas: {e}")

def send_emotion_in_thread(emotion):
    thread = threading.Thread(target=send_emotion_to_api, args=(emotion,))
    thread.start()