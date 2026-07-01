for i in range (1,13):
    print(f"interface fa0/{i}")
    print(" switchport mode access")

    if i <= 6:
        print(" switchport mode access vlan 10")
    else:
        print(" switchport mode access vlan 20")
    print("!")