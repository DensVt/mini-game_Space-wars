class Stats():
    """ Отслеживание игровой статистики """

    def __init__(self):
        """ Инициализация статистики """
        self.reset_stats()
        self.run_game = True

        with open('highscore.txt', 'r') as file:
        # отдельно выведеный рекорд с последующим сохранением, без затирания
            self.high_score = int(file.readline())


    def reset_stats(self):
        """ Статистика, меняющаяся во время игры """
        self.guns_left = 2   # Жизни
        self.score = 0