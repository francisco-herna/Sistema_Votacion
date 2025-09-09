import socket

HOST = "0.0.0.0"
PORT = 8080

votes = {"OpcionA": 0, "OpcionB": 0, "OpcionC": 0}
usuarios_votaron = set()

def mostrar_resultados():
    print("\n===== RESULTADOS =====", flush=True)
    for opt, count in votes.items():
        print(f"{opt}: {count}", flush=True)
    print("======================\n", flush=True)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()
    print(f"[SERVIDOR] Escuchando en {HOST}:{PORT}...", flush=True)

    while True:
        conn, addr = s.accept()
        with conn:
            print(f"[NUEVA CONEXIÓN] {addr}", flush=True)

            data = conn.recv(1024).decode("utf-8").strip()
            if not data.startswith("USER"):
                conn.sendall(b"Debes identificarte con: USER <nombre>\n")
                continue

            _, username = data.split(maxsplit=1)

            if username in usuarios_votaron:
                conn.sendall(b"Ya emitiste un voto. No puedes votar de nuevo.\n")
                continue

            data = conn.recv(1024)
            if not data:
                conn.sendall(b"No se recibio ningun voto.\n")
                continue

            message = data.decode().strip()
            if message.startswith("VOTE"):
                _, option = message.split(maxsplit=1)
                if option in votes:
                    votes[option] += 1
                    usuarios_votaron.add(username)
                    conn.sendall(b"Voto registrado con exito\n")
                    print(f"[VOTO] {username} ({addr}) votó por {option}", flush=True)
                else:
                    conn.sendall(b"Opcion invalida. Usa OpcionA / OpcionB / OpcionC\n")
            else:
                conn.sendall(b"Formato incorrecto. Usa: VOTE <Opcion>\n")

            mostrar_resultados()
