print("menentukan bilangan terbesar , jika angka 0 maka program terhenti")

max=0
while True:
	a=int(input("masukkan bilangan="))
	if max < a:
		max = a
	if a==0:
		break
print("\nbilangan terbesar=",max)
