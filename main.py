#Hasshya Shah 
#C082 
#Text extraction from image and coversion to voice.
import cv2
import pytesseract
import pyttsx3
import numpy as np
from gtts import gTTS

def thick_font(image):
    image = cv2.bitwise_not(image)
    kernel = np.array(([1,0],[0,1]), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    image = cv2.bitwise_not(image)
    return (image) 

def thin_font(image):
    import numpy as np
    image = cv2.bitwise_not(image)
    kernel = np.array(([1,1],[0,1]), np.uint8)
    image = cv2.erode(image, kernel, iterations=1)
    image = cv2.bitwise_not(image)
    return (image) 

def extract_text_from_image(image_path):
    try:
        image = cv2.imread(image_path)

        if image is None:
            return "Error: Unable to load the image."

        cv2.imshow("Input Image",image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Gray image",gray_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        _, thresholded_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        cv2.imshow('Thresholded Image', thresholded_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        thick_image = thick_font(thresholded_image)
        cv2.imshow("Thick image",thick_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        thin_image = thin_font(thick_image)
        cv2.imshow("Thick image",thin_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        text = pytesseract.image_to_string(thick_image)
        if not text.strip():
            return "No text found in the image."

        return text
    except Exception as e:
        return f"An error occurred: {str(e)}"

def text_to_speech(text):
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        return "Text converted to speech successfully."
    except Exception as e:
        return f"An error occurred: {str(e)}"

image1 = 'C:/SEM9/IP/Project/input images/sample1.png'
image2 = 'C:/SEM9/IP/Project/input images/sample2.png'
image3 = 'C:/SEM9/IP/Project/input images/sample3.png'
images = [image1,image2,image3]
k=0
for i in images:
    k+=1
    extracted_text = extract_text_from_image(i)

    if extracted_text.startswith("Error"):
        print(extracted_text)
    else:
        a=1
        print("Extracted Text:")
        print(extracted_text)
        result = text_to_speech(extracted_text)
        print(result)
        filepath = f'C:/SEM9/IP/Project/output/output{k}.mp3'
        tts = gTTS(extracted_text)
        tts.save(filepath)