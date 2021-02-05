weight = input("Berat badan dalam Kg: ")
height = input("Tinggi badan dalam Cm: ")
bmi = (float(weight)/float(height)/float(height))*10000
print("Indeks BMI anda adalah: " + str(bmi))

if bmi < 18.5:
    print("Buset ceking.")
elif 18.5 <= bmi <= 24.9:
    print("Selamat! Anda sehat dan bugar!")
elif 25 <= bmi <= 29.9:
    print("Lemak berlebihan. Gas diet!")
else:
    print("Selamat anda obesitas..")


