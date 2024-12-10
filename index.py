import cv2
from fer import FER
import requests
import time
import threading

emotion_detector = FER()

video = ""

last_emotion = None
last_emotion_time = 1
debounce_interval = 3

workspace_id = 1
api_url = "http://127.0.0.1:8001/api/v1/emotion"

cap = cv2.VideoCapture(video if video != "" else 0)

def translate_emotion(emotion: str) -> str:
    translations = {
        'angry': 'Raiva',
        'disgust': 'Nojo',
        'fear': 'Medo',
        'happy': 'Felicidade',
        'sad': 'Tristeza',
        'surprise': 'Surpresa',
        'neutral': 'Neutro',
    }
    return translations.get(emotion, '')

def send_emotion_to_api(workspace_id, emotion):
    try:
        payload = {"workspace_id": workspace_id, "emotion": emotion}
        response = requests.post(api_url, json=payload)
        if response.status_code == 200:
            print(f"Emoção enviada com sucesso: {emotion}")
        else:
            print(f"Erro ao enviar emoção: {response.status_code}")
    except Exception as e:
        print(f"Falha ao enviar emoção: {e}")

def send_emotion_in_thread(workspace_id, emotion):
    thread = threading.Thread(target=send_emotion_to_api, args=(workspace_id, emotion))
    thread.start()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    emotions = emotion_detector.detect_emotions(frame)
    
    for emotion in emotions:
        box = emotion['box']
        emotion_label = max(emotion['emotions'], key=emotion['emotions'].get)

        translated_emotion = translate_emotion(emotion_label)

        current_time = time.time()
        
        if emotion_label != last_emotion and (current_time - last_emotion_time) > debounce_interval:
            print(f"Emoção mudou para: {emotion_label}")
            send_emotion_in_thread(workspace_id, emotion_label)
            last_emotion = emotion_label
            last_emotion_time = current_time
        
        cv2.rectangle(frame, (box[0], box[1]), (box[0] + box[2], box[1] + box[3]), (0, 255, 0), 2)
        cv2.putText(frame, translated_emotion, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    cv2.imshow('Emotions', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()