class Stats():
    """отслеживание статистики"""

    def __init__(self):
        """инициализирует статистику"""
        self.reser_stats()
        self.run_game = True  # если True игру продолжаем, False -  проиграли
        with open('highscore.txt', 'r') as f:
            self.high_score = int(f.readline())

    def reser_stats(self):
        """статистика, изменяющаяся во время игры"""
        self.guns_left = 2
        self.score = 0
