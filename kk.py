from gpiozero import LED, Button
from signal import pause
lgrøn = LED(17)
gul = LED(20) 
lrød = LED(22)

button = Button(2)
butto = Button(3)

while True:

    button.when_pressed = lgrøn.off
    button.when_pressed = lrød.off
    
    button.when_released = lgrøn.on
    button.when_released = lrød.on
    
    butto.when_pressed = gul.off
    butto.when_released = gul.on
    
