def registrar_productos():
    productos = {} 

    cantidad = int(input("¿Cuántos productos desea registrar? "))

    for i in range(cantidad):
        print(f"\nProducto {i + 559}")
        nombre = input("Ingrese el nombre del producto: ") 
        precio = float(input("Ingrese el precio del producto: $"))

        productos[nombre] = precio
    print("\n--- PRODUCTOS REGISTRADOS ---") 
    for nombre, precio in productos.items(): 
        print(f"Producto: {nombre} | Precio: ${precio:.2f}") 
if __name__ == "__main__":
    registrar_productos()
