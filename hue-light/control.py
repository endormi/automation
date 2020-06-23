"""

author: @endormi

Automated philips hue light controller using Phue

"""

from phue import Bridge


ip = ''
b = Bridge(ip)
# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
b.connect()
lights = b.get_light_objects('name')

#for light in ['Kitchen']
#    lights[light].on = True
#    lights[light].hue = 15000
#    lights[light].saturation = 120


# Change the hue and saturation to change color

def movie():
    for light in lights:
        lights[light].on = True
        lights[light].hue = 5000
        lights[light].saturation = 100


def video_game():
    for light in lights:
        lights[light].on = True
        lights[light].hue = 20000
        lights[light].saturation = 120


def turn_off():
    for light in lights:
        lights[light].on = False


def main():
    choices = 'movie, video_game & turn_off'
    print("Commands to use: " + choices)

    choose_command = input("Type in the command you want to use: ")
    choose_command = choose_command.lower()

    if choose_command == "movie":
        movie()

    elif choose_command == "video_game":
        video_game()

    elif choose_command == "turn_off":
        turn_off()

    else:
        print("\nNot a valid command!")
        print("\nUse " + choices)


if __name__ == '__main__':
    main()
