from colorama import Fore
from processing.Reader import Reader
from processing.Scraper import Scrapper


def main():
    end = False
    reader = Reader()

    ## take input
    while not end:

        name = input("What is your name?")
        subject = input("What is your subject?")

        if name and subject:
            print(Fore.CYAN)
            # scrapping
            # toc_items = Scrapper.getWikiTOC(subject)

            # reading
            #  reader.read(subject)

            print(Fore.WHITE + "Ready to Go!")
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
