## Requisitos

- Tener **Docker instalado y abierto**  
  - Windows/Mac → abrir **Docker Desktop**  
  - Linux → tener el servicio Docker activo (`sudo systemctl start docker`)  
- Si el servidor y el cliente se ejecutan en **PC distintos**, deben estar en la misma red local.  

## Servidor

1. **Descargar la imagen**
   ```bash
   docker pull franciscoherna/server:latest
2. **Ejecutar el servidor**
      ```bash
      docker run -p 8080:8080 franciscoherna/server:latest
3. **El servidor quedará escuchando en el puerto 8080.**                 
No cierres esta ventana, aquí aparecerán las conexiones y los votos recibidos.

Imagen en Docker Hub: https://hub.docker.com/r/franciscoherna/server

## Cliente

1. **Descargar la imagen**
      ```bash
      docker pull franciscoherna/cliente:latest
2. **Ejecutar el cliente**
   ```bash
   docker run -it --rm franciscoherna/cliente:latest
3. **El cliente pedirá**
   - IP del servidor:
       - Si corre en otro PC de la red → se busca IP:
   ```bash
   ipconfig   # en Windows
   ifconfig   # en Linux/Mac
Ejemplo: 192.168.1.23

- Nombre de usuario

- Tu voto → OpcionA, OpcionB o OpcionC

4. **El servidor mostrará en consola quién se conectó y qué opción votó.**
  - Cada usuario puede votar solo una vez.

Imagen en Docker Hub: https://hub.docker.com/r/franciscoherna/cliente




