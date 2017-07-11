seats = range(1, 109)


def getSeat(seatNumber=None):
    for i in xrange(0, 108, 12):
        seat = [seats[i:i + 6], seats[i + 6:i + 12][::-1]]
        indx = None
        direct = 1
        if seatNumber in seat[0]:
            indx = seat[0].index(seatNumber)
        elif seatNumber in seat[1]:
            indx = seat[1].index(seatNumber)
            direct = 0
        if indx is not None:
            if indx in [0, 5]:
                return str(seat[direct][indx]) + " WS"
            elif indx in [1, 4]:
                return str(seat[direct][indx]) + " MS"
            else:
                return str(seat[direct][indx]) + " AS"


if __name__ == '__main__':
    T = int(input())
    sns = []
    for _ in range(T):
        seatNumber = int(input())
        sns.append(seatNumber)
    for each in sns:
        print getSeat(seatNumber=each)
