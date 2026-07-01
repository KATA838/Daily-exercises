vlans = [10,20,30]
vlan_count = len(vlans)
total_vlan_count = vlan_count * 4

for i in range(1,total_vlan_count + 1):
    vlan_index = (i-1) // 4
    vlan_id = vlans[vlan_index]

    print(f"interface fa0/{i}")
    print("    switchport mode access")
    print(f"    switchport access vlan {vlan_id}")
    print("!")