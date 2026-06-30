#字典+列表存储网络拓扑
network = {
    "core_switch":{             #创建的是什么，怎么存储的
        "name": "Core-SW-01",
        "ip" : "10.0.0.1",
        "ports" : 48,           #为什么没有双引号
        "vlans" : [10,20,30]
    },
    "access_switches" :[
        {"name": "Acc-SW-01", "ip": "10.0.0.11", "ports": 24},
        {"name": "Acc-SW-02", "ip": "10.0.0.12", "ports": 24},
        {"name": "Acc-SW-03", "ip": "10.0.0.13", "ports": 24}
    ]
}

#打印信息
core = network["core_switch"]  #为什么要core = 
print(f"核心交换机: {core['name']}")
print(f"管理ip:{core['ip']}")
print(f"端口数:{core['ports']}")
print(f"vlan: {core['vlans']}")

#统计接入交换机总端口数
total_access_ports = 0
for sw in network["access_switches"]:
    total_access_ports += sw["ports"]   #为什么”ports“直接计数了，不是字符串吗
print(f"\n接入交换机总端口:{total_access_ports}")