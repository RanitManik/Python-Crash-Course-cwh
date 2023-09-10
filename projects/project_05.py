import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

# credits ==>
print("Welcome to Facial Recognition Attendance System v3.4 created by Ranit Kumar Manik.")
print("Loading...")

# Initialize camera
video_capture = cv2.VideoCapture(0)

# Load known faces and their names
ranit_image = face_recognition.load_image_file("assets/ranit.jpg")
ranit_encoding = face_recognition.face_encodings(ranit_image)[0]

soumen_image = face_recognition.load_image_file("assets/soumen.jpg")
soumen_encoding = face_recognition.face_encodings(soumen_image)[0]

king_image = face_recognition.load_image_file("assets/king_khan.jpeg")
king_encoding = face_recognition.face_encodings(king_image)[0]

known_face_encodings = [ranit_encoding, soumen_encoding, king_encoding]
known_face_names = ["ranit", "soumen", "king"]

# Create a CSV file for attendance
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")
csv_file = open(f"{current_date}.csv", "w+", newline="")
csv_writer = csv.writer(csv_file)

while True:
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Initialize name as None for this frame
    name = None

    # Recognize faces
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distance)

        if matches[best_match_index]:
            name = known_face_names[best_match_index]

            # Write the name to the CSV file
            current_time = now.strftime("%H:%M:%S")
            csv_writer.writerow([name, current_date, current_time])

    # Add the text if a person is present
    if name is not None:
        font = cv2.FONT_HERSHEY_SIMPLEX
        bottomLeftCornerOfText = (10, 100)
        fontScale = 1.5
        fontColor = (256, 0, 0)
        thickness = 3
        lineType = 2
        cv2.putText(frame, name + " present", bottomLeftCornerOfText, font, fontScale, fontColor, thickness, lineType)

    cv2.imshow("Attendance", frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release video capture and close CSV file
video_capture.release()
csv_file.close()

# Close all OpenCV windows
cv2.destroyAllWindows()
