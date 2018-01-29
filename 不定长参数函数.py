def random_num_sum(a, b, *any_num):
    """不定长数量加数相加

    具体使用方法"""
    print(a + b + sum(any_num))

# random_num_sum(1)
random_num_sum(1, 2)
random_num_sum(1, 2, 3)
random_num_sum(1, 2, 3, 4)

help(random_num_sum)
