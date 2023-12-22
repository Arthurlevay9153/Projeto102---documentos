import os
import shutil

from_dir = 'C:/Users/55819/Downloads/'
to_dir = 'C:/Users/55819/Documents/'

files = os.listdir(from_dir)
print(files)  

for file in files:
    name,extension = os.path.splitext(file)
    print(name)
    print(extension)

    if extension in [".txt",".doc",".docx",".pdf"]:
        path_1 = from_dir+file
        path_2 = to_dir+'/dowloads'
        path_3 = to_dir+'/dowloads/'+file

        if os.path.exists(path_2):
            shutil.move(path_1,path_3)
            print('movendo o arquivo',file)
        else:
            os.makedirs(path_2)
            shutil.move(path_1,path_3)
            print('criando a pasta & movendo o arquivo',file)