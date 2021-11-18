import json


class ShelfBooks:
    def __init__(self):
        pass

    def get_books_info(self):
        info_books = json.dumps({
            'name_books': [
                'Книга 7 звичок надзвичайно ефективних людей',
                'Книга Магия утра. Как первый час дня определяет ваш успех',
                'Під три чорти турботи!',
                'На межі. Тиждень без жалості до себе',
                'Думай і багатій',
                'Джорж Семюель Клейсон',
                'Книга Чоловіки з Марса, жінки з Венери',
                'Книга Життя без обмежень',
                'Книга Лідер без титулу',
                'Книга Приборкай своїх драконів. Як перетворити недоліки на переваги',
                'Книга Лідерство починається з призначення'
            ],
            'authors': [
                'Стівен Кові',
                'Гел Елрод',
                'Річард Бренсон',
                'Ерік Бертран Ларссен',
                'Наполеон Гілл',
                'Джорж Семюель Клейсон',
                'Джон Грей',
                'Нік Вуйчич',
                'Робін Шарма',
                'Хосе Стівенс',
                'Нік Крейґ'
            ],
            'urls': [
                'https://www.yakaboo.ua/ua/the-7-habits-of-highly-effective-people.html',
                'https://www.yakaboo.ua/ua/magija-utra-kak-pervyj-chas-dnja-opredeljaet-vash-uspeh-2247198.html',
                'https://bukva.ua/ua/catalog/browse/327/1/720298?gclid=CjwKCAiA7dKMBhBCEiwAO_crFAFs_DkV7K8wVQVJWZe88lK6nhBZyLHOgxvSJNYfPpvLeddzIjucXhoCwCcQAvD_BwE',
                'https://www.yakaboo.ua/na-predele-nedelja-bez-zhalosti-k-sebe-1879306.html?gclid=CjwKCAiA7dKMBhBCEiwAO_crFOHAL7l-jdmhfiC4_I0xyaAp-WK3gQw0Olm1qZA3hKM_8J-EYmEpdRoCogwQAvD_BwE',
                'https://www.yakaboo.ua/ua/dumaj-i-bagatij-1606035.html',
                'https://www.yakaboo.ua/ua/samyj-bogatyj-chelovek-v-vavilone-2261438.html',
                'https://www.yakaboo.ua/ua/choloviki-z-marsa-zhinki-z-veneri-1909669.html',
                'https://www.yakaboo.ua/ua/zhittja-bez-obmezhen.html',
                'https://www.yakaboo.ua/ua/lider-bez-titulu-2259062.html',
                'https://www.yakaboo.ua/ua/priborkaj-svoih-drakoniv-jak-peretvoriti-nedoliki-na-perevagi.html',
                'https://www.yakaboo.ua/ua/liderstvo-pochinaet-sja-z-priznachennja.html'
            ]
        }, ensure_ascii = False).encode('utf-8')
        return info_books.decode()

    def get_photos_path(self):
        photos_path = []

        for i in range(0, 10):
            photos_path.append(f'./media/photos/photo_{i}.jpg')

        path = json.dumps({
            'path': photos_path
        })

        return path
