# 字典里面套字典，字典里面套列表
# 就像文件夹里套文件夹

network = {
    # "core" 是键，值是另一个字典
    "core": {
        "name": "Core-SW",
        "ip": "10.0.0.1",
        "ports": 48
    },
    # "access" 是键，值是一个列表
    # 列表里面有3个字典
    "access": [
        {"name": "Acc-SW-1", "ip": "10.0.0.11", "ports": 24},
        {"name": "Acc-SW-2", "ip": "10.0.0.12", "ports": 24},
        {"name": "Acc-SW-3", "ip": "10.0.0.13", "ports": 24}
    ]
}

# 取核心交换机名字
# network["core"] 是 {"name": "Core-SW", ...}
# 再 ["name"] 取 "Core-SW"
print(f"核心交换机: {network['core']['name']}")

# len() 算列表有几个元素
# "access" 列表有3个字典，所以是3
print(f"接入交换机数量: {len(network['access'])}")

# 计算总端口
# 先设 total = 0
total_access_ports = 0

# 循环：一个一个接入交换机看
# 第一次：sw = {"name": "Acc-SW-1", "ip": "10.0.0.11", "ports": 24}
# 第二次：sw = {"name": "Acc-SW-2", ...}
# 第三次：sw = {"name": "Acc-SW-3", ...}
for sw in network["access"]:
    # sw["ports"] 是当前交换机的端口数
    # total_access_ports += ... 是累加
    # 第一次：0 + 24 = 24
    # 第二次：24 + 24 = 48
    # 第三次：48 + 24 = 72
    total_access_ports += sw["ports"]

print(f"接入层总端口: {total_access_ports}")
# 输出：接入层总端口: 72