from time import sleep
from gpiozero import LED

rVØ = LED(22)
yVØ = LED(27)
gVØ = LED(17)
rNS = LED(21)
yNS = LED(20)
gNS = LED(16)

stå = 3
vent = 1
kør = 2

def state0():
        yVØ.off()
        rNS.on()
        rVØ.on()
        sleep(stå)
        return state1()
    
def state1():
        rNS.off()
        yNS.on()
        sleep(vent)
        yNS.off()
        gNS.on()
        sleep(kør)
        return state3()

def state3():
        gNS.off()
        yNS.on()
        sleep(vent)
        rNS.on()
        sleep(vent)
        yNS.off()
        return state4()

def state4():
        rVØ.off()
        yVØ.on()
        sleep(vent)
        yVØ.off()
        gVØ.on()
        sleep(kør)
        return state5()
    
def state5():
        gVØ.off()
        yVØ.on()
        sleep(vent)
        rVØ.on()
        sleep(vent)
        return state0()
    
    
    
state=state0
while state: state=state()
