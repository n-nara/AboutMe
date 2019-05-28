print("\nPython Program to combine multiple txt/csv files into songle txt file\n")

#using os module for accessing local drive files
import os

#listing files in the directory
#for testing, I am using hardcode values but, I am going to use sys arguements for the directory/folder names in the future.

orgn = os.listdir('FilesFolder')
dest = os.listdir('FullFile')

f_dir = 'FilesFolder/'
out_f = 'FullFile/FullFile.txt'

try:
#validating if file exist or not. if exist, deleting the file otherwise writing the header to the file

    if len(dest) > 0:
      os.remove('FullFile/FullFile.txt')
      open(dest, 'a').close()

    else:
#creating empty file
      open(dest, 'a').close()

except:
    with open('FullFile/FullFile.txt', 'a+') as f:
        hdr = 'Col1, Col2, Col3, Col4\n'
#writing the header
        f.write(hdr)
        
#looping through n number of files in the directory and writing complete data to single file.
    output = ''
    for lin1 in orgn:
        f_dir1 = f_dir+'/'+lin1
        
        with open(f_dir1) as f:
          content = f.read().strip("\n")
        output += content + '\t\n'

    with open(out_f, 'a+') as f:
        f.write(output)

print("\nFor testing, all user inputs are hardcoded, please check 'FilesFolder' and 'FullFile' folder to validate the program\n")

