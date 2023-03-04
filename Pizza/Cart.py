class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            self.session["cart"] = {}
            self.cart = cart
        else:
            self.cart = cart

    def add(self, producto):
        id = str(producto.id)
        if id not in self.cart.keys():
            self.cart[id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "acumulado": producto.precio,
                "cantidad": 1,
            }
        else:
            self.cart[id]["cantidad"] += 1
            self.cart[id]["acumulado"] += producto.precio
        self.guardarCarrito()

    def guardarCarrito(self):
        self.session["cart"] = self.cart
        self.session.modified = True

    def delete(self, producto):
        id = str(producto.id)
        if id in self.cart:
            del self.cart[id]
        self.guardarCarrito()

    def restart(self, producto):
        id = str(producto.id)
        if id in self.cart.keys():
            self.cart[id]["cantidad"] -= 1
            self.cart[id]["acumulado"] -= producto.precio
            self.guardarCarrito()
            if self.cart[id]["cantidad"] <= 0:
                self.delete(producto)
            self.guardarCarrito()

    def clean(self):
        self.session["cart"] = {}
        self.session.modified = True
