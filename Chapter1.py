import cv2
"""
Show Image
"""
# print("Package imported")
#
# img =cv2.imread("Ressources/lena.png")
#
# cv2.imshow("Output", img)
# cv2.waitKey(0)

"""
Show Video
"""
cap = cv2.VideoCapture("Ressources/test_video.mp4")
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
"""
Show Camera
"""
# cap = cv2.VideoCapture(0)
# cap.set(3, 640)
# cap.set(4, 480)
# cap.set(10, 100)
#
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


