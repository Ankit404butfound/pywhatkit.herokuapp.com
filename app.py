from flask import Flask, request, redirect
import re
import urllib.request
import string
import os
import numpy as np
from PIL import Image
import cv2
import random
import requests


char = string.ascii_lowercase
file_code_name = {}

UPLOAD_FOLDER = ''

width = 50
height = 0
newwidth = 0
arr = string.ascii_letters
arr = arr + string.digits + "+,.-? "
letss = string.ascii_letters

app = Flask(__name__, static_url_path='')

try:
    os.mkdir("static")
except:
    pass


def getimg(case,col):
    global width,height,back
    try:
        url = "https://raw.githubusercontent.com/Ankit404butfound/HomeworkMachine/master/Image/%s.png"%case
        imglink=urllib.request.urlopen(url)
    except:
        url = "https://raw.githubusercontent.com/Ankit404butfound/HomeworkMachine/master/Image/%s.PNG"%case
        imglink=urllib.request.urlopen(url)
    imgNp=np.array(bytearray(imglink.read()))
    img = cv2.imdecode(imgNp,-1)
    cv2.imwrite(r"%s.png"%case,img)
    img = cv2.imread("%s.png"%case)
    img[np.where((img!=[255,255,255]).all(axis=2))] = col
    cv2.imwrite("chr.png",img)
    cases = Image.open("chr.png")
    back.paste(cases,(width,height))
    newwidth = cases.width
    width = width + newwidth


def text_to_handwriting(string,rgb=[0,0,138]):
    """Convert the texts passed into handwritten characters"""
    save_path = ""
    for i in range(10):
        save_path = save_path+random.choice(letss)
    
    global arr, width, height, back
    #rgb.reverse() not working, IDK why.
    try:
        back = Image.open("zback.png")
    except:
        url = "https://raw.githubusercontent.com/Ankit404butfound/HomeworkMachine/master/Image/zback.png"
        imglink=urllib.request.urlopen(url)
        imgNp=np.array(bytearray(imglink.read()))
        img = cv2.imdecode(imgNp,-1)
        cv2.imwrite("zback.png",img)
        back = Image.open("zback.png")
    rgb = [rgb[2],rgb[1],rgb[0]]
    count = -1
    lst = string.split()
    for letter in string:
        if width + 150 >= back.width or ord(letter) == 10:
            height = height + 227
            width = 50
        if letter in arr:
            if letter == " ":
                count += 1
                letter = "zspace"
                wrdlen = len(lst[count+1])
                if wrdlen*110 >= back.width-width:
                    width = 50
                    height = height+227

            elif letter.isupper():
                letter = "c"+letter.lower()
            elif letter == ",":
                letter = "coma"
            elif letter == ".":
                letter = "fs"
            elif letter == "?":
                letter = "que"

            getimg(letter,rgb)

    #back.show()
    back.save(f"static/{save_path}.png")
    back.close()
    back = Image.open("zback.png")
    #rgb = [0,0,138]
    width = 50
    height = 0
    newwidth = 0
    return save_path
    
          
   



@app.route("/handwriting")
def api():
    text = request.args.get("text")
    rgb = request.args.get("rgb")
    if rgb:
        path = text_to_handwriting(str(text),str(rgb).split(","))
    else:
        path = text_to_handwriting(str(text))
    return redirect(f"https://pywhatkit.herokuapp.com/{path}.png",302)

@app.route("/request-feature")
def new_feature():
    return redirect("https://docs.google.com/forms/d/1gReJDTC7MpO-4wUqrByGibF5fFCSjMsUsQuB5nk2FjI/",302)


@app.route("/")
def new():
    return"""<!DOCTYPE html>
<!DOCTYPE html>
<html>
    <head>
      <meta name="viewport" content="width=device-width,initial-scale=1.0" />
      <meta name="theme-color" content="#000000" />
      <link rel="icon" href="https://github.com/Ankit404butfound/PyWhatKit/blob/master/Images/icon.PNG?raw=true" type="image/gif" sizes="16x16">
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" integrity="sha384-wvfXpqpZZVQGK6TAh5PVlGOfQNHSoD2xbE+QkPxCAFlNEevoEH3Sl0sibVcOQVnN" crossorigin="anonymous">     
<style>
            .center {
              margin: auto;
              width: 90%;
              border: 3px;
              padding: 10px;
            }
            
            .bg{
                /*background-image: url("C:/Users/pc/Desktop/bg3.png");*/
                background-color: rgb(37, 37, 37);
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
            h3{
                text-align: center;
                background-color: rgb(49, 48, 48);
                color: rgb(0, 255, 106);
            }

            b{
                color: rgb(255, 255, 255)
            }
            ul{
                text-align: center; 
            }
            .margn div{
                margin: 60px auto;
            }
            .mid i:hover{
                color:#ffffff;
            }
            h4{
                color: rgb(191, 134, 255);
            }
            .mid{
                margin:10px auto;
                text-align: center;
                font-size: 40px;
 
            } 
            img{
                width:100%;
            }
        </style>
    </head>
    <body class="bg">
        <div class="basic-text">
            <h1 style="background-color: rgb(58, 58, 58);">PyWhatKit</h1>
        </div>
    
            <div class="mid">
                <a href="https://github.com/Ankit404butfound/PywhatKit" target="_blank"><i class="fa fa-github"></i></a>
                <a href="https://www.quora.com/What-was-one-of-the-first-things-you-made-with-Python/answer/Ankit-Raj-Mahapatra-3" target="_blank"><i class="fa fa-quora"></i></a>
                <a href="#"><i class="fa fa-youtube"></i></a>
            </div>
        <div style="text-align: center; color: rgb(217, 233, 236); font-size: 20px;">
           
            <div class="center">
                <div class="margn">
                    <br><a href="https://pypi.org/project/pywhatkit/" target="_blank">PyWhatKit</a> is a Python library with various
                    helpful features. It is an easy to use library which does not requires you to do some additional setup. Currently it has about 100k+ downloads and counting and we regularly update and fix any bug. The source code of this library can be found on <a href="https://github.com/Ankit404butfound/PywhatKit">GitHub</a>, you are free update/add some features to it and open a Pull Request, we will review it and include that feature in the next update if the feature was found to be relavent and helpful.
                    <div class="basic-text">
                        <div>
                            <h2>Installation</h2>
                            <p>This library can be installed by the pip command, open you command prompt and type in the following command...</p>
                            <code>pip install pywhatkit</code>
                        </div>
                
                        <h2>Functions of this library</h2>
                        <p>First import the library using the command <code>import pywhatkit as kit</code> and then proceed to call the functions</p>

                        <h3 id="sendwhatmsg">kit.sendwhatmsg()</h3>
                        <p>
                            This function can be used to send WhatsApp message at certain time<br><br>
                            <img src="https://raw.githubusercontent.com/Ankit404butfound/PyWhatKit/master/Images/sendwhatmsg.png"><br>
                            <h4>The parameters are</h4>
                            <b>phone_num</b> (required) - Phone number of target with country code
                            <br><b>message</b> (required) - Message that you want to sendwhatmsg
                            <br><b>time_hour</b> (required) - Hours at which you want to send message in 24 hour format
                            <br><b>time_min</b> (required) - Minutes at which you want to send message
                            <br><b>wait_time</b> (optional, val=20) - Seconds after which the message will be sent after opening the web
                            <br><b>print_waitTime</b> (optional, val=True) - Will print the remaining time if set to true<br>
                        </p>
                        
                        <p>
                            <h4>Some common errors</h4>
                            <b>CountryCodeException</b> - Check if the phone number passed into the paramter has <a href="https://en.wikipedia.org/wiki/List_of_country_calling_codes" target="_blank">country code</a><br>
                            <b>Message not getting delivered</b> - Check internet speed and increase wait_time to 30 or above
                            <b>CallTimeException</b> - The web takes some time to load so some delay is required, make sure the seconds left is greater than the wait_time<br>
                            <b>SyntaxError</b> - Make sure the first two parameters are string and the rest are int
                        </p>
                        
                        <br><h3 id="playonyt">kit.playonyt()</h3>
                        <p>
                            This function can be used to search and play a particular video on YouTube by using just the keyword, like "Shape of You song"<br><br>
                            <img src="https://raw.githubusercontent.com/Ankit404butfound/PyWhatKit/master/Images/playonyt.png" ><br>
                            <h4>The parameters are</h4>
                            <b>topic</b> (required) - Topic or title that is related to the video
                        </p>
                        <p>
                            <h4>Some common errors</h4>
                            <b>Video not opening</b> - Make sure the topic exists or you have provided proper spelling
                        </p>

                        <br><h3 id="search">kit.search()</h3>
                        <p>
                        This function can be used to make a google search for any term<br><br>
                        <img src="https://raw.githubusercontent.com/Ankit404butfound/PyWhatKit/master/Images/search.PNG">
                        <h4>The parameters are</h4>
                        <b>topic</b> (required) - Topic or title that you want to search
                        </p>
                        
                        <br><h3 id="info">kit.info()</h3>
                        
                        <p>
                        This function can be used to fetch information about any topic<br><br>
                        <img src="https://raw.githubusercontent.com/Ankit404butfound/PyWhatKit/master/Images/info.PNG">
                        <h4>The parameters are</h4>
                        <b>topic</b> (required) - Topic or title that you want to get information about<br>
                        <b>lines</b> (optional, val=3) - Number of lines that you want to print about it
                        </p>
                        <p>
                            <h4>Some common errors</h4>
                            <b>Not returning paragraph</b> - Make sure the topic exists and you are providing specific title
                        </p>

                        <br><h3 id="asciiart">kit.image_to_ascii_art()</h3>
                        <p>
                        This function can be used to convert any image to ASCII art<br><br>
                        <img src="https://raw.githubusercontent.com/Ankit404butfound/PyWhatKit/master/Images/asciiart.PNG">
                        <h4>The parameters are</h4>
                        <b>imgpath</b> (required) - Path to the image that you want to convert<br>
                        <b>output_file</b> (optional, val=pywhatkit_asciiart.txt") - File where you want to save the output characters
                        </p>

                        <p>
                            <h4>Some common errors</h4>
                            <b>File not found</b> - Make sure that the path of the image is valid
                        </p>

                        <br><h3 id="handwriting">kit.text_to_handwriting()</h3>
                        <p>
                        This function can be used to convert text to hand written characters, the character sets has been written by me<br><br>
                        <img src="https://raw.githubusercontent.com/Ankit404butfound/PyWhatKit/master/Images/text_to_handwriting.PNG">
                        <h4>The parameters are</h4>
                        <b>string</b> (required) - String that you want to convert to handwritten text<br>
                        <b>save_to</b> (optional, val = "pywhatkit.png") - Path where the image will be saved<br>
                        <b>rgb</b> (optional, val = [0,0,138]) - Color of the handwritten character in rgb format
                        </p>
                    </div>
                </div>
            </div>
        </div>
        <div style="text-align: right;">
            <a href="about-me">About me</a>
        </div>
    </body>
</html>
"""

@app.route("/about-me")
def me():
    return """<!DOCTYPE html>
<html>
    <head>
        <style>
            .page-content{
                background-image: url("https://qphs.fs.quoracdn.net/main-qimg-344fafc838d1be7011f7b926f4583cde");
            }

            .page-text{
                text-align: center;
                color: rgb(200, 255, 241);
                font-size: 20px;
                margin:100px auto;
            }

            h1{
                text-decoration: underline;
                }

            a{
                color: rgb(110, 185, 155);
            }

    </style>
    </head>
    <body class=page-content>
        <h1 style="color:rgb(16, 223, 238)"; align="center"; >
            ANKIT RAJ MAHAPATRA
        </h1>
        <div class=page-text>
            <p>Hello there, I am Ankit Raj aka Ankit Raj Mahpatra, I am a first-year BTech student.</p>
            <p>I know a bit of <a href="https://www.python.org" target="blank">Python</a>, <a href="https://www.arduino.cc" target="blank">Arduino</a> and currently learning HTML-CSS.</p>
            <p>I am the creator of <a href="https://pypi.org/project/pywhatkit/" target="blank">PyWhatKit</a> which has over 100k userbase till now.</p>
            <p>I have a <a href="https://github.com/Ankit404butfound" target="blank">GitHub account</a> where I share most of my projects, there are some basic CS projects only.</p>
            <p>Currently, I am living in Delhi and I have been to almost 5 states of India.</p>

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


@app.route('/playonyt')
def playonyt():
    """Will play video on following topic, takes about 10 to 15 seconds to load"""
    topic = request.args.get("topic")
    url = 'https://www.youtube.com/results?q=' + topic
    count = 0
    cont = requests.get(url)
    data = cont.content
    data = str(data)
    lst = data.split('"')
    for i in lst:
        count+=1
        if i == 'WEB_PAGE_TYPE_WATCH':
            break
    if lst[count-5] == "/results":
        raise Exception("No video found.")
    
    #print("Videos found, opening most recent video")
    #web.open("https://www.youtube.com"+lst[count-5])
    return "https://www.youtube.com"+lst[count-5]



@app.route("/remote-kit")
def rkit():
    return """

<!DOCTYPE html>
<html>
    <head>
      <meta name="viewport" content="width=device-width,initial-scale=1.0" />
      <meta name="theme-color" content="#000000" />
      <link rel="icon" href="https://github.com/Ankit404butfound/PyWhatKit/blob/master/Images/icon.PNG?raw=true" type="image/gif" sizes="16x16">
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" integrity="sha384-wvfXpqpZZVQGK6TAh5PVlGOfQNHSoD2xbE+QkPxCAFlNEevoEH3Sl0sibVcOQVnN" crossorigin="anonymous">     
<style>
            .center {
              margin: auto;
              width: 90%;
              border: 3px;
              padding: 10px;
            }
            
            .bg{
                /*background-image: url("C:/Users/pc/Desktop/bg3.png");*/
                background-color: rgb(37, 37, 37);
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
            h3{
                text-align: center;
                background-color: rgb(49, 48, 48);
                color: rgb(0, 255, 106);
            }

            b{
                color: rgb(255, 255, 255)
            }
            ul{
                text-align: center; 
            }
            .margn div{
                margin: 60px auto;
            }
            .mid i:hover{
                color:#ffffff;
            }
            h4{
                color: rgb(191, 134, 255);
            }
            .mid{
                margin:10px auto;
                text-align: center;
                font-size: 40px;
 
            } 
            img{
                width:100%;
            }
        </style>
    </head>
    <body class="bg">
        <div class="basic-text">
            <h1 style="background-color: rgb(58, 58, 58);">PyWhatKit - Feature test</h1>
        </div>
    
            <div class="mid">
                <a href="https://github.com/Ankit404butfound/Remote_Mouse_Keyboard" target="_blank"><i class="fa fa-github"></i></a>
                
            </div>
        <div style="text-align: center; color: rgb(217, 233, 236); font-size: 20px;">
           
            <div class="center">
                <div class="margn">
                    <br><a href="https://github.com/Ankit404butfound/Remote_Mouse_Keyboard" target="_blank">RemoteKit</a> is an upcoming feature of PyWhatKit, it allows you to controll your PC wirelessly on same network, you can controll the PC without installing any thing on your phone, this feature is written in Python and JavaScript with front-end in HTML-CSS.<div class="basic-text">
                        <div>
                            <h2><u>Setup</u></h2>
                            <p>In order to test this feature you need to <a href="https://github.com/Ankit404butfound/Remote_Mouse_Keyboard" target="_blank">download the code</a> and install few libraries, run the following command to install them</p>
                            <code>pip install flask <br>
                            pip install pyautogui</code> 
                        </div>
                
                        <h2><u>Usage</u></h2>
                        <p>First, make sure your PC and the phone that you want to control PC with, are on the same network, either connected to hotspot or WiFi<br><br>
                            <img src="https://raw.githubusercontent.com/Ankit404butfound/Remote_Mouse_Keyboard/main/Images/wifi.PNG"><br><br>
                            Now open command prompt in the same directory where you downloaded the codes and type the following and hit enter<br><br>
                            <code>python RemoteKit.py</code><br><br>
                            You should see something like this<br><br>
                            <img src="https://raw.githubusercontent.com/Ankit404butfound/Remote_Mouse_Keyboard/main/Images/startt.PNG"><br><br>
                            Now get the IPV4 address of your PC, on windows you can get it by typing "ipconfig" on command prompt, relavent command for all OS.<br><br>
                            <img src="https://raw.githubusercontent.com/Ankit404butfound/Remote_Mouse_Keyboard/main/Images/ip.PNG"><br><br>
                            Now open any browser on your phone and type <code>IPV4_address:8000</code> and hit enter.<br><br>
                            <img src="https://raw.githubusercontent.com/Ankit404butfound/Remote_Mouse_Keyboard/main/Images/phn.PNG"><br><br>
                            Move your finger over the grey area, your cursor should also move.
                            Report any issue on GitHub or directly contact us on <a href="https://discord.gg/uwznv4jKgk">Discord</a>
                            
                        </p>

                    </div>
                </div>
            </div>
        </div>
    </body>
</html>
"""



if __name__ == '__main__':
    app.run(host= '0.0.0.0')
