import colorama
from colorama import Fore, Style

# Initialize colorama
colorama.init(autoreset=True)

def banner():
    print("\t    __  __________   _________________  __  _____    __       __________  ___   ________ __ __________ \n\t   /  |/  / ____/ | / / ___/_  __/ __ \/ / / /   |  / /      /_  __/ __ \/   | / ____/ //_// ____/ __ \ \n\t  / /|_/ / __/ /  |/ /\__ \ / / / /_/ / / / / /| | / /     / / / /_/ / /| |/ /   / ,<  / __/ / /_/ / \n\t / /  / / /___/ /|  /___/ // / / _, _/ /_/ / ___ |/ /___     / / / _, _/ ___ / /___/ /| |/ /___/ _, _/ \n\t/_/  /_/_____/_/ |_//____//_/ /_/ |_|\____/_/  |_/_____/    /_/ /_/ |_/_/  |_\____/_/ |_/_____/_/ |_|  \n \t")
    print("\t\t\t\t\t "+Fore.YELLOW +"v1.0\t\t"+Style.RESET_ALL +"DEVELOPED BY :"+Fore.RED +" VISHWAJITH SHAIJUKUMAR")
    print(Fore.BLUE +"\t\t Also available in c & c++ on github.com/root-cyborg127"+Fore.GREEN +"\t\t v2.0\tCOMING SOON !\n\n\n")
    
    


def main():
    cycleLength = int(input(Fore.BLUE +"CYCLE TRACKER Step 1: CYCLE LENGTH\n\n"+Style.RESET_ALL +"Please enter the number of days your previous cycle lasted: "))
    print("\n\n")

    menstrualLength = int(input(Fore.BLUE +"CYCLE TRACKER Step 2: PERIOD LENGTH\n\n"+Style.RESET_ALL +"Please enter the number of days your period lasted: "))
    print("\n\n")

    print(Fore.BLUE +"CYCLE TRACKER Step 3: WHEN DID YOUR LAST PERIOD START?"+Style.RESET_ALL +"\n")
    day = int(input("Day: "))
    month = int(input("Month: "))
    year = int(input("Year: "))
    print("\n\n")

    day = day + cycleLength

    if day > 31:
        month += 1
        day = day - 31

    print(Fore.BLUE +"<<====================  YOUR NEXT PERIOD STARTS FROM : " + str(day) + " - " + str(month) + " - " + str(year) + "  =================>>\n\n\n")

    mEnds = day + menstrualLength

    if mEnds > 31:
        month += 1
        mEnds = mEnds - 31

    print(Fore.BLUE +"<<====================   YOUR PERIODS ENDS ON : " + str(mEnds) + " - " + str(month) + " - " + str(year) + "  ==================>>\n\n\n")

    A = day + 10
    oPeriod = A

    if A > 31:
        A = A - 31
        month += 1

    print(Fore.BLUE +"<<====================   YOUR OVULATION STARTS ON : " + str(A) + " - " + str(month) + " - " + str(year) + "  =================>>\n\n\n")

    oEnd = A + 6

    if A > 31:
        month += 1
        A = A - 31

    print(Fore.BLUE +"<<====================   YOUR OVULATION ENDS ON : " + str(oEnd) + " - " + str(month) + " - " + str(year) + "  =================>>\n\n\n")

    print("\n\n\n")
    print(Fore.RED +"Ask your doctor about any concerns or questions you may have about your menstrual experience for best results.")
    print(Fore.RED +"For more information, visit "+Fore.YELLOW +"WomensHealth.gov"+Fore.RED +" or"+Fore.YELLOW +" GirlsHealth.gov"+Fore.RED +" for more facts about menstruation.")

if __name__ == "__main__":
    banner()
    main()
