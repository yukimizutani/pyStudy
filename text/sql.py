f = open('C:\\Users\\ymizu\\OneDrive\\ドキュメント\\single_option_mapping.csv')
f2 = open('single_option', 'w')

prefix = 'INSERT INTO single_option_mapping (package_id,single_option_code,option_type,display_order) values('
postfix = ');'

if __name__ == '__main__':
    dbs = f.readlines()
    count = 0
    for l in dbs:
        elements = l.rstrip().split(',')
        print(
            '{}\'{}\',\'{}\',{},{}{}'.format(prefix, elements[4], elements[5], '2', elements[3], postfix))
        count += 1
        # f2.write('{}{}{}{}{}'.format(prefix, elements[0], elements[1], elements[2], elements[3], postfix) + '\n')
        f2.flush()
    f2.close()
