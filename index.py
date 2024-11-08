import cv2
from fer import FER

emotion_detector = FER()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    emotions = emotion_detector.detect_emotions(frame)
    
    for emotion in emotions:
        box = emotion['box']
        emotion_label = max(emotion['emotions'], key=emotion['emotions'].get)
        
        cv2.rectangle(frame, (box[0], box[1]), (box[0] + box[2], box[1] + box[3]), (0, 255, 0), 2)
        cv2.putText(frame, emotion_label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    cv2.imshow('Emotions', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()