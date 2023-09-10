import cv2

# credits ==>
print("Welcome to image resizer v1.9 created by Ranit Kumar Manik.")

# writing the image name ==>
choice = input("If you want to try a demo press: 'd', if you want to go for custom press:'c' ==>\n")
if choice == 'd':
    image_name = ["assets/ranit.jpg"]
elif choice == 'c':
    image_name = input("Enter the image file name with extension with location: ")
else:
    print("Plz Enter a valid choice")

# If you want to use a list (consistent with the demo case):
# image_name = ["assets/ranit.jpg"] if choice == 'd' else [input("Enter the image file name with extension with location: ")]

# reading the image ==>
img = cv2.imread(image_name[0], cv2.IMREAD_UNCHANGED)

# prints the original dimension of the image ==>
print('Original Dimensions : ', img.shape)

# percent of the original size you want to keep in the Resized image ==>
scale_percent = int(input("Enter the percentage of original size: "))
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

# resize image ==>
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

# prints the original dimension of the image ==>
print('Resized Dimensions : ', resized.shape)

# This will write the image as Resized image.png ==>
cv2.imwrite("Resized image.png", resized)

# completing the process ==>
cv2.waitKey(0)
cv2.destroyAllWindows()
