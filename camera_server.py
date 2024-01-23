from flask import Flask, render_template, Response, request
import cv2
import numpy as np

app = Flask(__name__)

# Set up a global variable to store the latest frame
global_frame = None

def gen():
    while True:
        if global_frame is not None:
            # Encode the frame in JPEG format
            _, buffer = cv2.imencode('.jpg', global_frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/upload', methods=['POST'])
def upload():
    global global_frame
    frame_data = request.data
    frame_np = np.frombuffer(frame_data, dtype=np.uint8)
    global_frame = cv2.imdecode(frame_np, flags=1)  # 1 means load color image
    return 'OK'

@app.route('/preview')
def preview():
    return render_template('preview.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
