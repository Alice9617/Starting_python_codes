def A(x,y):
    result=x+y
    return result
    
def B(x,y):
    result=x-y
    return result
    
def C(x,y):
    result=x*y
    return result
    
def D(x,y):
    result=x/y
    return result
    
while True:
    print("モードを入力。１は加算。２は減算。３は乗算。４は除算です。終了したい場合は１００を入力してください。")
    mode=int(input("モードを入力："))
    x=int(input("x:"))
    y=int(input("y:"))
    if mode==1:
        print("加算")
        print(A(x,y))
    elif mode==2:
        print("減算")
        print(B(x,y))
    elif mode==3:
        print("乗算")
        print(C(x,y))
    elif mode==4:
        print("除算")
        print(D(x,y))
    elif mode==100:
        print("good bye")
        break
    else:
        print("1,2,3,4,100以外の数を入力してください!!")

