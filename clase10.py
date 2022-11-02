class Atleta:
  def __init__(self,nombre, apellido, altura, peso,telefono):
    self.__nombre = nombre
    self.__apellido = apellido
    self.__altura = altura
    self.__peso = peso
    self.__telefono = telefono


  # supongamos que no quiero hacer publico(accesible) el telefono

  def get_nombre(self):
    return self.__nombre

  def get_apellido(self):
    return self.__apellido

  def get_altura(self):
    return self.__altura
  
  def get_peso(self):
    return self.__peso 


  def set_nombre(self, nombre):
    self.__nombre = nombre

  def set_apellido(self, apellido):
    self.__nombre = apellido

  def set_altura(self, altura):
    self.__altura = altura

  def set_peso(self, peso):
    self.__peso = peso

atleta1 = Atleta("Juan", "Perez", 1.80, 90, 3635433)

print(atleta1.get_nombre())
print(atleta1.get_apellido())

atleta1.set_nombre("Pablo")

print(atleta1.get_nombre())