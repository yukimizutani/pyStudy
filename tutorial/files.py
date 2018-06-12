import os

root_dir = "/home/yuki/PycharmProjects/pyStudy/bottle/static/images"
file_set = set()
file_dict = {}

for dir_, _, files in os.walk(root_dir):
    for fileName in files:
        rel_dir = os.path.relpath(dir_, root_dir)
        rel_file = os.path.join(rel_dir, fileName)
        file_set.add(rel_file)

for elm in file_set:
    key = str(elm).split('/')
    print(key)
    if key[0] in file_dict:
        file_dict[key[0]].append(key[1])
    else:
        file_dict[key[0]] = [key[1]]
print(file_dict)
