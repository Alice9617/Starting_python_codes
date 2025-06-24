#論理演算子

#and「～かつ～」の意味。両方達成していないと処理を行わない。どちらも真
a=5
b=3
if a==5 and b==5:
    print("真")
else:
    print("偽")

#or 「AかつB」の場合、どちらか一部が条件達成していると処理を行う。両方又は片方が真で処理を行う。
c=5
if c<6 or c<=4:
    print("真")
else:
    print("偽")

#not どちらも成り立たない場合、処理を行う。どちらも偽
d=4
if not d==2:
    print("真")
else:
    print("偽")