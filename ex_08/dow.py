han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    wds = line.split()
    if len(wds) > 0:
        if wds[0] != 'From':
            continue
    if len(wds) > 1:
        print(wds[2] + '\n')
