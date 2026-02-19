
class Cliente:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

class Pedido:
    contador_id = 1

    def __init__(self, cliente, zona, distancia_km):
        self.id_pedido = Pedido.contador_id
        Pedido.contador_id += 1
        self.cliente = cliente
        self.zona = zona
        self.distancia_km = distancia_km
        self.tarifa = 0
        self.repartidor = None


class Rutas:
    TARIFAS_ZONA = {
        "Marbella": {"km": 10, "precio": 10000},
        "Torices": {"km": 15, "precio": 25000},
        "Bicentenario": {"km": 30, "precio": 70000}
    }

    @staticmethod
    def calcular_tarifa(zona):
        if zona in Rutas.TARIFAS_ZONA:
            return Rutas.TARIFAS_ZONA[zona]["precio"]
        else:
            return 0