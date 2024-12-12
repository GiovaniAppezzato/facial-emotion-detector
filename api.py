import requests
import threading

def send_emotion_to_api(workspace_id, emotion):
    try:
        payload = {"workspace_id": workspace_id, "emotion": emotion}
        response = requests.post(api_url, json=payload)

        if response.status_code == 200:
            print(f"Emotion sent successfully: {emotion}")
        else:
            print(f"Error sending emotion: {response.text}")
            
    except Exception as e:
        print(f"Error sending emotion: {e}")

def send_emotion_in_thread(workspace_id, emotion):
    thread = threading.Thread(target=send_emotion_to_api, args=(workspace_id, emotion))
    thread.start()