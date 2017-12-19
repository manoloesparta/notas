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

SUMA=`expr 7 + 5`
echo $SUMA
```
## Comandos
Cuando usamos comandos en bash necesitmos usar tildes agudas o el simbolo para invocar variables
```
COMANDO=`pwd`
COMMAND=$(ls $UNO)
```
## Control de flujo
Son los comandos if else solo que es este caso se usa diferentes operadores entre string e ints, 0 es verdadero y n es verdadero
```
#!/bin/bash
read NUMERO
if [ $NUMERO == 1 ]; then
	echo "seleccionaste el numero 1";
else
	echo "seleccionaste el numero $NUMERO"
fi
```

Para crear y buscar archivos

```
pwd=$(pwd)
read ARCHIVO
if [ -f $ARCHIVO]; then
	cat $archivo
elif [ $ARCHIVO == "/dir/readme.md" ]
	touch $ARCHIVO
	if [ -f $ARCHIVO ]; then
		echo "Archivo creado exitosamente"
	fi
else
	echo "No existe"
fi
```

Usar case/switch

```
read VAR
case $VAR in
	"Hola")
		echo "es hola"
		;;
	"Adios")
		echo "es adios"
		;;
	*)
		echo "no c"
		;;
esac
```
## Ciclos
while
```
declare -i VALOR
VALOR=1
while [ $VALOR < 10 ]
do
	echo $VALOR
	let $VALOR+=1
done
```
until
```
declare -i VALOR
VALOR=1
until [ $VALOR > 10 ]
do
	echo $VALOR
	let $VALOR+=1
done
```
for
```
pwd=$(pwd)
for i in `ls`
do
	echo $i
done
```
## Funciones
```
funcion_hola(){
	echo "Hola"
	echo $1
}
funcion_hola argumento
```