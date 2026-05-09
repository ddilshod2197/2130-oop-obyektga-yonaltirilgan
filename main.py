class Avto:
    def __init__(self, rang, model, yil):
        self.rang = rang
        self.model = model
        self.yil = yil
        self.km = 0

    def get_info(self):
        return f"Rang: {self.rang}, Model: {self.model}, Yil: {self.yil}, KM: {self.km}"

    def km_yo_sifatida(self, km):
        self.km += km

class AvtoPark:
    def __init__(self):
        self.avtolar = []

    def qo'sh(self, avto):
        self.avtolar.append(avto)

    def chiqar(self, avto):
        self.avtolar.remove(avto)

    def get_avtolar(self):
        return self.avtolar

avto1 = Avto("Qora", "Toyota", 2020)
avto2 = Avto("Oq", "Honda", 2015)

avto_park = AvtoPark()
avto_park.qo'sh(avto1)
avto_park.qo'sh(avto2)

print(avto_park.get_avtolar())

avto1.km_yo_sifatida(1000)
print(avto1.get_info())
```

```python
class Avto:
    def __init__(self, rang, model, yil):
        self.rang = rang
        self.model = model
        self.yil = yil
        self.km = 0

    def get_info(self):
        return f"Rang: {self.rang}, Model: {self.model}, Yil: {self.yil}, KM: {self.km}"

    def km_yo_sifatida(self, km):
        self.km += km

class AvtoPark:
    def __init__(self):
        self.avtolar = []

    def add(self, avto):
        self.avtolar.append(avto)

    def remove(self, avto):
        self.avtolar.remove(avto)

    def get_avtolar(self):
        return self.avtolar

avto1 = Avto("Qora", "Toyota", 2020)
avto2 = Avto("Oq", "Honda", 2015)

avto_park = AvtoPark()
avto_park.add(avto1)
avto_park.add(avto2)

print(avto_park.get_avtolar())

avto1.km_yo_sifatida(1000)
print(avto1.get_info())
