import cv2
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
ds_factor=0.6

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
    
    def __del__(self):
        self.video.release()
        
    
    def get_frame(self):
        success,frame = self.video.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30))
        

        # Draw a rectangle around the faces
        d=0
        for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    crop_face = frame[y:y+h, x:x+w]
                    cv2.imwrite('C:/Users/Samridhi Prasad/Documents/project/saveimage/file_%d.jpg'%d,crop_face)
                    d = d+1
        
        
        
        ret, jpeg = cv2.imencode('.jpg', frame)

        return jpeg.tobytes()

       