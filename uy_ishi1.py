class Klinika:
    def __init__(self):
        self.shifokorlar = []
        self.bemorlar = []

    def bemorniShifokorgaTayinlash(self, bemor_ssn, shifokor_id):
        bemor = next((b for b in self.bemorlar if b.ssn == bemor_ssn), None)
        if bemor is None:
            raise Exception("Bunday bemor mavjud emas")

        shifokor = next((s for s in self.shifokorlar if s.id == shifokor_id), None)
        if shifokor is None:
            raise Exception("Bunday shifokor mavjud emas")

        bemor.shifokor = shifokor
        shifokor.bemorlar.append(bemor)

    def bandShifokorlar(self):
        return sorted([s for s in self.shifokorlar if not s.getBemorlar()], key=lambda s: (s.familiya, s.ism))

    def bandlikdanChetgaChiqqanShifokorlar(self):
        o_rta_bemorlar_soni = sum(len(s.getBemorlar()) for s in self.shifokorlar) / len(self.shifokorlar)
        return sorted([s for s in self.shifokorlar if len(s.getBemorlar()) > o_rta_bemorlar_soni],
                      key=lambda s: (s.familiya, s.ism))

    def shifokorlarniBemorlarSoniBoyicha(self):
        return sorted([f"{len(s.getBemorlar())}: {s.id} {s.familiya} {s.ism}" for s in self.shifokorlar],
                      key=lambda s: int(s.split(":")[0]), reverse=True)

    def bemorlarniMutaxassislikBoyichaHisoblash(self):
        # Har bir shifokorning 'mutaxassislik' atributi borligini tasavvur qilamiz
        mutaxassisliklar = {}
        for s in self.shifokorlar:
            if s.mutaxassislik not in mutaxassisliklar:
                mutaxassisliklar[s.mutaxassislik] = len(s.getBemorlar())
            else:
                mutaxassisliklar[s.mutaxassislik] += len(s.getBemorlar())

        return sorted([f"{soni} - {mutaxassislik}" for mutaxassislik, soni in mutaxassisliklar.items()],
                      key=lambda s: (-int(s.split(" - ")[0]), s.split(" - ")[1]))


# Shifokor va Bemor klasslarini yaratamiz
class Shifokor:
    def __init__(self, id, ism, familiya):
        self.id = id
        self.ism = ism
        self.familiya = familiya
        self.bemorlar = []

    def getBemorlar(self):
        return self.bemorlar


class Bemor:
    def __init__(self, ssn):
        self.ssn = ssn
        self.shifokor = None

    def getShifokor(self):
        return self.shifokor


klinika = Klinika()

shifokor1 = Shifokor(1, "Ali", "Valiyev")
shifokor2 = Shifokor(2, "Vali", "Aliev")
bemor1 = Bemor("111-11-1111")
bemor2 = Bemor("222-22-2222")

klinika.shifokorlar.append(shifokor1)
klinika.shifokorlar.append(shifokor2)
klinika.bemorlar.append(bemor1)
klinika.bemorlar.append(bemor2)

# Bemorni shifokorga tayinlash
klinika.bemorniShifokorgaTayinlash("111-11-1111", 1)
klinika.bemorniShifokorgaTayinlash("222-22-2222", 2)

# Natijalarni tekshirish
print(bemor1.getShifokor().ism)  # Ali
print(bemor2.getShifokor().ism)  # Vali
print(len(shifokor1.getBemorlar()))  # 1
print(len(shifokor2.getBemorlar()))  # 1
