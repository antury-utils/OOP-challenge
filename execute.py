from persona import Persona

class Execute:
    def getInfo(self):
        self.name = input('Name: ')
        self.age = int(input('Age: '))
        self.gender = input('Gender: ')
        self.weight = float(input('Weight: '))
        self.height = float(input('Height: '))

    def test(self):
        person1 = Persona(self.name, self.age, self.gender, weight=self.weight,
                        height=self.height)
        person2 = Persona(self.name, self.age, self.gender)
        person3 = Persona()
        person3.setName('Ricardo Montealegre')
        person3.setAge(15)
        person3.setDni('DBU123654789')
        print(person1.toString() + ', es mayor: ' + '{}'.format(person1.esMayorDeEdad()))
        print(person2.toString() + ', es mayor: ' + '{}'.format(person2.esMayorDeEdad()))
        print(person3.toString() + ', es mayor: ' + '{}'.format(person3.esMayorDeEdad()))



if __name__ == '__main__':
    obj = Execute()
    obj.getInfo()
    obj.test()

