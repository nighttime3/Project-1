from board import Board
from flag import Flag
from all_enemies import AllEnemies
from player import Player
import settings

class Game:
    def __init__(self):
        self.game_state = True
        self.level_index = 0
        self.score = 0
        self.ball = settings.LEVELS[self.level_index]['ball']
        self.difficulty = settings.LEVELS[self.level_index]['difficulty']
        self.player = Player()
        self.player.life = settings.LEVELS[self.level_index]
        self.level_board = Board(
            f'Level: {self.level_index + 1}',
            (-settings.WIDTH / 2 + 50, settings.HEIGHT /2 - 50),
            align='left'
        )
        self.score_board = Board('', (0, settings.HEIGHT / 2 - 50))
        self.life_board = Board(
            f'Remain: {self.player.life}',
            (settings.WIDTH / 2 - 50,
            settings.HEIGHT / 2 - 50),
            align='right'
        )
        self.game_board = Board('', position=(0,20))
        self.menu_board = Board(
            'Press s to start',
            (0, -20),
            align='center',
            color='lightgrey'
        )
        self.flag = Flag(
            width=settings.WIDTH,
            height=settings.HEIGHT
        )
        self.all_enemies = AllEnemies(
            num=self.ball,
            difficulty=self.difficulty
        )

    def add_score(self, score):
        self.score += score
        print(self.score)

    def next_level(self):
        self.level_index += 1
        self.player.life = settings.LEVELS[self.level_index]['life']
        self.ball = settings.LEVELS[self.level_index]['ball']
        self.difficulty = settings.LEVELS[self.level_index]['difficulty']
        self.reset_level()
    
    def reset_level(self):
        for ob in self.all_enemies.balls:
            ob.hideturtle()
        self.flag.hideturtle()
        self.all_enemies = AllEnemies(
            num=self.ball,
            difficulty=self.difficulty
            ) # create new enemie
        self.flag = Flag(
            width=settings.WIDTH,
            height=settings.HEIGHT
            ) # create new flag
        self.player.life = settings.LEVELS[self.level_index]['life']

    def update_board(self):
        self.life_board.message = f'Remain: {self.player.life}'
        self.life_board.update_message()
        self.score_board.message = f'Score: {self.score}'
        self.score_board.update_message()
        self.level_board.message = f'Level: {self.level_index} + 1'
        self.level_board.update_message()

    def reset_board(self):
        self.level_board.clear()
        self.life_board.clear()
        self.score_board.clear()
        self.game_board.clear()
        self.menu_board.clear()

    def reset(self):
        self.game_state = True
        self.level_index = 0
        self.difficulty = 1
        self.score = 0
        self.player.goto(0, -settings.HEIGHT/2 + 20)
        self.ball = settings.LEVELS[self.level_index]['ball']
        self.reset_level()
        self.reset_board()



