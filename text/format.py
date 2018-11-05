input_file = 'tes.csv'

if __name__ == '__main__':
    f = open(input_file)
    for line in f.read():
        print(line)
