def letter_by_letter(start, end):
    if len(start) != len(end):
        print("Start and end strings are different lengths!")

    print(start)

    for i in xrange(len(start)):
        if start[i] == end[i]:
            continue

        start = start[:i] + end[i] + start[i + 1:]
        print(start)


if __name__ == '__main__':
    letter_by_letter("a fall to the floor", "braking the door in")
