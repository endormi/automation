"""

author: @endormi

Automated Git commands
Automate the process of using commands such as clone, commit, branch, pull, merge and blame

"""

import subprocess
from pyfiglet import figlet_format
from termcolor import cprint


logo = 'Git-Commands'


class color:
    NOTICE = '\033[91m'
    END = '\033[0m'


info = color.NOTICE + '''
Automate the process of using commands such as clone, commit, branch, pull, merge and blame.\n''' + color.END


dict = {}


def run(*args):
    return subprocess.check_call(['git'] + list(args))


def clone():
    print('\nYou will be asked for the user first and then the repository name.\n')

    user = input('User: ')
    repo = input('Repository: ')

    subprocess.Popen(['git', 'clone', 'https://github.com/' + user + '/' + repo + '.git'])


def commit():
    commit_message = input('\nType in your commit message: ')
    run('commit', '-am', commit_message)
    run('push', '-u', 'origin', 'master')


def branch():
    branch = input('\nType in the name of the branch you want to make: ')
    run('checkout', '-b', branch)

    choice = input('\nDo you want to push the branch right now to GitHub? (y/n): ').lower()

    if choice == 'y':
        run('push', '-u', 'origin', branch)
    else:
        print('\nOkay, goodbye!\n')


def pull():
    print('\nPulls changes from the current folder if *.git is initialized.')
    choice = input('\nDo you want to pull the changes from GitHub? (y/n): ').lower()

    if choice == 'y':
        run('pull')
    else:
        print('\nOkay, goodbye!\n')


def fetch():
    print('\nFetches changes from the current folder.')
    run('fetch')


def merge():
    branch = input('\nType in the name of your branch: ')
    run('merge', branch)


def reset():
    filename = input('\nType in the name of your file: ')
    run('reset', filename)


def blame():
    file = input('\nType in the name of the file: ')
    run('blame', file)


def main():
    cprint(figlet_format(logo, font='slant'), 'green')
    print(f'{info} \n')

    print('Commands to use: clone, commit, branch, pull, fetch, merge, reset and blame')

    choose_command = input('Type in the command you want to use: ').lower()

    dict = {
        'clone': clone,
        'commit': commit,
        'branch': branch,
        'pull': pull,
        'fetch': fetch,
        'merge': merge,
        'reset': reset,
        'blame': blame
    }

    dict.get(choose_command, lambda: "Invalid")()


if __name__ == '__main__':
    main()
