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
dict = {}

# for light in ['Kitchen']
#    lights[light].on = True
#    lights[light].hue = 15000
#    lights[light].saturation = 120


# Change the hue and saturation to change color

def movie():
    for light in lights:
        lights[light].on = True
        lights[light].hue = 5000
        lights[light].saturation = 100


def turn_off():
    for light in lights:
        lights[light].on = False


def main():
    print('Commands to use: movie & turn_off')

    choose_command = input("Type in the command you want to use: ").lower()

    dict = {
        'movie': movie,
        'turn_off': turn_off,
    }

    dict.get(choose_command, lambda: 'Invalid')()


if __name__ == '__main__':
    main()
