numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
T = int(input())
for _ in xrange(T):
    N = int(input())
    inp = raw_input()
    numbersStart = False
    count = 0
    out = ""
    for each in inp:
        if each in numbers:
            numbersStart = True
            out += each
        else:
            numbersStart = False
            if out != "":
                count += 1
            out = ""
    else:
        if out != "":
            count += 1
    print count