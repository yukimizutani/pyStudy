lines = []

with open("tasks") as f:
    for line in f:
        lines.append(line.rstrip().replace("-core", "").replace("-main", "").replace("-iface", ""))

mp = {}

for l in lines:
    if '-' in l:
        l = l.split("-")
        if ":" in l[len(l) - 1]:
            key = l[len(l) - 1].split(":")[0]
            if key in mp.keys():
                mp[key] += 1
            else:
                print("a1 " + key)
                mp[key] = 0
        else:
            if l[len(l) - 1] in mp.keys():
                mp[l[len(l) - 1]] += 1
            else:
                print("a2 " + l[len(l) - 1])
                print(l)
                mp[l[len(l) - 1]] = 0
    elif ':' in l:
        l = l.split(":")
        if l[len(l) - 1] in mp.keys():
            mp[l[len(l) - 1]] += 1
        else:
            print("a3 " + l[len(l) - 1])
            mp[l[len(l) - 1]] = 0
    else:
        if l in mp.keys():
            mp[l] += 1
        else:
            print("a4 " + l)
            mp[l] = 0

for k, v in sorted(mp.items(), key=lambda x: x[1]):
    print(k)
