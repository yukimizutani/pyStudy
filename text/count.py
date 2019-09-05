with open('result2') as f:
    names_list = [line.strip() for line in f if line.strip()]

mapas = {}

for l in names_list:
    last = l.split()[len(l.split()) - 1]
    if last not in mapas.keys():
        mapas[last] = 1
    else:
        mapas[last] += 1

for k in mapas.keys():
    if not mapas[k] == 1:
        print(k)
        print(mapas[k])
