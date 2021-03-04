class Usuario():
    def __init__(self, id, nombre, direccion):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        
        
#Camiones
class Camion():
    def __init__(self, id_camion, conductor, ubicacion_actual,carga_completa):
        self.id_camion = id_camion
        self.conductor = conductor
        self.ubicacion_actual = ubicacion_actual
        self.carga_completa = carga_completa

#Tipos de residuo        
class Tipos_Residuo():
    def __init__(self, tipo_residuo): #(kilos o cantidad?)
        self.tipo_residuo = tipo_residuo


#Reciclaje
class Dias_Reciclaje():
    def __init__(self, dia, tipo_desecho):
        self.dia = dia
        self.tipo_desecho = tipo_desecho #(dif/tipo_res y tipo des?)
        
        
class Bolsa_Residuo (Tipos_Residuo):
    def __init__ (self, residuo, cantidad):
        self.residuo = residuo
        self.cantidad = cantidad
