# pypang_final_modify.py
# 버그 수정

# 1. 파이게임 초기화
# 2. 게임환경 초기화 (화면 설정)
# 3. 캐릭터 이동
# 4. 무기 발사
# 5. 공 추가
# 6. 충돌 처리
# 7. 공 나누기
# 8. 메시지 출력

import pygame
import os

# 파이게임 초기화
pygame.init()

# 화면 설정
screen_width = 640
screen_height = 480
screen_size = (screen_width, screen_height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("PYGAME!")








# 파이게임 종료
pygame.quit()