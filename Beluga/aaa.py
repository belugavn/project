def sochansole():
    chuoi = []
    for i in range (1,2000):
        if i%3==0:
           continue
        if i%2==0:
            chuoi.append(i)
    return chuoi if chuoi else False
def main():
        chuoi1 = sochansole()
        if chuoi1:
            print("So can tim", chuoi1)
        else:
            print("khong co so nao")

main()