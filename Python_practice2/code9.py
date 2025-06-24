#加法か減法かを指定して計算するプログラム
print("加法を行いたい場合は１、減法を行いたい場合は２を入力してください")
a=int(input("モードを入力:"))
if a==1:
    print("加法です。数を入力してください。")
    b=int(input("A:"))
    c=int(input("B:"))
    print(b+c)
elif a==2:
    print("減法です。数を入力してください。")
    f=int(input("A:"))
    g=int(input("B:"))
    print(f-g)
else:
    print("１か２を入力してください。")



#正答例:外で変数を指定すると楽だぞ‼
print("1：加算,2：減算")
a=int(input("モードを入力；"))
b=int(input("A:"))
c=int(input("b:"))
if a==1:
    print(a+b)
elif a==2:
    print(a-b)
else:
    print("適切な数値を入力してください。")