def solution(A):
    new_array = [item for item in A if -9 <= item <= 9]
    max_value = max(new_array)
    return max_value


# Testes
print(solution([-6, -91, 1011, -100, 84, -22, 0, 1, 473]))
print(solution([-6, -91, 1011, -100, 84, -22, 0, -7, 473]))
print(solution([-6, -91, 1011, -100, 84, -22, -4, -7, 473]))
