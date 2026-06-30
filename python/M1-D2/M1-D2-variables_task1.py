#定义变量
total_ports = 24
used_ports = 18
reserved_ports = 2 #预留端口

#计算可用端口
calculate_ports = total_ports - used_ports - reserved_ports

#输出
print(f"交换机总端口:{total_ports}")    #为什么用f
print(f"已使用端口:{used_ports}")
print(f"预留端口:{reserved_ports}")
print(f"可用端口:{calculate_ports}")