import sys


def solution(N):
    text = ""
    for index in range(0, N - 1):
        text += "L\n"
    text += "L" * N
    sys.stdout.write(text)


# Testes
solution(6)
solution(10)