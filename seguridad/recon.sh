#!/bin/bash
HOME=$(pwd)
DATOS=$HOME/datos/
f_error() {
	echo
	echo -e "******* ERROR *******"
	echo
	sleep 1
	echo
	f_main
}
f_recon() {
	echo "EN CONSTRUCCIÓN"
	read
	f_main
}
f_escaneo() {
	echo "EN CONSTRUCCIÓN"
	read
	f_main
}
f_baner(){
echo
echo -e "******* RECON V 0.1 ********"
echo
}
f_main(){
clear
f_baner
if [ ! -d $DATOS ]; then
	mkdir -p $DATOS
fi
echo -e "Bienvenidos al Script de Reconocimiento de Platzi"
echo
echo -e "Qué opción desea ejecutar"
echo
echo -e "1) RECONOCIMIENTO"
echo
echo -e "2) ESCANEO DE HOSTS"
echo 
read OPCION
case $OPCION in
	1)
		f_recon
		;;
	2)
		f_escaneo
		;;
	
	99)
		clear
		exit
		;;
	*)
		f_error
		;;
esac
}
while true; do f_main; done
