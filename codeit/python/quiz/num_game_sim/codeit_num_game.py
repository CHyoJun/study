import random

Answer = random.randint(1, 20)
num_tries = 4

guess = -1
tries = 0

while guess != Answer and tries < num_tries:
    guess = int(int(input(f"기회가 {num_tries - tries}번 남았습니다. 1-20 사이의 숫자를 맞춰 보세요:")))
    tries += 1

    if Answer > guess:
        print("Up")
    elif Answer < guess:
        print("Down")

if guess == Answer and tries < num_tries:
    print(f"축하합니다 {num_tries}번 만에 숫자를 맞추셨습니다")
else:
    print(f"아쉽습니다. 정답은{Answer}")


