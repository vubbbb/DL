import os
from PIL import Image
import random

# Đường dẫn tới các thư mục
folders = ['D:/HK1 2024 2025/Deep Learning/BTL/Final/dataset/test/A', 'D:/HK1 2024 2025/Deep Learning/BTL/Final/dataset/test/B', 'D:/HK1 2024 2025/Deep Learning/BTL/Final/dataset/test/C']
output_folder = 'augmented'  # Thư mục để lưu ảnh đã tăng cường

# Tạo thư mục đầu ra nếu chưa tồn tại
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Xoay ảnh
def rotate_images(folder):
    for filename in os.listdir(folder):
        if filename.endswith('.jpg') or filename.endswith('.png'):  # Kiểm tra định dạng ảnh
            img_path = os.path.join(folder, filename)
            img = Image.open(img_path)
            
            # Tạo một góc xoay ngẫu nhiên từ -5 đến 5 độ
            angle = random.uniform(-5, 5)
            rotated_img = img.rotate(angle)

            # Lưu ảnh đã xoay
            rotated_img.save(os.path.join(output_folder, f'rotated_{filename}'))

# Xoay ảnh trong từng thư mục
for folder in folders:
    rotate_images(folder)

print("Tăng cường dữ liệu hoàn tất!")
