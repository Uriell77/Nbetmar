from flask import Flask, request, render_template, redirect, url_for, flash, jsonify
import bd
from werkzeug.utils import secure_filename
import os
from PIL import Image
from flask_cors import CORS, cross_origin



app = Flask(__name__)
app.secret_key =b'clave'
app.config['UPLOAD_FOLDER'] = './static/img/img'
cors = CORS(app)
#app.config['CORS_HEADERS'] = 'Content-Type'


global user
a = ["<div class='box has-text-primary'>esto se genero por feo</div>", "es a", 'recarga1.html']
b = ["<div class='card is-primary'>esto se genero por horrible</div>", "es b"]




@app.route('/')
#@cross_origin()
def home():
    """Home de la aplicacion"""
    flash('Bienvenido al home')
    flash('Disfruta tu estadia')
    return render_template('index.html', navbar='navbarout.html', cont=b, contenido='home.html', vendedor='admin', reca='recas', banca='banca', bancadmin=1, userdat='')




@app.route('/registro', methods=['GET', 'POST'])
#@cross_origin()
def registro():
    """pagina de registro para usuarios nuevos"""
    vendedores = bd.vendedores()
    if request.method == 'POST': 
        datos = []
        nombre = request.form['nombre']
        correo = request.form['correo']
        password = request.form['password']
        celular = request.form['tlf']
        vendedor = request.form['vendedor']

        datos.extend([nombre,correo,password,vendedor,celular])
        try:
            bd.crear(datos)
            flash('Registro Correcto')
            return redirect(url_for('home'))
        except:
            flash('No se pudo registrar')
            return render_template('index.html', navbar='navbarout.html', cont=a, contenido='registro.html', vendedores=vendedores, vendedor='admin', reca='recas', banca='banca', bancadmin=1, userdat='')
    else:    
        flash('Bienvenido al registro')
        return render_template('index.html', navbar='navbarout.html', cont=a, contenido='registro.html', vendedores=vendedores, vendedor='admin', reca='recas', banca='banca', bancadmin=1, userdat='a')



@app.route('/login', methods=['GET', 'POST'])
#@cross_origin()
def login():
    """Pagina de login a la plataforma para usuarios registrados"""
    if request.method == 'POST':
        nombre = request.form['nombre']
        password = request.form['password']
        if bd.existecorreo(nombre):
            if bd.existepassword(password):
                user = bd.leer(nombre)
                return redirect(url_for('user', user=user[1]))

            else:
                flash('Error en Password')
                return redirect(request.path)
        else:
            flash('Error en Correo')
            return redirect(request.path)
    else:
        flash('Ingresa a la Plataforma')
        return render_template('index.html', navbar='navbarout.html', cont=a, contenido='login.html', vendedor='admin', reca='recas', banca='banca', bancadmin=1, userdat='a')



@app.route('/<user>', methods=['GET', 'POST'])
#@cross_origin()
def user(user):
    print(user)
    panelv = '<a class="navbar-item" href="/'+user+'/clientes">Clientes</a><a class="navbar-item" href="/'+user+'/metricas">Metricas</a> <a class="navbar-item" href="/'+user+'/administracion">Administracion</a>'
    panelu = '<a class="navbar-item" href="/'+user+'/metricas">Metricas</a><a class="navbar-item" href="/'+user+'/administracion">Administracion</a>'
    global reca
    reca = bd.leertodoreca(1)
    reca = bd.tresillo(reca,3)
    userdat = bd.leeruser(user)
    if userdat == None:
        pass
    else:
        global vendedor
        vendedor = bd.leervend(userdat[8])
        global banca
        banca = bd.leer_banca(userdat[8])
        global bancadmin
        bancadmin = bd.leer_banca(1)
        global servi
        servi = bd.leertodoservi(userdat[8])
        servi = bd.tresillo(servi,3)
        global nivel
        nivel = userdat[7]
        global listareca
        listareca = bd.ListaRecargas(userdat[0])
        global listacuentas
        listacuentas = bd.ListaCuentas(userdat[0])

    if request.method == 'POST':
        user = user
        solicitudes = request.form['solicitud']
        ref = request.form['referencia']
        vend = request.form['vendedor']
        formulario = request.form
        if formulario['action'] == 'recarga':
            recarganeta = request.form['recarganeta']
            bd.recarga(userdat[0], solicitudes, vend, ref, recarganeta)
            flash('Solicitud de recarga enviada')
            return redirect(url_for('user', user=user))
        elif formulario['action'] == 'servicio':
            solicitudes = solicitudes.split(',')
            bd.cuentas(userdat[0], solicitudes[1], solicitudes[0], solicitudes[2], solicitudes[3], vend, ref)
            flash('solicitud de cuenta enviada')
            return redirect(url_for('user', user=user))

    else:
        userdat = bd.leeruser(user)
        if userdat == None:
            pass
        else:
            nivel = userdat[7]
            if nivel == 3:
                flash('Bienvenido' + ' '+ user)
                return render_template('index.html', navbar='navbarin.html', cont=a, contenido='user.html', user=user, userdat=userdat, tabla='vendedor.html', servi=servi, reca=reca, listareca=listareca, listacuenta=listacuentas, vendedor=vendedor, banca=banca, bancadmin=bancadmin, PanelClient=panelu)

            if nivel == 2:
                flash('Bienvenido' + ' '+'vendedor'+' '+user)
                return render_template('index.html', navbar='navbarin.html', cont=a, contenido='user.html', user=user, userdat=userdat, tabla='vendedor.html', servi=servi, reca=reca, listareca=listareca, listacuenta=listacuentas, vendedor=vendedor, banca=banca, bancadmin=bancadmin, PanelClient=panelv)

            if nivel == 1:
                flash('Bienvenido' + ' '+'administrador'+' '+user)
                return render_template('index.html', navbar='navbarin.html', cont=a, contenido='user.html', user=user, userdat=userdat, tabla='admin.html', servi=servi, reca=reca, vendedor=vendedor, banca=banca, bancadmin=bancadmin, PanelClient=panelv)


@app.route('/<user>/clientes', methods=['GET', 'POST'])
#@cross_origin()
def UserClients(user):
    print(user)
    userdat = bd.leeruser(user)
    if userdat == None:
        pass
    else:
        nivel = userdat[7]
        global listacuenta
        listacuenta = bd.ListaCuentasvend(userdat[0])
        global listareca
        listareca = bd.ListaRecargasvend(userdat[0])
        global reca
        reca = bd.leertodoreca(1)
        reca = bd.tresillo(reca,3)
        global banca
        banca = bd.leer_banca(userdat[8])
        global bancadmin
        bancadmin = bd.leer_banca(1)
        panelv = '<a class="navbar-item" href="/'+user+'/clientes">Clientes</a><a class="navbar-item" href="/'+user+'/metricas">Metricas</a> <a class="navbar-item" href="/'+user+'/administracion">Administracion</a>'
        vendedor = bd.leervend(userdat[8])
        nivel = userdat[7]
        if request.method =='POST':
            formulario = request.form
            if formulario['action'] == 'aprobar_cuenta':
                aprobado = request.form['por_aprobar']
                aprobado = aprobado.split(',')
                bd.delcuent(aprobado[1].strip(), aprobado[0].strip())
                return redirect (request.path)
            else:
                aprobado = request.form['por_aprobar']
                aprobado = aprobado.split(',')
                bd.delrec(aprobado[1].strip(), aprobado[0].strip())
                return redirect(request.path)
        else:
            if nivel == 1:
                flash('Bienvenido' + ' ' +user)
                return render_template('index.html', navbar='navbarin.html', cont=a, contenido='clientes.html', user=user, userdat=userdat, PanelClient=panelv, vendedor=vendedor, reca=reca, banca=banca, bancadmin=bancadmin, listacuenta=listacuenta, listareca = listareca, listas="recarga1.html")
            elif nivel == 2:
                flash('Bienvenido' + ' '+user)
                return render_template('index.html', navbar='navbarin.html', cont=a, contenido='clientes.html', user=user, userdat=userdat, PanelClient=panelv, vendedor=vendedor, reca=reca, banca=banca, bancadmin=bancadmin, listacuenta=listacuenta, listareca = listareca, listas="cuenta1.html")


@app.route('/<user>/metricas', methods=['GET', 'POST'])
#@cross_origin()
def UserMetric(user):
    userdat = bd.leeruser(user)
    nivel = userdat[7]
    global listacuenta
    listacuenta = bd.ListaCuentasvend(userdat[0])
    global listareca
    listareca = bd.ListaRecargasvend(userdat[0])
    global reca
    reca = bd.leertodoreca(1)
    reca = bd.tresillo(reca,3)
    global banca
    banca = bd.leer_banca(userdat[8])
    global bancadmin
    bancadmin = bd.leer_banca(1)
    panelv = '<a class="navbar-item" href="/'+user+'/clientes">Clientes</a><a class="navbar-item" href="/'+user+'/metricas">Metricas</a> <a class="navbar-item" href="/'+user+'/administracion">Administracion</a>'
    panelu = '<a class="navbar-item" href="/'+user+'/metricas">Metricas</a><a class="navbar-item" href="/'+user+'/administracion">Administracion</a>'
    vendedor = bd.leervend(userdat[8])
    nivel = userdat[7]
    if nivel == 1:
        flash('estadisticas del Administrador')
        return render_template('index.html', navbar='navbarin.html', cont=a, contenido='metricas.html', user=user, userdat=userdat, PanelClient=panelv, vendedor=vendedor, reca=reca, banca=banca, bancadmin=bancadmin, listacuenta=listacuenta, listareca = listareca, listas="recarga1.html")
    elif nivel == 2:
        flash('Estadisticas del vendedor')
        return render_template('index.html', navbar='navbarin.html', cont=a, contenido='metricas.html', user=user, userdat=userdat, PanelClient=panelv, vendedor=vendedor, reca=reca, banca=banca, bancadmin=bancadmin, listacuenta=listacuenta, listareca = listareca, listas="cuenta1.html")
    elif nivel == 3:
        flash('Estadisticas del usuario')
        return render_template('index.html', navbar='navbarin.html', cont=a, contenido='metricas.html', user=user, userdat=userdat, PanelClient=panelu, vendedor=vendedor, reca=reca, banca=banca, bancadmin=bancadmin, listacuenta=listacuenta, listareca = listareca, listas="cuenta1.html")




@app.route('/<user>/administracion', methods=['GET', 'POST'])
#@cross_origin()
def UserAdmin(user):
    vendedores= bd.vendedores()
    userdat = bd.leeruserv(user)
    #print(userdat)
    nivel = userdat[7]
    global listacuenta
    listacuenta = bd.ListaCuentasvend(userdat[0])
    listaclientes = bd.leertodo()
    global listareca
    listareca = bd.ListaRecargasvend(userdat[0])
    global reca
    reca = bd.leertodoreca(1)
    recal = bd.tresillo(reca,3)
    global banca
    banca = bd.leer_banca(userdat[8])
    global bancadmin
    bancamia = bd.leer_banca(userdat[0])
    bancadmin = bd.leer_banca(1)
    banconame = list(bd.codi.keys())
    servicios = bd.leertodoservi(userdat[0])
    panelv = '<a class="navbar-item" href="/'+user+'/clientes">Clientes</a><a class="navbar-item" href="/'+user+'/metricas">Metricas</a> <a class="navbar-item" href="/'+user+'/administracion">Administracion</a>'
    panelu = '<a class="navbar-item" href="/'+user+'/metricas">Metricas</a> <a class="navbar-item" href="/'+user+'/administracion">Administracion</a>'

    if request.method == "POST":
        ter = request.form 
        userdat = bd.leeruserv(user)

        #editar datos de usuario
        if ter['accion'] == 'editar':
            nombre = request.form['nombre']
            email = request.form['email']
            password = request.form['password']
            mobil = request.form['mobil']
            vendedor = request.form['vendedor']
            vendedor= bd.leeruser(vendedor)
            divisa = request.form['divisa']
            divisa = divisa.replace('.','')[2:-3]
            try:
                bd.editar(userdat[0],[nombre,email,password,mobil,vendedor[0],divisa])
                flash('Datos Actualizados')
                return redirect('/'+nombre+'/administracion')
            except:
                return 'no se pudo editar'

            #editar clientes
        elif ter['accion'] == 'cambiar':
            aidi = request.form['aidi']
            statuscli = request.form['status']
            nivelcli = request.form['niveles']
            try:
                bd.editarSnivel(aidi, statuscli, nivelcli)
                flash('Cambios Realizados')
                return redirect('/'+user+'/administracion')
            except:
                return 'Cambios no realizados'

            #edicion de servicios
        elif ter['accion'] == 'cambiarserv':
            aidi = request.form['aidi']
            servicio = request.form['servicio']
            precio = request.form['precio']
            image = request.files['resume']
            if image:
                image_name = '{}.png'.format(servicio)
                image.save(os.path.join(app.config['UPLOAD_FOLDER'], image_name))
                img = Image.open(os.path.join(app.config['UPLOAD_FOLDER'], image_name))
                new_img = img.resize((300,150))
                new_img.save(os.path.join(app.config['UPLOAD_FOLDER'], image_name), 'png')
            else:
                pass
            try:
                bd.editarservicio(aidi, servicio, precio)
                flash('Cambios Realizados' +' '+ servicio +' '+ precio)
                return redirect('/'+user+'/administracion')
            except:
                return 'Cambios no realizados'

                #agregar un servicio
        elif ter['accion'] == 'addserv':
            aidi = request.form['aidi']
            servicio = request.form['servicio']
            precio = request.form['precio']
            image = request.files['resume']
            if image:
                image_name = '{}.png'.format(servicio)
                image.save(os.path.join(app.config['UPLOAD_FOLDER'], image_name))
                img = Image.open(os.path.join(app.config['UPLOAD_FOLDER'], image_name))
                new_img = img.resize((300,150))
                new_img.save(os.path.join(app.config['UPLOAD_FOLDER'], image_name), 'png')
            else:
                return 'No hay imagen'
            try:
                bd.AddServicio(aidi, servicio, precio)
                flash('Servicio agregado' +' '+ servicio +' '+ precio)
                return redirect('/'+user+'/administracion')
            except:
                return 'Cambios no realizados'

            #eliminar servicio
        elif ter['accion'] == 'borrarserv':
            aidi = request.form['aidi']
            servicio = request.form['servicio']
            precio = request.form['precio']
            try:
                bd.DelServicio(aidi, servicio, precio)
                flash('Servicio Borrado' +' '+ servicio +' '+ precio)
                return redirect('/'+user+'/administracion')
            except:
                return 'Cambios no realizados'



            #edicion de recargas
        elif ter['accion'] == 'cambiarrec':
            aidi = request.form['aidi']
            recarga = request.form['recarga']
            print(recarga)
            precio = request.form['precio']
            porcentaje = request.form['porcentaje']
            image = request.files['resume']
            if image:
                image_name = '{}.png'.format(recarga)
                image.save(os.path.join(app.config['UPLOAD_FOLDER'], image_name))
                img = Image.open(os.path.join(app.config['UPLOAD_FOLDER'], image_name))
                new_img = img.resize((300,150))
                new_img.save(os.path.join(app.config['UPLOAD_FOLDER'], image_name), 'png')
            else:
                pass
            try:
                bd.editarrecarga(aidi, recarga, precio, porcentaje)
                flash('Cambios Realizados' + ' ' + recarga + ' ' + precio + ' ' + porcentaje)
                return redirect('/'+user+'/administracion')
            except:
                return 'Cambios no realizados'

            #agregar una recarga
        elif ter['accion'] == 'addrec':
            aidi = request.form['aidi']
            recarga = request.form['recarga']
            precio = request.form['precio']
            porcentaje = request.form['porcentaje']
            image = request.files['resume']
            if image:
                image_name = '{}.png'.format(recarga)
                image.save(os.path.join(app.config['UPLOAD_FOLDER'], image_name))
                img = Image.open(os.path.join(app.config['UPLOAD_FOLDER'], image_name))
                new_img = img.resize((300,150))
                new_img.save(os.path.join(app.config['UPLOAD_FOLDER'], image_name), 'png')
            else:
                return 'No hay imagen'
            try:
                bd.AddRecarga(aidi, recarga, precio, porcentaje)
                flash('Recarga agregada' +' '+ recarga +' '+ precio+' '+porcentaje)
                return redirect('/'+user+'/administracion')
            except:
                return 'Cambios no realizados'

            #eliminar recarga
        elif ter['accion'] == 'borrarrec':
            aidi = request.form['aidi']
            recarga = request.form['recarga']
            precio = request.form['precio']
            porcentaje = request.form['porcentaje']
            try:
                bd.DelRecarga(aidi, recarga, precio, porcentaje)
                flash('Recarga Borrada' +' '+ recarga + ' ' + precio +' '+porcentaje)
                return redirect('/'+user+'/administracion')
            except:
                return 'Cambios no realizados'


            #edicion de pagos
        elif ter['accion'] == 'cambiopago':
            aidi = request.form['aidi']
            titular = request.form['titular']
            cedula = request.form['cedula']
            banco = request.form['banco']
            cuenta = request.form['cuenta']
            tipo = request.form['tipo']
            celular = request.form['celular']
            codigo = bd.codi[banco]
            try:
                bd.editarbanca(aidi, titular, str(cedula), banco, str(codigo), str(cuenta), tipo, str(celular))
                flash('Cambios Realizados' +' '+ titular +' '+ banco)
                return redirect('/'+user+'/administracion')
            except:
                return 'Cambios no realizados'


            #eliminar pago
        elif ter['accion'] == 'borrarpago':
            aidi = request.form['aidi']
            titular = request.form['titular']
            banco = request.form['banco']
            cuenta = request.form['cuenta']
            try:
                bd.DelPago(aidi, titular, banco, cuenta)
                flash('Metodo de pago Borrado con exito' +' '+ titular + ' ' + banco +' '+cuenta)
                return redirect('/'+user+'/administracion')
            except:
                return 'Cambios no realizados'

            #agregar nuevo metodo de pago
        elif ter['accion'] == 'addpago':
            aidi = request.form['aidi']
            titular = request.form['titular']
            cedula = request.form['cedula']
            nombre = request.form['nombre']
            cuenta = request.form['cuenta']
            if nombre not in bd.codi.keys():
                bd.codi[nombre] = '0000'
            codigo = bd.codi[nombre]
            tipo = request.form['tipo']
            celular = request.form['celular']
            image = request.files['resume']
            if image:
                image_name = '{}.png'.format(nombre)
                image.save(os.path.join(app.config['UPLOAD_FOLDER'], image_name))
                img = Image.open(os.path.join(app.config['UPLOAD_FOLDER'], image_name))
                new_img = img.resize((300,150))
                new_img.save(os.path.join(app.config['UPLOAD_FOLDER'], image_name), 'png')
            else:
                pass
            try:
                bd.AddPago(aidi, titular, cedula, nombre, cuenta, codigo, tipo, celular)
                flash('Metodo de Pago  agregado' +' '+ titular +' '+ nombre+' '+tipo)
                return redirect('/'+user+'/administracion')
            except:
                return 'Cambios no realizados'

    else:
        vendedor = bd.leervend(userdat[8])
        nivel = userdat[7]

        if nivel == 1:
            flash('Edicion  del Administrador')
            return render_template('index.html', navbar='navbarin.html', cont=a, contenido='administra.html', user=user, userdat=userdat, PanelClient=panelv, vendedor=vendedor, reca=recal, banca=banca, bancadmin=bancadmin, listacuenta=listacuenta, listareca = listareca, listas="recarga1.html", vendedores=vendedores,listaclientes=listaclientes,listaservicios = servicios, recargas= reca, bancamia=bancamia, banconame=banconame)

        elif nivel == 2:
            flash('Edicion del vendedor')
            return render_template('index.html', navbar='navbarin.html', cont=a, contenido='administra.html', user=user, userdat=userdat, PanelClient=panelv, vendedor=vendedor, reca=recal, banca=banca, bancadmin=bancadmin, listacuenta=listacuenta, listareca = listareca, listas="cuenta1.html", vendedores=vendedores, listaclientes=listaclientes, listaservicios = servicios, recargas='a', bancamia=bancamia, banconame=banconame)

        elif nivel == 3:
            flash('Edicion del usuario')
            return render_template('index.html', navbar='navbarin.html', cont=a, contenido='administra.html', user=user, userdat=userdat, PanelClient=panelu, vendedor=vendedor, reca=recal, banca=banca, bancadmin=bancadmin, listacuenta=listacuenta, listareca = listareca, listas="cuenta1.html", vendedores=vendedores, listaclientes='no')




@app.route('/api/', methods=['GET', 'POST'])
#@cross_origin()
def api():
    dato = request.args.get('dato')
   # print(dato)
    vendedorident = request.args.get('ident')
   # print(vendedorident)
    if dato == 'ListaCuentasvend':
        keysN = ['id', 'nombre', 'time', 'orden', 'cantidad', 'status',
                'fcorte', 'vendedor', 'dolar', 'bolivares', 'banco', 'referencia']
        cuentasN =  bd.ListaCuentasvend(vendedorident)
        res = []
        for cuent in cuentasN:
           res.append(dict(zip(keysN, cuent)))
           return jsonify(res)

    if dato == 'ListaRecargasvend':
        keysN = ['id', 'nombre', 'time', 'orden', 'status', 'vendedor', 'banco', 'referencia', 'montoneto']
        recargasN =  bd.ListaRecargasvend(1)
        res = []
        for rec in recargasN:
            res.append(dict(zip(keysN, rec)))
        return jsonify(res)

    if dato == 'ListaUsers':
        keysN = ['id', 'nombre', 'email', 'password', 'log', 'status', 'saldo', 'nivel', 'vendedor', 'divisa', 'tlf']
        users =  bd.leertodo()
        res = []
        for u in users:
            res.append(dict(zip(keysN, u)))
        return jsonify(res)






