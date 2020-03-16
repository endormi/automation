"""

author: @endormi

Automated NFL stats
Automate the process of getting player stats (passing, rushing and receiving) and best plays, also with the ability to add stats to csv

"""

import nflgame
from pyfiglet import figlet_format
from termcolor import cprint


year = input("Year: ")
__year__ = f'{year}'
week = input("Week: ")
__week__ = f'{week}'

games = nflgame.games(__year__, week=__week__)
players = nflgame.combine_game_stats(games)
plays = nflgame.combine_plays(games)

logo = 'NFL-Stats'


class color:
    NOTICE = '\033[91m'
    END = '\033[0m'


info = color.NOTICE + '''
This was made possible by BurntSushi and his awesome nflgame python package.
Link: [https://github.com/BurntSushi/nflgame].
It lists year (your choice), week (your choice) stats (limited to your choice).
I'll be thinking about more ideas to do with nflgame package.\n''' + color.END


def pas():
    cmd = 'players, plays and both'

    print("\nCommands to use: " + cmd)

    choice = input("\nType in the command you want to use: ")
    choice = choice.lower()

    li = input("\nLimit (normally 10): ")
    __li__ = f'{li}'

    if choice == "players":
        for p in players.passing().sort('passing_yds').limit(__li__):
            msg = '%s %d passes for %d yards and %d TDs'
            print(msg % (p, p.passing_att, p.passing_yds, p.passing_tds))
        print("")
        print("--QBs end here--")

    elif choice == "plays":
        for p in plays.sort('passing_yds').limit(__li__):
            print(p)
        print("")
        print("--Best passing plays end here--")

    elif choice == "both":
        for p in players.passing().sort('passing_yds').limit(__li__):
            msg = '%s %d passes for %d yards and %d TDs'
            print(msg % (p, p.passing_att, p.passing_yds, p.passing_tds))
        print("")
        print("--QBs end here--")

        for p in plays.sort('passing_yds').limit(__li__):
            print(p)
        print("")
        print("--Best passing plays end here--")

    else:
        print("\nNot a valid command!")
        print("\nUse " + cmd)


def rush():
    cmd = 'players, plays and both'

    print("\nCommands to use: " + cmd)

    choice = input("\nType in the command you want to use: ")
    choice = choice.lower()

    li = input("\nLimit (normally 10): ")
    __li__ = f'{li}'

    if choice == "players":
        for p in players.rushing().sort('rushing_yds').limit(__li__):
            msg = '%s %d carries for %d yards and %d TDs'
            print(msg % (p, p.rushing_att, p.rushing_yds, p.rushing_tds))
        print("")
        print("--RBs end here--")

    elif choice == "plays":
        for p in plays.sort('rushing_yds').limit(__li__):
            print(p)
        print("")
        print("--Best rushing plays end here--")

    elif choice == "both":
        for p in players.rushing().sort('rushing_yds').limit(__li__):
            msg = '%s %d carries for %d yards and %d TDs'
            print(msg % (p, p.rushing_att, p.rushing_yds, p.rushing_tds))
        print("")
        print("--RBs end here--")

        for p in plays.sort('rushing_yds').limit(__li__):
            print(p)
        print("")
        print("--Best rushing plays end here--")

    else:
        print("\nNot a valid command!")
        print("\nUse " + cmd)


def rec():
    cmd = 'players, plays and both'

    print("\nCommands to use: " + cmd)

    choice = input("\nType in the command you want to use: ")
    choice = choice.lower()

    li = input("\nLimit (normally 10): ")
    __li__ = f'{li}'

    if choice == "players":
        for p in players.receiving().sort('receiving_yds').limit(__li__):
            msg = '%s %d catches for %d yards and %d TDs'
            print(msg % (p, p.receiving_att, p.receiving_yds, p.receiving_tds))

        print("")
        print("--WRs and TEs end here--")

    elif choice == "plays":
        for p in plays.sort('receiving_yds').limit(__li__):
            print(p)
        print("")
        print("--Best receiving plays end here--")

    elif choice == "both":
        for p in players.receiving().sort('receiving_yds').limit(__li__):
            msg = '%s %d catches for %d yards and %d TDs'
            print(msg % (p, p.receiving_att, p.receiving_yds, p.receiving_tds))

        print("")
        print("--WRs and TEs end here--")

        for p in plays.sort('receiving_yds').limit(__li__):
            print(p)
        print("")
        print("--Best receiving plays end here--")

    else:
        print("\nNot a valid command!")
        print("\nUse " + cmd)


def stats_to_csv():
    cmd = 'stat (every statistic from a game), stat_p (statistics of every player from an entire season) and both'

    print("\nCommands to use: " + cmd)

    choice = input("\nType in the command you want to use: ")
    choice = choice.lower()

    year = input("Year: ")
    __year__ = f'{year}'

    if choice == "stat":
        games.players.csv('player-stats.csv')

    elif choice == "stat_p":
        nflgame.combine(nflgame.games(__year__)).csv('season_stats.csv')

    elif choice == "both":
        games.players.csv('player-stats.csv')

        nflgame.combine(nflgame.games(__year__)).csv('season_stats.csv')

    else:
        print("\nNot a valid command!")
        print("\nUse " + cmd)


def main():
    cprint(figlet_format(logo, font='slant'), 'green')
    print("\n" + info + "\n")

    choices = 'pas (passing), rush (rushing), rec (receiving) and stats_to_csv'
    print("Commands to use: " + choices)

    choose_command = input("Type in the command you want to use: ")
    choose_command = choose_command.lower()

    if choose_command == "pas":
        pas()

    elif choose_command == "rush":
        rush()

    elif choose_command == "rec":
        rec()

    elif choose_command == "stats_to_csv":
        stats_to_csv()

    else:
        print("\nNot a valid command!")
        print("\nUse " + choices)


if __name__ == '__main__':
    main()
