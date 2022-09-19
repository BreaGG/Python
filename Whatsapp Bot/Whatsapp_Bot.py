import pyautogui as pt
from time import sleep
import paperclip
import random
import pyperclip


sleep(2)

position1 = pt.locateOnScreen("Smiley_paperclip.PNG", confidence= .6)
x = position1[0]
y = position1[1]


#get message
def get_message():
    global x, y

    position =  pt.locateOnScreen("Smiley_paperclip.PNG", confidence=.6)
    x = position[0]
    y = position[1]
    pt.moºveTo(x, y, duration=.05)
    pt.moveTo(x + 70, y -55, duration=.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12,15)
    pt.click()
    whatsapp_message = pyperclip.paste()
    pt.click()
    print("message recived: " + whatsapp_message)

    return  whatsapp_message

#posts
def post_response(message):
    global x,y

    position =  pt.locateOnScreen("Smiley_paperclip.PNG", confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x + 200, y + 20, duration=.5)
    pt.click()
    pt.typewrite(message, interval=0.1)

    pt.typewrite("\n", interval=.01)

# process response
def process_response(message):
    random_no = random.randrange(3)

    if "?" in str(message).lower():
        return "no preguntes"

    else:
        if random_no == 0:
            return "hello world"
        elif random_no == 1:
            return "recuerda ducharte"
        else:
            return "tengo hambre, dame de comer"

#check for new message
def check_for_new_message():
    pt.moveTo(x + 50,y -35, duration=.5 )

    while True:
        #chechk for new msg
        try:
            position = pt.locateOnScreen("green_circle.PNG", confidence= .7)

            if position is not None:
                pt.moveTo(position)
                pt.position(-200,0)
                pt.click()
                sleep(.5)


        except(Exception):
            print("no new message")

        if pt.pixelMatchesColor(int(x + 50),int(y - 35),(105,105,105), tolerance=10):
            print("its black")
            processed_message = process_response(get_message())
            post_response(processed_message)
        else:
            print("no new mesage yet...")
        sleep(5)


check_for_new_message()
