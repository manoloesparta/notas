# Comandos escenciales de bash

### ls 
lista los archivos y directorios
### mkdir -p dir/dir 
crea una carpeta dir dentro de otra
### pdw 
imprime la ruta actual
### rmdir 
elimina directorios vacios
### rm -rf [ruta] 
elimina directorios recursivamente y forzando
### mv [directorio actual] [directorio destino]
mueve o renombra un archivo o directorio
### apropos [comando] 
dice en donde se encuentra el comando
### whatis [commando] 
muestra donde buscar en el manual
### mkdir -p uno/{uno,dos,tres} 
crear tres directorios dentro de un directorio
### cd cok? 
abre una carpeta que comience con cok y tenga cualquier carácter al final
### cd ~ 
dirige al home
### find [directorio] [patrón de busqueda] 
buscar directorios
### locale [directorio] 
buscar archivos
### whereis [comando] 
dice el directorio donde se ejecuta
### file [archivo o directorio] 
indica el tipo del archivo
### chown [archivo] [usuario] 
modifica propietario
### chmod [permisos] [archivo] 
agrega o elimina permisos
### tar cvf [nombre] [archivos] 
comprime un archivo
### tar xvf [archivo] 
descomprime un archivo

### Ver procesos y cerrar los que dan problemas
```
ps axf | grep firefox
ps aux | grep firefox
kill -9 numeroproceso
```

### En un directorio lleno de archivos de texto para buscar alguna palabra:
```
cat * | grep busqueda --color
```

### Buscar y mostrar los primeros 10 resultados
```
ls -la | grep e | head
```

### Borrar el historial de comandos cuando se trabaja en sesiones con linux
```
history -c
cat /dev/null > file_log.txt
```

### Observar algún log de comandos para buscar sesiones
```
cat /home/user/.bash_history >> ~/.bash_history_user
cat ~/.bash_history_user | grep mysql --color
cat ~/.bash_history_user | grep ssh --color
```