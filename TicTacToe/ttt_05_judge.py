# ttt_05_judge.py
#
# 틱택토 대각선 판정


# 보드 출력 함수 prn_board(tb)
def prn_board(tb):
    for r in range(3):
        print("{}:{}:{}".format(board[r][0], board[r][1], board[r][2]))
        print("-"*5)


# 판정 함수 judge(y, x)
def judge(y, x):
    win = False
    # 판정
    if board[y][0] == board[y][1] == board[y][2] == turn:
        win = True
    if board[0][x] == board[1][x] == board[2][x] == turn:
        win = True
    if y - x == 0 and board[0][0] == board[1][1] == board[2][2] == turn:
        win = True
    if abs(y - x) == 2 and board[2][0] == board[1][1] == board[0][2] == turn:
        win = True
    return win


# 돌 모양 변경
def change_stone(tt):
    if tt == 'X':
        tt = 'O'
    else:
        tt = 'X'

# 변수 초기화(board, turn)
turn = 'X'
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

# 게임 루프
prn_board(board)

for x in range(9):
    # 좌표 입력 받기
    while True:
        y, x = map(int, input("(y, x) : ").split(','))
        # 비어있는지 확인 후 넣기
        if board[y][x] != ' ':
            print("돌을 집어넣을 수 없습니다. 재입력해주세요.")
            break

    # 돌 놓기
    board[y][x] = turn
    prn_board(board)

    # 판정 (행, 열, 대각선)
    if judge(y, x):
        msg = turn + " 승리!"
        break

    # 돌 모양 변경
    turn = change_stone(turn)


# 종료
print("게임 종료")