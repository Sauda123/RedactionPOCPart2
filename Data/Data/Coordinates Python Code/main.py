import cv2
import pytesseract
from pdf2image import convert_from_path
from pytesseract import Output
tesseractpath ="C:\\Users\\sauda.maryam\\AppData\\Local\\Tesseract-OCR\\tesseract.exe"
popplerpath= "C:\\Users\\sauda.maryam\\poppler-0.68.0_x86\\poppler-0.68.0\\bin"
RuntimeImagesfolder_path = "C:\\Redaction POC\\BackgroundProcess\\Data\\RuntimeImages\\"
pdfpath = "E:\DU\w2-2.pdf"
file_number = "File123"
ssn = "618-42-2402"
def coordinates(pdfpath,tesseractpath,popplerpath,RuntimeImagesfolder_path,file_number,ssn):
    try:
        coordinate = []
        content = pdfpath
        TesseractPath = tesseractpath
        pytesseract.pytesseract.tesseract_cmd = TesseractPath
        pages = convert_from_path(content, poppler_path= popplerpath,dpi=500)
        image_counter = 0

        for page in pages:
            filename = RuntimeImagesfolder_path + file_number + "\\" + "page_" + str(image_counter) + ".png"
            page.save(filename, 'png')
            print(filename)
            image_counter += 1

            img = cv2.imread(filename,0)
            print(img.shape)

            image_data = pytesseract.image_to_data(img, output_type=Output.DICT)

            print(image_data['text'])
            for i, word in enumerate(image_data['text']):
                if word != "":
                    x,y,w,h = image_data['left'][i], image_data['top'][i], image_data['width'][i], image_data['height'][i]


                    if word == ssn:
                        print("ssn")
                        yc = y/6.94444
                        xc = x/6.94444
                        wc = w/6.94444
                        hc = h/6.94444
                        crdlist = str(yc) + "," + str(xc) + "," + str(wc) + "," + str(hc)

                        coordinate.append(str(crdlist))
                        print(crdlist)
                        print(x/6.94444,y/6.94444,(x+w)/6.94444,(y+h)/6.94444,w/6.94444,h/6.94444)
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)

            print(coordinate)
            return coordinate
    except Exception as e:
        return 'Following exception occured: ' + str(e)

print(coordinates(pdfpath,tesseractpath,popplerpath,RuntimeImagesfolder_path,file_number,ssn))
# #actual code started
# img = cv2.imread("89619cde-1c9f-4183-905c-d738d4332755.jpg",0)
# #funtion to detect each letter
# print(img.shape)
#
# image_data = pytesseract.image_to_data(img, output_type=Output.DICT)
# ssn= "213-21-1653"
# print(image_data['text'])
# for i, word in enumerate(image_data['text']):
#     if word != "":
#         x,y,w,h = image_data['left'][i], image_data['top'][i], image_data['width'][i], image_data['height'][i]
#
#
#         if word == ssn:
#             print("ssn")
#             print(x/4.16667,y/4.16667,(x+w)/4.16667,(y+h)/4.16667,w/4.16667,h/4.16667)
#             cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
#
#
# cv2.imshow("window", img)
# cv2.imwrite("RedactedFile.png", img)
# cv2.waitKey(0)
# #actual code ended


# for page in pages: 42.84  6.84  PageHeight=792(3300), PageWidth=612(2550)
#     filename = folder_path + file_number + "\\" + "page_" + str(image_counter) + ".png"
#     page.save(filename, 'png')
#     print(filename)
#     image_counter += 1
#
#     img = cv2.imread(filename)
#     # Image_ht,Image_wd,Image_thickness = img.shape
#     image_data = pytesseract.image_to_data(img, output_type=Output.DICT)
#     print(image_data['text'])
#     for i, word in enumerate(image_data['text']):
#         if word != "":
#             x,y,w,h = image_data['left'][i], image_data['top'][i], image_data['width'][i], image_data['height'][i]
#             if word == "1900":
#                 print("1900")
#                 print(3300 - y)
#                 print(x,y,x+w,y+h,w,h)
#                 crop_img = img[y:y + h, x:x + w]
#                 cv2.imshow("cropped", crop_img)
#                 cv2.waitKey(0)

# crop_img = img[191:191+43, 629:629+121]













# img = cv2.imread("W2-4.jpg")

# Image_ht,Image_wd,Image_thickness = img.shape
# import cv2
# img = cv2.imread("W2-4.jpg")
# crop_img = img[191:191+43, 629:629+121]
# cv2.imshow("cropped", crop_img)
# cv2.waitKey(0)
#
# print(Image_ht,Image_wd)
#function to detect words
# img = cv2.imread("W2.jpg")
# image_data = pytesseract.image_to_data(img, output_type=Output.DICT)
# ssn= "37-1508469"
# print(image_data['text'])
# for i, word in enumerate(image_data['text']):
#     if word != "":
#         x,y,w,h = image_data['left'][i], image_data['top'][i], image_data['width'][i], image_data['height'][i]
#         if word == ssn:
#             print("ssn")
#             print(x,y,x+w,y+h,w,h)
#

# for i, word in enumerate(image_data['text']):
#
#     if word != "":
#
#         x,y,w,h = image_data['left'][i], image_data['top'][i], image_data['width'][i], image_data['height'][i]
#         #cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255),3)
#         #cv2.putText(img, word, (x,y-16), cv2.FONT_HERSHEY_COMPLEX, fontScale=1, color=(0, 255, 0))
#         if word == "1900":
#             print("1900")
#             print(x,y,x+w,y+h,w,h)
#
#         if word == ssn:
#             print(word)
#             print(x,y,x+w,y+h,w,h)


# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
#
# image = cv2.imread("W2-4.jpg", 1)
# # Loading the image
#
# half = cv2.resize(image, (0, 0), fx=0.1, fy=0.1)
# bigger = cv2.resize(image, (1050, 1610))
#
# stretch_near = cv2.resize(image, (780, 540),
#                           interpolation=cv2.INTER_NEAREST)
#
# Titles = ["Original", "Half", "Bigger", "Interpolation Nearest"]
# images = [image, half, bigger, stretch_near]
# count = 4
#
# for i in range(count):
#     plt.subplot(2, 2, i + 1)
#     plt.title(Titles[i])
#     plt.imshow(images[i])
#
# plt.show()
