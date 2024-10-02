import os
import random
import shutil

label_dirs = {
    'A': 'D:/HK1 2024 2025/Deep Learning/BTL/Final/data preparation/DATA/A',
    'B': 'D:/HK1 2024 2025/Deep Learning/BTL/Final/data preparation/DATA/B',
    'C': 'D:/HK1 2024 2025/Deep Learning/BTL/Final/data preparation/DATA/C'
}

output_base_dir = 'D:/HK1 2024 2025/Deep Learning/BTL/Final/dataset'
splits = ['train', 'test', 'validate']

for split in splits:
    for label in label_dirs.keys():
        split_dir = os.path.join(output_base_dir, split, label)
        os.makedirs(split_dir, exist_ok=True)

train_ratio = 0.80
test_ratio = 0.10
validation_ratio = 0.10

for label, label_dir in label_dirs.items():
    all_images = [f for f in os.listdir(label_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]
    random.shuffle(all_images)
    
    total_images = len(all_images)
    train_count = int(total_images * train_ratio)
    test_count = int(total_images * test_ratio)
    validation_count = total_images - train_count - test_count

    train_images = all_images[:train_count]
    test_images = all_images[train_count:train_count + test_count]
    validation_images = all_images[train_count + test_count:]

    for image in train_images:
        shutil.copy(os.path.join(label_dir, image), os.path.join(output_base_dir, 'train', label, image))
    
    for image in test_images:
        shutil.copy(os.path.join(label_dir, image), os.path.join(output_base_dir, 'test', label, image))
    
    for image in validation_images:
        shutil.copy(os.path.join(label_dir, image), os.path.join(output_base_dir, 'validate', label, image))

print("Hoàn thành chia tập dữ liệu!")
