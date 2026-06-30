a = int(input("请输入第一个数:\n"))
x = str(input("请输入操作(+,-,*,/):\n"))
b = int(input("请输入第二个数:\n"))

def culculate (a:int,x:str,b:int) -> tuple[str,int]:
    if x == "+":
        return a+b
    if x == "-":
        return a-b
    if x == "*":
        return a*b
    if x == "/":
        return a/b

c = culculate (a , x , b)
print(f"{a} {x} {b} = {c}")

    


