class Stats():
    """ Отслеживание игровой статистики """

    def __init__(self):
        """ Инициализация статистики """
        self.reset_stats()


    def reset_stats(self):
        """ Статистика, меняющаяся во время игры """
        self.guns_left = 2