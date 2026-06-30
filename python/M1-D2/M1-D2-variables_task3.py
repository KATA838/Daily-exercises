# 字典用花括号 {}
# 格式：键: 值，键: 值
# "name" 是键，"Core-SW-01" 是值
device = {
    "name": "Core-SW-01",    # 设备名
    "ip": "10.0.0.1",        # IP地址
    "vendor": "Cisco",        # 厂商
    "ports": 48,              # 端口数（数字不用引号）
    "vlans": [10, 20, 30],   # VLAN列表（列表可以当值）
    "status": "up"            # 状态
}

# 查字典：用方括号 [] 里面写键
# device["name"] 就是取 "name" 对应的值
print(f"设备名: {device['name']}")
# 输出：设备名: Core-SW-01

print(f"厂商: {device['vendor']}")
# 输出：厂商: Cisco

# 修改字典：直接赋值
# 原来没有 "location"，现在加上
device["location"] = "机房A"
# 现在 device 里多了 "location": "机房A"

# 修改已有的值
device["ports"] = 52
# 原来48，现在变成52

# 遍历：一个一个看
# .items() 把字典变成一对一对的
# 第一次：key="name", value="Core-SW-01"
# 第二次：key="ip", value="10.0.0.1"
# ...
print("\n--- 设备完整信息 ---")
for key, value in device.items():
    print(f"{key}: {value}")