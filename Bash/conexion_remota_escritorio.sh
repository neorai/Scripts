#!/bin/bash

<< 'MULTILINE-COMMENT'
    editar
    sudo nano /etc/xdg/lxsession/LXDE-pi/autostart

    añadir al final

    @lxterminal -e /path/script.sh


    meter sleep porque no inicia red

    SCRIPT

    sleep 10
    echo "admin" | ssvncviewer -autopass 192.168.1.20
MULTILINE-COMMENT


echo "Esperando red  segundos"
sleep 5

fecha=$(date "+%Y/%m/%d %H:%M:%S")

log_conexion () {
ping -q -c5 8.8.8.8 > /dev/null
if [ $? -eq 0 ]
then
  swaks --to "xxxxxx@xxxxxx.es" \
--from "xxxxxxxx@xxxxxx.es" \
--header "Subject:Raspi xxxxx " \
--body "$fecha intento de reconexion" \
--server xxxxxx.xxxxxxx.com \
--auth LOGIN \
--auth-user "xxxxx@xxxxxxx.es" \
--auth-password "xxxxxxxxxxx" \
--tls -p 587 --auth-hide-password
echo "correo enviado"
echo $fecha >> /home/pi/log.txt
echo "registro en log local creado"
else
echo $fecha >> /home/pi/log.txt
echo "registro en log local creado"
fi
}

while :
do
declare -i n=0
while ! ping -c1 192.168.1.213 $1 &>/dev/null
do
n=$(( n + 1))
if [ $n -eq 1 ]; then log_conexion; fi
echo "Esperando equipo disponible, intento numero $n"
sleep 3
done

echo "admin" | ssvncviewer -autopass -fullscreen 192.168.1.213
# tambien se puede con rdesktop instalar antes, si se quita -p pedira contraseña en el rdp no en el terminal.
# la tasa de refreso de Rdesktop es mejor usar rdesktop
rdesktop -u admin -p admin 192.168.1.213 -k es-es -f
echo "error conexion, reconectando...."
log_conexion
sleep 3
done
