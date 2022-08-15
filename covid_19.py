import os

def run():

    while True:

        estados = {
            "Aguascalientes":3000,
            "Baja California":1500,
            "Baja California Sur":12000,
            "Campeche":1500,
            "Coahuila":12000,
            "Colima":4000,
            "Chiapas":600,
            "Chihuahua":9000,
            "Ciudad de México":2460,
            "Durango":34200,
            "Guanajuato":31000,
            "Guerrero":12000,
            "Hidalgo":56000,
            "Jalisco":35679,
            "Estado de México":1294,
            "Michoacán":569679,
            "Morelos":12567,
            "Nayarit":7667,
            "Nuevo Leon":67676,
            "Oaxaca":13245,
            "Puebla":4554,
            "QUeretaro":45569,
            "Quintana Roo":23243,
            "San Luis Potosí":56565,
            "Sinaloa":55657,
            "Sonora":56767,
            "Tabasco":45676,
            "Tamaulipas":56776,
            "Tlaxcala":45687,
            "Veracruz":56760,
            "Yucatán":45656,
            "Zacatecas":45766
        }
        estados_lista = [estado for estado in estados]
        num=0
        selcción = ("Seleccione una opción:")
        
        for key in estados:
            num += 1
            print(num ,"-", key )

        try:
            opc = int(input("---------->"))
        except:
            print("Sólo puede ingresar números enteros")

        print(estados_lista[opc-1], " Registró ", estados[estados_lista[opc-1]], " casos hasta el 19 de mayo")
        d = input("¿Desea consultar otro estado?-------->(s/n)")
        os.system('cls')
        if d == 'n':
            break
        


if __name__ == "__main__":
    run()
