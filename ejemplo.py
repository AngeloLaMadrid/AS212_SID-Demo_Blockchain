
#comentar todo el codigo de abajo
import hashlib


usuarios_lista = ["naomi.camas", "abel.huamani","angelo.la.madrid", "jefferson.mauricio", "gian.nuñez", "pedro.porras", "erick.portuguez", "jhon.sotomayor", "carlos.hernandez", "jonny.silverhand", "diego.sanchez", "valeria.ramirez"]
usuarios = {i+1: {"nombres": ' '.join(nombre.split('.')[:-1]), "apellidos": nombre.split('.')[-1]} for i, nombre in enumerate(usuarios_lista)}


blockchain = []

def elegir_usuario(mensaje):
    return int(input(mensaje))

def enviar_soles(id_origen, id_destino, soles):
    print(f"{id_origen:02} {usuarios[id_origen]['nombres']} {usuarios[id_origen]['apellidos']} ENVIARÁ A "
          f"{id_destino:02} {usuarios[id_destino]['nombres']} {usuarios[id_destino]['apellidos']} {soles:.2f} SOL COINs")

def secret_function():
    print("\n--- HISTORIAL DE TRANSACCIONES ---")
    for block_hash in blockchain:
        print(block_hash)

while True:
    print("\n--- NUEVA TRANSACCIÓN ---\n")
    print("Usuarios Disponibles:")
    for id, usuario in usuarios.items():
        print(f"{id} {usuario['nombres']} {usuario['apellidos']}")
        
    print("\n---------------------------\n")
    id_origen = elegir_usuario("\nElija un usuario que va a ENVIAR por su ID: ")
    id_destino = elegir_usuario("Elija un usuario que va a RECIBIR por su ID: ")
    soles = float(input("Ingrese la cantidad de SOL COINs a enviar: "))
    confirmacion = input(f"\n¿Está seguro de enviar {soles:.2f} SOL COINs a {usuarios[id_destino]['nombres']} {usuarios[id_destino]['apellidos']}? (S/N): ")
    if confirmacion.upper() == 'S':
        enviar_soles(id_origen, id_destino, soles)
        transaction = (id_origen, id_destino, soles)
        # Obtenemos el hash del último bloque en la cadena si existe, si no, se asigna "0"
        previous_hash = blockchain[-1] if blockchain else "0"
        #abajo se genera el hash de la transaccion y apilarlo con el ultimo hash
        block_hash = hashlib.sha256((str(transaction) + previous_hash).encode()).hexdigest()
        blockchain.append(block_hash)
        print("¡Transacción exitosa!")
    else:
        print("Transacción cancelada!")
    next_action = input("¿Desea realizar otra transacción o ver el historial? (S/N/historial): ")
    if next_action.upper() == 'HISTORIAL' or next_action.upper() == '':
        secret_function()
    elif next_action.upper() != 'S':
        break

print("\n--- HISTORIAL DE TRANSACCIONES ---")
for block_hash in blockchain:
    print(block_hash)


''' descomentar si es necesario codigo backup
usuarios = {
    1: {"nombres": "Naomi", "apellidos": "Cama"},
    2: {"nombres": "Abel", "apellidos": "Huamani"},
    3: {"nombres": "Angelo", "apellidos": "La Madrid"},
    4: {"nombres": "Jefferson", "apellidos": "Mauricio"},
    5: {"nombres": "Gian", "apellidos": "Nuñez"},
    6: {"nombres": "Pedro", "apellidos": "Porras"},
    7: {"nombres": "Erick", "apellidos": "Portuguez"},
    8: {"nombres": "Jhon", "apellidos": "Sotomayor"},
    9: {"nombres": "Carlos", "apellidos": "Hernandez"},
    10: {"nombres": "Jonny", "apellidos": "Silverhand"},
    11: {"nombres": "Diego", "apellidos": "Sanchez"},
    12: {"nombres": "Valeria", "apellidos": "Ramirez"}
}
'''