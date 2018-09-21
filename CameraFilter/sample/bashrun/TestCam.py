import numpy
import socket
import time
from PIL import Image

def ShutterCap():

    filename = 'RAW.pgm'
     
    image = numpy.asarray(Image.open(filename))
    
    val = numpy.mean(image)
    
#    print(val)
    print('\n')
    print('Timestamp: ', time.time()) #Seconds since 01 jan 1970
    print('Device name: '+ str(socket.gethostname()))    
    if val > 4:
        print('Image data: light')
    else:
        print('Image data: dark')
	


if __name__ == "__main__":
	
	ShutterCap()
