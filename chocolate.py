divisao = int(input())
val = [int(divisao) for divisao in input().split()]
amz = sum(val) - divisao
print(amz)