#se crea una lista llamda liosta_compras
lista_compras=[]

print("🛒lista de compras🛒")
#agregar producto
producto1 = input("agrega el primer producto: ")
lista_compras.append(producto1)

#agregar producto
producto2 = input("agrega el segundo producto: ")
lista_compras.append(producto2)

producto3 = input("agrega el tercer producto: ")
lista_compras.append(producto3)

print("\n📌 tu lista de compras es:")
for producto in lista_compras:
print(ƒ"- {producto}")

print("\n✅¡lista creada con exito!")