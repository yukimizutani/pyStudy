import os

src = '/home/yuki/x-siem/cell/www/src'

for root, dirs, files in os.walk(src):
    for file in files:
        if file.endswith(".ts"):
            f = open(os.path.join(root, file))
            file_str = [line.strip() for line in f if line.strip()]
            f.close()

            for l in file_str:
                print(l)

            # f = open(os.path.join(root, file), 'w')
            # f.write(file_str)
            # f.close()
