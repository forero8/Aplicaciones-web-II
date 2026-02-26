
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

class MotorRutas:
    TARIFAS_ZONA = {
        "Mompellín": {"km": 10, "precio": 10000},
        "Torices": {"km": 15, "precio": 25000},
        "Bicentenario": {"km": 30, "precio": 70000}
    }

    @staticmethod
    def calcular_tarifa(zona):
        if zona in MotorRutas.TARIFAS_ZONA:
            return MotorRutas.TARIFAS_ZONA[zona]["precio"]
        else:
            return 0


class Repartidor:
    def __init__(self, nombre, zonas):
        self.nombre = nombre
        self.zonas = zonas


class AsignadorRepartidores:
    @staticmethod
    def asignar(pedido, repartidores):
        for r in repartidores:
            if pedido.zona in r.zonas:
                pedido.repartidor = r.nombre
                return
        pedido.repartidor = "No disponible"


class SmartDelivery:
    def __init__(self):
        self.pedidos = []
        self.repartidores = []

    def agregar_repartidor(self, repartidor):
        self.repartidores.append(repartidor)

    def registrar_pedido(self, cliente, zona, distancia_km):
        pedido = Pedido(cliente, zona, distancia_km)

        pedido.tarifa = MotorRutas.calcular_tarifa(zona)

        AsignadorRepartidores.asignar(pedido, self.repartidores)

        self.pedidos.append(pedido)
        return pedido

    def mostrar_pedidos(self):
        for p in self.pedidos:
            print("---------------")
            print(f"Pedido Nº: {p.id_pedido}")
            print(f"Cliente: {p.cliente.nombre}")
            print(f"Dirección: {p.cliente.direccion}")
            print(f"Teléfono: {p.cliente.telefono}")
            print(f"Zona: {p.zona}")
            print(f"Tarifa: ${p.tarifa}")
            print(f"Repartidor: {p.repartidor}")

sistema = SmartDelivery()

sistema.agregar_repartidor(Repartidor("Luis", ["Centro"]))
sistema.agregar_repartidor(Repartidor("Roy", ["Torices", "Mompellín"]))
sistema.agregar_repartidor(Repartidor("Daniel", ["Bicentenario", "Centro"]))
sistema.agregar_repartidor(Repartidor("Blenda", ["Torices"]))

cliente1 = Cliente(
    nombre="Juan Pérez",
    direccion="Cra 10 #45-20",
    telefono="3001234567"
)

pedido1 = sistema.registrar_pedido(cliente1, "Torices", 15)

sistema.mostrar_pedidos()