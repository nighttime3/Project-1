from turtle import Screen
from game import Game
import settings

screen = Screen()
screen.tracer(0)
screen.bgcolor('grey')
screen.setup(
    width=settings.WIDTH,
    height=settings.HEIGHT
)

game = Game()

def game_brain():
    game.reset()
    while game.game_state:
        game.all_enemies.move()
        game.update_board() # update in every move
        for ball in game.all_enemies.balls:
            if ball.distance(game.player) <= 20:
                game.game_board.set_message('Game Over: You are under attack!!!')
                game.menu_board.set_message('Press s for restart.')
                game.update_board()
                game.game_state = False
        if game.player.life == 0:
            game.game_board.set_message('Game Over: No enough move left!')
            game.score_board.message = f'Score: {game.score}'
            game.menu_board.set_message('Press s for restart.')
            game.life_board.set_message('Remain: 0')
            game.game_state = False
        if game.player.distance(game.flag) <= 40:
            if game.level_index < len(settings.LEVELS) - 1:
                game.add_score(game.player.life)
                game.next_level()
                game.player.next_level(game.player.life)
            else: #win the game
                game.add_score(game.player.life)
                game.update_board
                game.game_board.set_message(f'You win with score: {game.score}')
                game.menu_board.set_message('Press s for restart.')
                game.game_state = False
        screen.update()

screen.listen()
screen.onkeypress(key='Down', fun=game.player.move_down)
screen.onkeypress(key='Up', fun=game.player.move_up)
screen.onkeypress(key='Left', fun=game.player.move_left)
screen.onkeypress(key='Right', fun=game.player.move_right)
screen.onkey(key='s', fun=game_brain)

screen.exitonclick()