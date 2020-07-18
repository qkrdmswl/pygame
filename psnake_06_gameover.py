# psnake_06_gameover.py

import pygame
import random

# 화면 초기화
pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("PYSNAKE")
clock = pygame.time.Clock()

# 변수 초기화
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# 셀
CELL_SIZE = 40
COL_COUNT = SCREEN_WIDTH // CELL_SIZE
ROW_COUNT = SCREEN_HEIGHT // CELL_SIZE

# 이동방향
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
direction = DOWN

# 정수
score = 0

# 글꼴 설정
score_font = pygame.font.SysFont("comicsans", 40)

# 뱀 좌표 리스트 만들기
s_pos = (COL_COUNT // 2, ROW_COUNT // 2)
bodies = [s_pos]

# 먹이 생성 함수 add_food()
def add_food():
    while True:
        c_idx = random.randint(0, COL_COUNT-1)
        r_idx = random.randint(0, ROW_COUNT-1)
        f_pos = (c_idx, r_idx)
        if f_pos not in bodies and f_pos not in foods:
            foods.append(f_pos)
            break



# 먹이 10개 좌표 리스트 만들기
foods = []
for _ in range(10):
    add_food()

# 게임 루프
while True:

    # 뱀 머리 추출하고 다음 방향으로 이동

    # 먹이 충돌 체크 & 꼬리 지우기

    # 화면 초기화

    # 격자 그리기

    # 먹이 그리기

    # 뱀 그리기

    # 점수 출력

    # 화면 업데이트

# 게임 종료
pygame.quit()