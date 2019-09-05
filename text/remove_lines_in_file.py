word_to_remove = []

with open("remove","r") as f:
    for l in f.readlines():
        word_to_remove.append(l.rstrip())


def check_word(l):
    for word in word_to_remove:
        if word in l:
            return False
    return True


with open("tasks") as f:
    lines = [line.strip() for line in f if line.strip()]

finai_lines = []

for l in lines:
    if check_word(l):
        finai_lines.append(l + "\n")

fw = open("taskss", "w")
fw.writelines(finai_lines)
