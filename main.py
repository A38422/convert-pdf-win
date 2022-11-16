from flask import Flask, request, Response
from flask_restful import Api

from subprocess import Popen

app = Flask(__name__)
api = Api(app)

LIBRE_OFFICE = r"C:\Program Files\LibreOffice\program\soffice.exe"


def convert_to_pdf(input_docx, out_folder):
    p = Popen([LIBRE_OFFICE, '--headless', '--convert-to', 'pdf', '--outdir',
               out_folder, input_docx])
    p.communicate()


@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == 'POST':
        out_folder = request.form['out_folder']
        sample_doc = request.form['sample_doc']
        convert_to_pdf(sample_doc, out_folder)
        return Response(f"{'out_folder':{out_folder}}", status=201, mimetype='application/json')
    else:
        return Response("{'msg':'get'}", status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run()
