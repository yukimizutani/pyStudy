import re

prefix = "==== <sub><sup><sub><sup>?</sup></sub></sup></sub> [http://redmine-xsiem.dev.infoscience.co.jp/redmine/issues/"
premiddle = " (#"
postmiddle = ")] <span style=\"color:orange;\">[開発中]</span>"
postfix = " ===="

if __name__ == '__main__':
    f = open("tickets")
    for l in f.readlines():
        # print(l.rstrip())
        g = re.search(r'\* {{bug\|(.+)}}(.*): \d*\.?\d$', l.rstrip())
        if g is not None:
            num = g.group(1)
            title = g.group(2)
            # print(num)
            # print(title)
            print(prefix + num + premiddle + num + postmiddle + title + postfix)
