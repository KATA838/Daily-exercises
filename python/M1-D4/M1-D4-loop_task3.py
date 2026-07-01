# ============================================
# 文件名: M1-D4-loop_task3.py
# 功能: 批量生成接入端口配置（12个端口，都属VLAN 10）
# ============================================

# range(1, 13) 生成：1, 2, 3, ..., 12
# 从1开始，到13结束（不包括13）
for i in range(1,13):
    
    # 打印接口名
    # fa0/1, fa0/2, ..., fa0/12
    # fa = FastEthernet，快速以太网接口
    print(f"interafce fa0/{i}")
    
    # 设置端口模式为access（接入模式）
    # 前面有空格，是接口配置子命令
    print(" switchport mode access")
    
    # 设置端口归属VLAN 10
    print(" switchport access vlan 10")
    
    # 分隔符
    print("!")
    
# 循环结束后，生成了12个端口的配置