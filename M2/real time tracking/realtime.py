import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from google.colab import files
from matplotlib import pyplot as plt

# --- Prompt user to upload both model and image ---
print("Please upload your 'emotion_model.h5' AND at least one image file (jpg/png/jpeg).")
uploaded = files.upload()

# --- Check uploads ---
if 'emotion_model.h5' not in uploaded:
    raise FileNotFoundError(
        "You must upload 'emotion_model.h5'.\n"
        "Run the upload cell again and select your model file."
    )

# pick the first image-like file
image_keys = [k for k in uploaded.keys() if k.lower().endswith(('.jpg', '.jpeg', '.png'))]
if not image_keys:
    raise FileNotFoundError(
        "No image file found in upload—please upload a .jpg, .jpeg, or .png image."
    )
image_path = image_keys[0]

# --- Load face detector and emotion model ---
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)
emotion_model = load_model('emotion_model.h5')

# --- Define emotion labels ---
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

# --- Read and preprocess the image ---
image = cv2.imread(image_path)
if image is None:
    raise IOError(f"Could not load image at '{image_path}'")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# --- Detect faces ---
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

# --- For each face, predict emotion and annotate ---
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    roi_gray = gray[y:y+h, x:x+w]
    roi = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)
    roi = roi.astype("float") / 255.0
    roi = img_to_array(roi)
    roi = np.expand_dims(roi, axis=0)

    preds = emotion_model.predict(roi)[0]
    idx = np.argmax(preds)
    label = emotion_labels[idx]
    conf = preds[idx]

    text = f"{label}: {conf*100:.1f}%"
    cv2.putText(
        image, text, (x, y - 10),
        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2
    )

# --- Display the result ---
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(8, 6))
plt.imshow(image_rgb)
plt.axis('off')
plt.show()
