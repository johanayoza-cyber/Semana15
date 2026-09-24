lista_compras = []
 
lista_compras.append("Leche")
lista_compras.append("Pan")
lista_compras.append("Huevos")
 
print("Mi lista de compras:")
for producto in lista_compras:
    print("-", producto)
 
nuevo_producto = input("\nEscribe el producto que quieres agregar: ")
lista_compras.append(nuevo_producto)
 
print("\nLista actualizada:")
for producto in lista_compras:
    print("-", producto)
 
producto_buscar = "Pan"
if producto_buscar in lista_compras:
    print(f"\n{producto_buscar} está en la lista.")
else:
    print(f"\n{producto_buscar} no está en la lista.")
 
lista_compras.remove("Leche")
 
print("\nLista después de comprar la leche:")
for producto in lista_compras:
    print("-", producto)
 