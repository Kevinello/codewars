def solution(number: int):
    cal = lambda x: x if (x % 3 == 0) or (x % 5 == 0) else 0
    return sum(map(cal, range(1,number)))

print(solution(10))
    