import face_recognition
import cv2
import numpy as np

video = cv2.VideoCapture(0)

image1 = face_recognition.load_image_file("./photos/Samarth.jpeg")
image1_encoding = face_recognition.face_encodings(image1)[0]

image2 = face_recognition.load_image_file("./photos/Khushi.jpeg")  
image2_encoding = face_recognition.face_encodings(image2)[0]

user_face_encodings = [image1_encoding, image2_encoding]
user_face_names = ["Samarth", "Khushi"]

found_name = None  

while True:
    _, frame = video.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
    face_names = []

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(user_face_encodings, face_encoding, tolerance=0.6)

        name = "Unknown"

        if any(matches):
            best_match_index = np.argmin(face_recognition.face_distance(user_face_encodings, face_encoding))
            name = user_face_names[best_match_index]

            found_name = name
            break

        face_names.append(name)

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    cv2.imshow("User", frame)
    
    if found_name is not None:
        break

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()

print("Found Name:", found_name)

if(found_name == "Khushi"):
    print("Worked")
    