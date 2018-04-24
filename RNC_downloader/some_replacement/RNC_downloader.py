import os, flask,StringIO
from flask import *
download_link="http://dgii.gov.do/app/WebApps/consultas/Paginas/RNC/DGII_RCN.zip"


@app.route('/download/', methods=['GET'])
def download():
    url = request.args['url']
    filename = request.args.get('filename', 'image.png')
    r = requests.get(url)
    strIO = StringIO.StringIO(r.content)
return send_file(strIO, as_attachment=True, attachment_filename=filename)