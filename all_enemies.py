from enemy import Enemy
import settings

class AllEnemies:
    def __init__(self, num=5, difficulty=5):
        self.balls = []
        for i in range(num):
            new_enemy = Enemy(
                width=settings.WIDTH,
                height=settings.HEIGHT,
                difficulty=difficulty
            )
            self.balls.append(new_enemy)

    def move(self):
        for ball in self.balls:
            ball.move()
            for other_ball in self.balls:
                if ball.distance(other_ball) < 20:
                    other_ball.setheading(-other_ball.heading() + 180)
                    ball.setheading(-ball.heading() + 180)