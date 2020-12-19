#Create bouncing ball
from sense_hat import SenseHat
from time import sleep


sense = SenseHat()

#colors 
r = (255, 0, 0)
g = (0, 255, 0)
b = (0, 0, 255)
k = (0, 0, 0)
w = (255, 255, 255)
c = (0, 255, 255)
y = (255, 255, 0)
o = (255, 128, 0)
n = (255, 128, 128)
p = (128, 0, 128)
d = (255, 0, 128)
l = (128, 255, 128)

#make bouncing ball

beginning= [
  k, k, k, k, k, k, k, k,
  k, k, k, k, k, k, k, k,
  k, k, k, k, k, k, k, k,
  k, k, k, k, k, k, k, k,
  k, k, k, k, k, k, k, k,
  k, k, k, k, k, k, k, k,
  k, k, k, k, k, k, k, k,
  w, w, w, w, w, w, w, w
]
		
bounce1 = [
  k, k, k, k, k, k, k, k,
  k, k, k, k, k, k, k, k,
  k, k, k, k, k, k, k, r,
  k, k, k, k, k, k, k, k,
  k, k, k, k, k, k, k, k,
  k, k, k, k, k, k, k, k,
  k, k, k, k, k, k, k, k,
  w, w, w, w, w, w, w, w
]		

bounce2 = [
  k, k, k, k, k, k, k, k,
  k, k, k, k, k, k, k, k,
  k, k, k, k, k, k, k, k,
  k, k, k, k, k, k, r, k,
  k, k, k, k, k, k, k, k,
  k, k, k, k, k, k, k, k,
  k, k, k, k, k, k, k, k,
  w, w, w, w, w, w, w, w
  ]
		
bounce3 = [
  k, k, k, k, k, k, k, k,
  k, k, k, k, k, k, k, k,
  k, k, k, k, k, k, k, k,
  k, k, k, k, k, k, k, k,
  k, k, k, k, k, r, k, k,
  k, k, k, k, k, k, k, k,
  k, k, k, k, k, k, k, k,
  w, w, w, w, w, w, w, w,
   ]	

bounce4 = [
  k, k, k, k, k, k, k, k,
  k, k, k, k, k, k, k, k,
  k, k, k, k, k, k, k, k,
  k, k, k, k, k, k, k, k,
  k, k, k, k, k, k, k, k,
  k, k, k, k, r, k, k, k,
  k, k, k, k, k, k, k, k,
  w, w, w, w, w, w, w, w,
]		

bounce5 = [
  k, k, k, k, k, k, k, k,
  k, k, k, k, k, k, k, k,
  k, k, k, k, k, k, k, k,
  k, k, k, k, k, k, k, k,
  k, k, k, k, k, k, k, k,
  k, k, k, k, k, k, k, k,
  k, k, k, r, k, k, k, k,
  w, w, w, w, w, w, w, w,
]		

bounce6 = [
  k, k, k, k, k, k, k, k,
  k, k, k, k, k, k, k, k,
  k, k, k, k, k, k, k, k,
  k, k, k, k, k, k, k, k,
  k, k, k, k, k, k, k, k,
  k, k, r, k, k, k, k, k,
  k, k, k, k, k, k, k, k,
  w, w, w, w, w, w, w, w,
]		

bounce7 = [
  k, k, k, k, k, k, k, k,
  k, k, k, k, k, k, k, k,
  k, k, k, k, k, k, k, k,
  k, k, k, k, k, k, k, k,
  k, r, k, k, k, k, k, k,
  k, k, k, k, k, k, k, k,
  k, k, k, k, k, k, k, k,
  w, w, w, w, w, w, w, w,
]		
	
bounce8 = [
  k, k, k, k, k, k, k, k,
  k, k, k, k, k, k, k, k,
  k, k, k, k, k, k, k, k,
  r, k, k, k, k, k, k, k,
  k, k, k, k, k, k, k, k,
  k, k, k, k, k, k, k, k,
  k, k, k, k, k, k, k, k,
  w, w, w, w, w, w, w, w,
]		
		
#hoop entering picture
hoop1 = [
  k, k, k, k, k, k, k, k,
  k, k, k, k, k, k, k, k,
  b, k, k, k, k, k, k, k,
  k, k, k, k, k, k, k, k,
  k, k, k, k, k, k, k, r,
  k, k, k, k, k, k, k, k,
  k, k, k, k, k, k, k, k,
  w, w, w, w, w, w, w, w,
]	
	
hoop2 = [
  k, k, k, k, k, k, k, k,
  k, b, k, k, k, k, k, k,
  b, b, k, k, k, k, k, k,
  k, k, k, k, k, k, k, k,
  k, k, k, k, k, k, k, k,
  k, k, k, k, k, k, r, k,
  b, k, k, k, k, k, k, k,
  w, w, w, w, w, w, w, w,
]	
		
hoop3 = [
  b, k, k, k, k, k, k, k,
  b, k, b, k, k, k, k, k,
  b, b, b, k, k, k, k, k,
  b, k, k, k, k, k, k, k,
  b, k, k, k, k, k, k, k,
  b, k, k, k, k, k, k, k,
  b, k, k, k, k, r, k, k,
  w, w, w, w, w, w, w, w
]	


hoop4 = [
  b, k, k, k, k, k, k, k,
  b, k, b, k, k, k, k, k,
  b, b, b, k, k, k, k, k,
  b, k, k, k, k, k, k, k,
  b, k, k, k, k, k, k, k,
  b, k, k, k, k, r, k, k,
  b, k, k, k, k, k, k, k,
  w, w, w, w, w, w, w, w,
  ]
  
hoop5 = [
  b, k, k, k, k, k, k, k,
  b, k, b, k, k, k, k, k,
  b, b, b, k, k, k, k, k,
  b, k, k, k, k, k, k, k,
  b, k, k, k, k, r, k, k,
  b, k, k, k, k, k, k, k,
  b, k, k, k, k, k, k, k,
  w, w, w, w, w, w, w, w
]

hoop6 = [
  b, k, k, k, k, k, k, k,
  b, k, b, k, k, k, k, k,
  b, b, b, k, k, k, k, k,
  b, k, k, k, k, r, k, k,
  b, k, k, k, k, k, k, k,
  b, k, k, k, k, k, k, k,
  b, k, k, k, k, k, k, k,
  w, w, w, w, w, w, w, w
]

hoop7 = [
  b, k, k, k, k, k, k, k,
  b, k, b, k, k, k, k, k,
  b, b, b, k, k, r, k, k,
  b, k, k, k, k, k, k, k,
  b, k, k, k, k, k, k, k,
  b, k, k, k, k, k, k, k,
  b, k, k, k, k, k, k, k,
  w, w, w, w, w, w, w, w
]

hoop8 = [
  b, k, k, k, k, k, k, k,
  b, k, b, k, r, k, k, k,
  b, b, b, k, k, k, k, k,
  b, k, k, k, k, k, k, k,
  b, k, k, k, k, k, k, k,
  b, k, k, k, k, k, k, k,
  b, k, k, k, k, k, k, k,
  w, w, w, w, w, w, w, w
]

hoop9 = [
  b, k, k, r, k, k, k, k,
  b, k, b, k, k, k, k, k,
  b, b, b, k, k, k, k, k,
  b, k, k, k, k, k, k, k,
  b, k, k, k, k, k, k, k,
  b, k, k, k, k, k, k, k,
  b, k, k, k, k, k, k, k,
  w, w, w, w, w, w, w, w
]

hoop10 = [
  b, k, r, k, k, k, k, k,
  b, k, b, k, k, k, k, k,
  b, b, b, k, k, k, k, k,
  b, k, k, k, k, k, k, k,
  b, k, k, k, k, k, k, k,
  b, k, k, k, k, k, k, k,
  b, k, k, k, k, k, k, k,
  w, w, w, w, w, w, w, w
]

hoop11 = [
  b, k, k, k, k, k, k, k,
  b, r, b, k, k, k, k, k,
  b, b, b, k, k, k, k, k,
  b, k, k, k, k, k, k, k,
  b, k, k, k, k, k, k, k,
  b, k, k, k, k, k, k, k,
  b, k, k, k, k, k, k, k,
  w, w, w, w, w, w, w, w
]
		
hoop12 = [
  b, k, k, k, k, k, k, k,
  b, k, b, k, k, k, k, k,
  b, b, b, k, k, k, k, k,
  b, r, k, k, k, k, k, k,
  b, k, k, k, k, k, k, k,
  b, k, k, k, k, k, k, k,
  b, k, k, k, k, k, k, k,
  w, w, w, w, w, w, w, w
]
		
hoop13 = [
  b, k, k, k, k, k, k, k,
  b, k, b, k, k, k, k, k,
  b, b, b, k, k, k, k, k,
  b, k, k, k, k, k, k, k,
  b, k, r, k, k, k, k, k,
  b, k, k, k, k, k, k, k,
  b, k, k, k, k, k, k, k,
  w, w, w, w, w, w, w, w
]		
		
hoop14 = [
  b, k, k, k, k, k, k, k,
  b, k, b, k, k, k, k, k,
  b, b, b, k, k, k, k, k,
  b, k, k, k, k, k, k, k,
  b, k, k, k, k, k, k, k,
  b, k, k, r, k, k, k, k,
  b, k, k, k, k, k, k, k,
  w, w, w, w, w, w, w, w
]
		
hoop15 = [ 
  b, k, k, k, k, k, k, k,
  b, k, b, k, k, k, k, k,
  b, b, b, k, k, k, k, k,
  b, k, k, k, k, k, k, k,
  b, k, k, k, k, k, k, k,
  b, k, k, k, k, k, k, k,
  b, k, k, k, r, k, k, k,
  w, w, w, w, w, w, w, w
]		
		

while True:
  sense.set_pixels(beginning)
  sleep(0.5)
  sense.set_pixels(bounce1)
  sleep(0.5)
  sense.set_pixels(bounce2)
  sleep(0.5)
  sense.set_pixels(bounce3)
  sleep(0.5)
  sense.set_pixels(bounce4)
  sleep(0.5)
  sense.set_pixels(bounce5)
  sleep(0.5)
  sense.set_pixels(bounce6)
  sleep(0.5)
  sense.set_pixels(bounce7)
  sleep(0.5)
  sense.set_pixels(bounce8)
  sleep(0.5)
  

  
  for i in range(2):
    
    sense.set_pixels(hoop1)
    sleep(0.5)
  
    sense.set_pixels(hoop2)
    sleep(0.5)
    sense.set_pixels(hoop3)
    sleep(0.5)
    sense.set_pixels(hoop4)
    sleep(0.5)
    sense.set_pixels(hoop5)
    sleep(0.5) 
    sense.set_pixels(hoop6)
    sleep(0.5)
    sense.set_pixels(hoop7)
    sleep(0.5)
    sense.set_pixels(hoop8)
    sleep(0.5)
    sense.set_pixels(hoop9)
    sleep(0.5)
    sense.set_pixels(hoop10)
    sleep(0.5)
    sense.set_pixels(hoop11)
    sleep(0.5)
    sense.set_pixels(hoop12)
    sleep(0.5)
    sense.set_pixels(hoop13)
    sleep(0.5)
    sense.set_pixels(hoop14)
    sleep(0.5)
    sense.set_pixels(hoop15)