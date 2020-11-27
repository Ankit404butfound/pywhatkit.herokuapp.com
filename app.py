from flask import Flask,abort,render_template,request,redirect,url_for,send_file
import os
import random
import string

char = string.ascii_lowercase
file_code_name = {}

app = Flask(__name__)
UPLOAD_FOLDER = ''



@app.route('/')
def index():
    return """<!DOCTYPE html>
<html>
    <head>
        <style>
            .bg{
                background-image: url("https://qphs.fs.quoracdn.net/main-qimg-344fafc838d1be7011f7b926f4583cde");
            }

            .basic-text{
                text-align: center;
                color: rgb(220, 250, 248);
                font-size: 18px;
            }

            h1{
                text-align: center;
                color: rgb(49, 196, 188);
                text-decoration: underline;
            }

            h2{
                text-align: center;
                color: rgb(131, 235, 221);
            }

            a{
                color: rgb(184, 245, 240);
            }

            h3{
                text-align: center;
                color: rgb(164, 238, 228);
            }
            ul{
                text-align: center; 
            }

        </style>
    </head>
    <body class=bg>
        <h1>PyWhatKit</h1>
        <h2>Introduction</h2>
        <div class=basic-text>
            <p><a href="https://pypi.org/project/pywhatkit/" target="blank">PyWhatKit</a> is a Python library with various helpful features solving many daliy life problems. It is an easy to use library which does not requires you to do some additional setup. Currently it has about 100k+ downloads and counting and we regularly update and fix any bug. The source code of this library can be found on <a href="https://github.com/Ankit404butfound/PyatKit">GitHub</a>, you are free update/add some features to it and open a Pull Request, we will review it and include that feature in the next update if the feature was found to be relavent and helpful.</p>
            <h2>Installation</h2>
            <p>This library can be installed by the pip command, open you command prompt and type in the following command...</p>
            <code>pip install pywhatkit</code>
            <h2>Functions of this library</h2>
            <h3><b>sendwhatmsg()</b></h3>
            
        </div>

    </body>
</html>"""

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name = None):
    return "Hello"+name

@app.route("/download")
def download():
    fileid = str(request.args.get("id"))
    name = file_code_name[fileid]
    print(name)
    return send_file(name,as_attachment=True)

    
@app.route('/upload/',methods = ['GET','POST'])
def upload_file():
    if request.method =='POST':
        file = request.files['file[]']
        print(file)
        if file:
            filecode = ""
            for i in range(10):
                filecode = filecode+random.choice(char)
                print(filecode)
            file.save(UPLOAD_FOLDER+"/"+file.filename)
            file_code_name[filecode] = file.filename
              
            return """<!doctype HTML>
<head>
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
</head>
<style>
    body{
        background-color: rgb(199, 241, 234);
        }
    p{
        text-align: center;
        font-size: 20px;
    }
    div{
        margin:150px auto;
    }
</style>
<body>
    <div>
        <h1 style="text-align: center;">File Has be successfully uploaded</h1>
        <p>Use this link to download your file<br><a href="https:/pywhatkit.herokuapp.com/download?id=%s">url</a></p>
</body>"""%filecode
        
    return """<!doctype html>

<title>Upload new File</title>
<style>
    body{
        background-color: rgb(199, 241, 234);
        }
    form{
        text-align: center;
        margin:50px auto;
        
    }
    div{
        margin:150px auto;
        }
    
</style>
<head>
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
</head>
<body>
    <div>
        <h1 style = "text-align:center; color: rgb(7, 92, 73);">Upload new File</h1>
        <form action='' method="POST" enctype="multipart/form-data">
            <p>
                <input type='file' name='file[]'>
                <input type='submit' value='upload'>
            </p>
        </form>
    </div>
</body>"""



if __name__ == '__main__':
    app.run(host= '0.0.0.0')
