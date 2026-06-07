import os
import face_recognition
import pickle
import numpy as np
from PIL import Image

def encode_students(directory='student_db/'):
    known_encodings = []
    known_metadata = []

    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created {directory}.")
        return

    print("Scanning and processing images...")

    for filename in os.listdir(directory):
        if filename.lower().endswith((".jpg", ".png", ".jpeg")):
            path = os.path.join(directory, filename)

            try:
                pil_img = Image.open(path).convert('RGB')
                img = np.array(pil_img, dtype='uint8')
                encodings = face_recognition.face_encodings(img)

                if len(encodings) > 0:
                    known_encodings.append(encodings[0])
                    metadata = os.path.splitext(filename)[0]
                    known_metadata.append(metadata)
                    print(f"Success: {metadata}")
                else:
                    print(f"No face found in: {filename}")

            except Exception as e:
                print(f"Error in {filename}: {str(e)}")

    if known_encodings:
        data = {
            "encodings": known_encodings,
            "metadata": known_metadata
        }

        with open("encodings.p", "wb") as f:
            pickle.dump(data, f)

        print("\nEncodings saved successfully to 'encodings.p'")
    else:
        print("\nEncoding failed. Please check the photos again.")

if __name__ == "__main__":
    encode_students()
