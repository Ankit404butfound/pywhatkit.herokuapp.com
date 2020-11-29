from flask import Flask,abort,render_template,request,redirect,url_for,send_file
import os
import random
import string

char = string.ascii_lowercase
file_code_name = {}

app = Flask(__name__)
UPLOAD_FOLDER = ''

@app.route("/")
def new():
    return"""<!DOCTYPE html>
<html>
    <head>
        <style>
            .center {
              margin: auto;
              width: 70%;
              border: 3px;
              padding: 10px;
            }
            
            .bg{
                /*background-image: url("C:/Users/pc/Desktop/bg3.png");*/
                background-color: rgb(50, 50, 50);
            }
            .basic-text{
                text-align: left;
                color: rgb(217, 233, 236);
                font-size: 20px;
                align-content: center;
            }
            h1{
                text-align: center;
                color: rgb(16, 223, 238);
                text-decoration: underline;
            }
            h2{
                text-align: left;
                color: rgb(40, 236, 194);
            }
            a{
                color: rgb(184, 245, 240);
            
            }
            h3, b{
                text-align: left;
                color: rgb(133, 245, 230);
            }
            ul{
                text-align: center; 
            }
            .margn div{
                margin: 70px auto;
            }
            .onhover a:hover{
                background-color: rgb(137, 144, 145);
            }
            h4{
                color: rgb(139, 99, 248);
            }
            .mid{
                display: block;
                margin-left: auto;
                margin-right: auto;
                width: 9%;
}

        </style>
    </head>
    <body class=bg>
        <div class=basic-text>
            <h1>PyWhatKit</h1>
        </div>
            <div class="onhover">
                <div class=mid>
                <a href="https://github.com/Ankit404butfound/PywhatKit" target="blank"><img src="https://raw.githubusercontent.com/Ankit404butfound/PyWhatKit/master/Images/github_i.png" style="width:30px;height:30px;"></a>
                <a href="https://www.quora.com/What-was-one-of-the-first-things-you-made-with-Python/answer/Ankit-Raj-Mahapatra-3" target="blank"><img src="https://raw.githubusercontent.com/Ankit404butfound/PyWhatKit/master/Images/quora.png" style="width:30px;height:30px;"></a>
                <img src="https://raw.githubusercontent.com/Ankit404butfound/PyWhatKit/master/Images/yt.png" style="width:30px;height:30px;">
            </div>
        </div>
        
           <div class=basic-text>
            <div class=center>
            <div class=margn>
                <br><a href="https://pypi.org/project/pywhatkit/" target="blank">PyWhatKit</a> is a Python library with various
                 helpful features. It is an easy to use library which does not requires you to do some additional setup. Currently it has about 100k+ downloads and counting and we regularly update and fix any bug. The source code of this library can be found on <a href="https://github.com/Ankit404butfound/PywhatKit">GitHub</a>, you are free update/add some features to it and open a Pull Request, we will review it and include that feature in the next update if the feature was found to be relavent and helpful.</p>
                <div>
                    <h2>Installation</h2>
                    <p>This library can be installed by the pip command, open you command prompt and type in the following command...</p>
                    <code>pip install pywhatkit</code>
                </div>
                <div>
                    <h2>Functions of this library</h2>
                    <p>First import the library using the command <code>import pywhatkit as kit</code> and then proceed to call the functions</p>
                    <h3>kit.sendwhatmsg()</h3>
                    <p>
                        This function can be used to send WhatsApp message at certain time<br><br>
                        <img src="https://raw.githubusercontent.com/Ankit404butfound/PyWhatKit/master/Images/sendwhatmsg.png" style="width: 900px;height: 500px;"><br>
                        <h4>The parameters are</h4>
                        <b>phone_num</b> (required) - Phone number of target with country code
                        <br><b>message</b> (required) - Message that you want to sendwhatmsg
                        <br><b>time_hour</b> (required) - Hours at which you want to send message in 24 hour format
                        <br><b>time_min</b> (required) - Minutes at which you want to send message
                        <br><b>wait_time</b> (optional, val=20) - Seconds after which the message will be sent after opening the web
                        <br><b>print_waitTime</b> (optional, val=True) - Will print the remaining time if set to true
                    </p><br>
                    <h3>kit.playonyt()</h3>
                    <p>
                        This function can be used to search and play a particular video on YouTube by using just the keyword, like "Shape of You song"<br><br>
                        <img src="https://raw.githubusercontent.com/Ankit404butfound/PyWhatKit/master/Images/playonyt.png" style="width: 900px;height: 500px;"><br>
                        <h4>The parameters are</h4>
                        <b>topic</b> (required) - Topic or title that is related to the video 
                    </p>
                </div>
            </div>
    </div>
        </div>
    </body>
</html>"""


@app.route('/old')
def index():
    return """<!DOCTYPE html>
<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            .bg{
                /*background-image: url("C:/Users/pc/Desktop/bg3.png");*/
                background-color: rgb(2, 2, 0);
            }

            .basic-text{
                text-align: center;
                color: rgb(217, 233, 236);
                font-size: 20px;
            }

            h1{
                text-align: center;
                color: rgb(16, 223, 238);
                text-decoration: underline;
            }

            h2{
                text-align: center;
                color: rgb(40, 236, 194);
            }

            a{
                color: rgb(184, 245, 240);
            }

            h3, b{
                text-align: center;
                color: rgb(133, 245, 230);
            }
            ul{
                text-align: center; 
            }
            .margn div{
                margin: 70px auto;
            }

            .onhover a:hover{
                background-color: rgb(137, 144, 145);
            }

            h4{
                color: rgb(139, 99, 248);
            }

            

        </style>
    </head>
    <body class=bg>
        <div class=basic-text>
            <h1>PyWhatKit</h1>
            <div class="onhover">
                <a href="https://github.com/Ankit404butfound/PywhatKit" target="blank"><img src="https://raw.githubusercontent.com/Ankit404butfound/PyWhatKit/master/Images/github_i.png" style="width:30px;height:30px;"></a>
                <a href="https://www.quora.com/What-was-one-of-the-first-things-you-made-with-Python/answer/Ankit-Raj-Mahapatra-3" target="blank"><img src="https://raw.githubusercontent.com/Ankit404butfound/PyWhatKit/master/Images/quora.png" style="width:30px;height:30px;"></a>
                <img src="https://raw.githubusercontent.com/Ankit404butfound/PyWhatKit/master/Images/yt.png" style="width:30px;height:30px;">
            </div>
            <div class=margn>
                <br><a href="https://pypi.org/project/pywhatkit/" target="blank">PyWhatKit</a> is a Python library with various
                 helpful features. It is an easy to use library which does not requires you to do some additional setup. Currently it has about 100k+ downloads and counting and we regularly update and fix any bug. The source code of this library can be found on <a href="https://github.com/Ankit404butfound/PywhatKit">GitHub</a>, you are free update/add some features to it and open a Pull Request, we will review it and include that feature in the next update if the feature was found to be relavent and helpful.</p>
                <div>
                    <h2>Installation</h2>
                    <p>This library can be installed by the pip command, open you command prompt and type in the following command...</p>
                    <code>pip install pywhatkit</code>
                </div>
                <div>
                    <h2>Functions of this library</h2>
                    <p>First import the library using the command <code>import pywhatkit as kit</code> and then proceed to call the functions</p>
                    <h3>kit.sendwhatmsg()</h3>
                    <p>
                        This function can be used to send WhatsApp message at certain time<br><br>
                        <img src="https://raw.githubusercontent.com/Ankit404butfound/PyWhatKit/master/Images/sendwhatmsg.png" style="width: 900px;height: 500px;"><br>
                        <h4>The parameters are</h4>
                        <b>phone_num</b> (required) - Phone number of target with country code
                        <br><b>message</b> (required) - Message that you want to sendwhatmsg
                        <br><b>time_hour</b> (required) - Hours at which you want to send message in 24 hour format
                        <br><b>time_min</b> (required) - Minutes at which you want to send message
                        <br><b>wait_time</b> (optional, val=20) - Seconds after which the message will be sent after opening the web
                        <br><b>print_waitTime</b> (optional, val=True) - Will print the remaining time if set to true
                    </p><br>
                    <h3>kit.playonyt()</h3>
                    <p>
                        This function can be used to search and play a particular video on YouTube by using just the keyword, like "Shape of You song"<br><br>
                        <img src="https://raw.githubusercontent.com/Ankit404butfound/PyWhatKit/master/Images/playonyt.png" style="width: 900px;height: 500px;"><br>
                        <h4>The parameters are</h4>
                        <b>topic</b> (required) - Topic or title that is related to the video 
                    </p>
                </div>
            </div>
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
            url = "https://pywhatkit.herokuapp.com//download?id="
            for i in range(10):
                filecode = filecode+random.choice(char)
                print(filecode)
            url = url+filecode
            file.save(file.filename)
            file_code_name[filecode] = file.filename
            print(file_code_name)
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
        <p>Use this link to download your file<br></p>
        <p><a href="%s" target="blank">https:/pywhatkit.herokuapp.com/download?id=%s</a></p>
</body>"""%(url,filecode)
        
    return """<!doctype html>

<title>Upload new File</title>
<meta name="viewport" content="width=device-width,initial-scale=1.0">
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
