import json

class Operaciones:
    #operaciones del crud
    #def __init__(self,):
    def starconfig(self):
        file = open('log.json', 'r+')
        if (len(file.read()) < 1):
            json.dump([], file)
        else:
            pass
        file.close()
    
    def CreatePersona(self, nombre, edad, telefono, casado):
        try:
            dic = {
                "Nombre": nombre,
                "Edad": edad,
                "Telefono": telefono,
                "Casado": casado
            }
            self.starconfig()
            file = open('log.json', 'r+')  # read+ se puede leer y escribir
            data = json.load(file)  # se usa para leer un json file y obtener los datos
            data.append(dic)  # agrega el entry en el json
            file.seek(0)  # pone el cursor en el inicio
            json.dump(data, file, indent=4)  # indent lo muestra mejor, no en una sola linea
            file.close()
            return True
        except Exception as e:
            return False

    def UpdatePersona(self,nombre, edad, telefono, casado):
        try:
            file = open('log.json', 'r+')
            data = json.load(file)
            for idx, obj in enumerate(data):  # [0{},1{}]
                if obj['Nombre'] == nombre:
                    dic = {
                        "Nombre": nombre,
                        "Edad": edad,
                        "Telefono": telefono,
                        "Casado": casado
                    }
                    data[idx] = dic
            # print(data)
            json.dump(data, open('log.json', 'w'), indent=4)  # indent lo muestra mejor, no en una sola linea
            file.close()
            return True
        except Exception as e:
            return False
            
    def DeletePersona(self,nombre):
        try:
            file = open('log.json', 'r+')
            data = json.load(file)
            for idx, obj in enumerate(data):  # [0{},1{}]
                if obj['Nombre'] == nombre:
                    data.pop(idx)
            json.dump(data, open('log.json', 'w'), indent=4)
            file.close()
            return True
        except Exception as e:
            return False
        
    def PrintPersonas(self):
        str_data = open('log.json').read()
        #jsondata = json.loads(str_data)
        print(str_data)
        file.close()
        #for value in jsondata:
            #print(type(value.items()))
            #print('/////////////////////////')
            #for k,v in value.items():
                #print(k,'=',v,'; ')

    def Validaciones(self,nombre, edad, telefono, casado):
        if len(nombre) == None  or edad == None  or telefono == None  or casado  == None:
            return False
        else:
            if edad.isnumeric() and telefono.isnumeric() and bool(casado):
                return True
            else:
                return False
