from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

#UPLOAD_FOLDER = os.path.join('D:\\upload', 'images')
UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'images')
ALLOWED_EXTENSIONS = set(['png', 'jpg'])

app = Flask(__name__, template_folder = '.')
app.config['SECRET_KEY'] = 'learning'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.route('/file', methods = ['GET']) #método http
def index():
    return render_template('file.html') #arquivo que a gente vai puxar

def allowed_file(file_name):
    return '.' in file_name and file_name.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS #só vai retornar se o ponto existir e apenas 1 ponto / minusculo


@app.route('/file/uploaded', methods = ['POST']) #método http
def upload_file():
    if 'image' not in request.files:
        return 'A imagem não pode ser enviada!'

    print(request)

    file = request.files['image']
    if file.file_name == '':
        return 'imagem não selecionada'

    if file and allowed_file(file.file_name):
        file_name = secure_filename(file.file_name)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
        "imagem recebida com sucesso"
        
    return redirect(url_for('index'))

app.run(debug = True)