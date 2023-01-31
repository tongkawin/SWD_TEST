num = 3423114 # input number here
res = [int(x) for x in str(num)]
thai = { 1: "หนึ่ง", 2: "สอง", 3: "สาม", 4: "สี่", 5: "ห้า", 6: "หก", 7: "เจ็ด", 8: "แปด", 9: "เก้า" }
thai2 = { 1: "เอ็ด", 2: "ยี่"}
unit = { 1: "ล้าน", 2: "แสน", 3: "หมื่น", 4: "พัน", 5: "ร้อย", 6: "สิบ" }
calUnit = 7-len(res)
word = ''
j = 0
for i in res:
    j+=1
    if j == len(res) and i == 1:
        word += thai2[i]
    elif j == len(res)-1 and i == 2:
        word += (thai2[i]+unit[j+calUnit])
    elif j == len(res)-1 and i == 1:
        word += (unit[j+calUnit])
    elif j != len(res):
        word += (thai[i]+unit[j+calUnit])
    else:
        word += thai[i]
        
print(num, ' ', word)