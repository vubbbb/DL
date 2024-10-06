import cv2
import mediapipe as mp
import os

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_drawing = mp.solutions.drawing_utils

nameoflable = 'W'

output_dir = f'D:/HK1 2024 2025/Deep Learning/BTL/Final/dataset/validation/{nameoflable}'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

cap = cv2.VideoCapture(0)

img_count = 0
max_images = 100

padding = 0.5

while img_count < max_images:
    ret, frame = cap.read()
    if not ret:
        break
    
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    result = hands.process(frame_rgb)
    
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            h, w, c = frame.shape
            x_min = min([landmark.x for landmark in hand_landmarks.landmark]) * w
            x_max = max([landmark.x for landmark in hand_landmarks.landmark]) * w
            y_min = min([landmark.y for landmark in hand_landmarks.landmark]) * h
            y_max = max([landmark.y for landmark in hand_landmarks.landmark]) * h
            
            box_width = x_max - x_min
            box_height = y_max - y_min
            x_min = max(0, int(x_min - padding * box_width))
            x_max = min(w, int(x_max + padding * box_width))
            y_min = max(0, int(y_min - padding * box_height))
            y_max = min(h, int(y_max + padding * box_height))
            
            hand_image = frame[y_min:y_max, x_min:x_max]
            
            hand_image_resized = cv2.resize(hand_image, (128, 128))
            
            img_filename = os.path.join(output_dir, f'{nameoflable}_{img_count}.jpg')
            cv2.imwrite(img_filename, hand_image_resized)
            
            img_count += 1
            print(f'Đã chụp {img_count}/{max_images} ảnh')
    
    cv2.imshow('Hand Detection', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
