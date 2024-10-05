import cv2
import numpy as np
from tensorflow.keras.models import load_model
import mediapipe as mp

# Tải lại mô hình đã huấn luyện
model = load_model('D:/HK1 2024 2025/Deep Learning/BTL/Final/models/CNN_1.keras')

# Khởi tạo thư viện MediaPipe để phát hiện bàn tay
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)  # Giới hạn phát hiện 1 bàn tay
mp_drawing = mp.solutions.drawing_utils

# Ánh xạ nhãn
label_map = {0: 'A', 1: 'B', 2: 'C'}

# Khởi tạo webcam
cap = cv2.VideoCapture(0)

padding = 0.5  # Tỷ lệ mở rộng vùng chứa bàn tay

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    if not ret:
        break
    
    # Chuyển khung hình sang RGB vì MediaPipe yêu cầu định dạng này
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Phát hiện bàn tay
    result = hands.process(frame_rgb)
    
    # Nếu phát hiện bàn tay
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Lấy bounding box của bàn tay
            h, w, c = frame.shape
            x_min = min([landmark.x for landmark in hand_landmarks.landmark]) * w
            x_max = max([landmark.x for landmark in hand_landmarks.landmark]) * w
            y_min = min([landmark.y for landmark in hand_landmarks.landmark]) * h
            y_max = max([landmark.y for landmark in hand_landmarks.landmark]) * h
            
            # Tính toán thêm viền ngoài (padding)
            box_width = x_max - x_min
            box_height = y_max - y_min
            x_min = max(0, int(x_min - padding * box_width))
            x_max = min(w, int(x_max + padding * box_width))
            y_min = max(0, int(y_min - padding * box_height))
            y_max = min(h, int(y_max + padding * box_height))
            
            # Cắt khung hình rộng hơn chứa bàn tay
            hand_image = frame[y_min:y_max, x_min:x_max]
            
            # Thay đổi kích thước ảnh về 256x256 để dự đoán
            hand_image_resized = cv2.resize(hand_image, (128, 128))
            
            # Chuẩn hóa ảnh và thêm trục để phù hợp với input của mô hình
            hand_image_resized = hand_image_resized / 255.0
            hand_image_resized = np.expand_dims(hand_image_resized, axis=0)
            
            # Dự đoán nhãn
            predictions = model.predict(hand_image_resized)
            predicted_label = np.argmax(predictions)
            predicted_class = label_map[predicted_label]
            
            #filp
            

            # Hiển thị kết quả dự đoán lên màn hình
            cv2.putText(frame, f'Prediction: {predicted_class}', (x_min, y_min-40), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
            
            # Vẽ các điểm và kết nối của bàn tay
            # mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    
    # Hiển thị khung hình với dự đoán
    
    cv2.imshow('Hand Detection and Prediction', frame)
    
    # Thoát khi nhấn phím 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng tài nguyên
cap.release()
cv2.destroyAllWindows()
