import cv2

image = cv2.imread('mysterious.jpg')
if image is None:
    raise FileNotFoundError("404! FILE NOT FOUND")

image1 = cv2.resize(image, (200, 200))
image2 = cv2.resize(image, (400, 400))
image3 = cv2.resize(image, (600, 600))

cv2.namedWindow('1st Image', cv2.WINDOW_NORMAL)
cv2.namedWindow('2nd Image', cv2.WINDOW_NORMAL)
cv2.namedWindow('3rd Image', cv2.WINDOW_NORMAL)

cv2.imshow('1st Image', image1)
cv2.imshow('2nd Image', image2)
cv2.imshow('3rd Image', image3)

key = cv2.waitKey(0)

if key == ord('s'):
    cv2.imwrite('input_image_small.jpg', image1)
    cv2.imwrite('input_image_medium.jpg', image2)
    cv2.imwrite('input_image_large.jpg', image3)
    print("All Images Saved.")
else:
    print("Images are not saved.")

cv2.destroyAllWindows()

print(f"Image Dimensions:\n"
      f"Image 1: {image1.shape}\n"
      f"Image 2: {image2.shape}\n"
      f"Image 3: {image3.shape}")

