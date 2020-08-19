class Persona:
    name = ""
    age = 0
    dni = str
    gender = 'M'
    weight = 0.0
    height = 0.0

    def __init__(self, name="", age=0, gender='M', dni="",weight=0.0, height=0.0):
        self.name = name
        self.age = age
        self.dni = dni
        self.weight = weight
        self.height = height
        self.comprobarSexo(gender)
    
    def setName(self, name: str):
        self.name = name

    def setAge(self, age: int):
        self.age = age

    def setGender(self, gender: str):
        self.comprobarSexo(gender)

    def setDni(self, dni: str):
        self.dni = dni

    def setWeight(self, weight: float):
        self.weight = weight

    def setHeight(self, height: float):
        self.height = height    

    def esMayorDeEdad(self):
        if self.age > 18:
            return True
        return False
    
    def toString(self):
        return 'name: {}, age: {}, gender: {}, DNI: {}, weight: {}, Height: {}'.format(self.name, self.age,
                self.gender, self.dni, self.weight, self.height)
    
    def comprobarSexo(self, gender: str):
        if gender != 'F' and gender != 'M':
            self.gender = 'M'
        else:
            self.gender = gender
