# ttt_04_judge.py
#
# 틱택토 판정


# 보드 출력 함수 prn_board(tb)
def prn_board(tb):
    for r in range(3):
        print("{}:{}:{}".format(board[r][0], board[r][1], board[r][2]))
        print("-"*5)


# 변수 초기화(board, turn)
turn = 'X'
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

prn_board(board)

# 게임 루프
for x in range(9):
    # 좌표 입력 받기
    while True:
        y, x = map(int, input("(y, x) : ").split(','))
        if board[y][x] != ' ':
            print("돌을 놓을 수 없습니다. 다시 지정하세요.")
            break

        # 좌표에 돌 넣기 (보드 출력)
        board[y][x] = turn
        prn_board(board)


        # 승리 판정
        if board[y][0] == turn and board[y][1] == turn and board[y][2] == turn:
            break
        elif board[0][x] == turn and board[1][x] == turn and board[2][x] == turn:
            break
        else:
            # 턴(돌) 변경하기
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'

    # 승리 멘트
    print(turn,"가 이겼습니다!")
    break

# 게임 종료
print("종료")
