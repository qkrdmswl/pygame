# ttt_08_input.py
# 파이게임 마우스 입력 처리

import pygame

pygame.init()

# 창 설정
SCREEN_WIDTH = 450
SCREEN_HEIGHT = 450
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# 창 출력
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("TIC TAC TOE")

# 변수 초기화
WHITE = (255, 255, 255)
CELL_SIZE = 150
ROW_COUNT = SCREEN_HEIGHT // CELL_SIZE
COL_COUNT = SCREEN_WIDTH // CELL_SIZE


# 격자 그리기 함수 draw_grid()
def draw_grid():
    for gy in range(ROW_COUNT):
        for gx in range(COL_COUNT):
            one_rect = pygame.Rect(gx * CELL_SIZE, gy * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, WHITE, one_rect, 3)


# 클릭한 셀의 좌표를 보드의 좌표로 변경
def cell_to_board(tm_pos):
    for y in range(ROW_COUNT):
        for x in range(COL_COUNT):
            if y * CELL_SIZE <= tm_pos[1] < y * CELL_SIZE + CELL_SIZE:
                row = y
            if x * CELL_SIZE <= tm_pos[0] < x * CELL_SIZE + CELL_SIZE:
                col = x

    return row, col


# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_pos = pygame.mouse.get_pos()

            r, c = cell_to_board(m_pos)
            print("행: {}, 열: {}".format(r, c))


            # 마우스 오른쪽 버튼 클릭하면 게임 종료
            if event.button == 3:
                running = False

    # 사각형 그리기
    draw_grid()

    # 화면 업데이트
    pygame.display.update()


# 파이게임 종료
pygame.quit()