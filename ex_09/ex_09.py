fname = input('Enter File: ')
if len(fname)<1 : fname = 'clown.txt'
hand = open(fname)

di = dict()


for lin in hand:
        lin = lin.rstrip()
        wds = lin.split()
        for w in wds:
            di[w] = di.get(w,0) + 1
print(di)

# find the most common word
occur = -1
for k,v in di.items():
    print(k,v)
    if v > occur:
        occur = v
        most_common = k

print('Most common word:', most_common)
print('Occurance:', occur , 'times' )
