import eel

settings = {
    'mode': "chrome", #or "chrome-app",
    'host': 'localhost',
    'port': 8080,
    'chromeFlags': ["--start-fullscreen", "--browser-startup-dialog"]
}

@eel.expose
def get_time(time):
    print(time)

@eel.expose
def timer(time):
    return time + 1

eel.init('web')
eel.start('index.html', size = (700, 700), mode = 'chrome', cmdline_args = ['--browser-startup-dialog'])