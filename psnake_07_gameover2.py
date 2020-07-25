# psnake07_gameover2.py
#
# 게임오버 만들기
#

import pygame
import random

# 화면 그리기
pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("PYSNAKE")
clock = pygame.time.Clock()

# 변수 초기화
BLUE = (0, 0, 255)        # 뱀색
GRAY = (128, 128, 128)    # 격자색
BLACK = (0, 0, 0)         # 배경색
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)       # 먹이색
YELLOW = (255, 255, 0)
DEEPBLUE = (0, 0, 100)     # 뱀 머리색

CELL_SIZE = 40
COL_COUNT = SCREEN_WIDTH // CELL_SIZE
ROW_COUNT = SCREEN_HEIGHT // CELL_SIZE

LEFT, RIGHT, UP, DOWN = 0, 1, 2, 3
direction = DOWN

GAMEOVER = False

# 점수 초기화
score = 0

# 폰트 설정
score_font = pygame.font.SysFont("comicsans", 40)
gameover_font = pygame.font.SysFont("comicsans", 80)

# 뱀 좌표 리스트 (화면 중앙)
bodies = [(COL_COUNT // 2 , ROW_COUNT // 2)]




# 먹이 추가 함수 add_food() 만들기
def add_food():
    while True:
        c_idx = random.randint(0, COL_COUNT - 1 )
        r_idx = random.randint(0, ROW_COUNT - 1 )
        f_pos = (c_idx, r_idx)
        if f_pos not in bodies and f_pos not in foods:
            foods.append(f_pos)
            break

# 먹이 10개 리스트 만들기
foods = []
for _ in range(10):
    add_food()


# 게임 루프
while True:
    # 키 처리
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    if event.type == pygame.KEYDOWN and not GAMEOVER:
        if event.key == pygame.K_LEFT:
            direction = LEFT
        if event.key == pygame.K_RIGHT:
            direction = RIGHT
        if event.key == pygame.K_UP:
            direction = UP
        if event.key == pygame.K_DOWN:
            direction = DOWN


    # 뱀 머리 추출 후 다음 방향 이동
    head = bodies[0]
    c_idx, r_idx = head[0], head[1]
    if direction == LEFT:
        c_idx -= 1
    elif direction == RIGHT:
        c_idx += 1
    elif direction == UP:
        r_idx -= 1
    elif direction == DOWN:
        r_idx += 1
    head_pos = (c_idx, r_idx)

    # 충돌 감지
    if head_pos in bodies or c_idx <0 or c_idx > COL_COUNT or r_idx > ROW_COUNT or r_idx < 0:
        GAMEOVER = True


    bodies.insert(0, head_pos)

    # 먹이 먹기
    if head_pos in foods:
        foods.remove(head_pos)
        add_food()
        score += 10
    else:
        bodies.pop()


    # 화면 초기화
    screen.fill(BLACK)

    # 격자 그리기
    for c_idx in range(COL_COUNT):
        for r_idx in range(ROW_COUNT):
            rect = (c_idx * CELL_SIZE, r_idx * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GRAY, rect, 1)

    # 뱀 그리기
    for one in bodies:
        rect = (one[0] * CELL_SIZE, one[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, BLUE, rect)

    head_rect = (bodies[0][0] * CELL_SIZE, bodies[0][1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, DEEPBLUE, head_rect)


    # 먹이 그리기
    for food in foods:
        f_rect = (food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, GREEN, f_rect)


    # 점수 출력
    score_img = score_font.render(f"SCORE: {score}", True, YELLOW)
    screen.blit(score_img, (10, 10))

    # 게임 오버 출력:
    if GAMEOVER:
        gover_img = gameover_font.render("GAME OVER", True, YELLOW)
        screen.blit(gover_img, (SCREEN_WIDTH // 2 - gover_img.get_width() // 2 , SCREEN_HEIGHT // 2))

    # 화면 업데이트
    pygame.display.update()
    clock.tick(6)

# 게임 종료
pygame.quit()
