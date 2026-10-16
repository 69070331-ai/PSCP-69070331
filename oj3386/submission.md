ห้ามคัดลอกคำอธิบายจาก AI

ห้ามคัดลอกคำอธิบายจากคนอื่น

```text
วิธีสุดท้ายเหมือนกับแผนแรก
```

---

## 5. การทดสอบของฉัน

เขียน test cases อย่างน้อย 3 กรณีที่ลองเองหรือออกแบบเอง

พยายามเลือก test cases ที่แตกต่างกัน

แต่ละ test case ให้อธิบายว่าทำไมเลือกกรณีนั้น

ถ้า input หรือ output มีหลายบรรทัด ให้เขียนไว้ใน text blocks

### Test Case 1

ทำไมเลือก case นี้:

```text
เพื่อทดสอบการหารายชื่อที่ซ้ำกันระหว่างสองกลุ่ม และตรวจสอบว่าระบบเรียงรายชื่อจากมากไปน้อยตามตัวอักษร โดย David มาก่อน Bob
```

Input:

```text
4
3
Alice
Bob
Charlie
David
Bob
David
Eve
```

Expected output:

```text
David
Bob
```

Actual output:

```text
David
Bob
```

Result:

```text
Pass
```

### Test Case 2

ทำไมเลือก case นี้:

```text
เพื่อทดสอบกรณีที่ทั้งสองกลุ่มไม่มีรายชื่อร่วมกัน โปรแกรมต้องแสดง Nope แทนการพิมพ์รายชื่อ
```

Input:

```text
3
2
Alice
Bob
Charlie
David
Eve
```

Expected output:

```text
Nope
```

Actual output:

```text
Nope
```

Result:

```text
Pass
```

### Test Case 3

ทำไมเลือก case นี้:

```text
เพื่อทดสอบว่า set ช่วยตัดรายชื่อที่ซ้ำกันภายในกลุ่มได้ และผลลัพธ์จะแสดงชื่อ Mali เพียงครั้งเดียว แม้จะปรากฏหลายครั้งในข้อมูลนำเข้า
```

Input:

```text
4
3
Mali
Nina
Mali
Ploy
Mali
Mali
Som
```

Expected output:

```text
Mali
```

Actual output:

```text
Mali
```

Result:

```text
Pass
```

---

## 6. การใช้ AI

ใช้ AI กับโจทย์นี้หรือไม่

```text
No
```

ถ้าใช้ AI ต้องทำไฟล์นี้ด้วย:

```text
ai_reflection.md
```

ถ้าถามเฉพาะเพื่อน TA หรือผู้สอน และไม่ได้ใช้ AI ไม่ต้องทำ `ai_reflection.md`

---

## 7. ความช่วยเหลือจากคน / การร่วมมือ

ได้ถามเพื่อน TA ผู้สอน หรือบุคคลอื่นเพื่อขอความช่วยเหลือในโจทย์นี้หรือไม่

```text
No
```

ถ้าใช่ ให้อธิบายสั้น ๆ ว่าได้รับความช่วยเหลือแบบใด

ตัวอย่างที่อนุญาต:

- อธิบายความหมายของโจทย์
- อธิบาย concept การเขียนโปรแกรม
- ให้ hint เกี่ยวกับแนวทาง
- คุยเรื่อง debugging
- คุยเรื่อง test cases
- ช่วยอธิบาย error message

สิ่งที่ไม่อนุญาต:

- คัดลอก code ของผู้อื่น
- ส่ง solution ของผู้อื่น
- ขอให้ผู้อื่นเขียน solution ให้
- ใช้ OJ submission ของผู้อื่น
- ขอให้ผู้อื่นส่ง OJ แทน

ใครช่วยคุณ

```text

```

เขาช่วยอะไร

```text

```

คุณยังทำอะไรด้วยตนเอง

```text

```

คุณคัดลอก code จากคนอื่นหรือไม่

```text
No
```

---

## 8. คำรับรองของนักศึกษา

เขียน `Yes` ในแต่ละ statement

| Statement | Yes/No |
|---|---|
| I wrote this submission in my own words. | Yes |
| I understand my final code. | Yes |
| I recorded the real OJ status. | Yes |
| I did not copy AI-generated text directly into this file. | Yes |
| I did not copy code from another person. | Yes |
| If I received human help, I disclosed it in this file. | Yes |
| I submitted the final code to the OJ by myself. | Yes |
