#短袖的信息
id1= 1
nema1= "短袖"
price1=150
num1=120
quan1="A+"
add1="北京"
#短裤的信息
id2= 2
nema2= "短裤"
price2=100
num2=150
quan2="B+"
add2="海南"
#羽绒服的信息
id3= 3
nema3= "羽绒服"
price3=1035
num3=160
quan3="A+"
add3="上海"
#牛仔裤的信息
id4= 4
nema4= "牛仔裤"
price4=100
num4=1500
quan4="C+"
add4="海南"
#衬衫的信息
id5= 5
nema5= "衬衫"
price5=50
num5=150
quan5="B+"
add5="开封"
#丝袜的信息
id6= 6
nema6= "丝袜"
price6=2800
num6=150
quan6="B+"
add6="莆田"
print("====================欢迎来到宫浩凯服装商城==========================")
print("编号       名称        价格        数量       品质       供货地")
print("--------------------------------------------------------------------")
print(id1,"     ",nema1,"    ",price1,"    ",num1,"     ",quan1,"     ",add1)
print(id2,"     ",nema2,"    ",price2,"    ",num2,"     ",quan2,"     ",add2)
print(id3,"     ",nema3,"    ",price3,"    ",num3,"     ",quan3,"     ",add3)
print(id4,"     ",nema4,"    ",price4,"    ",num4,"     ",quan4,"     ",add4)
print(id5,"     ",nema5,"    ",price5,"    ",num5,"     ",quan5,"     ",add5)
print(id6,"     ",nema6,"    ",price6,"    ",num6,"     ",quan6,"     ",add6)
print("---------------------------------------------------------------------")
print("总金额：￥",(price1 * num1  +  price2 * num2 + price3 * num3 + price4* num4+ price5 * num5+ price6 * num6))