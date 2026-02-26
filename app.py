print("")
print("#################################")
print("#                               #")
print("#        RiwiTechStore          #")
print("#                               #")
print("#################################")
print("")

try:
    nombreCliente = input("Hola, por favor ingrese el nombre del cliente: ")
    precioProducto = float(input("Por favor ingrese el precio unitario del producto: "))
    cantidadProductos = float(input("Por favor ingrese la cantidad de productos comprados: "))
    vip = input("Tiene membresia VIP? (s/n) ").lower()
    vipBool = (vip == "s")
    
    subtotal = precioProducto * cantidadProductos
    descuento = 0.0
    
    if vipBool:
        descuento = subtotal * 0.10
    
    totalPagar = subtotal - descuento

    print("\n" + "*" * 45)
    print("* FACTURA DE LA COMPRA      ")
    print(F"Nombre:                        {nombreCliente}")
    print(f"Subtotal:                      ${subtotal:.2f}")
        
    if vipBool:
        print(f"Descuento aplicado (10%):      ${descuento:.2f}")
    else:
        print(f"Descuento aplicado (10%):      No aplica")
    
    print(f"Total final a pagar:           ${totalPagar:.2f}")

except ValueError:
    print("Error: Por favor ingrese valores numericos validos para precio y cantidad.")

