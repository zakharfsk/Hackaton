import eel
import time

sec = 0

@eel.expose
def get_time(time):
    print(time)

@eel.expose
def timer(time):
    return time + 1

eel.init('web')
eel.start('index.html', size = (700, 700))