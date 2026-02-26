print("")
print("#################################")
print("#                               #")
print("#        RiwiTechStore          #")
print("#                               #")
print("#################################")
print("")

nombreCliente = input("Hola, por favor ingrese el nombre del cliente: ")
precioProducto = float(input("Por favor ingrese el precio unitario del producto: "))
cantidadProductos = float(input("Por favor, ingrese la cantidad de productos comprados: "))
vip = input("Tiene membresia VIP? (s/n) ")

if vip == "s":
    subtotal = precioProducto * cantidadProductos
    descuentoAplicado = subtotal * 0.1
    totalPagar = subtotal - descuentoAplicado
    print("")
    print("*********************************************************")
    print("*                  RECIBO DE LA COMPRA                  *")
    print(f"Nombre:                                  {nombreCliente}")
    print(f"Subtotal:                               ${subtotal:.2f}")
    print(f"Valor del descuento aplicado (10%):     ${descuentoAplicado:.2f}")
    print(f"Total final a pagar:                    ${totalPagar:.2f}")
    print("*********************************************************")

else:
    subtotal = precioProducto * cantidadProductos
    print("")
    print("*********************************************************")
    print("*                  RECIBO DE LA COMPRA                  *")
    print(f"Nombre:                                  {nombreCliente}")
    print(f"Subtotal:                               ${subtotal:.2f}")
    print(f"Valor del descuento aplicado (10%)       No aplica")
    print(f"Total final a pagar:                    ${subtotal:.2f}")
    print("*********************************************************")

