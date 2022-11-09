import cv2
import numpy as np
import time
import telepot
from telegram import running
import time, datetime
from dotenv import load_dotenv
import os

load_dotenv() # Environment Variables


now = datetime.datetime.now() #libraries

weights_path = r"yolov4-tiny-custom_best.weights"
cfg_path = r"yolov4-tiny-custom.cfg"

# Load Yolo
net = cv2.dnn.readNet(weights_path, cfg_path)
classes = ["Sehat", "Sakit"]
with open("obj.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))

bot = telepot.Bot(os.getenv("TELEBOT_TOKEN"))

class Video(object):
    def __init__(self):
        self.video=cv2.VideoCapture(0)
    def __del__(self):
        self.video.release()
    def get_frame(self):
        ret, frame = self.video.read()
        font = cv2.FONT_HERSHEY_PLAIN
        starting_time = time.time()
        frame_id = 0 
        
        height, width, channels = frame.shape

    # Detecting objects
        blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        frame_id += 1
        net.setInput(blob)
        outs = net.forward(output_layers)
        # Showing informations on the screen
        class_ids = []
        confidences = []
        boxes = []
        for out in outs:
            img_counter = 0
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.2:
                    # Object detected
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
                    # Rectangle coordinates
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)


        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.4, 0.3)
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                confidence = confidences[i]
                color = colors[class_ids[i]]
                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                cv2.rectangle(frame, (x, y), (x + w, y + 30), color, -1)
                cv2.putText(frame, label + " " + str(round(confidence, 2)), (x, y + 30), font, 3, (255,255,255), 3)

                elapsed_time = time.time() - starting_time
                fps = frame_id / elapsed_time
                cv2.putText(frame, "FPS: " + str(round(fps, 2)), (10, 50), font, 3, (0, 0, 0), 3)
                # cv2.imshow("Image", frame)
                key = cv2.waitKey(1)
                if key == 27:
                    break

                if label == "Sakit" and confidence > 0.8:
                    chat_id = os.getenv("CHAT_ID")
                    img_name = "Ayam Sakit.jpg".format(img_counter)
                    cv2.imwrite(img_name,frame)
                    # running()
                    bot.sendPhoto(chat_id, (open('Ayam Sakit.jpg', "rb")))
                    bot.sendMessage(chat_id, str("Terdeteksi Ayam Sakit,")+str("\nPukul: ")+str(now.hour)+str(":")+str(now.minute)+str(" WIB")+ str("\nTanggal: ")+str(now.day)+ str(" ")+ str(now.strftime("%B")) + str(" ")+ str(now.year))
 

        ret,jpg=cv2.imencode('.jpg',frame)
        return jpg.tobytes()