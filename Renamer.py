import os
import re
import csv

data = {} #словарь - {респондент : ответы} 
with open('Words_Records.csv', newline='') as csvfile:
    for row in csvfile:
        reader = list(filter(None, row.strip().split(',')))
        data.update({reader[0] : reader[1:]})

dirs = [] #список папок с ответами
for el_dir in os.listdir():
    if re.search(r'\.', el_dir):
        pass
    else:
        dirs.append(el_dir + '\\')

for path in dirs:
    time = {}
    sizedict = {}
    sizelist = []
    
    for filename in os.listdir(path):    #доступ к файлам в папке
        if filename.endswith('mp3') or filename.endswith('m4a'):
            info = os.stat(path + filename)
            if info.st_mtime in time.keys(): #удаление копии
                os.remove(path + filename)
            else:
                time.update({info.st_mtime : filename})  #словарь - {время созд. : имя файла}
    time_list = list(time.keys()) #список времени создания аудиофайла

    i = 0
    while len(time)>0:
        early = time_list.pop(time_list.index(min(time_list))) #самое раннее время
        name = time.pop(early) #имя раннего файла
        
        if os.path.getsize(path + name) not in sizelist:
                info = os.path.getsize(path + name)
                print(name, info)
                sizedict.update({info : name})
                sizelist.append(info)
                pathname = re.sub(r'(\\)+', '', path) #имя папки
                os.rename(path + name, path + pathname + '_' + data[pathname][i] + '.mp3')
                i = i + 1
        elif os.path.getsize(path + name) in sizelist: #удаление повторной записи(?)                
                print("Дубликат имеет название: ", name)
                os.remove(path + name)
                
#==============================================        
    
