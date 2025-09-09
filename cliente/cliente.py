import socket

# Pedir datos de conexión al usuario
HOST = input("Ingrese la IP del servidor: ").strip()
PORT = 8080

opciones_validas = ["OpcionA", "OpcionB", "OpcionC"]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f"[CLIENTE] Conectado a -> {HOST}:{PORT}")

    usuario = input("Ingresa tu nombre de usuario: ")
    s.sendall(f"USER {usuario}".encode("utf-8"))

    while True:
        opcion = input("Escribe tu voto (OpcionA / OpcionB / OpcionC): ").strip()

        if opcion not in opciones_validas:
            print("❌ Opción inválida, inténtalo de nuevo...")
            continue

        s.sendall(f"VOTE {opcion}".encode("utf-8"))
        respuesta = s.recv(1024).decode("utf-8").strip()
        print(f"[SERVIDOR]: {respuesta}")
        break

    print("[CLIENTE] Conexión cerrada")
