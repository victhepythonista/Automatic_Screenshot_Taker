



"""
Author  : Leting Victor Kipkemboi
github  : victhepythonista@github.com


This  is  a simple  pyhton  code that
takes screenshots   of  the host  PC and saves them at the   
[directory_to_store_images]
change it to change  your storage location


and as usual I'll make  more of this...expect much more
ENJOY
"""



import  datetime
import  mss
import  subprocess
import pyarmor
import os
import random,time, datetime,shutil,random
duration_between_shots = 10

user  = os.getlogin()
camera  = mss.mss()

directory_to_store_images = f"C:/Users/{user}/Desktop/screenshots/"

if  os.path.isdir(directory_to_store_images) == False:
    os.makedirs(directory_to_store_images)
os.chdir(directory_to_store_images)


def rename_the_file():
    # rename the file because the next one will have
    ## a similar name 'monitor-1.png'
    c_time = datetime.datetime.now()
    new_name = c_time.strftime("%Y_%m_%d_%H_%M_%S") + ".png"
    os.rename('monitor-1.png' , new_name )
    pass

def  mainloop():
    #main loop
    # I keep thinking I should have use classes 
    ## well next time to update Ill do it !
    take_screen_shots = True
    while   take_screen_shots:
        
        time.sleep(duration_between_shots)
        image_file = camera.shot()
        print(image_file)
        rename_the_file()
        print(os.getcwd())
        print(os.listdir())



mainloop()
