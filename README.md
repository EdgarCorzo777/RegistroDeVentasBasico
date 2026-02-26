# 🛒 RiwiTechStore - Sistema de Facturación

Este es un script de Python diseñado para gestionar ventas minoristas de forma rápida. El programa permite calcular el total de una compra, aplicando automáticamente descuentos exclusivos para miembros **VIP**.

---

## 🌟 Características

* **Interfaz de Consola:** Menú visual sencillo para una mejor experiencia de usuario.
* **Lógica de Descuentos:** Aplica un **10% de descuento** si el cliente cuenta con membresía VIP.
* **Formateo de Moneda:** Los valores financieros se muestran con dos decimales (`.2f`) para mayor precisión contable.
* **Recibo Detallado:** Genera un resumen final con el subtotal, descuento aplicado y total a pagar.

---

## 📊 Lógica del Cálculo

El programa utiliza las siguientes fórmulas dependiendo del tipo de cliente:

1. **Subtotal:** $$Subtotal = Precio \times Cantidad$$

2. **Descuento (Solo VIP):** $$Descuento = Subtotal \times 0.10$$

3. **Total:** $$Total = Subtotal - Descuento$$

---

## 🛠️ Requisitos

* **Python 3.x**

## 🚀 Cómo usarlo

1. Descarga o copia el archivo `app.py`.
2. Ejecuta el script en tu terminal:
   ```bash
   python app.py