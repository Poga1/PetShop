from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.IntegerField()
    descripcion = models.TextField()
    id_categoria = models.IntegerField()
    fecha_vencimiento = models.DateField ()
    imagen = models.ImageField(upload_to="productos", null=True)
   
    def __str__(self):
        return self.nombre 
       
class Category(models.Model):
    nombre = models.CharField(max_length=300)
    presentado = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nombre
    
class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            cart=self.session["cart"] = {}
        self.cart = cart
        
    def add (self,producto):
        if str(producto.id) not in self.cart.keys():
            self.cart[producto.id] = {
                "id": producto.id,
                "nombre": producto.nombre,
                "cantidad": 1,
                "precio": str(producto.precio),
                "imagen": producto.image.url
            }
        else: 
            for key, value in self.cart.items():
                if key ==str(producto.id):
                    value["cantidad"] = value["cantidad"] +1
                    break
        self.save()
    
    def save(self):
        self.session["cart"] = self.cart
        self.session.modified = True
        
    def remove(self, producto):
        producto_id = str(producto_id)
        if producto_id in self.cart:
            del self.cart[producto_id]
            self.save()
    
    def decrement(self, producto):
        for key, value in self.cart.items():
                if key ==str(producto.id):
                    value["cantidad"] = value["cantidad"] -1
                    if value["cantidad"] <1:
                        self.remove(producto)
                    else:
                        self.save()
                    break
                else:
                    print("El producto no existe en el carrito :)")
    
    
    def clear(self):
        self.session["cart"] = {}
        self.session.modified = True
                        
        