#importing necessary libraries
from gpiozero import LED
from time import sleep
l1 = LED(17)
l2 = LED(27)
l3 = LED(22)
delay = 1
dela = 2
dilay = 3

while True:
    #set LED to on for the delay time
    l1.on()
    sleep(delay)
    print('LED set to on')
    l1.off()
    print ('LED off')
    sleep(delay)
 
    l2.on()
    sleep(dela)
    print('ON')
    l2.off()
    print('OFF')
    sleep(dela)
    
    
    l3.on()
    sleep(dilay)
    print('ON')
    l3.off()
    print('OFF')
    sleep(dilay)