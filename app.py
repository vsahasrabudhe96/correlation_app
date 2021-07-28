from flask import Flask, render_template, request, redirect, url_for, flash, jsonify,send_from_directory
import os
import pandas as pd
import seaborn as sns


app = Flask(__name__)

app.config["DEBUG"] = True

if not os.path.exists("static/files"):
    os.mkdir("static/")
    os.mkdir("static/files")
if not os.path.exists("heatmaps/"):
    os.mkdir("heatmaps/")

UPLOAD_FOLDER = 'static/files'
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


IMAGE_FOLDER = 'heatmaps/'
app.config["IMAGE_FOLDER"] = IMAGE_FOLDER

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/heatmap",methods=["GET", "POST"])
def heatmap():
    if request.method == "POST":
        global image_name
        target = UPLOAD_FOLDER
        print(target)

        if not os.path.isdir(target):
            os.mkdir(target)
        uploaded_file = request.files.get("csvfile")
        print(uploaded_file)
        print("DONE")
        file_path = os.path.join(target, uploaded_file.filename)
        print("DONE fp")
        print(file_path)
            # set the file path
        uploaded_file.save(file_path)
        print("SAVING THE FILE")
            # save the file
        print(uploaded_file.filename)

        if file_path.split('.')[-1]=='csv':
            data = pd.read_csv(file_path)
        else:
            data = pd.read_csv(file_path, sep='\t')
        print("DATA READ PROPERLY")
        sns.set(rc={'figure.figsize':(16,6)})
        # plt.figure(figsize=(16, 6))
        heatmap = sns.heatmap(data.corr(), vmin=-1, vmax=1, annot=True, cmap='rainbow')
        heatmap.set_title('Correlation Heatmap__' +uploaded_file.filename, fontdict={'fontsize':18}, pad=12)              
        image_name= os.path.join(IMAGE_FOLDER , uploaded_file.filename + '_heatmap.png')
        heatmap.figure.savefig(image_name)
    return send_from_directory(app.config["IMAGE_FOLDER"], uploaded_file.filename + '_heatmap.png')
    
if __name__ == '__main__':
    app.run(debug=True)
