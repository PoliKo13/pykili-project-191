import os

path = 'memes/'
time = {}
newname = ['a', 'b', 'c', 'd', 'e', 'f']
for filename in os.listdir(path):
    if filename.endswith('mp3'):
        info = os.stat(path + filename)
        print(filename , info.st_ctime)
        time.update({info.st_ctime : filename})
print(time)
time_list = list(time.keys())
print(time_list)
i = 0
while len(time)>0:
    print(min(time_list))
    early = time_list.pop(time_list.index(min(time_list)))
    name = time.pop(early)
    print(name)
    os.rename(path + name, path + newname[i] + '.mp3')
    i = i + 1

        
    
