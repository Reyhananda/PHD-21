## PROPERTY OF PHD-21 ##
from flask import Flask, render_template, request, Response, jsonify
from flask import Markup
from camera import Video
import cv2
import sqlite3
import os
import json

currentdirectory = os.path.dirname(os.path.abspath(__file__))

# import math 
# from time import sleep
# from servo import servo_bawah, servo_atas


app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route("/test", methods=["POST"])
# def test():
#     # Get slider Values
#     slider1 = request.form["slider1"]
#     slider2 = request.form["slider2"]
    
#     minVal = int(slider1)
#     maxVal = int(slider2)
    
#     # Change duty cycle
#     servo_bawah.value = math.sin(math.radians(float(slider1)))
#     servo_atas.value = math.sin(math.radians(float(slider2)))
#     print(servo_bawah.value)
#     print(servo_atas.value)
#     # Give servo some time to move
#     sleep(5)
    
#     return render_template('index.html')



def gen(camera):
    while True:
        frame=camera.get_frame()
        yield(b'--frame\r\n'
       b'Content-Type:  image/jpeg\r\n\r\n' + frame +
         b'\r\n\r\n')

@app.route('/video')

def video():
    return Response(gen(Video()),
    mimetype='multipart/x-mixed-replace; boundary=frame')

# @app.route('/capture', methods=["POST"] )
# def capture():

@app.route('/chart')
def chart():
    connection = sqlite3.connect(currentdirectory +"\data.db")
    cursor = connection.cursor()
    query1 = 'SELECT * FROM history_scan'
    result = cursor.execute(query1).fetchall()
    # connection.commit()
    # result = dict((y,x) for x, y in result)
    print(result)
    res = []
    for item in result:
        res.append({
            "created_at": item[0],
            "status": item[1]
        })

    return render_template('chart.html', data=Markup(res))



app.run(debug=True)