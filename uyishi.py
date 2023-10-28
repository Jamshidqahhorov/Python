class Flat:
    def __init__(self, code, dimension):
        self.code = code
        self.dimension = dimension
        self.tariffs = []

    def getCode(self):
        return self.code

    def getDimension(self):
        return self.dimension

    def setTariffs(self, tariffs):
        self.tariffs = tariffs

    def getTariffs(self):
        return self.tariffs


class Client:
    def __init__(self, name, surname, id):
        self.name = name
        self.surname = surname
        self.id = id

    def getName(self):
        return self.name

    def getSurname(self):
        return self.surname

    def getID(self):
        return self.id


class Manager:
    def __init__(self):
        self.flats = {}
        self.clients = {}

    def newFlat(self, code, dimension):
        flat = Flat(code, dimension)
        self.flats[code] = flat
        return flat

    def newClient(self, name, surname, id):
        client = Client(name, surname, id)
        self.clients[id] = client
        return client

    def getClient(self, id):
        return self.clients.get(id)

    def getClients(self):
        return list(self.clients.values())


manager = Manager()

# Kvartira yaratish
flat1 = manager.newFlat("K1", 100)
flat2 = manager.newFlat("K2", 120)

# Kvartira tariflarini o'rnatish
flat1.setTariffs([1000, 2000, 3000])
flat2.setTariffs([1500, 2500, 3500])

# Mijozlarni kiritish
client1 = manager.newClient("Ali", "Valiyev", "C1")
client2 = manager.newClient("Vali", "Aliyev", "C2")

# Kvartira va mijoz ma'lumotlarini tekshirish
print(
    f"Kvartira kod: {flat1.getCode()}, Kvartira maydoni: {flat1.getDimension()}, Kvartira tariflari: {flat1.getTariffs()}")
print(f"Mijoz ismi: {client1.getName()}, Mijoz familiyasi: {client1.getSurname()}, Mijoz ID: {client1.getID()}")

# Barcha mijozlarni olish
clients = manager.getClients()
for client in clients:
    print(f"Mijoz ismi: {client.getName()}, Mijoz familiyasi: {client.getSurname()}, Mijoz ID: {client.getID()}")
