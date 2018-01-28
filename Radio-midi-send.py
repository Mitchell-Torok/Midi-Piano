from microbit import *
import radio

radio.on()

lastC = False
lastD = False
lastE = False
lastF = False
lastK = False
lastL = False
lastM = False
lastO = False
lastP = False
lastQ = False
lastR = False
lastS = False
lastG = False
lastI = False
lastJ = False

display.off()
while True:

    #microbit.accelerometer.get_x()
    #microbit.accelerometer.get_y()   
    #microbit.accelerometer.get_z()    

    c = pin0.read_digital()
    d = pin1.read_digital()
    e = pin2.read_digital()
    f = pin3.read_digital()
    g = pin4.read_digital()
    i = pin6.read_digital()
    j = pin7.read_digital()
    k = pin8.read_digital()
    l = pin9.read_digital()
    m = pin10.read_digital()
    o = pin12.read_digital()
    p = pin13.read_digital() 
    q = pin14.read_digital()
    r = pin15.read_digital()
    s = pin16.read_digital()


    if f==True and lastF==False:
        radio.send(str(45))        
    if c==True and lastC==False:
        radio.send(str(46))    
    if g==True and lastG==False:
        radio.send(str(47))
    if i==True and lastI==False:
        radio.send(str(48))     
    if j==True and lastJ==False:
        radio.send(str(49))
    if d==True and lastD==False:
        radio.send(str(50))         
    if k==True and lastK==False:
        radio.send(str(51))
    if l==True and lastL==False:
        radio.send(str(52))     
    if m==True and lastM==False:
        radio.send(str(53))     
    if o==True and lastO==False:
        radio.send(str(54))       
    if e==True and lastE==False:
        radio.send(str(55))        
    if p==True and lastP==False:
        radio.send(str(56))
    if q==True and lastQ==False:
        radio.send(str(57))     
    if r==True and lastR==False:
        radio.send(str(58))     
    if s==True and lastS==False:
        radio.send(str(59))         
           

    lastC = c
    lastD = d
    lastE = e
    lastF = f
    lastK = k
    lastL = l
    lastM = m
    lastO = o 
    lastP = p
    lastQ = q
    lastR = r
    lastS = s
    lastG = g
    lastI = i
    lastJ = j
    sleep(10)
