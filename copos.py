n = int(input())
pos_ini = input().upper()

for i in range(n):
    mov = int(input())
    if pos_ini == 'A':
        if mov == 1:
            pos_ini = 'B'
        elif mov == 3:
            pos_ini = 'C'
    elif pos_ini == 'B':
        if mov == 1:
            pos_ini = 'A'
        elif mov == 2:
            pos_ini = 'C'
    else:
        if mov == 2:
            pos_ini = 'B'
        elif mov == 3:
            pos_ini = 'A'

print(pos_ini)
