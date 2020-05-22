import pygame as pg
from Color import *
from Snake import *
from Food import *


class SnakeGame:
    def __init__(self, dis_width=400, dis_height=300):
        self.gameover = False
        self.dis_width = dis_width
        self.dis_height = dis_height
        self.level = 1
        self.score = 0
        self.bonus = 10

    def message(self, surface, msg, color, pos):
        font_style = pg.font.Font(None, 25)
        text = font_style.render('Your Score', True, color)
        text_rect = text.get_rect(center=(self.dis_width // 2, self.dis_height // 2 - 30))
        surface.blit(text, text_rect)

        text = font_style.render(str(self.score), True, color)
        text_rect = text.get_rect(center=(self.dis_width // 2, self.dis_height // 2))
        surface.blit(text, text_rect)
        pg.display.update()

    def checkAteFood(self, surface, snake, food, color):
        if [snake.x, snake.y] in food.pos:
            self.level += 1
            if self.level // 10:
                self.bonus = self.level // 10 * 50
            self.score += self.bonus
            snake.body.append((snake.x, snake.y))
            food.pos.remove([snake.x, snake.y])

            # Avoid the food generated on the snake's body
            if not food.pos:
                for i in range(self.level // 10 + 1):
                    res = True
                    while res:
                        new_food = food.createFood()
                        res = new_food in snake.body
                    food.pos.append([new_food[0], new_food[1]])

            # Speed up whenever 5 more level is reached
            if not self.level % 5:
                snake.speed += 3
            else:
                snake.speed += 1

    def run(self):
        pg.init()
        display = pg.display
        surface = display.set_mode((self.dis_width, self.dis_height))

        display.set_caption('Snake game by AndyYeung')
        color = Color()
        snake = Snake(200, 150, 10)
        food = Food(self.dis_width, self.dis_height, 10)

        clock = pg.time.Clock()

        while not self.gameover:
            snake.auto_move()
            self.checkAteFood(surface, snake, food, color)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.gameover = True
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT:
                        snake.move(-10, 0)
                    elif event.key == pg.K_RIGHT:
                        snake.move(10, 0)
                    elif event.key == pg.K_UP:
                        snake.move(0, -10)
                    elif event.key == pg.K_DOWN:
                        snake.move(0, 10)
                    elif event.key == pg.K_ESCAPE:
                        self.gameover = True

            self.checkAteFood(surface, snake, food, color)

            # Reset the position of the snake if exceed the display's boundary
            if snake.x < 0:
                snake.x = self.dis_width - snake.size
            elif snake.x >= self.dis_width:
                snake.x = 0
            elif snake.y < 0:
                snake.y = self.dis_height - snake.size
            elif snake.y >= self.dis_height:
                snake.y = 0

            display.update()

            # Check if the snake head touches itself body
            if snake.dead:
                surface.fill(color.Black)
                self.message(surface, 'Your', color.Red, [(self.dis_width // 2) - (len('') // 2 * 10), self.dis_height // 2])

                display.update()
                while True:
                    for event in pg.event.get():
                        if event.type == pg.QUIT:
                            self.gameover = True
                            return
                        elif event.type == pg.KEYDOWN:
                            if event.key == pg.K_ESCAPE:
                                self.gameover = True
                                return
                            elif event.key == pg.K_SPACE:
                                return self.run()

            surface.fill(color.Black)

            for sb in snake.body:
                pg.draw.rect(surface, color.White, [sb[0], sb[1], 10, 10])

            for f in food.pos:
                pg.draw.rect(surface, color.Blue, [f[0], f[1], 10, 10])

            display.update()
            clock.tick(snake.speed)


# Start the game
SnakeGame().run()
pg.quit()
quit()
