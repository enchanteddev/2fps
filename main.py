import cv2
from PIL import Image
import numpy as np

def add_images(i1: np.ndarray, i2: np.ndarray):
    new_img = (i1 / 2 + i2 / 2).astype(np.uint8)
    return new_img


vid = cv2.VideoCapture(input("Enter Input File Name > "))
fps = vid.get(cv2.CAP_PROP_FPS)

success, prev = vid.read()
print(f'{fps = } and res =', prev.shape[:2])

fourcc = cv2.VideoWriter_fourcc(*'XVID') # type: ignore
out = cv2.VideoWriter(input("Enter Output File Name (without file extention) > ") + ".avi", fourcc, 2 * fps, tuple(prev.shape)[0:2][::-1])

out.write(prev)
while vid.isOpened():
    success, image = vid.read()
    if image is None: break
    if prev is not None:
        mid = add_images(image, prev)
        out.write(mid)
        cv2.imshow('interpolated frame', mid)
    out.write(image)
    prev = image
    if cv2.waitKey(1) == ord('q'):
        break

vid.release()
out.release()
cv2.destroyAllWindows()
print("file saved")
