`class Person:
    def __init__(self, ism, familiya, ssn):
        self.ism = ism
        self.familiya = familiya
        self.ssn = ssn

    def get_ism(self):
        return self.ism

    def get_familiya(self):
        return self.familiya

    def get_ssn(self):
        return self.ssn


class Doctor(Person):
    def __init__(self, ism, familiya, ssn, id, mutaxassislik):
        super().__init__(ism, familiya, ssn)
        self.id = id
        self.mutaxassislik = mutaxassislik

    def get_id(self):
        return self.id

    def get_mutaxassislik(self):
        return self.mutaxassislik


class Clinic:
    def __init__(self):
        self.bemorlar = {}
        self.shifokorlar = {}

    def addPatient(self, bemor: Person):
        if bemor.get_ssn() in self.bemorlar:
            raise Exception("Bemor allaqachon ro'yxatdan o'tgan")
        self.bemorlar[bemor.get_ssn()] = bemor

    def getPatient(self, ssn):
        if ssn not in self.bemorlar:
            raise Exception("NoSuchPatient")
        return self.bemorlar[ssn]

    def addDoctor(self, shifokor: Doctor):
        if shifokor.get_id() in self.shifokorlar:
            raise Exception("Shifokor allaqachon ro'yxatdan o'tgan")
        self.shifokorlar[shifokor.get_id()] = shifokor

    def getDoctor(self, id):
        if id not in self.shifokorlar:
            raise Exception("NoSuchDoctor")
        return self.shifokorlar[id]


klinika = Clinic()

# Bemor va shifokorlarni yaratish
bemor1 = Person('Ali', 'Valiyev', '123-45-6789')
shifokor1 = Doctor('Hasan', 'Abdullayev', '987-65-4321', '001', 'Terapevt')

# Bemor va shifokorni klinikaga qo'shish
klinika.addPatient(bemor1)
klinika.addDoctor(shifokor1)

# Bemor va shifokorni klinikadan topib olish
print(klinika.getPatient('123-45-6789').get_ism())  # Ali
print(klinika.getDoctor('001').get_mutaxassislik())  # Terapevt
`
