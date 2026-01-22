import cv2
import pytesseract
import re

image = cv2.imread("car.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 11, 17, 17)
edges = cv2.Canny(gray, 30, 200)

contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

plates = []

for c in contours:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.018 * peri, True)

    if len(approx) == 4:
        x, y, w, h = cv2.boundingRect(approx)
        plate_img = gray[y:y+h, x:x+w]
        text = pytesseract.image_to_string(plate_img, config="--psm 8")
        text = re.sub(r"[^A-Z0-9]", "", text.upper())
        if len(text) >= 5:
            plates.append(text)

for plate in set(plates):
    print("Recognized license plate:", plate)
