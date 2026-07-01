vlan_id = input("请输入你的vlan id:\n")
try:
    vlan_id = int(vlan_id)
    if vlan_id < 1 :
        print("vlan id错误!不存在小于1的vlan")
    elif vlan_id > 4094 :
        print("vlan id错误！不存在大于4094的vlan")
    else :
        print(f"vlan id {vlan_id} 正确！")
except ValueError:
    print(f"请输入数字！你输入的{vlan_id}不是数字")







