# ============================================
# 文件名: M1-D4-loop_task5.py
# 功能: 前6个端口给VLAN 10，后6个端口给VLAN 20
# ============================================

# range(1, 13) 生成1-12，共12个端口
for i in range (1,13):
    
    # 打印接口名
    print(f"interface fa0/{i}")
    
    # 设置access模式
    print(" switchport mode access")

    # 条件判断：前6个端口给VLAN 10
    # i <= 6 表示 i 小于或等于 6
    # 也就是 i = 1, 2, 3, 4, 5, 6 时成立
    if i <= 6:
        print(" switchport mode access vlan 10")
    
    # 否则（i = 7, 8, 9, 10, 11, 12）
    else:
        print(" switchport mode access vlan 20")
    
    # 分隔符
    print("!")
    
# 循环结束后：
# fa0/1 到 fa0/6 属于 VLAN 10
# fa0/7 到 fa0/12 属于 VLAN 20