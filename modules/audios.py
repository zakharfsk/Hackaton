import json


class ShelfAudios:
    def __init__(self):
        pass

    def get_auidos_info(self):
        info_audios = json.dumps({
            'themes': [
                'Настойчивость.',
                '3 важнейших правила денег.',
                'Советы начинающим инвесторам.',
                'НАЙДИ свою страсть.',
                'Жизненные советы от миллионера.',
                'Как перейти от бедности к богатству.',
                'Ваше время ограничено.',
                'Ни о чем не жалей. Правила Успеха.'
            ],
            'authors': [
                'Дуэйн Джонсон',
                'Игорь Рыбаков',
                'Уоренн Баффет',
                'Уоррен Баффет',
                'Джек Ма',
                'Роберт Кийосаки',
                'Стив Джобс',
                'Джефф Безос'
            ]
        }, ensure_ascii = False).encode('utf-8')

        return info_audios.decode()

    def get_path_audios(self):
        audios_path = []

        for i in range(0, 7):
            audios_path.append(f'./media/audio/audio_{i}.mp3')
        
        path = json.dumps({
            'path': audios_path
        })

        return path