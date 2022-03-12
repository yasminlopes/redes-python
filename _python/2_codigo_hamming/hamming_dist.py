class HammingDistance:
    def calcDistancia(x,y):
        count=0
        resultado=x^y
        for i in range(32):
            if (resultado>>i)&1 ==1:
                count+=1

        return count

    print(calcDistancia(30, 50))