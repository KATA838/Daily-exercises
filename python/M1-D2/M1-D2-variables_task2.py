#初始vlan列表
vlans = [10,20,30]

#添加vlan
vlans.append(40)
vlans.append(50)

#打印信息
print(f"当前vlan列表{vlans}")
print(f"vlan数量{len(vlans)}")
print(f"第一个vlan{vlans[0]}") #索引从0开始
print(f"最后一个vlan{vlans[-1]}") #-1最后一个

#删除vlan
vlans.remove(20)
print(f"删除vlan 20后{vlans}")