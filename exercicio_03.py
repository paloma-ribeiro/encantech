def solution(S):
    if 'a' not in S or 'b' not in S:
        return True
    order = ''.join(sorted(S))
    return order == S


# Testes
print(solution('aabb'))
print(solution('ba'))
print(solution('aaaa'))
print(solution('bbb'))
print(solution('abba'))
print(solution('abab'))
