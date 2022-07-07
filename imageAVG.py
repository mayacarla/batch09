#CSCI 127
#Maya Carla Loletha Anderson

import numpy as np
import matplotlib.pyplot as plt

def average(region):
    """
    Takes region of an image,
    returns its avg. RGB values
    """
    red, green, blue = 0, 0, 0
    
    redAvg = np.average(region[:, :, 0])
    greenAvg = np.average(region[:, :, 1])
    blueAvg = np.average(region[:, :, 2])
   
    
    return(redAvg, greenAvg, blueAvg)


def setRegion(region, r, g, b):
    """
    sets region with values of RGB
    """
    region[:, :, 0] = redAvg
    region[:, :, 1] = greenAvg
    region[:, :, 2] = blueAvg

    return(redAvg, greenAvg, blueAvg)


def quarter(img2, levels):
     """
     Takes an image and the number of splits to make.
     Splits the image into regions (2**levels x 2**levels pieces)
     and averages each of these regions separately.
     Calls average() and setRegion() to average and set colors for the
     regions.
     """
     h = img2.shape[0]
     w = img2.shape[1]
     hReg = h//2**levels
     wReg = w//2**levels
     for i in range(2**levels):
          for j in range(2**levels):              
               #Average the region:
               r,g,b = average(img2[i*hReg:(i+1)*hReg,j*wReg:(j+1)*wReg])
               setRegion(img2[i*hReg:(i+1)*hReg,j*wReg:(j+1)*wReg],r,g,b)


def main():
     inFile = input('Enter image file name: ')
     img = plt.imread(inFile)

     #Divides the image in 1/2, 1/4, 1/8, ... 1/2^8, and displays each:
     for i in range(8):
          img2 = img.copy()   #Make a copy to average
          quarter(img2,i)     #Split in half i times, and average regions
     
          plt.imshow(img2)    #Load our new image into pyplot
          plt.show()          #Show the image (waits until closed to continue)

     #Shows the original image:
     plt.imshow(img)	      #Load image into pyplot
     plt.show()               #Show the image (waits until closed to continue)


#Allow script to be run directly:
if __name__ == "__main__":
     main()
