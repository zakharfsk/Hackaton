import eel
from modules.audios import ShelfAudios
from modules.books import ShelfBooks

books = ShelfBooks()
audios = ShelfAudios()

@eel.expose
def bookstore():
    return books.get_books_info()


@eel.expose
def path_photos_books():
    return books.get_photos_path()


@eel.expose
def audiosstore():
    return audios.get_auidos_info()


@eel.expose
def path_audios():
    return audios.get_path_audios()



eel.init('web')
eel.start('index.html', size = (700, 700), mode = 'chrome')
