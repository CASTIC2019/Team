#import OpenCV module
import cv2
#import os module for reading training data directories and paths
import os
#import numpy to convert python lists to numpy arrays as 
#it is needed by OpenCV face recognizers
import numpy as np
import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

subjects = ["", "tianwentao", "mayunfei","jiamo"]


#function to detect face using OpenCV
def detect_face(img):
    #convert the test image to gray image as opencv face detector expects gray images
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    #load OpenCV face detector, I am using LBP which is fast
    #there is also a more accurate but slow Haar classifier
    face_cascade = cv2.CascadeClassifier('opencv-files/lbpcascade_frontalface.xml')

    #let's detect multiscale (some images may be closer to camera than others) images
    #result is a list of faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5);
    
    #if no faces are detected then return original img
    if (len(faces) == 0):
        return None, None
    
    #under the assumption that there will be only one face,
    #extract the face area
    (x, y, w, h) = faces[0]
    
    #return only the face part of the image
    return gray[y:y+w, x:x+h], faces[0]


# I am using OpenCV's **LBP face detector**. On _line 4_, I convert the image to grayscale because most operations in OpenCV are performed in gray scale, then on _line 8_ I load LBP face detector using `cv2.CascadeClassifier` class. After that on _line 12_ I use `cv2.CascadeClassifier` class' `detectMultiScale` method to detect all the faces in the image. on _line 20_, from detected faces I only pick the first face because in one image there will be only one face (under the assumption that there will be only one prominent face). As faces returned by `detectMultiScale` method are actually rectangles (x, y, width, height) and not actual faces images so we have to extract face image area from the main image. So on _line 23_ I extract face area from gray image and return both the face image area and face rectangle.
# 
# Now you have got a face detector and you know the 4 steps to prepare the data, so are you ready to code the prepare data step? Yes? So let's do it. 

# In[4]:

#this function will read all persons' training images, detect face from each image
#and will return two lists of exactly same size, one list 
# of faces and another list of labels for each face
def prepare_training_data(data_folder_path):
    
    #------STEP-1--------
    #get the directories (one directory for each subject) in data folder
    dirs = os.listdir(data_folder_path)
    
    #list to hold all subject faces
    faces = []
    #list to hold labels for all subjects
    labels = []
    
    #let's go through each directory and read images within it
    for dir_name in dirs:
        
        #our subject directories start with letter 's' so
        #ignore any non-relevant directories if any
        if not dir_name.startswith("s"):
            continue;
            
        #------STEP-2--------
        #extract label number of subject from dir_name
        #format of dir name = slabel
        #, so removing letter 's' from dir_name will give us label
        label = int(dir_name.replace("s", ""))
        
        #build path of directory containin images for current subject subject
        #sample subject_dir_path = "training-data/s1"
        subject_dir_path = data_folder_path + "/" + dir_name
        
        #get the images names that are inside the given subject directory
        subject_images_names = os.listdir(subject_dir_path)
        
        #------STEP-3--------
        #go through each image name, read image, 
        #detect face and add face to list of faces
        for image_name in subject_images_names:
            
            #ignore system files like .DS_Store
            if image_name.startswith("."):
                continue;
            
            #build image path
            #sample image path = training-data/s1/1.pgm
            image_path = subject_dir_path + "/" + image_name

            #read image
            image = cv2.imread(image_path)
            
            #display an image window to show the image 
            cv2.imshow("Training on image...", cv2.resize(image, (400, 500)))
            cv2.waitKey(100)
            
            #detect face
            face, rect = detect_face(image)
            
            #------STEP-4--------
            #for the purpose of this tutorial
            #we will ignore faces that are not detected
            if face is not None:
                #add face to list of faces
                faces.append(face)
                #add label for this face
                labels.append(label)
            
    cv2.destroyAllWindows()
    cv2.waitKey(1)
    cv2.destroyAllWindows()
    
    return faces, labels


#function to draw rectangle on image 
#according to given (x, y) coordinates and 
#given width and heigh
def draw_rectangle(img, rect):
    (x, y, w, h) = rect
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
#function to draw text on give image starting from
#passed (x, y) coordinates. 
def draw_text(img, text, x, y):
    cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)


# First function `draw_rectangle` draws a rectangle on image based on passed rectangle coordinates. It uses OpenCV's built in function `cv2.rectangle(img, topLeftPoint, bottomRightPoint, rgbColor, lineWidth)` to draw rectangle. We will use it to draw a rectangle around the face detected in test image.
# 
# Second function `draw_text` uses OpenCV's built in function `cv2.putText(img, text, startPoint, font, fontSize, rgbColor, lineWidth)` to draw text on image. 
# 
# Now that we have the drawing functions, we just need to call the face recognizer's `predict(face)` method to test our face recognizer on test images. Following function does the prediction for us.

# In[9]:

#this function recognizes the person in image passed
#and draws a rectangle around detected face with name of the 
#subject
def predict(test_img):
    global familyID
    #make a copy of the image as we don't want to chang original image
    img = test_img.copy()
    #detect face from the image
    cv2.imshow("imgface",img)
    cv2.waitKey(1000)
    face, rect = detect_face(img)
    if face is None :
        print("对不起，没有识别到人脸")
        return img;

    cv2.imshow("face",face)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

    #predict the image using our face recognizer 
    label, confidence = face_recognizer.predict(face)
    print("label,confidence",label,confidence)
    #get name of respective label returned by face recognizer
    label_text = subjects[label]
    familyID=label
    
    #draw a rectangle around face detected
    draw_rectangle(img, rect)
    #draw name of predicted person
    draw_text(img, label_text, rect[0], rect[1]-5)
    
    return img

face_cascade = cv2.CascadeClassifier('C:\chess\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:\chess\haarcascade_eye.xml')
faces, labels = prepare_training_data("training-data")
print("Data prepared")

#print total faces and labels
print("Total faces: ", len(faces))
print("Total labels: ", len(labels))


# This was probably the boring part, right? Don't worry, the fun stuff is coming up next. It's time to train our own face recognizer so that once trained it can recognize new faces of the persons it was trained on. Read? Ok then let's train our face recognizer. 


#create our LBPH face recognizer 
face_recognizer = cv2.face.LBPHFaceRecognizer_create()

#or use EigenFaceRecognizer by replacing above line with 
#face_recognizer = cv2.face.EigenFaceRecognizer_create()

#or use FisherFaceRecognizer by replacing above line with 
#face_recognizer = cv2.face.FisherFaceRecognizer_create()


# Now that we have initialized our face recognizer and we also have prepared our training data, it's time to train the face recognizer. We will do that by calling the `train(faces-vector, labels-vector)` method of face recognizer. 

# In[7]:

#train our face recognizer of our training faces
print(labels)
face_recognizer.train(faces, np.array(labels))


# **Did you notice** that instead of passing `labels` vector directly to face recognizer I am first converting it to **numpy** array? This is because OpenCV expects labels vector to be a `numpy` array. 
# 
# Still not satisfied? Want to see some action? Next step is the real action, I promise! 

# ### Prediction

# Now comes my favorite part, the prediction part. This is where we actually get to see if our algorithm is actually recognizing our trained subjects's faces or not. We will take two test images of our celeberities, detect faces from each of them and then pass those faces to our trained face recognizer to see if it recognizes them. 
# 
# Below are some utility functions that we will use for drawing bounding box (rectangle) around face and putting celeberity name near the face bounding box. 

# In[8]:


# Now that we have the prediction function well defined, next step is to actually call this function on our test images and display those test images to see if our face recognizer correctly recognized them. So let's do it. This is what we have been waiting for. 



resp=urlopen('http://www.weather.com.cn/weather/101020100.shtml')
soup=BeautifulSoup(resp,'html.parser')
tagDate=soup.find('ul',class_="t clearfix")
dates=tagDate.h1.string

tagToday=soup.find('p',class_="tem")
try:
	temperatureHigh=tagToday.span.string
except AttributeError as e:
	temperatureHigh=tagToday.find_next('p',class_="tem").span.string

temperatureLow=tagToday.i.string
weather=soup.find('p',class_="wea").string

tagWind=soup.find('p',class_="win")
winL=tagWind.i.string

import datetime 
today = datetime.date.today() 
print ("Year: %d" % today.year )
print ("Month: %d" % today.month )
print ("Day: %d" % today.day )
print ("Weekday: %d" % today.weekday()) # Day of week Monday = 0, Sunday = 6 
print ("ISO Weekday: %d" % today.isoweekday()) # Day of week Monday = 1, Sunday = 7 
print ("ISO Format: %s" % today.isoformat()) # YYYY-MM-DD format 
print ("ISO Calendar: %s" % str(today.isocalendar())) # Tuple of (ISO year, ISO week number, ISO weekday) 
print (today.strftime("%Y/%m/%d"))
familyID=0
print('上海天气：')
print('今天是：'+dates)
print('风级：'+winL)
print('最低温：'+temperatureLow)
print('最高温：'+temperatureHigh)
print('天气：'+weather)

cap=cv2.VideoCapture(0)
while(True):
    ret,frame = cap.read()
    face,rect=detect_face(frame)
    print("detecting face")
    if face is not None:
        cv2.imwrite("test-data/face.jpg",frame)
        cv2.imshow("face-detected",face)
        draw_rectangle(frame, rect)
        cv2.waitKey(2000)
        break
    cv2.imshow("cam frame",frame)
    cv2.waitKey(300)
cv2.destroyAllWindows()

print("Predicting images...")

#load test images
test_img1 = cv2.imread("test-data/face.jpg")

predicted_img1 = predict(test_img1)
print("Prediction complete")

#display both images
cv2.imshow(subjects[1], cv2.resize(predicted_img1, (400, 500)))

cv2.waitKey(5000)
cv2.destroyAllWindows()

if 1<=today.month and today.month<5:
    print("春天")
    season=0
if 5<=today.month and today.month<7:
    print("夏天")
    season=1
if 7<=today.month and today.month<10:
    print("秋天")
    season=2
if 10<=today.month and today.month<12:
    print("冬天")
    season=3
if"雨" in weather:
    rain = True
else:
    rain = False

print("你好客户",familyID)
print("现在是",season,"季")
print("今天有雨吗",rain)
