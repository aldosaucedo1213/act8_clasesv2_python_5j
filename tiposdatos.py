print(" Clases V2 Aldo saucedo 22308051281310")
# zona de clase 
class Datos:
    # el constructor
    def __init__(self,estatura,peso):
        self.estatura=estatura
        self.peso=peso
    def mostrar_datos(self):
        print(f" Estatura: {self.estatura} mts, peso {self.peso}")
    def mi_lista(self):
        celulares=["motorola", "samnsung", "nokia"]
        print(celulares)
        for cel in celulares:
            print(cel)
    def diccionario(self):
        auto =	{
    "Marca": "nissan",
    "Modelo": "sentra",
    "Año": 2017
}
        print(auto)
        for x,y in auto.items():
            print(x,y) 
    def mi_set(self):
        Frutas = {"manzana", "platano", "cereza"}
        print(Frutas)
        for x in Frutas:
            print(x) 
    def mi_tupla(self):
        misnovias = (" melissa", "sofia", "nadie")
        print(misnovias)
        for p in misnovias:
            print(p) 
# creacion de objeto
info=Datos(1.75,10.5)
# utilizando el obj.
info.mostrar_datos()
print(" Lista de usuarios Aldo saucedo")
info.mi_lista()
print(" Lista de informacion de auto")
info.diccionario()
print(" Lista de frutas")
info.mi_set()
print(" Lista de mis novias")
info.mi_tupla()