from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from twilio.rest import Client
from flask import Flask
from flask import request
from flask import send_from_directory
app = Flask(__name__)
app.config

# create image and save it
W, H = (100,100)
img = Image.new("RGBA",(W,H),"#00274C")
draw = ImageDraw.Draw(img)
myfont = ImageFont.truetype('/Library/Fonts/Arial.ttf', 10)
w, h = draw.textsize("Sharkey")
draw.text(((W-w)/2,(H-h)/2), "Sharkey", fill="#FFCB05")
img.save('image.png')

# locate image
@app.route('/image.png', methods=['GET', 'POST'])
def uploaded_file(filename):
    return send_from_directory("/Users/jacksharkey/Desktop/photo",
                               filename)

# send text
account_sid = "ACb7ae4c940d199198375051874e9aa34e"
auth_token  = "530d608acb95ea00bd5a60422b1421b7"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+15105095903", 
    from_="+12035909034",
    body="Made a temp script.",
    media_url= 'http://242e1119.ngrok.io/{}'.format("image.png"))