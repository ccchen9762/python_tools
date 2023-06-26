import cv2
import os

path = ""
other = ""
pics = os.listdir(path)

for i in range(len(pics)):
    print(pics[i])
    img = cv2.imread(path+pics[i])
    '''img = cv2.medianBlur(img,25)
    cv2.imwrite("D:\\Download\\b\\"+str(i+1)+".png", img)'''
    '''cv2.normalize(img, img, 30, 255, norm_type=cv2.NORM_MINMAX)
    cv2.imwrite("D:\\Download\\b\\"+str(i+1)+".png", img)'''
    alpha = 1.0  # Contrast control (1.0-3.0)
    beta = 15    # Brightness control (0-100)
    adjusted_img = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
    if i+1 < 10:
        cv2.imwrite(other+str(0)+str(i+1)+".jpg", adjusted_img)
    else:
        cv2.imwrite(other+str(i+1)+".jpg", adjusted_img)


# import cv2

# # Load the image
# img = cv2.imread('')

# # Apply contrast adjustment
# alpha = 1.5  # Contrast control (1.0-3.0)
# beta = 0    # Brightness control (0-100)
# adjusted_img = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

# # Display the original and adjusted images
# cv2.imshow('Original', img)
# cv2.imshow('Adjusted', adjusted_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
