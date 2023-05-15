import cv2
import pyzbar.pyzbar as pyzbar

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:
    success, frame = cap.read()

    a = False
    for code in pyzbar.decode(frame):
        cv2.imwrite('qrbarcode_image.png', frame)
        my_code = code.data.decode('utf-8')
        if my_code:
            print("인식 성공 : ", my_code)
            a = True
            break
        else:
            pass

    if a:
        break  

    cv2.imshow('QRcode Barcode Scan', frame)

    cv2.waitKey(1)

