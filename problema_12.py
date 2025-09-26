meses = ["enero", "febrero", "marzo", "abril","mayo", "junio", "julio","agosto","septiembre", "octubre", "noviembre", "diciembre"]
fecha = input ("ingrese fecha(mm/dd/aaaa)").strip()
if "/" in fecha :
    m,d,a = fecha.split("/")
    m,d,a = int(m), int(d), int(a)

else:
    mes, resto = fecha.split(" ",1)
    d,a = resto.replace(",", "").split()
    m = meses.index(mes) + 1
    d,a = int(d), int(a)

print(f"{a}-{m:02}-{d:02}")