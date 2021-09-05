import sqlite3
import datetime

def leeruserv(dato):
    #busca registro por nombre o id
    base = sqlite3.connect('user.db', check_same_thread=False)
    cursor = base.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE nombre = '{0}'".format(dato))
    respuesta = cursor.fetchone()
    base.close()
    return respuesta

def leervend(dato):
    #busca registro por  o id
    base = sqlite3.connect('user.db', check_same_thread=False)
    cursor = base.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE id = '{0}'".format(dato))
    respuesta = cursor.fetchone()
    base.close()
    return respuesta



def crear(datos):
    print(datos)
    #ingresa un usuario a la bd parametro datos es tupla en el orden de campos en bd`
    base = sqlite3.connect('user.db', check_same_thread=False)
    cursor = base.cursor()
    vendedor = leeruserv(datos[3])[0]
    print(vendedor)
    cursor.execute("INSERT INTO usuarios(nombre, correo, password, vendedor, tlf) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')".format(datos[0], datos[1], datos[2], vendedor, datos[4]))
    base.commit()
    base.close()




def leeruser(dato):
    #busca registro por nombre o id
    base = sqlite3.connect('user.db', check_same_thread=False)
    cursor = base.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE nombre = '{0}'".format(dato))
    respuesta = cursor.fetchone()
    base.close()
    return respuesta






def leer(dato):
    #busca registro por correo
    base = sqlite3.connect('user.db', check_same_thread=False)
    cursor = base.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE correo = '{0}'".format(dato))
    respuesta = cursor.fetchone()
    base.close()
    return respuesta



def vendedores():
    #busca todos los registros que tengan nivel 1 o 2 osea los vendedores
    base = sqlite3.connect('user.db', check_same_thread=False)
    cursor = base.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE nivel = ? OR nivel = ?", (1, 2))
    respuesta = cursor.fetchall()
    base.close()
    respuesta.reverse()
    return respuesta





def leertodo():
    #retorna toda la bd
    base = sqlite3.connect('user.db', check_same_thread=False)
    cursor = base.cursor()

    cursor.execute("SELECT * FROM usuarios")
    respuesta = cursor.fetchall()
    base.close()
    respuesta.reverse()
    return respuesta



def leertodoservi(Vid):
    #retorna toda la bd
    base = sqlite3.connect('user.db', check_same_thread=False)
    cursor = base.cursor()

    cursor.execute("SELECT * FROM servicios WHERE id ='{0}'".format(Vid))
    respuesta = cursor.fetchall()
    base.close()
    respuesta.reverse()
    return respuesta

def leertodoreca(Vid):
    #retorna toda la bd de servicios de recargas
    base = sqlite3.connect('user.db', check_same_thread=False)
    cursor = base.cursor()

    cursor.execute("SELECT * FROM recas WHERE id ='{0}'".format(Vid))
    respuesta = cursor.fetchall()
    base.close()
    respuesta.reverse()
    return respuesta



def editar(id, datos):
    #print(datos)
    base = sqlite3.connect('user.db', check_same_thread=False)
    cursor = base.cursor()

    cursor.execute("""UPDATE usuarios SET nombre ='{0}', correo='{1}', password='{2}', tlf='{3}', vendedor='{4}', divisa='{5}' WHERE id = '{6}'""".format(datos[0],datos[1],datos[2],datos[3],datos[4],datos[5], id))
    base.commit()
    base.close()


def borrar(ide):
    base = sqlite3.connect('user.db', check_same_thread=False)
    cursor = base.cursor()

    cursor.execute("DELETE FROM usuarios WHERE id = '{0}'".format(ide))
    base.commit()
    base.close()


def existecorreo(datos):
    """valida si existe el correo en base de datos"""
    base = sqlite3.connect('user.db', check_same_thread=False)
    cursor = base.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE correo = '{0}'".format(datos))
    if cursor.fetchone():
        base.close()
        return True
    else:
        base.close()
        return False

def existepassword(datos):
    """valida si existe el password en bd"""
    base = sqlite3.connect('user.db', check_same_thread=False)
    cursor = base.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE password = '{0}'".format(datos))
    if cursor.fetchone():
        base.close()
        return True
    else:
        base.close()
        return False


def log(dato):
    #parametro dato es el nombre
    datos = leer(dato)
    datos = list(datos)
    #print(datos)
    datos[4] = 'Conectado'
    #print(datos)
    datos = tuple(datos)
    #print(datos)
    #print(datos[0])
    editar(datos[0], datos)
    return True


def logout(dato):
    #parametro dato es el nombre
    datos = leer(dato)
    datos = list(datos)
    #print(datos)
    datos[4] = 'Desconectado'
    #print(datos)
    datos = tuple(datos)
    #print(datos)
    editar(datos[0], datos)
    return True
    
    
def counteo():
    plantilla = leertodo()[1:]
    cusuarios = len(plantilla)
    cconect = [i for i in plantilla if i[4]=='Conectado']
    cdesconect = cusuarios - (len(cconect))
    cactiv = [i for i in plantilla if i[5] =='Activo']
    cinactiv = cusuarios - (len(cactiv))
    aldia = [i for i in plantilla if i[6]>= 0.0]
    morosos = [i for i in plantilla if i[6]< 0.0]

    res =  (cusuarios, len(cconect), cdesconect, len(cactiv), cinactiv, len(aldia), len(morosos))
    return res



def recarga(id, ordenu, banco, ref, recarganeta):
    """para agregar una recarga en base de datos, la ordenu es una lista en el orden de la bd
    ejem: \'empresa,numero,monto\'
    """
    base = sqlite3.connect('user.db', check_same_thread=False)
    cursor = base.cursor()

    datosu = leervend(id)
    time = str(datetime.datetime.now())
    cursor.execute("INSERT INTO recargas(id,nombre,time,orden, vendedor, banco, referencia, montoneto) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}')".format(datosu[0], datosu[1], time[:time.index('.')], ordenu, datosu[8], banco, ref, recarganeta))
    base.commit()
    base.close()



def rec(li):
    '''Recibe una lista de 3 elemnetos que son empresa,numero,monto'''
    res = li.split(',')
    return res

def ListaRecargas(id):
    """Consulta la lista de recargas en bd de un usuario por medio del id"""

    base = sqlite3.connect('user.db', check_same_thread=False)
    cursor = base.cursor()

    datosu = leer(id)
    cursor.execute("SELECT * FROM recargas WHERE id = '{0}'".format(id))

    res = cursor.fetchall()
    base.close()
    res.reverse()
    return res



def ListaRecargasvend(id):
    """Consulta la lista de recargas en bd de un usuario por medio del id del vendedor"""

    base = sqlite3.connect('user.db', check_same_thread=False)
    cursor = base.cursor()

    datosu = leer(id)
    cursor.execute("SELECT * FROM recargas")

    res = cursor.fetchall()
    base.close()
    res.reverse()
    return res


def todarecarga():
    #retorna toda la bd de recargas
    base = sqlite3.connect('user.db', check_same_thread=False)
    cursor = base.cursor()

    cursor.execute("SELECT * FROM recargas")
    respuesta = cursor.fetchall()
    base.close()
    respuesta.reverse()
    return respuesta


def delrec(ide, fech):
    #borra un registo de la base de datos recargas por la fecha
    base = sqlite3.connect('user.db', check_same_thread=False)
    cursor = base.cursor()
    cursor.execute("UPDATE recargas SET status = '{2}' WHERE nombre = '{0}' AND time = '{1}'".format(ide, fech, '1'))
    base.commit()
    base.close()




def ListaCuentas(id):
    """Consulta la lista de cuentass en bd de un usuario por medio del id"""

    base = sqlite3.connect('user.db', check_same_thread=False)
    cursor = base.cursor()

    datosu = leer(id)
    cursor.execute("SELECT * FROM cuentas WHERE id = '{0}'".format(id))

    res = cursor.fetchall()
    base.close()
    res.reverse()
    return res


def ListaCuentasvend(id):
    """Consulta la lista de cuentass en bd de un usuario por medio del id del vendedor"""

    base = sqlite3.connect('user.db', check_same_thread=False)
    cursor = base.cursor()

    datosu = leer(id)
    cursor.execute("SELECT * FROM cuentas WHERE vendedor = '{0}'".format(id))

    res = cursor.fetchall()
    base.close()
    res.reverse()
    return res



def todacuenta():
    '''retorna toda la bd de cuentas'''
    base = sqlite3.connect('user.db', check_same_thread=False)
    cursor = base.cursor()

    cursor.execute("SELECT * FROM cuentas")
    respuesta = cursor.fetchall()
    base.close()
    respuesta.reverse()
    return respuesta


def cuentas(id, pantallas, empresa, dolar, bolivar, banco, referencia):
    """para agregar una compra de pantallas en base de datos, la pantallas es la cantidad de pantallas a comprar y empresa es la empresa de streaming a comprar
    """
    base = sqlite3.connect('user.db', check_same_thread=False)
    cursor = base.cursor()

    datosu = leervend(id)
    time = datetime.datetime.now()
    fcorte = str(time + datetime.timedelta(days=30))
    cursor.execute("INSERT INTO cuentas(id,nombre,time,orden, cantidad, fcorte, vendedor, dolar, bolivar, banco, referencia) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}','{8}', '{9}', '{10}')".format(datosu[0], datosu[1], str(time)[:str(time).index('.')], empresa, pantallas, fcorte[:fcorte.index('.')], datosu[8], dolar, bolivar, banco, referencia))
    base.commit()
    base.close()



def delcuent(ide, fech):
    #borra un registo de la base de datos cuenta por la fecha
    base = sqlite3.connect('user.db', check_same_thread=False)
    cursor = base.cursor()
    cursor.execute("UPDATE cuentas SET status = '{2}' WHERE nombre = '{0}' AND time = '{1}'".format(ide, fech, '1'))
    base.commit()
    base.close()


def leer_serv(dato):
    #busca servicio por nombre o id
    base = sqlite3.connect('user.db', check_same_thread=False)
    cursor = base.cursor()

    cursor.execute("SELECT * FROM servicios WHERE id = ? OR nombre_serv = ?", (dato, dato))
    respuesta = cursor.fetchone()
    base.close()
    return respuesta

def tresillo(arr, size):
     arrs = []
     while len(arr) > size:
         pice = arr[:size]
         arrs.append(pice)
         arr   = arr[size:]
     arrs.append(arr)
     return arrs


def leer_banca(dato):
    #busca servicio por nombre o id
    base = sqlite3.connect('user.db', check_same_thread=False)
    cursor = base.cursor()

    cursor.execute("SELECT * FROM pagobanco WHERE id = '{0}'".format(dato))
    respuesta = cursor.fetchall()
    base.close()
    respuesta.reverse()
    return respuesta

