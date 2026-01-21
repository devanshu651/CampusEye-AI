import cv2
import os
import numpy as np
DB_FOLDER = 'student_db/'
def sanitize_dataset():
    print(f"🚀 Starting Data Sanitization in '{DB_FOLDER}'...")
    count = 0
    
    if not os.path.exists(DB_FOLDER):
        print(f"❌ Error: Folder '{DB_FOLDER}' nahi mila!")
        return
        
    for filename in os.listdir(DB_FOLDER):
        if filename.lower().endswith((".jpg", ".png", ".jpeg")):
            img_path = os.path.join(DB_FOLDER, filename)
            
            try:
                img = cv2.imread(img_path)
                
                if img is None:
                    print(f"⚠️ Warning: {filename} read nahi ho payi. Skipping.")
                    continue
                
                img_clean = np.array(img, dtype=np.uint8)
                cv2.imwrite(img_path, img_clean, [cv2.IMWRITE_JPEG_QUALITY, 95])
                
                print(f"✅ Cleaned: {filename}")
                count += 1
                
            except Exception as e:
                print(f"❌ Error processing {filename}: {e}")
                
    print(f"\n✨ Sanitization Complete! Total {count} photos cleaned.")
    print("👉 Ab tum 'python encoder.py' chala sakte ho.")

if __name__ == "__main__":

    sanitize_dataset()
