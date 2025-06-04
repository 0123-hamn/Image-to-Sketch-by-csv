import cv2
image = cv2.imread(r'C:\Users\HEMANTA\OneDrive\Desktop\hemanta cv.jpg')
if image is None:
    print("Image not found. Please check the path.")
else:
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    invert = cv2.bitwise_not(gray_img)
    blur = cv2.GaussianBlur(invert, (21, 21), 0)
    inverted_blur = cv2.bitwise_not(blur)
    sketch = cv2.divide(gray_img, inverted_blur, scale=256.0)
    cv2.imwrite('sketch.png', sketch)
    print("Sketch saved as sketch2.png")
