# Bash Scripting

## Cosas especiales

Nombre del archivo: se guarda en la variable

```$0```

Argumentos: se colocan los argumentos a lado del archivo en el comando de ejecucion ./archivo.sh arg1 arg2 arg3

```$1 $2 $3```

Comando shift: voltea todos los valores, descarta el primero
```
$# : numero de argumentos

$* : todos los argumentos

$@ : todos los argumentos

$_ : comando anteriormente ejecutado

$$ : PID del propio proceso shell

$? : se ejecuto con exito o no

#!/bin/bash : le dice al interpretador que entorno se va ejecutar
```
## Varibales
En mayusculas, por defecto todas son string y para invocarlas se usa $[variable], se usa comilla dobles para usar las variables dentro de string
```
read VARIABLES
HOLA="hola mundo"
echo "El valor de la variables es $VARIABLE"
```
Tambien tenemos las famosas variables de entorno que son vairbales que se declaran fuera del script 
```
$ export VAR="valor"
./archivo.sh VAR
```
Asi se delcaran integers porque todo lo toma como string aunque no este entre comillas, una vez hecha int no se le puede asignar un string
```
declare -i NUM
NUM=7
```
## Comandos