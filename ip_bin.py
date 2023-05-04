#-*-coding: utf-8 -*-

ip = input("Introduce la dirección IP: ")
mask = input("Introduce la máscara de red: ")
# Calculamos el binario de la ip
octetos_ip = ip.split('.')
binario_ip = [format(int(octeto), '08b') for octeto in octetos_ip]
binario_ip = '.'.join(binario_ip)

# Calculamos el binario de la mascara de red
octetos_mask = mask.split('.')
binario_mask = [format(int(octeto), '08b') for octeto in octetos_mask]
binario_mask = '.'.join(binario_mask)
# Contamos los ceros de la mascara de red
ceros = binario_mask.count('0')
host = (2**ceros)-2 # esta es la formula pa saber cuantos host pueden conectarse

# Aqui calcula el and
and_cal = []
for i in range(4):
    octeto_ip = int(octetos_ip[i])
    octeto_mask = int(octetos_mask[i])
    and_cal.append(format(octeto_ip & octeto_mask, '08b'))

# Covertimos el Binario del AND a decimal
and_cal = '.'.join(and_cal)
red_decimal = [str(int(octeto, 2)) for octeto in and_cal.split('.')]
red_decimal = '.'.join(red_decimal)

print(f"La dirección IP {ip} en binario es: {binario_ip}")
print(f"La máscara de red {mask} en binario es: {binario_mask}")
print(f"El AND binario de la IP y la máscara de red es: {and_cal}")
print(f"La dirección de red resultante es: {red_decimal}")
print(f"La máscara de red {mask} puede tener {host} hosts.")
print("             By Mr Star")