import os
from PIL import Image

# Đường dẫn đến 3 thư mục chứa ảnh
dirs = ['A_right', 'B_right', 'C_right']


# Duyệt qua từng thư mục
for dir_path in dirs:
    # Số thứ tự bắt đầu
    counter = 1
    # Thư mục để lưu ảnh đã đổi tên
    output_dir = F'DATA/{dir_path}_renamed'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for filename in os.listdir(dir_path):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(dir_path, filename)
            
            # Đặt tên mới cho ảnh theo số thứ tự
            new_filename = f'{counter}.jpg'
            output_path = os.path.join(output_dir, new_filename)
            
            # Mở và lưu ảnh với tên mới
            img = Image.open(image_path)
            img.save(output_path)
            
            # Tăng số thứ tự
            counter += 1

print("Hoàn thành đổi tên tất cả các ảnh!")
