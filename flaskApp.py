from flask import Flask, render_template, Response, jsonify, request, session
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
from wtforms.validators import InputRequired
from detection import run as objectDetection
import os
import cv2

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cyongkypranowo'
app.config['UPLOAD_FOLDER'] = 'static/files'
BASE_URL = 'http://127.0.0.1:5000/'  # Base URL statis dari aplikasi Flask Anda

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Run")

fpsCount = 0
frameSize = 0
detectedObjects = 0
inferenceTimes = ""
resultPath = ""
typeFile = ""

def generate_frames(path):
    yolov9_output = objectDetection(weights='weights/coconut_model.pt', source=path, view_img=False, nosave=True, classes=0)  # Sesuaikan argumen sesuai kebutuhan
    for im0, frameRate, frameShape, totalDetection, inf, pathFile, dataType in yolov9_output:
        ret, buffer = cv2.imencode('.jpg', im0)
        global fpsCount
        fpsCount = str(frameRate)
        global frameSize
        frameSize = str(frameShape[0])
        global detectedObjects
        detectedObjects = str(totalDetection)
        global inferenceTimes
        inferenceTimes = str(inf)
        global resultPath
        resultPath = str(pathFile)
        global typeFile
        typeFile = str(dataType)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/', methods=['GET', 'POST'])
def front():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        session['filePath'] = file_path
        return render_template('index.html', form=form, uploaded=True, filename=filename)
    #remove session
    session.pop('filePath', None)
    return render_template('index.html', form=form, uploaded=False)

@app.route('/detections', methods=['GET', 'POST'])
def detections():
    file_path = session.get('filePath', None)
    if file_path:
        return Response(generate_frames(path=file_path), mimetype='multipart/x-mixed-replace; boundary=frame')
    else:
        return "No video uploaded"

@app.route('/status', methods=['GET'])
def status():
    global fpsCount, detectedObjects, frameSize, inferenceTimes, resultPath, typeFile
    resultPath = resultPath.replace('\\', '/')
    full_url = BASE_URL + resultPath
    return jsonify(fpsresult=fpsCount, dcountresult=detectedObjects, fsizeresult=frameSize, inferenceTimes=inferenceTimes, resultPath=full_url, typeFile=typeFile)

if __name__ == "__main__":
    app.run(debug=True)
