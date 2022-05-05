from sense_hat import SenseHat
from random import randint
import sys
import requests
import datetime
import time
from PIL import Image
from resizeimage import resizeimage
sense = SenseHat()
sense.set_rotation(180)

def lowLighttrue():
      sense.low_light = True

def lowLightfalse():
      sense.low_light = False

#def exitLoop():
#    print("Exiting")
#    sys.exit("Exiting on buttonPress")

def displayClock():
    global exitLoop 
    exitLoop = "unset"
    while(True):
        bg = getTextColor()
        now = datetime.datetime.now()
        sense.show_message("Time: "+str(now.hour) + ":" + str(now.minute), scroll_speed=0.08, text_colour=bg, back_colour=(10,10,10))
        sense.show_message("Weather: "+fetchCurrentConditions(),scroll_speed=0.08, text_colour=bg)
        #displayImage('icon.png')
        sense.stick.direction_up = lowLighttrue
        sense.stick.direction_down = lowLightfalse
        if(exitLoop == "set"):
            sense.clear()
            break
            #sense.stick.direction_right = exitLoop
            #for event in sense.stick.get_events():
            #    print(event.direction, event.action)
            #    if(event.direction=="right"):
            #        print("breaking now")
            #        break
            
        #sense.clear()
    return 'Done'

def getTextColor():
    num1 = randint(0,255)
    num2 = randint(0,255)
    num3 = randint(0,255)
    color = (num1,num2,num3)
    return color

def displayImage(imageName):
    sense.load_image(imageName) 
    time.sleep(5)

def displayMessage(message):
    exitLoop="set"
    sense.clear()
    sense.show_message(message, text_colour=getTextColor())
    return message

def fetchCurrentConditions():
     r = requests.get('http://api.openweathermap.org/data/2.5/weather?id=5375480&APPID=d7b7a157926739ecefcb4c4c0882a159')
     result=r.json()
     weatherMain=result["weather"][0]["main"]
     desc=result["weather"][0]["description"]
     icon=result["weather"][0]["icon"]
     icon_request=requests.get("http://openweathermap.org/img/w/"+icon+".png")
     with open(icon+'.png', 'wb') as f:
         f.write(icon_request.content)
     with open(icon+'.png', 'r+b') as f:
         with Image.open(f) as image:
             cover = resizeimage.resize_cover(image, [8,8])
             cover.save('icon.png', image.format)
     return weatherMain
