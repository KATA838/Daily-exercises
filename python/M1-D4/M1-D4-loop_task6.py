# ============================================
# 文件名: M1-D4-loop_task6.py
# 功能: 动态分配VLAN（3个VLAN，每个4个端口）
# ============================================

# 定义VLAN列表
vlans = [10,20,30]

# len() 计算列表长度
# vlan_count = 3（因为有3个VLAN）
vlan_count = len(vlans)

# 计算总端口数
# 3个VLAN × 每个4个端口 = 12个端口
total_vlan_count = vlan_count * 4

# range(1, 13) 生成1-12
for i in range(1,total_vlan_count + 1):
    
    # 计算当前端口属于哪个VLAN
    # (i-1) 是为了让计算从0开始
    # // 是整除（取商的整数部分）
    # 
    # i=1: (0)//4 = 0 → vlans[0] = 10
    # i=2: (1)//4 = 0 → vlans[0] = 10
    # i=3: (2)//4 = 0 → vlans[0] = 10
    # i=4: (3)//4 = 0 → vlans[0] = 10
    # i=5: (4)//4 = 1 → vlans[1] = 20
    # ...
    # i=9: (8)//4 = 2 → vlans[2] = 30
    vlan_index = (i-1) // 4
    
    # 根据索引取VLAN编号
    vlan_id = vlans[vlan_index]

    # 打印接口配置
    print(f"interface fa0/{i}")
    print("    switchport mode access")
    print(f"    switchport access vlan {vlan_id}")
    print("!")
    
# 循环结束后：
# fa0/1-4  → VLAN 10
# fa0/5-8  → VLAN 20
# fa0/9-12 → VLAN 30