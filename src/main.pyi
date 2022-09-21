from Objective import Objective


def main():
    f = open("storage.txt", "r")
    phrase = f.read()
    goal = Objective(phrase)
    f.close()

    print(goal.__str__())


if __name__ == '__main__':
    main()
