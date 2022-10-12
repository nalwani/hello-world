from processing.Scraper import Scrapper
from processing.Scheduler import Scheduler


def main():
    end = False

    ## take input
    while not end:

        name = input("What is your name?")
        subject = input("What is your subject?")

        if name and subject:
            # scrapping
            topics = Scrapper.getWikiTOC(subject)
            schedule = Scheduler.createEasySchedule(topics)
            print(schedule)
            print("Ready to Go!")
            end = True
        else:
            quiting = input("Do you want to quit? (y/n)")

            if quiting == "y":
                end = True
            if quiting == "n":
                continue
            else:
                break


if __name__ == '__main__':
    main()
