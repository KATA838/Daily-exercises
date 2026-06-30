# 数字：交换机端口数量
total_ports = 24
used_ports = 18
available_ports = total_ports - used_ports
print(f"交换机总端口: {total_ports}")
print(f"已用端口: {used_ports}")
print(f"可用端口: {available_ports}")

# 字符串：设备名称
device_name = "Core-Switch-01"
print(f"设备名称: {device_name}")

# 列表：VLAN列表
vlans = [10, 20, 30, 40]
print(f"现有VLAN: {vlans}")
print(f"VLAN数量: {len(vlans)}")

# 添加VLAN
vlans.append(50)
print(f"新增后: {vlans}")