math_point_keep = int(input("คะแนนเก็บ = "))
if math_point_keep<=10:
    print("ไม่ผ่าน")
elif math_point_keep<=20:
    print("ปรับปรุง")
elif math_point_keep<=30:
    print("ดีมาก")
else:
    print("อย่าบ้า")

math_point_midterm = int(input("คะแนนสอบกลางภาค = "))
if math_point_midterm<=10:
    print("ไม่ผ่าน")
elif math_point_midterm<=20:
    print("ปรับปรุง")
elif math_point_midterm<=30:
    print("ดีมาก")
else:
    print("อย่าบ้า")

math_point_final = int(input("คะแนนสอบปลายภาค = "))
if math_point_final<=20:
    print("ไม่ผ่าน")
elif math_point_final<=25:
    print("ปรับปรุง")
elif math_point_final<=40:
    print("ดีมาก")
else:
    print("อย่าบ้า")

print("-----------------------------------------")


grade = (math_point_keep + math_point_midterm + math_point_final)

if 90<=grade<=100:
    print("Grade = A+")
elif 80<=grade<=89:
    print("Grade = A")
elif 75<=grade<=79:
    print("Grade = B+")
elif 70<=grade<=74:
    print("Grade = B")
elif 65<=grade<=69:
    print("Grade = C+")
elif 60<=grade<=64:
    print("Grade = C")
elif 55<=grade<=59:
    print("Grade = D+")
elif 50<=grade<=54:
    print("Grade = D")
elif 0<=grade<=49:
    print("Grade = F")
else:
    print("อย่าบ้าาา")

print("Point = ",grade)