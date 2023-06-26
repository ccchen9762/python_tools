import os
from xml.etree.ElementTree import tostring

path = ""
files = os.listdir(path)

for i in range(len(files)):
    old_name = os.path.join(path, files[i])
    new_name = ""
    if(i<10):
        new_name = os.path.join(path, "0"+str(i+1)+files[i][-4:])
    else:
        new_name = os.path.join(path, str(i+1)+files[i][-4:])
    
    os.rename(old_name, new_name)