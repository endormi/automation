"""

author: @endormi

Automated Git commands
Use git through an intuitive CLI

"""

import subprocess


def run(*args):

    return subprocess.check_call(['git'] + list(args))


def clone():

    print("\nYou will be asked for the user first and then the repository name\n")

    user = input("User: ")
    __user__ = f'{user}'
    repo = input("Repository: ")
    __repo__ = f'{repo}'

    print("\nChoose the local path for your clone.")
    local = input("Local path: ")
    local_path = f'{local}'

    subprocess.Popen(['git', 'clone', "https://github.com/" + __user__ + "/" + __repo__ + ".git", local_path])


def commit():

    message = input("\nType in your commit message: ")
    commit_message = f'{message}'

    run("commit", "-am", commit_message)
    run("push", "-u", "origin", "master")


def branch():

    branch = input("\nType in the name of the branch you want to make: ")
    br = f'{branch}'

    run("checkout", "-b", br)

    choice = input("\nDo you want to push the branch right now to GitHub? (y/n) ")
    choice = choice.lower()

    if choice == "y":
        run("push", "origin", branch)

    elif choice == "n":
        print("\nOkay, goodbye!\n")

    else:
        print("\nInvalid command! Use y or n.\n")


def pull():

    print("\nPulls changes from the current folder if *.git is initialized.")

    choice = input("\nDo you want to pull the changes from GitHub? (y/n) ")
    choice = choice.lower()

    if choice == "y":
        run("pull")

    elif choice == "n":
        print("\nOkay, goodbye!\n")

    else:
        print("\nInvalid command! Use y or n.\n")


def merge():

    branch = input("\nType in the name of your branch: ")
    br = f'{branch}'

    run("merge", br)


def blame():

    file = input("\nType in the name of the file: ")
    fi = f'{file}'

    run("blame", fi)


def stash():

    print("\nDo you want to save, list, pop, show, branch, clear or drop? ")

    choice = input("\nCommands to use: save, li, pop, show, branch, clear and drop \n")
    choice = choice.lower()

    if choice == "save":
        message = input("\nType in your stash message: ")
        stash_message = f'{message}'

        run("stash", "save", stash_message)

    if choice == "li":
        run("stash", "li")

    if choice == "pop":
        run("stash", "pop")

    elif choice == "show":
        run("stash", "show", "-p")

    elif choice == "branch":
        branch = input("\nType in the name of the branch you want to stash: ")
        br = f'{branch}'

        run("stash", "branch", br)

    elif choice == "clear":
        run("stash", "clear")

    elif choice == "drop":
        run("stash", "drop")

    else:
        print("\nInvalid command! Use list or n.\n")


def main():

    choices = 'clone, commit, branch, pull, merge, blame and stash'
    print("Commands to use: " + choices)

    choose_command = input("Type in the command you want to use: ")
    choose_command = choose_command.lower()

    if choose_command == "clone":
        clone()

    elif choose_command == "commit":
        commit()

    elif choose_command == "branch":
        branch()

    elif choose_command == "pull":
        pull()

    elif choose_command == "merge":
        merge()

    elif choose_command == "blame":
        blame()

    elif choose_command == "stash":
        stash()

    else:
        print("\nNot a valid command!")
        print("\nUse " + choices)


main()
