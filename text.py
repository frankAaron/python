for i in range(3,21):
    for j in range(3,round(i**0.5)+1,2):
        if i%j == 0:
            break
        else:
            print(i)