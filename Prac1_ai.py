def generate_magic_square(n):
    magic_square = [[0 for _ in range(n)] for _ in range(n)]
    i, j = 0, n // 2
    num = 1

    while num <= n * n:
        magic_square[i][j] = num
        num += 1
        new_i, new_j = (i - 1) % n, (j + 1) % n

        if magic_square[new_i][new_j]:
            i = (i + 1) % n
        else:
            i, j = new_i, new_j
    return magic_square

n = 3   
square = generate_magic_square(n)   
for row in square:
    print(row)
    print(row)
