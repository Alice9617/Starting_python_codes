#当ててほしい数
cnt=0
while True:
    cnt=cnt+1
    print("数値を当ててみてください。")
    a=int(input("数値を入力："))
    if A==10:
        print("正解")
        print(f"あなたは正解するまでに{cnt}回かかりました。")
        break
    else:
        print("間違い")
