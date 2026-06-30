# 这一行是注释，Python不会执行，给人看的
# 创建文件 study/day02/task1_port_usage.py

# 定义变量：给数据贴个标签，方便后面用
total_ports = 48      # 总端口数，这台交换机有48个口
used_ports = 35       # 已经插了网线的端口
reserved_ports = 4    # 预留的，不能用的端口

# 计算可用端口
# available 是"可用的"意思
# = 右边的计算：48 - 35 - 4 = 9
available = total_ports - used_ports - reserved_ports

# 计算利用率
# usage_rate 是"使用率"
# used_ports / total_ports = 35 / 48 = 0.729
# * 100 变成百分比：72.9
# 所以 usage_rate = 72.9
usage_rate = (used_ports / total_ports) * 100

# print 是"打印"，把内容显示到屏幕上
# f"" 是 f-string，可以在字符串里塞变量
# {total_ports} 会被替换成 48
print(f"总端口: {total_ports}")

# 这一行和上面一样，显示已用端口
print(f"已用: {used_ports}")

# 显示预留端口
print(f"预留: {reserved_ports}")

# 显示计算出来的可用端口
print(f"可用: {available}")

# :.1f 是格式化
# usage_rate 本来是 72.91666...
# :.1f 表示"保留1位小数"，变成 72.9
print(f"利用率: {usage_rate:.1f}%")