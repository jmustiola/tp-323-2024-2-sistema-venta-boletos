Sistema de venta de boletos para agencia de viajes JCBI - Pascal
=======================================================

Planteamiento del problema
--------------------------

La agencia de viajes "JCBI" desea automatizar el proceso de venta de boletos, con el fin de llevar el control de los clientes que puedan y desean viajar al exterior, para ello se cuenta con la siguiente información:

1. Numero de pasaporte.
2. Fecha de expedición del pasaporte.
3. Origen del pasaporte.
    + V = Venezolano.
    + E = Extranjero.
4. Fecha de expedición del certificado de vacuna.
5. Fecha de la declaración de impuesto, si el pasaporte fue expedido en Venezuela caducara al año, en caso contrario su duración es de dos años. El certificado de vacuna y la declaración de impuesto son válidos por un año.

Para la Automatización del proceso de venta de boletos se debe considerar la siguiente
información, donde se detalla el registro de los datos de cada cliente. Las características
de los campos: son longitud y tipo (numérico (N) y alfanumérico(X)).

INFORMACION LONGITUD TIPO

+ Apellidos y nombre 60 X.
+ Numero de pasaporte 10 N.
+ Fecha de expedición 8 N.
+ Fecha de certificado de vacuna 8 N.
+ Fecha de declaración - impuesto 8 N.
+ Origen del pasaporte 1 X.

Requerimientos
--------------

Con base a lo planteado, diseña un programa en Pascal que, haciendo uso de Arreglos (vectores y/o matrices), permita realizar lo siguiente:

1. Presentar un menú de mantenimiento con las opciones:
    + Incluir
    + Modificar
    + Eliminar
    + Reporte
    + Salida
2. Ingresar el registro del cliente por el número de pasaporte
3. Procesar la información dada de tal manera que chequee que los recaudos están vigentes, en caso contrario se debe imprimir, además de los datos del cliente, el mensaje `RECAUDOS NO VIGENTES`
4. Generar un reporte impreso que presente la siguiente información:
    + Cuántos clientes tienen pasaporte venezolano
    + Cuántos clientes tienen pasaporte extranjero
    + Cuántos clientes tienen vencida la declaración de impuestos
    + Cuántos clientes tienen los recaudos vigentes

Solución
========

En progreso...

De interés
==========

Ambiente de desarrollo para programar en Pascal
-----------------------------------------------

Aunque VSCode puede ser una buena alternativa para la edición, no obstante su soporte para Pascal no es muy bueno. Por eso, las recomendaciones son las siguientes:

+ [FreePascal - Windows](https://free-pascal.softonic.com/)
+ [FreePascal - MAC](https://free-pascal.uptodown.com/mac)
+ [Lazarus - Todos los SO](https://sourceforge.net/projects/lazarus/files/)

Si usas Linux, deberás tener instalado `gtk2-devel` como dependencia para poder instalar Lazarus

Aprendizaje
-----------

+ [Introducción a la programación](https://www.youtube.com/watch?v=VxrIZGQfxmE&pp=ygUeaW50cm9kdWNjacOzbiBhIGxhIHByb2dybWFjaW9u)
+ [Lógica de programación](https://www.youtube.com/watch?v=TdITcVD64zI&t=14500s&pp=ygUXbG9naWNhIGEgbGEgcHJvZ3JtYWNpb24%3D)
+ [Curso de programación en Pascal](https://www.nachocabanes.com/pascal/curso/)
+ [Roadmaps para diversas carreras](https://roadmap.sh/)
+ [Roadmap de programación](https://retosdeprogramacion.com/roadmap/)
