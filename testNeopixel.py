import board
import neopixel
import time
import numpy
from PIL import Image
import random
import pickle


pixels = neopixel.NeoPixel(board.D21, 256, auto_write=False)
brightness = 50
state = 2
metastate = "default"

def clearScreen():
    pixels.fill((0,0,0))


def displayImg(imageName, reflect):
    img = numpy.array(Image.open("icons/" + imageName))
    pixNum = 0

    #print(img)
    
    for i in range(len(img)):
        if (i % 2 == 1) == reflect:
            for j in reversed(range(len(img[i]))):
                # odd rows right to left
                pixels[pixNum] = (0, brightness*img[i][j], 0)
                pixNum += 1
        else:
            for j in range(len(img[i])):
                # even rows, left to right
                pixels[pixNum] = (0, brightness*img[i][j], 0)
                pixNum += 1
    pixels.show()


def longDelay():
    time.sleep(random.uniform(0.3,0.8))

def setState(newState):
    longDelay()
    global state
    state = newState
    if state <= 2:
        displayImg('eye' + str(state) + '.gif', True)
    else:
        displayImg('eye' + str(5 - state) + '.gif', False)

clearScreen()


while True:
    with open('deepSpeech/shared.pkl', 'rb') as f:
        metastate = pickle.load(f)
    
    print(metastate)

    if metastate == "default":
        randVal = random.random()
        if state == 1:
            if randVal < 0.5:
                setState(2)
            else:
                longDelay()
        elif state == 2:
            if randVal < 0.25:
                setState(1)
            elif randVal < 0.5:
                setState(3)
            elif randVal < 0.75:
                longDelay()
            else:
                displayImg('eye3.gif', True)
                time.sleep(0.05)
                displayImg('eye4.gif', True)
                time.sleep(0.05)
                displayImg('eye3.gif', True)
                time.sleep(0.05)
                displayImg('eye2.gif', True)
                longDelay()
        elif state == 3:
            if randVal < 0.25:
                setState(2)
            elif randVal < 0.5:
                setState(4)
            elif randVal < 0.75:
                longDelay()
            else:
                displayImg('eye3.gif', False)
                time.sleep(0.05)
                displayImg('eye4.gif', False)
                time.sleep(0.05)
                displayImg('eye3.gif', False)
                time.sleep(0.05)
                displayImg('eye2.gif', False)
                longDelay()
        elif state == 4:
            if randVal < 0.5:
                setState(3)
            else:
                longDelay()
    elif metastate == "pumpkin":
        displayImg('pumpkin.gif', False)
    elif metastate == "skeleton":
        displayImg('skull.gif', False)
    elif metastate == "yes":
        displayImg('check.gif', False)
    elif metastate == "no":
        displayImg('x.gif', False)
    elif metastate == "!":
        displayImg('!.gif', False)
    elif metastate == "?":
        displayImg('?.gif', False)
    elif metastate == "clock":
        displayImg('clock1.gif', False)
        time.sleep(0.1)
        displayImg('clock2.gif', False)
        time.sleep(0.1)
        displayImg('clock3.gif', False)
        time.sleep(0.1)
        displayImg('clock4.gif', False)
        time.sleep(0.1)
        displayImg('clock5.gif', False)
        time.sleep(0.1)
        displayImg('clock6.gif', False)
        time.sleep(0.1)
        displayImg('clock7.gif', False)
        time.sleep(0.1)
        displayImg('clock8.gif', False)
    elif metastate == "heart":
        displayImg('heart.gif', False) 
    elif metastate == "note":
        displayImg('note.gif', False)
        # play music here?
    elif metastate == "pi":
        displayImg('pi.gif', False)
    elif metastate == "wave":
        displayImg('wave1.gif', False)
        time.sleep(0.5)
        displayImg('wave2.gif', False)
        time.sleep(0.5)
        displayImg('wave3.gif', False)
        time.sleep(0.5)
        displayImg('wave2.gif', False)
    elif metastate == "wireless":
        displayImg('wireless1.gif', False)
        time.sleep(0.5)
        displayImg('wireless2.gif', False)
        time.sleep(0.5)
        displayImg('wireless3.gif', False)
    elif metastate == "clear":
        displayImg('clear.gif', False)

    time.sleep(0.5)
