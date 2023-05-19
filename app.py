import cv2
import numpy as np
import pandas as pd
import face_recognition
import os
from datetime import datetime
from flask import Flask, flash, request, redirect, url_for, render_template, Response
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = r'D:\Amrita 2nd Year\SEM 4\Multimedia Processing\End_Sem_Project\Project\images'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

picsFolder = os.path.join('static', 'pics')
app.config['UPLOAD_FOLDER1'] = picsFolder

@app.route('/')
def upload_file():
    logo = os.path.join(app.config['UPLOAD_FOLDER1'], 'logo.png')
    return render_template('upload1.html', user_img = logo)

@app.route('/index')
def index():
    logo = os.path.join(app.config['UPLOAD_FOLDER1'], 'logo.png')
    """Video streaming home page."""
    return render_template('index1.html', user_img = logo)


def gen():
    path = "images"
    images = []
    classNames = []
    attendance = pd.DataFrame(columns=["Name", "Date", "Time", "Status"])
    names = [""]
    myList = os.listdir(path)
    print("\nTotal Classes Detected : ", len(myList))
    print("\n\nClasses Detected : ", myList)

    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    print('\n------------------ Classes Loaded ------------------')
    print("\n")
    print(classNames)

    def findEncodings(images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList  
        
    encodeListKnown = findEncodings(images)
    print('\n------------------ Encoding Complete ------------------')

    cap = cv2.VideoCapture(0)

    while True:
        success, img = cap.read()
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
        
                if name not in names:
                    names.append(name)
                    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    attendance = attendance.append({"Name": name, "Date": date_time.split(" ")[0], "Time": date_time.split(" ")[1], "Status" : "p"}, ignore_index=True)
                    attendance.to_excel("Attendance.xlsx", index=False)
                    
                    print("\nAttendance marked for " + name + " at " + str(datetime.now()))
                    print(faceDis)
                    print("\n")
                    
                    # Calculating the accuracy of face detection
                    accuracy = (1 - faceDis[matchIndex]) * 100
                    print("Accuracy:", round(accuracy, 2), "%")
                else:
                    print("Attendance already marked for " + name)

        cv2.imshow('Webcam', img)
        cv2.waitKey(1) # exit on ESC

        frame = cv2.imencode('.jpg', img)[1].tobytes() # encode frame as jpeg
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n') # concat frame one by one and show result
        key = cv2.waitKey(20) # exit on ESC
        if key == 27: 
            break


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(debug=True)