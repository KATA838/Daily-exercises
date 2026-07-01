# ============================================
# 文件名: M1-D3-ifelse.py
# 功能: 检查用户输入的VLAN编号是否合法
# 作者: KATA
# ============================================

# 第1步: 获取用户输入
# input() 是一个内置函数，作用是弹出一个输入框，等待用户打字
# 用户输入的内容会被当成"字符串"保存到 vlan_id 变量里
# 比如用户输入 "100"，vlan_id 的值就是 "100"（带引号的字符串）
# \n 是换行符，让提示文字后面空一行，看起来更整齐
vlan_id = input("请输入你的vlan id:\n")

# 第2步: 尝试把字符串转成整数
# try 是"尝试执行"的意思
# 因为用户可能输入 "abc" 这样的文字，int("abc") 会报错崩溃
# 用 try 包裹起来，如果出错就跳到 except 处理，程序不会崩
try:
    # int() 是类型转换函数，把字符串变成整数
    # "100" → 100（现在可以数学比较了）
    vlan_id = int(vlan_id)
    
    # 第3步: 判断VLAN编号是否合法
    # VLAN的合法范围是 1-4094（思科标准）
    
    # 如果 vlan_id 小于 1
    if vlan_id < 1 :
        # print() 是打印输出到屏幕
        print("vlan id错误!不存在小于1的vlan")
    
    # elif 是 "else if" 的缩写，意思是"否则如果"
    # 如果 vlan_id 大于 4094
    elif vlan_id > 4094 :
        print("vlan id错误！不存在大于4094的vlan")
    
    # else 是"否则"，就是上面两个条件都不满足的情况
    # 也就是 vlan_id 在 1-4094 之间，合法！
    else :
        # f"" 是 f-string，可以在字符串里插入变量
        # {vlan_id} 会被替换成实际的数字，比如 "vlan id 100 正确！"
        print(f"vlan id {vlan_id} 正确！")

# 第4步: 处理转换失败的情况
# except 是"捕获异常"
# ValueError 是一种错误类型，表示"值错误"
# 当 int("abc") 失败时，就会抛出 ValueError
except ValueError:
    # 这里 {vlan_id} 还是原来的字符串 "abc"
    # 告诉用户输入的不是数字
    print(f"请输入数字！你输入的{vlan_id}不是数字")