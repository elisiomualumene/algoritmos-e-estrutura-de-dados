def contagem(i):
    print(i)
    if i >= 10:
        return
    else:
        contagem(i+1)

print(contagem(1))