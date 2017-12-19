## Configurar interfaces de red:
```
ifconfig
macchanger -h (help)
macchanger -r (mac aleatoria)
macchanger -m (la que yo quiero)
macchanger -p (original)
```
## Pasos para cambiar la mac:
```
ifconfig eth0 down
macchanger -r eth0 (ejemplo)
ifconfig eth0 up
```
## Descubrir segmentos de ip dentro de la red local:
```
netdiscover -i eth0
arp-scan -l -I eth0 (local)
```
## Subir un servicio:
```
service apache2 start / stop
```
## Ver servicios que están corriendo:
```
netstat -ntpl (tcp)
service ssh status (ejemplo con ssh)
```
## Qué servicios tiene Kali?
```
cd /etc/init.d/ && ls
```