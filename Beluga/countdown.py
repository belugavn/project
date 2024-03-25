n = int(input("Nhap so"))
while n>0:
        n = n-1
        print(n)
if n==0:
    print('Happy New Year')

n = int(input("Nhập số n: "))
numbers = list(range(n+1))
reversed_numbers = numbers[::-1]
print(f"Dãy số đảo ngược từ 0 đến {n} là: {reversed_numbers}")

