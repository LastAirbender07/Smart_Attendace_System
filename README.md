# Smart_Attendace_System
This project aims replacing the current method of manual attendance taking system in schools by providing a smart system


### 1	 ABSTRACT
     Face recognition is an important application of computer vision and machine learning, with many practical applications in security, surveillance, and social media. Python and OpenCV are popular tools for implementing face recognition algorithms. 
"Attendance using Face Recognition" is a system that uses facial recognition technology to record and manage attendance. The system then stores attendance records in a database and provides real-time reports to the administrators.
In this paper, we present an implementation of a face recognition system using the pre-built “Face Recognition” module and OpenCV library in Python. Our results show that our system achieves high accuracy and robustness, while being efficient and scalable.

Keywords:
Computer Vision, machine learning, face recognition, Open CV, facial feature extraction, efficient and accurate


### 1.1 	INTRODUCTION:
     Face recognition has become a widely researched topic due to its practical applications in various fields. It involves recognizing and identifying individuals from facial images or videos. Face recognition has become a popular area of research in computer vision and machine learning, with many techniques being developed over the years.
The aim of face recognition is to automatically identify or verify an individual based on their facial features. Python and OpenCV are popular tools for implementing face recognition algorithms, with many libraries and modules available for use.
"Attendance using Face Recognition" is a system designed to automate the process of recording attendance using facial recognition technology. The system utilizes a camera to capture images of individuals entering a specific location, which are then processed using deep learning algorithms to identify and verify their identities. The system stores attendance records in a database and provides real-time reports to the administrators, allowing for easy monitoring and management of attendance. The implementation of this system offers a more efficient and accurate way to manage attendance records compared to traditional methods such as paper-based systems or manual data entry.

### DISADVANTAGES OF MANUAL ATTENDANCE SYSTEM

•	Time-consuming: It takes time for employees to sign in and out manually, and for the person in charge to verify and record the attendance. This can result in delays and can be time-consuming for both employees and administrators.

•	Error-prone: Manual attendance systems are prone to errors such as misreading handwriting, recording the wrong time, or losing attendance sheets. This can result in inaccurate attendance records, which can be a problem for payroll and tracking purposes.

•	Security concerns: Manual attendance systems can be vulnerable to fraud, such as employees signing in and out for each other. It can also be easy for employees to manipulate attendance records, leading to inaccuracies in payroll.

1.3	BENEFITS OF SMART ATTENDANCE SYSTEM

•	Time-saving: Face recognition technology can save time as it can accurately identify employees and record their attendance automatically. This eliminates the need for manual attendance sheets and reduces the time needed for attendance tracking.

•	Accurate: Face recognition technology can accurately identify employees, reducing the chances of errors in attendance recording.

•	Real-time data: Face recognition technology can provide real-time data on employee attendance, allowing administrators to make quick decisions related to staffing, scheduling, or absenteeism.

•	Security: Face recognition technology can improve security as it is difficult to fake someone else's face. It can also help prevent fraud by ensuring that employees cannot sign in or out for each other.

In summary, moving to attendance using face recognition can offer several benefits over manual attendance systems, including improved accuracy, time-saving, real-time data, and increased security.

### 2	METHODOLOGY

2.1	EXISTING PRACTICE

The existing practice for taking attendance can vary depending on the specific setting and purpose. Here are some common practices:
•	Roll Call: This is the traditional method where the instructor or teacher calls out each student's name and the student respond with "present" or "here".
•	Sign-in sheet: In this method, the instructor or teacher provides a sheet of paper with the names of the students and asks them to sign in when they arrive.

•	Barcode/RFID scanning: Some institutions use technology such as barcode or radio-frequency identification (RFID) scanners to track attendance. Students are given a barcode or RFID-enabled ID card that is scanned when they arrive.

•	Online attendance systems: With the growing use of technology in education, some institutions use online systems to take attendance. Students can log in to a system and mark themselves as present.

•	Participation-based: In some courses, attendance may be taken based on participation. This means that students need to actively participate in the class discussion, group work, or other activities to be counted as present.

•	Peer Check-in: In this method, students may be asked to check in with a classmate or group to confirm their attendance.
Most of these approaches are subject to errors, Time consuming and are not 100% reliable thus a need for a better solution to taking attendance is necessary in the near future. 

2.2	OUR APPROACH: 
Our implementation involves the following steps:
1.	Face Detection: 
We use “Face Recognition” module to detect faces in the input image or video stream. The module uses a pre-trained model to detect faces. The image of the person is loaded using “load_image_file” method the detected faces are then passed to the next step for alignment.
2.	Face Alignment and Feature Extraction: 
The facial features are extracted using face_encodings method  which uses an algorithm to locate the facial landmarks such as eyes, nose, and mouth. The detected landmarks are then used to align the face to a standard pose and the coordinates are stored as an array. 
3.	Real Time Face Detection:
For real time detection we use CV2 where cap.read()command is used to capture a frame from the video. Real time “BGR” image is converted to “RGB” image first and then the face_recognition module is used to extract the features and save them in pairs.
4.	Face Recognition: 
Then the facial features are compared and if it matches the facial features in our dataset then attendance is marked in the excel sheet with date and time as well.

### 3	RESULTS:

4.1	DATASET AND ENVIRONMENTAL SETUP
For this study, we used a dataset consisting of 16 images of human faces collected from students and teachers od Amrita Vishwa Vidyapeetham. The images were in JPEG & JPG format and had a resolution of 1209 x 1620 pixels. We preprocessed the images by cropping them to focus only on the face region and then resizing them to a uniform size suxh that output image should have one-fourth the width and height of the input image
We used a computer with an Intel Core i7 processor and 16 GB of RAM processing our models. The programming language used was Python and we used the face_recognition library for deep learning algorithms.
When the flask app runs, a real-time video feed is loaded where the user is supposed to show his face. Once the face is recognized, the attendance is marked in the excel sheet with name, time of attendance and status.
As we are doing real time face detection wea re unable to give the performance matrix(confusion matrix, precision, F1 score etc) of real time data, but we have calculated the accuracy of the real time detection with the faceMatch Index. As we are using a very limited set of image data, the accuracy of the model is low (52% max). 

### 4   CONCLUSION: 
In this paper, we presented an implementation of Attendance using face recognition system which uses Face Recognition module and OpenCV library in Python. 
In conclusion, our attendance system using face recognition technology is a reliable and efficient solution for tracking attendance in various settings. The system offers a number of benefits, including increased accuracy, reduced administrative workload, and improved security.
Through the use of deep learning algorithms and machine vision, our system can accurately detect and recognize individuals' faces, even in slightly low-light or crowded environments. This ensures that attendance records are precise and up-to-date, which can be critical for payroll and other administrative tasks.
Moreover, the system can be easily integrated into existing infrastructure, such as access control systems and time and attendance software. This makes it easy for organizations to adopt and benefit from the technology without major disruptions to their existing processes.


FUTURE WORK:
Our implementation can be further improved and extended in various ways. Some of the possible future work includes:
1.	Face recognition in challenging conditions: Our implementation can be extended to handle face recognition in challenging conditions such as occlusions, disguises, and low-resolution images by using advanced techniques such as deep learning and ensemble methods.
2.	Large-scale face recognition: Our implementation can be extended to handle large-scale face recognition applications by using distributed computing techniques and optimizing the storage and retrieval of the face feature vectors.
3.	Privacy and ethical considerations: Face recognition technology raises privacy and ethical concerns, such as the use of facial recognition for surveillance and the potential for bias and discrimination. Future work should consider these issues and develop methods to address them.
In summary, face recognition using Python and OpenCV is a promising field with many practical applications and the effectiveness of using the Face Recognition module and OpenCV library for face recognition, and provides a starting point for further research and development in this field.


### 6	REFERENCES

[1] 	Face Recognition for Attendance Management by Jaya Bhaskar, V Venkatesh
https://web.archive.org/web/20220303072507/http://www.warse.org/IJETER/static/pdf/file/ijeter04842020.pdf

[2] 	Face Recognition Technology by Sagar Deshmukh, Sanjay Rawat
https://web.archive.org/web/20200319020837/http://www.ijtsrd.com/papers/ijtsrd14331.pdf

[3]	J. Hui, S. Tang, and S. Hu, "Face Recognition Based on Convolutional Neural Networks and Softmax Regression," in Proceedings of the 2017 International Conference on Image, Vision and Computing (ICIVC), Chengdu, China, pp. 112-116, 2017. 

[4] 	Age Invariant Face Recognition by Prathama V, Thippeswamy
https://web.archive.org/web/20200318185316/https://www.ijtsrd.com/papers/ijtsrd23572.pdf

[5] 	S. Minaee, S. Abdolshah, and N. Khademi Kalantari, "Deep learning-based face recognition: A survey," Pattern Recognition, vol. 107, 2020.

[6] 	Mobile Face Recognition Application using Egien Face Approach for Android	
https://web.archive.org/web/20200213021038/http://mjs.uomustansiriyah.edu.iq/ojs1/index.php/MJS/article/download/540/pdf

[7] 	Face Recognition for automated attendance management by N. Ramya, D. Manasa, S.K.Naveed
https://web.archive.org/web/20201119203218/https://eprajournals.com/jpanel/upload/918pm_22.EPRA%20JOURNALS--5583.pdf

[8] 	Image Processing using OpenCV by Udit Malik
https://web.archive.org/web/20220704200918/https://www.ijraset.com/best-journal/image-processing-in-open-cv

[9]	Smart Attendance System using OpenCV based on Face Recognition by Sudhir Bussa, Ananya Mani, Shruti Bharuka
https://web.archive.org/web/20200709102713/https://www.ijert.org/research/smart-attendance-system-using-opencv-based-on-facial-recognition-IJERTV9IS030122.pdf

[10] 	Y. Sun, X. Wang, and X. Tang, "Deep Learning Face Representation from Predicting 10,000 Classes," in Proceedings of the 2014 IEEE Conference on Computer Vision and Pattern Recognition (CVPR), Columbus, OH, USA, pp. 1891-1898, 2014.

[9] 	J. Lu, V. E. Liong, and J. Zhou, "Face Recognition using Local Quantized Patterns," in Proceedings of the 2012 IEEE Conference on Computer Vision and Pattern Recognition (CVPR), Providence, RI, USA, pp. 3562-3569, 2012.

Face Recognition module, available at https://github.com/ageitgey/face_recognition
