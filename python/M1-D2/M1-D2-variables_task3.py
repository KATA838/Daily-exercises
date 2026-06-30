#ip地址列表
ip_list = ["192.168.1.1","192.168.1.2","192.168.1.3","192.168.1.4"]

#添加新ip
ip_list.append("192.168.1.5")

#打印所有ip
print("所有ip:")
for ip in ip_list:          #为什么遍历不输出
    print(f" - {ip}")

#统计数量
print(f"\n总设备数:{len(ip_list)}")

#检查某个ip是否存在
target_ip = "192.168.1.5"
if target_ip in ip_list:        
    print(f"{target_ip}在线")
else:
    print(f"{target_ip}不在线")

print("删除.5")
ip_list.remove("192.168.1.5")
print(f"所有ip{ip_list}")
if target_ip in ip_list:
    print(f"{target_ip}在线")
else:
    print(f"{target_ip}不在线")