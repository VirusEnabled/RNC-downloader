from flask import Flask,render_template


app = Flask("__name__")

download_link="http://dgii.gov.do/app/WebApps/consultas/Paginas/RNC/DGII_RCN.zip"

@app.route("/",methods=["GET"])
def home():
	return render_template("home.html")



#@app.route('/download/', methods=['GET'])
#def download():
#	url = request.args['url']
#	filename = request.args.get('filename', 'image.png')
#	r = requests.get(url)
#	strIO = StringIO.StringIO(r.content)
#	return send_file(strIO, as_attachment=True, attachment_filename=filename)

if __name__ == '__main__':
	app.run(debug = True)