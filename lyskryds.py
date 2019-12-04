from gpiozero import LED
from time import sleep
lgrøn = LED(17)
lgul = LED(27)
lrød = LED(22)
grøn = LED(16)
gul = LED(20)
rød = LED(21)

delay = 1
dela = 2
dilay = 3

while True:
    #set LED to on for the delay time
    lgrøn.on()
    rød.on()
    sleep(dela)
    lgrøn.off()
    sleep(dela)
    
    lgul.on()
    gul.on()
    sleep(delay)
    rød.off()
    lgul.off()
    gul.off()
    sleep(dela)

    lrød.on()
    grøn.on()
    sleep(dela)
    grøn.off()
    sleep(dela)
    
    lgul.on()
    gul.on()
    sleep(delay)
    lrød.off()
    lgul.off()
    gul.off()