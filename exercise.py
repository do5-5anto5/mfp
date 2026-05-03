# create a car class with model, age informations
# also, it has accelerate, reduce speed, and reverse functions
# depends on car age. it accelerates more

class Car:
    def __init__(self, model: str, year: int, max_speed: int, gears: int):
        
        
        
        self.model= model
        self.year = year
        self.gears = gears
        self.max_speed = max_speed
        self.speed = 0

    def stop(self):
        
        self.speed = 0
        print(f'{self.model} está parado')

    def accelerate(self):
        if self.speed < 0:
            self.stop()

        if self.speed < self.max_speed:
            self.speed += 10
            return f'Velocidade atual: {self.speed}'
        else: return 'Velocidade máxima atingida'

    def reduce_speed(self):
        if self.speed > 0:
            self.speed -= 10
            return f'Reduzindo. Velocidade atual: {self.speed}'
        else: return f'{self.model} está parado'

    def reverse(self):
        if self.speed > 0:
            print('Não recomendado engatar marcha ré quando acelerando')
        elif self.speed == 0:
            self.speed -= 10
            return f'{self.model} em marcha ré'
        elif self.speed < 0:
            return f'Marcha ré engatada.'

    

fusca = Car(model='Fusca', year='1975', max_speed=110, gears=5)

# for _ in range(1,20): fusca.accelerate

for _ in range(20): print(fusca.accelerate())
for _ in range(11): print(fusca.reduce_speed())
print(fusca.reduce_speed())

print(fusca.reverse())
print(fusca.reverse())

print(fusca.accelerate())

fusca.model = "mudei essa porra"

print(fusca.model)