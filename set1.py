n=int(input("Введите количество элементов списка "))

spisok = list(map(int, input().split()))[:n]

f=set(spisok)

print(len(f))