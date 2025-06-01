import sys
import tty
import termios

def print_table(left_r, right_r, ball):
    for height in range(25):  # height - высота поля
        for width in range(80):  # width - ширина поля
            if height == 0 or height == 24:
                print("-", end="")
            elif ((height == left_r or height == left_r + 1 or height == left_r - 1) and width == 0) or \
                 ((height == right_r or height == right_r + 1 or height == right_r - 1) and width == 79):
                print("|", end="")
            elif height == 12 and width == ball:
                print("o", end="")
            else:
                print(" ", end="")
        print()

def player_one_turn(key, current_position):
    if key == 'a':
        if current_position > 2:
            current_position -= 1
    elif key == 'z':
        if current_position < 22:
            current_position += 1
    return current_position

def player_two_turn(key, current_position):
    if key == 'k':
        if current_position > 2:
            current_position -= 1
    elif key == 'm':
        if current_position < 22:
            current_position += 1
    return current_position

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def main():
    left_r = 12
    right_r = 12
    ball = 1
    prev_ball = 0
    player_one_score = 0
    player_two_score = 0

    while player_one_score <= 21 and player_two_score <= 21:
        if player_one_score == 21:
            print("Player 1 win! Congratulations!")
            break
        elif player_two_score == 21:
            print("Player 2 win! Congratulations!")
            break

        key = getch()
        if key == 'a' or key == 'z':
            left_r = player_one_turn(key, left_r)
        elif key == 'k' or key == 'm':
            right_r = player_two_turn(key, right_r)
        elif key == 'q':
            print(f"Player 1: {player_one_score}\nPlayer 2: {player_two_score}")
            break

        # Обработка движения мяча
        if ball == 1 and (left_r == 11 or left_r == 12 or left_r == 13):
            prev_ball = ball
            ball += 1
            print_table(left_r, right_r, ball)
        elif ball == 78 and (right_r == 11 or right_r == 12 or right_r == 13):
            prev_ball = ball
            ball -= 1
            print_table(left_r, right_r, ball)
        elif ball == 1 and (left_r != 11 and left_r != 12 and left_r != 13):
            player_two_score += 1
            print(f"Player 1: {player_one_score}\nPlayer 2: {player_two_score}")
            ball = 1
            prev_ball = 0
            left_r = 12
            right_r = 12
        elif ball == 78 and (right_r != 11 and right_r != 12 and right_r != 13):
            player_one_score += 1
            print(f"Player 1: {player_one_score}\nPlayer 2: {player_two_score}")
            ball = 78
            prev_ball = 0
            left_r = 12
            right_r = 12
        elif 1 < ball < 78:
            if prev_ball < ball:
                prev_ball = ball
                ball += 1
                print_table(left_r, right_r, ball)
            elif prev_ball > ball:
                prev_ball = ball
                ball -= 1
                print_table(left_r, right_r, ball)
        else:
            print("Ball motion mistake!\n")

if __name__ == "__main__":
    main()
