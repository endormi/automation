"""

author: @endormi

Automated NFL stats
Automate the process of getting player stats (passing, rushing and receiving) and best plays, also with the ability to add stats to csv

"""

import nflgame

games = nflgame.games(2013, week=13)
players = nflgame.combine_game_stats(games)
plays = nflgame.combine_plays(games)


class color:
    NOTICE = '\033[91m' # red
    END = '\033[0m' #normal color


hey = color.NOTICE + '''
Hello,
This was made possible by BurntSushi and his awesome nflgame python package.
Link: [https://github.com/BurntSushi/nflgame].
This is just a very small script and not that useful. It lists 2013, week 13 stats (limited to 15).
Why year 2013? I'm a huge fan of the Seahawks and this is the year the Seahawks won the Superbowl.
I'll be thinking about more ideas to do with nflgame package.\n''' + color.END


def pas():

    cmd = 'players, plays and both'

    print("\nCommands to use: " + cmd)

    choice = input("\nType in the command you want to use: ")
    choice = choice.lower()

    if choice == "players":
        for p in players.passing().sort('passing_yds').limit(15):
            msg = '%s %d passes for %d yards and %d TDs'
            print(msg % (p, p.passing_att, p.passing_yds, p.passing_tds))
        print("")
        print("--QBs end here--")

    elif choice == "plays":
        for p in plays.sort('passing_yds').limit(15):
            print(p)
        print("")
        print("--Best passing plays end here--")

    elif choice == "both":
        for p in players.passing().sort('passing_yds').limit(15):
            msg = '%s %d passes for %d yards and %d TDs'
            print(msg % (p, p.passing_att, p.passing_yds, p.passing_tds))
        print("")
        print("--QBs end here--")

        for p in plays.sort('passing_yds').limit(15):
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

    if choice == "players":
        for p in players.rushing().sort('rushing_yds').limit(15):
            msg = '%s %d carries for %d yards and %d TDs'
            print(msg % (p, p.rushing_att, p.rushing_yds, p.rushing_tds))
        print("")
        print("--RBs end here--")

    elif choice == "plays":
        for p in plays.sort('rushing_yds').limit(15):
            print(p)
        print("")
        print("--Best rushing plays end here--")

    elif choice == "both":
        for p in players.rushing().sort('rushing_yds').limit(15):
            msg = '%s %d carries for %d yards and %d TDs'
            print(msg % (p, p.rushing_att, p.rushing_yds, p.rushing_tds))
        print("")
        print("--RBs end here--")

        for p in plays.sort('rushing_yds').limit(10):
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

    if choice == "players":
        for p in players.receiving().sort('receiving_yds').limit(15):
            msg = '%s %d catches for %d yards and %d TDs'
            print(msg % (p, p.receiving_att, p.receiving_yds, p.receiving_tds))

        print("")
        print("--WRs and TEs end here--")

    elif choice == "plays":
        for p in plays.sort('receiving_yds').limit(15):
            print(p)
        print("")
        print("--Best receiving plays end here--")

    elif choice == "both":
        for p in players.receiving().sort('receiving_yds').limit(15):
            msg = '%s %d catches for %d yards and %d TDs'
            print(msg % (p, p.receiving_att, p.receiving_yds, p.receiving_tds))

        print("")
        print("--WRs and TEs end here--")

        for p in plays.sort('receiving_yds').limit(15):
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

    if choice == "stat":
        games.players.csv('player-stats.csv')

    elif choice == "stat_p":
        nflgame.combine(nflgame.games(2013)).csv('season2013.csv')

    elif choice == "both":
        games.players.csv('player-stats.csv')

        nflgame.combine(nflgame.games(2013)).csv('season2013.csv')

    else:
        print("\nNot a valid command!")
        print("\nUse " + cmd)


def main():

    print(hey + "\n")

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


main()
