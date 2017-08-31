#!/usr/bin/env python
 
import time
import grovepi
import math

###############################################3
# Connect the Grove Button to digital port D3
# SIG,NC,VCC,GND
button = 3

grid_led_pin=5
con_led_pin=6

grovepi.pinMode(button,"INPUT")
grovepi.ledBar_init(grid_led_pin, 0)
grovepi.ledBar_init(con_led_pin, 0)
####################################
grid_led_pct_init=70
grid_led_pct=grid_led_pct_init

user_led_pct_init=100
user_led_pct=user_led_pct_init

####################################
def pct_to_ledhex(argument):
    switcher = {
        0: 0,
        10: 0x200,
        20: 0x300,
        30: 0x380,
        40: 0x3C0,
        50: 0x3E0,
        60: 0x3F0,
        70: 0x3F8,
        80: 0x3FC,
        90: 0x3FE,
        100: 0x3FF
    }
    return switcher.get(argument, 0)


def display_Grid_LED(ledpct):
    #grid_led_pin=5
 
    print "Grid is now at ", ledpct, "load"

    ledcount=(int(math.floor(ledpct/10)))*10
    ledhex=pct_to_ledhex(ledcount)
    grovepi.ledBar_setBits(grid_led_pin,pct_to_ledhex(ledcount) )

def display_Con_LED(ledpct):
    #con_led_pin=6

    print "Consumer is now at ", ledpct, "load"

    ledcount=(int(math.floor(ledpct/10)))*10
    ledhex=pct_to_ledhex(ledcount)
    grovepi.ledBar_setBits(con_led_pin,pct_to_ledhex(ledcount) )


while True:

#####################
# state 1
#####################
    print "\nEntering State 1"

    display_Grid_LED(80)
    display_Con_LED(100)

    time.sleep(2)

    while grovepi.digitalRead(button)==0:
        time.sleep(.5)


#####################
# state 2
#####################
    print "\nEntering State 2"

    display_Grid_LED(100)
    display_Con_LED(100)

    time.sleep(2)

    while grovepi.digitalRead(button)==0:
        time.sleep(.5)



#####################
# state 3
#####################
    print "\nEntering State 3"

    display_Grid_LED(90)
    display_Con_LED(70)

    time.sleep(2)

    while grovepi.digitalRead(button)==0:
        time.sleep(.5)



'''
while True:
    try:
        print(grovepi.digitalRead(button))
        time.sleep(.5)

    

    except IOError:
        print ("Error")


'''


