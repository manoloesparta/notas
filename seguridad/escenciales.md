# Herramientas escenciales

## Netcat (nc)

Escuchar en el puerto 8080 (servidor)
```
nc -l -v -p 8080
```
Para conectarse a ese puerto (cliente), usamos localhost o la siguiente ip
```
nc 127.0.0.1 8080
```
Conexion UDP (servidor)
```
nc -l -u -v -p 8080
```
Conexion UDP (cliente)
```
nc -u 127.0.0.1 8080
```
Cuando abrimos un puerto en el servidor y queremos conectar un cliente, el cliente va abrir otro puerto independiente, generalmente de 20,000 hacia arriba

Cuando alguien se conecta mandar el contenido de un archivo
```
nc -l -v -p 8080 < archivo.txt
```
Recibir archivo y guardarlo
```
nc 127.0.0.1 > archivo_nuevo.txt
```
Si queremos mandar el contenido de un archivo por medio netcat hacia el servidor
```
nc 127.0.0.1 < archivo.txt
```
Cuando se conecte a nuestro servidor ejecute algun programa (bash)
```
nc -l -v -p 8080 -e /bin/bash
```
Cuando nos conectemos ejecutamos
```
nc 127.0.0.1 -e /bin/bash
```
Crear dos servidores y uno se ejcute bash mientras en otro son mensajes
```
nc -l -v -p 8080 | /bin/bash | nc -l -v -p 9090
```
La desventaja de netcat es que todo va en texto plano, eso significa que se puede ver todo lo que hagamos para eso usamos crypcat que se usa de la misma manera que netcat

## Wireshark

Es un programa para escanear la red con interfaz grafica.
En este programa elegimos la interfaz que usamos, primero checaremos los paquetes TCP, vemos la trama TCP con click derecho > Follow > TCP Stream,
los textos rojos son lo que se pidio como info y lo azul lo que se recibio. Se ve tambien de donda y a donde va la informacion.

Las peticiones DNS tambien se pueden encontrar que es practicamente ingresar a un pagina en el navegador

## TCPdump

Tiene la misma funcion que wireshark solo que en terminal, le indicamos la interfaz, en este caso sera localhost
```
tcpdump -i lo0
```
Escaneo a la red conectada mostrando mas info
```
tcpdump -v -i en0
```
No mostrar hostnames ni puertos y buscar algo en especifico
```
tcpdump -nn -i en0 host 206.79.206.21 and port 80
```
Guardar en un archivo y poder exportar a wireshark
```
tcpdump -vvv -nn -i en0 host 206.79.206.21 and port 80 -w prueba.pcap
```
Para ver los paquetes que se mandan
```
tcpdump -XX -i en0
```

## Nslookup

Sirve para saber informacion de un DNS
```
nslookup google.com
```

## Puerto abiertos
```
netstat -ap tcp | grep -i "listen"
```

## SSH
Sirve para accesar a otros dispositivos por medio de la red, nos podemos conectar localmente por medio de un puerto para de ahi ejecutar comandos
```
ssh -l root 192.168.1.70 -L 8080:192.168.1.21:80
```
Con esto en mi puerto 8080 va relfejar la ip 192.168.1.21:80

Tambien se puede dejar al otro cleinte que vea nuestro dispositivo, mas bien nos conectamos para que ellos se conecten
```
ssh -l root 192.168.1.70 -R 8080:192.168.1.21:80
```

Podemos hacer un socket para hacer comunicaciones por el, esto es como un VPN o Proxy
```
ssh -l root 192.168.1.70 -D 8080
```

Para ver registros usamos
```
w
```