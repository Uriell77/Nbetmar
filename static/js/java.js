//funcionalidad del Navbar
document.addEventListener('DOMContentLoaded', () => {

    // Get all "navbar-burger" elements
    const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

    // Check if there are any navbar burgers
    if ($navbarBurgers.length > 0) {

        // Add a click event on each of them
        $navbarBurgers.forEach(el => {
            el.addEventListener('click', () => {

                // Get the target from the "data-target" attribute
                const target = el.dataset.target;
                const $target = document.getElementById(target);

                // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
                el.classList.toggle('is-active');
                $target.classList.toggle('is-active');

            });
        });
    }
});



/*
//Botones de recarga
document.addEventListener('DOMContentLoaded', () => {
    var boton1 = document.getElementById('Movilnet');
    var boton2 = document.getElementById('Movistar');
    var boton3 = document.getElementById('Digitel');
    var ventana = document.getElementById('modal1');
    var title = document.getElementById('modtitle');
    var empresa = document.getElementById('empresa')
    boton1.onclick = function() {
        ventana.classList.toggle('is-active');
        title.innerHTML = "Recarga Movilnet";
        empresa.value = "movilnet";


    };
    boton2.onclick = function() {
        ventana.classList.toggle('is-active');
        title.innerHTML = "Recarga Movistar";
        empresa.value = "movistar";

    };
    boton3.onclick = function() {
        ventana.classList.toggle('is-active');
        title.innerHTML = "Recarga Digitel";
        empresa.value = "digitel";

    };

});


*/

//Botones de Cuentas
document.addEventListener('DOMContentLoaded', () => {
    var boton1 = document.getElementById('bot-edit-div');
    var boton2 = document.getElementById('Disney+');
    var boton3 = document.getElementById('Amazon Prime');
    var ventana = document.getElementById('modal1');
    var title = document.getElementById('modtitle');
    var empresa = document.getElementById('empresa')
    boton1.onclick = function() {
        ventana.classList.toggle('is-active');
        title.innerHTML = "Edicion de Divisa";
        empresa.value = "divisa";


    };
    boton2.onclick = function() {
        ventana.classList.toggle('is-active');
        title.innerHTML = "Cuentas Disney+";
        empresa.value = "Disney+";

    };
    boton3.onclick = function() {
        ventana.classList.toggle('is-active');
        title.innerHTML = "Cuentas Amazon Prime";
        empresa.value = "Amazon Prime";

    };

});




//Funcionalidad del Modal
document.addEventListener('DOMContentLoaded', () => {
    var boton = document.getElementById('bot-edit-logo');
    var ventana = document.getElementById('modal1');
    var close = document.getElementById('del');
    var back = document.getElementById('modalback');
    var cancel = document.getElementById('cancel');
    close.onclick = function() {
        ventana.classList.toggle('is-active');

    };
    back.onclick = function() {
        ventana.classList.toggle('is-active');


    };
    cancel.onclick = function() {
        ventana.classList.toggle('is-active');

    };
});




//Desplegable del navbar
document.addEventListener('DOMContentLoaded', () => {
    var desplegable = document.getElementById('desplegable');
    //console.log(screen.width);
    if (screen.width > 769) {
        desplegable.classList.toggle('is-right');
    };
    desplegable.onclick = function() {
        desplegable.classList.toggle('is-active');

    };

});

document.addEventListener('DOMContentLoaded', () => {
    var imagenes = document.querySelectorAll('#articulos');

    if (screen.width < 769) {
        for (item of imagenes) {
            item.classList.toggle('is-clickable');
        };
    };

});


//Funcionalidad de las Tabs
function openTab(evt, tabName) {
    var i, x, tablinks;
    x = document.getElementsByClassName("content-tab");
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tab");
    for (i = 0; i < x.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" is-active", "");
    }
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " is-active";
};




//Ajax carga listado de usuarios
function loadDoc(div, page) {
    //console.log('se ejecuta');
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var content = JSON.parse(this.responseText)
            document.getElementById(div).innerHTML = '';
            for (let item of content.slice(1)) {
                document.getElementById(div).innerHTML += ` <div class="card has-background-dark has-text-light" id='${item[1]}'>
                <div class="card-header has-background-link">
                &nbsp${item[1]}&nbsp&nbsp&nbspSaldo:` + ' ' + item[6].toFixed(1) +
                    `</div>
                <div class="card-content">
                Email: ${item[2]}<br>Conexion: ${item[4]}<br>Estatus: ${item[5]}
                </div>
                </div>

               </div><br>`;
                conectado();
            }
            //document.getElementById(div).innerHTML = ;
        }
    };
    xhttp.open("GET", page, true);
    xhttp.send();
};



//Ajax carga el conteo de usuarios
function loadDoccont(div, page) {
    //console.log('se ejecuta');
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var content = JSON.parse(this.responseText)
            document.getElementById(div).innerHTML = '';
            //for (let item of content.slice(0)) {
            document.getElementById(div).innerHTML = `<div class="tag is-primary">Total de Clientes: <div id="total"> ${content[0]}</div></div>
                <i class="fas fa-fw">&nbsp</i>
                <div class="tag is-link">Conectados: <div id="conect">${content[1]}</div></div>
                <div class="tag is-link">Desconectados: <div id="desc">${content[2]}</div></div>
                <i class="fas fa-fw">&nbsp</i>
                <div class="tag is-link">Activos: <div id="activ">${content[3]}</div></div>
                <div class="tag is-link">Inactivos: <div id="inact">${content[4]}</div></div>
                <i class="fas fa-fw">&nbsp</i>
                <div class="tag is-link">Al Dia: <div id="aldia">${content[5]}</div></div>
                <div class="tag is-link">Morosos: <div id="moros">${content[6]}</div></div>

`;
        }
        //document.getElementById(div).innerHTML = ;
    }

    xhttp.open("GET", page, true);
    xhttp.send();
};




//Pruebas
function pruebas() {
    console.log('esto si funciona');
    var content = document.getElementById("clientes");
    content.innerHTML = content.innerHTML;
};



//Ocultar Notificacion
function borrado() {
    document.addEventListener('DOMContentLoaded', () => {
        setTimeout(() => {
            var mensaje = document.getElementById("notification");
            mensaje.style.display = "none";
        }, 3000);
    });
};




//Usuario Conectado
function conectado() {
    //console.log('aqui1');
    var conectado = document.querySelectorAll('.card-content')
        //console.log('aqui2')
    for (i = 0; i < conectado.length; i++) {
        if (conectado[i].innerHTML.indexOf('Conectado') != -1) {
            //console.log(conectado[i].innerHTML);
            conectado[i].classList.remove('has-background-link');
            conectado[i].classList.add('has-background-primary');
            conectado[i].classList.remove('has-text-light');
            conectado[i].classList.add('has-text-black-bis');
            //console.log('aqui tambien');

        };
    };
};

function actu() {
    document.addEventListener('DOMContentLoaded', () => {
        var btn = document.getElementById('entrar');
        btn.onclick = function() {
            var dive = document.getElementById('client');
            var url = 'http://localhost:5000/api/datos/?datos=todo';

            loadDoc(dive, url);
            todos();
        };
    });
};





function ClickCard(aidi) {
    var bancoption = []
    var lista = [];
    var banco = '';
    var bancolist = '<option></option> ';
    var bang = [];

    var bancoptionadmin = []
    var listadmin = [];
    var bancoadmin = '';
    var bancolistadmin = '<option></option> ';
    var bangadmin = [];
    //console.log(recas[0][0]);
    var serv = document.getElementById(aidi);
    var servfooter = document.getElementById("CardEnvio");
    var recarga = 'Recarga'
    var servicio = 'Servicio'
    servfooter.innerHTML = 'Facturar';



    //var divisa = document.getElementById('monto')
    for (bankadmin of bancadmin) {
        listadmin.push(bankadmin);
        bancoptionadmin.push(bankadmin[3]);
        bancolistadmin = bancolistadmin + `<option>${bankadmin[3]}</option>`;
    };
    for (bank of banca) {
        lista.push(bank);
        bancoption.push(bank[3]);
        bancolist = bancolist + `<option>${bank[3]}</option>`;
    };


    var form_recarga = `
    <div class="section">
    <form id="formula" method="POST">

    <label>Operadora a Recargar</label>
    <input class="input is-primary" type="text" name="solicitud" id="operadora" placeholder="${aidi}" value="${aidi}" readonly>
    <label>Numero a Recargar</label>
    <input class="input is-primary" type="text" name="numero" id="numero" placeholder="Numero a ser Recargado">

    <label>Monto a Recargar</label>
    <input class="input is-primary" type="text" name="montoreca" id="monto" placeholder="Monto de Recarga">

    </form>
    </section>`


    var form_servicio = `
    <div class="section">
    <form id="formula" method="POST">
    <label>Servicio a solicitar</label>
    <input class="input is-primary" type="text" name="solicitud" placeholder="${aidi}" value="${aidi}" readonly id="servicioa">

    <label>Numero de Pantallas</label>
    <input class="input is-primary" type="text" name="pantallas" placeholder="Cantidad de Pantallas a solicitar" id="panta">

    </form>
    </section>`


    var ventana = document.getElementById('modal1');
    ventana.classList.toggle('is-active');

    if (serv.children[1].textContent.includes('recargas')) {

        for (op of recas[0]) {
            if (op.includes(aidi)) {
                var porcent = op[4]
            }
        }
        ventana.childNodes[3].childNodes[1].childNodes[1].innerHTML = `Solicitud de ${recarga} ${aidi}`;
        ventana.childNodes[3].childNodes[3].innerHTML = form_recarga;

        var monto = document.getElementById('monto');

        var mont = new AutoNumeric(monto, { currencySymbol: 'Bs', decimalCharacter: ',', digitGroupSeparator: '.' });

        servfooter.onclick = function() {
            var operadora = document.getElementById('operadora');
            var numero = document.getElementById('numero');
            var monto = document.getElementById('monto');
            //var monto = monto.value.slice(2, monto.value.indexOf(','));

            ventana.childNodes[3].childNodes[1].childNodes[1].innerHTML = `Factura de ${servicio} ${aidi}`;
            ventana.childNodes[3].childNodes[3].innerHTML = `
            <div class="card m-0 p-0">
            <div class="card-content m-0 p-0">
            <div class="content m-0 p-0">
        <table class="table is-striped is-bordered is-size-7-mobile is-narrow m-0">
            <thead>
                <tr>
                    <th>Operadora</th>
                    <th>Numero</th>
                    <th>Monto</th>
                    <th>Porcentaje</th>
                </tr>
            </thead>
    
            <tbody>
                <tr>
                    <td>${operadora.value}</td>
                    <td>${numero.value}</td>
                    <td>${monto.value}</td>
                    <td>${porcent}%</td>
                </tr>
                <tr><td></td><td></td><td></td><td></td></tr>
                <tr>
                    <td>Total</td>
                    <td id="porcentaje"> ${mont.getNumber() * parseInt(porcent)/100}</td>
                    <td class="has-text-weight-bold" id="precioR">${mont.getNumber() + mont.getNumber()*porcent/100}</td>
                    <td></td>
                </tr>
            </tbody>
        </table>
        </div>
        </div>
        </div>

    <form id="formula" method="POST">
    <input class="input is-primary" type="text" name="solicitud" value="${operadora.value},${numero.value},${mont.getNumber() + mont.getNumber()*porcent/100}" readonly id="servicioa">
    <div class="hero is-link">Datos de Deposito</div>
    <div class="box">
        <label class="label is-size-6" for="vendedor">Deposito en Banco</label>
        <div class="select vendedores is-primary">
            <select class='vendedores' name='vendedor' id="bancosladmin" placeholder="Elige un Banco">
            ${bancolistadmin}
            </select>
        </div>
        <div class="m-0 p-0" id="dbancoadmin"></div>
    </div>
    
    <label class="is-size-6">Referencia Bancaria</label>
    <input class="input is-primary" type="text" name="solicitud" required placeholder="Referencia de Deposito"></input>
    </form>`;
            var tasadmin = document.getElementById('bancosladmin');
            var dbancoadmin = document.getElementById('dbancoadmin');
            tasadmin.addEventListener("change", function() {
                bangadmin = listadmin[bancoptionadmin.indexOf(tasadmin.value)];
                console.log(bangadmin);
                bancoadmin = `
        <div class="card sombra m-0 p-0">
        <div class"card-content m-0 p-0">
        <div class="content m-0 p-0">
        <table class="table is-size-7-mobile is-striped is-narrow is-bordered">
        <tbody>
        <tr>
            <td>Titular: <p class="has-text-weight-semibold">${bangadmin[1]}</p></td>
            <td>Cedula: <p class="has-text-weight-semibold	">${bangadmin[2]}</p></td>
            <td>Banco: <p class="has-text-weight-semibold	">${bangadmin[3]}/${bangadmin[4]}</p></td>
        </tr>
        <tr>
            <td>Tipo de Cuenta: <p class="has-text-weight-semibold	">${bangadmin[6]}</p></td>
            <td class="tdlow">Cuenta: <p class="has-text-weight-semibold	">${bangadmin[5]}</p></td>
            <td>Celular: <p class="has-text-weight-semibold	">${bangadmin[7]}</p></td>
        </tr>
            </tbody>
            </table>
            </div>
            </div>
            </div>`
                dbancoadmin.innerHTML = bancoadmin;
            });
            servfooter.innerHTML = 'Comprar';
            factura('recarga')


        }

    } else {
        ventana.childNodes[3].childNodes[1].childNodes[1].innerHTML = `Solicitud de ${servicio} ${aidi}`;
        ventana.childNodes[3].childNodes[3].innerHTML = form_servicio;

        servfooter.onclick = function() {
            var servicioa = document.getElementById('servicioa');
            var panta = document.getElementById('panta');
            var costoso = serv.children[1].textContent.split(' ')[3]

            ventana.childNodes[3].childNodes[1].childNodes[1].innerHTML = `Factura de ${servicio} ${aidi}`;
            ventana.childNodes[3].childNodes[3].innerHTML = `
    <div class="content">

        <div class="box">
        <table class="table is-size-7-mobile">
            <thead>
                <tr>
                    <th>Servicio</th>
                    <th>N.Pantallas</th>
                    <th>Precio</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>${servicioa.value}</td>
                    <td>${panta.value}</td>
                    <td>${parseInt(costoso.slice(0,1))}$</td>
                </tr>
                <tr><td></td><td></td><td></td></tr>
                <tr>
                    <td>Total</td>
                    <td> ${parseInt(costoso.slice(0,1)) * panta.value}$</td>
                    <td class="has-text-weight-bold" id="precioS">${((parseInt(costoso.slice(0,1)) * panta.value) * vendedor[9]).toFixed(0)}Bs</td>
                </tr>
            </tbody>
        </table>
        </div>

        <form id="formula" method="POST">
        
    <input class="input is-primary is-hidden" type="text" name="solicitud" value="${servicioa.value},${panta.value}, ${parseInt(costoso.slice(0,1)) * panta.value}" readonly id="servicioa">
    
    <div class="hero is-link">Datos de Deposito</div>
    <div class="box p-0">
        <label class="label" for="vendedor">Deposito en Banco</label>
        <div class="select vendedores is-primary">
            <select class='vendedores' name='vendedor' id="bancosl">
            ${bancolist}
            </select>
        </div>
        <div class="box" id="dbanco"></div>
    </div>
    
    <label class="label">Referencia Bancaria</label>
    <input class="input is-primary" type="text" name="solicitud" required placeholder="Referencia de Deposito"></input>
    </form>
    </div>`;
            var tas = document.getElementById('bancosl');
            var dbanco = document.getElementById('dbanco');

            tas.addEventListener("change", function() {
                bang = lista[bancoption.indexOf(tas.value)];
                console.log(bang);
                banco = `<div class="box p-1 sombra">
                <div class="content">
        <table class="table is-size-7-mobile">
        <tbody>
        <tr>
            <td>Titular: <p class="has-text-weight-semibold">${bang[1]}</p></td>
            <td>Cedula: <p class="has-text-weight-semibold	">${bang[2]}</p></td>
            <td>Banco: <p class="has-text-weight-semibold	">${bang[3]}/${bang[4]}</p></td>
        </tr>
        <tr>
            <td>Tipo de Cuenta: <p class="has-text-weight-semibold	">${bang[6]}</p></td>
            <td>Cuenta: <p class="has-text-weight-semibold	">${bang[5]}</p></td>
            <td>Celular: <p class="has-text-weight-semibold	">${bang[7]}</p></td>
        </tr>
            </tbody>
            </table>
            </div>
            </div>`
                dbanco.innerHTML = banco;
            });
            servfooter.innerHTML = 'Comprar';
            factura('servicio')




        }



    };

};


function factura(state) {
    var servfooter = document.getElementById("CardEnvio");
    if (state == 'servicio') {
        var valord = document.getElementById("precioS");
    } else {
        var valord = document.getElementById("precioR");
    };

    new AutoNumeric(valord, { currencySymbol: 'Bs', decimalCharacter: ',', digitGroupSeparator: '.' });
    new AutoNumeric(document.getElementById('porcentaje'), { currencySymbol: 'Bs', decimalCharacter: ',', digitGroupSeparator: '.' });

    servfooter.addEventListener('click', () => {
        console.log('yeah cuate');
        servfooter.setAttribute('form', 'formula');
        servfooter.setAttribute('name', 'action');

        if (state == 'recarga') {
            servfooter.setAttribute('value', 'recarga');
        }
        if (state == 'servicio') {
            servfooter.setAttribute('value', 'servicio');
        };

    });
};



//Ajax carga listado de recargas
function loadrec(div, page) {
    //console.log('se ejecuta');
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var content = JSON.parse(this.responseText)
            document.getElementById(div).innerHTML = '';
            for (item of content) {
                if (item[4] == 0) {
                    var ord = item[3].split(',');
                    document.getElementById(div).innerHTML += `<div class="card has-background-dark has-text-light" id="${item[2]}" onclick="ClickCard(this.id,item)
                "><div class="card-header has-background-link">&nbsp${item[1]}</div><div class="card-content" style="cursor:pointer">
                    Fecha: ${item[2]}<br>Orden:<br>&nbsp&nbsp&nbsp
                                     Empresa: ${ord[0]}<br>&nbsp&nbsp&nbspNumero: ${ord[1]}<br>&nbsp&nbsp&nbspMonto:
                ${ord[2]}
                             </div>
                      </div><br>
             </div>`
                };
            }
            //document.getElementById(div).innerHTML = ;
        }
    };
    xhttp.open("GET", page, true);
    xhttp.send();
};

function limpiar() {
    var ider = document.getElementById('ider');
    var fecha = document.getElementById('fecha');
    ider.value = '';
    fecha.value = '';

}


function todos() {
    loadrec('todosorden', 'http://localhost:5000/api/datos/?datos=rec');
    loadDoc('todos', 'http://localhost:5000/api/datos/?datos=todo');
    loadDoccont('tags', 'http://localhost:5000/api/datos/?datos=cuenta');

    conectado();

    //loadrec('todosorden', 'http://uriell77.pythonanywhere.com/api/datos/?datos=rec');
    //loadDoc('todos', 'http://uriell77.pythonanywhere.com/api/datos/?datos=todo');
    //loadDoccont('tags', 'http://uriell77.pythonanywhere.com/api/datos/?datos=cuenta');

};


function hiden() {
    caja = document.querySelectorAll('#articulos');
    for (item of caja) {
        //console.log(item.childNodes[1].childNodes[1].childNodes[1].src);
        if (item.childNodes[1].childNodes[1].childNodes[1].src == 'http://localhost:8000/static/img/.-.jpeg') {
            console.log(item.childNodes);
            item.classList.toggle('is-hidden');

        }
    }

}


//nombre del logo
//const fileInput = document.querySelector('#logofile input[type=file]');
//console.log(fileInput.files[0].name)
//fileInput.onchange = () => {
//    if (fileInput.files.length > 0) {
//        const fileName = document.querySelector('#logofile .file-name');
//        fileName.textContent = fileInput.files[0].name;
//    }
//};

//formatear montos de monedas
document.addEventListener('DOMContentLoaded', () => {
    var valord = document.getElementById("divice");
    new AutoNumeric(valord, { currencySymbol: 'Bs', decimalCharacter: ',', digitGroupSeparator: '.' });
});