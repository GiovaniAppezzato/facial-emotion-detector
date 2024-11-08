import cv2

cap = cv2.VideoCapture(0)

# Only show the 
while True:
    ret, frame = cap.read()

    # Show the frame
    cv2.imshow('frame', frame)

    # Break the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()