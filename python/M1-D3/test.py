age = int(input("年龄是?\n"))

if age < 18:
    print(f"未成年，年龄:{age}")
else:
    print(f"成年，年龄:{age}")

score = int(input("成绩？\n"))

if score >= 90 :
    print(f"优秀，成绩:{score}")
elif score >= 60:
    print(f"及格,成绩:{score}")
else:
    print(f"不及格，成绩:{score}")