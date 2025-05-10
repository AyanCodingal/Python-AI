import cv2
import numpy as np

IMAGE_PATH = 'feature.jpg'  
WINDOW_NAME = 'Real-Time Color Filter'


current_filter = None   
intensity = 50         


if IMAGE_PATH == 0:
    cap = cv2.VideoCapture(0)
    get_frame = lambda: cap.read()[1]
else:
    img = cv2.imread(IMAGE_PATH)
    if img is None:
        raise IOError(f"Could not load image at '{IMAGE_PATH}'")
    get_frame = lambda: img.copy()

cv2.namedWindow(WINDOW_NAME)

print(__doc__ := """
Keys:
  r - apply red tint
  g - apply green tint
  b - apply blue tint
  n - no filter
  + - increase intensity (max 255)
  - - decrease intensity (min 0)
  q or ESC - quit
""")
print(__doc__)

while True:
    frame = get_frame()
    if frame is None:
        break

    b, g, r = cv2.split(frame.astype(np.int16))

    if current_filter == 'R':
        r = np.clip(r + intensity, 0, 255)
    elif current_filter == 'G':
        g = np.clip(g + intensity, 0, 255)
    elif current_filter == 'B':
        b = np.clip(b + intensity, 0, 255)


    filtered = cv2.merge([b, g, r]).astype(np.uint8)

    label = f"Filter: {current_filter or 'None'}   Intensity: {intensity}"
    cv2.putText(filtered, label, (10, 25),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)

    cv2.imshow(WINDOW_NAME, filtered)

    key = cv2.waitKey(30) & 0xFF
    if key == ord('q') or key == 27:
        break
    elif key == ord('r'):
        current_filter = 'R'
    elif key == ord('g'):
        current_filter = 'G'
    elif key == ord('b'):
        current_filter = 'B'
    elif key == ord('n'):
        current_filter = None
    elif key == ord('+') or key == ord('='):
        intensity = min(255, intensity + 10)
    elif key == ord('-') or key == ord('_'):
        intensity = max(0, intensity - 10)

if IMAGE_PATH == 0:
    cap.release()
cv2.destroyAllWindows()
