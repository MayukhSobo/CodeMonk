from string import ascii_lowercase

upperAlppha = list(ascii_lowercase.upper())
lowerAlpha = list(ascii_lowercase)

upperAlpphaASCI = map(ord, upperAlppha)
lowerAlphaASCI = map(ord, lowerAlpha)

primes = [67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]

T = int(input())
for i in range(T):
    N = input()
    s = raw_input()
    out = ""
    for each in s:
        asci = ord(each)
        diff = abs(primes[0] - asci)
        for i in range(1, len(primes)):
            if abs(primes[i] - asci) < diff:
                diff = abs(primes[i] - asci)
            else:
                out += chr(primes[i - 1])
                break
        else:
            out += chr(primes[-1])

    print(out)
