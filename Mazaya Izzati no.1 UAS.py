#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def konversiSuhu(suhu):
   drjt = int(suhu[:-1])
   inputan = suhu[-1]

   if inputan.upper() == "C":
     hasil1 = float((9 * drjt) / 5 + 32)
     hasil2 = float(drjt + 273.15)
     hasil3 = float(4/5 * drjt)
     jenisX = "Celcius"
     jenis1 = "Fahrenheit"
     jenis2 = "Kelvin"
     jenis3 = "Reamur"
     print(drjt,jenisX,"=","{:.1f}".format(hasil1),jenis1)
     print(drjt,jenisX,"=","{:.1f}".format(hasil2),jenis2)
     print(drjt,jenisX,"=","{:.1f}".format(hasil3),jenis3)
                
   elif inputan.upper() == "F":
     hasil1 = float((drjt - 32) * 9 / 5)
     hasil2 = float(((drjt - 32) * 9 / 5) + 273.15)
     hasil3 = float(9/5 * (drjt-32))
     jenisX = "Fahrenheit"
     jenis1 = "Celsius"
     jenis2 = "Kelvin"
     jenis3 = "Reamur"
     print(drjt,jenisX,"=","{:.1f}".format(hasil1),jenis1)
     print(drjt,jenisX,"=","{:.1f}".format(hasil2),jenis2)
     print(drjt,jenisX,"=","{:.1f}".format(hasil3),jenis3)

   elif inputan.upper() == "K":
     hasil1 = float(drjt - 273.15)
     hasil2 = float(((drjt - 273.15) * 9 / 5)+32)
     hasil3 = float(4/5 * (drjt-273))
     jenisX = "Kelvin"
     jenis1 = "Celcius"
     jenis2 = "Fahrenheit"
     jenis3 = "Reamur"
     print(drjt,jenisX,"=","{:.1f}".format(hasil1),jenis1)
     print(drjt,jenisX,"=","{:.1f}".format(hasil2),jenis2)
     print(drjt,jenisX,"=","{:.1f}".format(hasil3),jenis3)
     
   elif inputan.upper() == "R":
     hasil1 = float((4/5) * drjt)
     hasil2 = float((9/5 * drjt) + 32)
     hasil3 = float((4/5 * drjt) + 273)
     jenisX = "Reamur"
     jenis1 = "Celcius"
     jenis2 = "Fahrenheit"
     jenis3 = "Kelvin"
     print(drjt,jenisX,"=","{:.1f}".format(hasil1),jenis1)
     print(drjt,jenisX,"=","{:.1f}".format(hasil2),jenis2)
     print(drjt,jenisX,"=","{:.1f}".format(hasil3),jenis3)
     
   else:
      print("Inputan tidak sesuai!! Perhatikan Penulisan Input")


i=0
print("Program Konversi Suhu")
while i==0:
   temp = input("\nMasukan suhu? (Misal: 30C, 20F, 21K, 44R): ")
   konversiSuhu(temp)

   lagi=int(input("Hitung lagi?1=ya & 0=tidak = "))
   if(lagi==1):
      i=0
   elif(lagi!=1):
      i=1

