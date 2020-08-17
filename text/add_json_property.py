inputF = "UpdateContractRequest.java"
outputF = "Att.2020-04_30_水谷祐貴.csv"
jsonPropPre = "@JsonProperty(\""
jsonPropPost = "\")"

f = open(inputF, "r", encoding="utf-8")
f2 = open(outputF, "w", encoding="utf-8")
lines = f.readlines()
for line in lines:
    if 'private' in line.rstrip():
        converted = ''
        elements = line.rstrip().split()
        for l in elements[2]:
            if l == ';':
                continue
            if l.isupper():
                print(elements[2])
                print(l.lower())
                converted += '_' + l.lower()
            else:
                converted += l
        f2.write('  ' + jsonPropPre + converted + jsonPropPost + '\n')
        f2.write(line.rstrip() + '\n')
    else:
        f2.write(line.rstrip() + '\n')
