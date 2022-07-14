import pygame

pygame.init()

# 创建游戏的窗口 480 * 700
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# 1. 加载图像数据  - 加载
bg = pygame.image.load("./imgaes/background.png")
# 2. blit 绘制图像  - 调整位置
screen.blit(bg, (0, 0))
# 3. update 更新屏幕显示  - 更新
pygame.display.update()

# 绘制英雄的飞机
hero = pygame.image.load("./imgaes/me1.png")
screen.blit(hero, (150, 500))
pygame.display.update()

while True:
    pass

pygame.quit()
