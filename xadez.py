linhas = int(input())
coluna = int(input())

if linhas % 2 != 0 and coluna % 2 != 0:
    print(1)

elif linhas % 2 == 0 and coluna % 2 == 0:
    print(1)

elif linhas % 2 == 0 and coluna % 2 != 0:
    print(0)
else:
    print(0)