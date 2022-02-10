from pyzbar.pyzbar import decode
from PIL import Image
import pyautogui as pyg
import time
import pyperclip
import os

time.sleep(1)

unixtimestamp = round(time.time())

screenshotName = str(unixtimestamp) + ".png"

myScreenshot = pyg.screenshot()
myScreenshot.save(screenshotName)



qrCodes = decode(Image.open(screenshotName))

allResults = []

for qrCode in qrCodes:
    allResults.append((qrCode.data).decode("utf-8"))


if os.path.exists(screenshotName):
    os.remove(screenshotName)

toCopy = "\n".join(allResults)
pyperclip.copy(toCopy)



















# import cv2
# from pyzbar import pyzbar
# from PIL import Image
# import pyautogui as pyg
# import time



# def read_barcodes(frame):
#     barcodes = pyzbar.decode(frame)
#     for barcode in barcodes:
#         x, y , w, h = barcode.rect
        
#         barcode_info = barcode.data.decode('utf-8')
#         cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
        
#         font = cv2.FONT_HERSHEY_DUPLEX
#         cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)
        
#         with open("barcode_result.txt", mode ='w') as file:
#             # file.write("Recognized Barcode:" + barcode_info)
#             print("Recognized Barcode:" + barcode_info)
#     return frame



# def main():
    
#     camera = cv2.VideoCapture(0)
#     ret, frame = camera.read()
    
#     while ret:
#         ret, frame = camera.read()
#         frame = read_barcodes(frame)
#         cv2.imshow('Barcode/QR code reader', frame)
#         if cv2.waitKey(1) & 0xFF == 27:
#             break
    
#     camera.release()
#     cv2.destroyAllWindows()

#     # time.sleep(3)

#     # myScreenshot = pyg.screenshot()
#     # myScreenshot.save("hi.png")


#     # frame = read_barcodes(Image.open("hi.png"))
#     # cv2.imshow('Barcode/QR code reader', frame)




# if __name__ == '__main__':
#     main()
