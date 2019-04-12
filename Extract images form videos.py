import cv2
import os

fp = open('PathOfSource', 'r') # This source file is text file and it contains name of Video files with path.
for filePath in fp.readlines():
    words = filePath.split("/")[-1:]
    vidcap = cv2.VideoCapture(filePath)
    count = 0
    success = True
    fps = int(vidcap.get(cv2.CAP_PROP_FPS))
    words = filePath.split("/")[-1:]   
    docd = [i.split('.', 1)[0] for i in words]
    last = " ".join(str(x) for x in docd)
    print(last)
    while success:
        directory = "pathOfDestination"+last # Where you want to store file.
        if not os.path.exists(directory):
            os.makedirs(directory)
        success,image = vidcap.read()
        if count%(10*fps) == 0 : # This capture images every 10 second till end of video.
            cv2.imwrite(directory+'/frame%d.jpg'%count,image)
            print('# ',end='')
        count+=1


# In[ ]:




