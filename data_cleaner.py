import cv2
import os
import numpy as np

# Folder ka path define karo
DB_FOLDER = 'student_db/'

def sanitize_dataset():
    print(f"🚀 Starting Data Sanitization in '{DB_FOLDER}'...")
    count = 0
    
    # Folder check karo
    if not os.path.exists(DB_FOLDER):
        print(f"❌ Error: Folder '{DB_FOLDER}' nahi mila!")
        return

    # Har file ko loop mein check karo
    for filename in os.listdir(DB_FOLDER):
        if filename.lower().endswith((".jpg", ".png", ".jpeg")):
            img_path = os.path.join(DB_FOLDER, filename)
            
            try:
                # 1. Photo ko OpenCV se read karo (Ye header thik karne ki koshish karega)
                img = cv2.imread(img_path)
                
                if img is None:
                    print(f"⚠️ Warning: {filename} read nahi ho payi. Skipping.")
                    continue
                
                # 2. (Optional but Good) Force convert to standard RGB just to be sure
                # OpenCV reads as BGR, let's ensure it's a clean BGR array before saving
                img_clean = np.array(img, dtype=np.uint8)

                # 3. Wapas overwrite karo (Is step mein saara purana metadata udd jayega)
                # Quality 95% rakhenge taaki chehra saaf rahe
                cv2.imwrite(img_path, img_clean, [cv2.IMWRITE_JPEG_QUALITY, 95])
                
                print(f"✅ Cleaned: {filename}")
                count += 1
                
            except Exception as e:
                print(f"❌ Error processing {filename}: {e}")
                
    print(f"\n✨ Sanitization Complete! Total {count} photos cleaned.")
    print("👉 Ab tum 'python encoder.py' chala sakte ho.")

if __name__ == "__main__":
    sanitize_dataset()