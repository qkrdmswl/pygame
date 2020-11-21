# ttt_07_grid.py
# 격자 그리기

import pygame

# pygame 초기화
pygame.init()

# pygame 창 설정
SCREEN_WIDTH = 450
SCREEN_HEIGHT = 450
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# pygame 창 생성
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("TIC TAC TOE")

# 변수설정
CELL_SIZE = 150
ROW_COUNT = SCREEN_HEIGHT // CELL_SIZE
COL_COUNT = SCREEN_WIDTH // CELL_SIZE
WHITE = (255, 255, 255)

# 실행 루프
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # 사각형 그리기
    for y in range(3):
        for x in range(3):
            one_rect = (x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, WHITE, one_rect, 1)

    # pygame.draw.rect(screen, (255, 255, 255), (0, 0, 150, 150), 1)
    # pygame.draw.rect(screen, (255, 255, 255), (150, 0, 150, 150), 1)
    # pygame.draw.rect(screen, (255, 255, 255), (300, 0, 150, 150), 1)
    # pygame.draw.rect(screen, (255, 255, 255), (0, 150, 150, 150), 1)
    # pygame.draw.rect(screen, (255, 255, 255), (150, 150, 150, 150), 1)
    # pygame.draw.rect(screen, (255, 255, 255), (300, 150, 150, 150), 1)
    # pygame.draw.rect(screen, (255, 255, 255), (0, 300, 150, 150), 1)
    # pygame.draw.rect(screen, (255, 255, 255), (150, 300, 150, 150), 1)
    # pygame.draw.rect(screen, (255, 255, 255), (300, 300, 150, 150), 1)

    # 화면 업데이트
    pygame.display.update()


# pygame 종료
pygame.quit()