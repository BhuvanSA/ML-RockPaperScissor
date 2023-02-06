import cv2

path = "./rps/paper/"

for i in range(1,501):
    frame = cv2.imread(path + str(i) + ".jpeg")

    cv2.imwrite((path + str(i) + "-90.jpeg"), cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE))

    cv2.imwrite((path + str(i) + "-180.jpeg"), cv2.rotate(frame, cv2.ROTATE_180))

    cv2.imwrite((path + str(i) + "-270.jpeg"), cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE))