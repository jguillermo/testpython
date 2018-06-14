Notas
-----

para instalar   make install

para iniciar    make up

para detener    make down


los servicios son : 

para crear notas
POST
http://localhost/v1/notas
 {
    "name":"Guillermo",
    "nota":"5",
    "token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJrZXkiOiIxMjMifQ.NZSC6wT0yGUtpsStZ2spJsMMkegplIcJtlwfRMPO2TM"
 }



para listar las notas
GET
http://localhost/v1/notas?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJrZXkiOiIxMjMifQ.NZSC6wT0yGUtpsStZ2spJsMMkegplIcJtlwfRMPO2TM





Serializacion y validacion
la validacion se debe hacer en la capa de dominio, por ser logica de negocio


Autorización

Para esto hay que registrar las notas con el id de usuario, para hacer filtros por un usuario

Generar un JWT en el logue del usuario, que tenga el id del usuario
Decodifical el jwt buscar las notas en el idUsuario decodificado
la url a consultar seria http://localhost/v1/notas/ID
