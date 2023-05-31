from api_limit_call import check_api_limit


def calc_square(x):
    check_api_limit()
    return x**2

nums = [2,3,5]
result = list(map(calc_square, nums))
print(result)
for i, num in enumerate(result):
    print(f'{i}, {num}')