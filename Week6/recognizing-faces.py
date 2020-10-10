import cv2 as cv
import os
import numpy as np
from matplotlib import pyplot as plt

subjects = ["", "Bill Gates", "Steve Jobs"]

#function to detect and face using open cv
def detect_face(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

    #if no faces are detected then return original image
    if len(faces) == 0:
        return None, None

    #under the assumption that there will be only face
    #extract the face area
    (x, y, w, h) = faces[0]

    #return only the face part of image
    return gray[y:y + h, x:x + w], faces[0]

def preparing_training_data(data_folder_path):
    #-------STEP-1---------
    #get the directories(only one directory in each subject) for one folder
    dirs = os.listdir(data_folder_path)

    #list to hold all subjects faces
    faces = []

    #list to hold all labels for subjects
    labels = []

    # let's go through each directory and read images within it
    for dir_name in dirs:

        # our subject directories start with letter 's' so
        # ignore any non-relevant directories if any
        if not dir_name.startswith("a"):
            continue;

        label = int(dir_name.replace("a", ""))

        subject_dir_path = data_folder_path + "/" + dir_name

        # get the images names that are inside the given subject directory
        subject_image_names = os.listdir(subject_dir_path)

        for image_names in subject_image_names:

            # ignore system files like .DS_Store
            if image_names.startswith("."):
                continue;

            #building path
            #sample image path = training_data2/a1/1.jpg
            image_path = subject_dir_path + "/" + image_names

            #read name
            image = cv.imread(image_path)

            # display an image window to show the image
            cv.imshow("Training on image...", cv.resize(image, (300, 200)))
            cv.waitKey(100)

            #detect face
            face, rect = detect_face(image)

            # ------STEP-4--------
            # for the purpose of this tutorial
            # we will ignore faces that are not detected
            if face is not None:
                #add face to list of faces
                faces.append(face)
                #add label for this face
                labels.append(label)

    cv.destroyAllWindows()
    cv.waitKey(1)
    cv.destroyAllWindows()

    return faces, labels

print("Preparing Data...")
faces, labels = preparing_training_data("training-data2")
print("Data Prepared")

#print total faces and labels
print("Total faces", len(faces))
print("Total labels", len(labels))

#create our LBPH face recognizer
face_recognizer = cv.face.LBPHFaceRecognizer_create()

#train our face recognizer for our training data
face_recognizer.train(faces, np.array(labels))

# function to draw rectangle on image
# according to given (x, y) coordinates and
# given width and height

def draw_rect(img, rect):
    (x, y, w, h) = rect
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

# function to draw text on give image starting from
# passed (x, y) coordinates.
def draw_text(img, text, x, y):
    cv.putText(img, text, (x, y), cv.FONT_HERSHEY_PLAIN, 5, (0, 255, 0), 3)

def predict(test_img):
    # this function recognizes the person in image passed
    # and draws a rectangle around detected face with name of the
    # subject

    # make a copy of the image as we don't want to change original image
    img = test_img.copy()
    #detect face from this image
    face, rect = detect_face(img)

    #predict image using our face_recognizer
    label = face_recognizer.predict(face)

    # get name of respective label returned by face recognizer
    label_text = subjects[labels[0]]

    # draw a rectangle around face detected
    draw_rect(img, rect)
    # draw name of predicted person
    draw_text(img, label_text, rect[0], rect[1] - 5)

    return img

print("Predicting images...")

# load test images
test_img1 = cv.imread("test-data1/test1.jpg")
test_img2 = cv.imread("test-data1/test2.jpg")

# perform a prediction
predicted_img1 = predict(test_img1)
predicted_img2 = predict(test_img2)
print("Prediction complete")

# display both images
# cv2.imshow(subjects[1], predicted_img1)
# cv2.imshow(subjects[2], predicted_img2)

titles = [subjects[1], subjects[2]]
images = [predicted_img1, predicted_img2]

for i in range(2):
    plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
cv.waitKey(0)
cv.destroyAllWindows()