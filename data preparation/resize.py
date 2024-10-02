import os
import cv2

def resize_images_in_folder(folder, size=(128, 128)):
    files = os.listdir(folder)
    
    for idx, filename in enumerate(files):
        img_path = os.path.join(folder, filename)
        
        img = cv2.imread(img_path)
        
        if img is not None:
            resized_img = cv2.resize(img, size)
            
            new_filename = f"{idx + 1}.jpg"
            new_img_path = os.path.join(folder, new_filename)
            
            cv2.imwrite(new_img_path, resized_img)
            
            os.remove(img_path)

folder_path = 'hand_images/Luan_C'

resize_images_in_folder(folder_path)