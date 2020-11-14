# ttt_02_input.py
#
# 틱택토 입력 받기


# 보드 출력 함수 선언
def prn_board(tb):
    for r in range(3):
        print("{}:{}:{}".format(board[r][0], board[r][1], board[r][2]))
        print("-"*5)

# 보드 초기화
board = [
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' ']
]

# 보드 출력
prn_board(board)


# 입력 받기
for cnt in range(9):
    while True:
        y, x = map(int, input("좌표(y, x) : ").split(','))
        # y, x에 돌을 놓을 수 있는지 확인
        if board[y][x] == ' ':
            break;
        print("돌을 놓을 수 없습니다. 다시 지정하세요.")

    board[y][x] = 'X'
    prn_board(board)

