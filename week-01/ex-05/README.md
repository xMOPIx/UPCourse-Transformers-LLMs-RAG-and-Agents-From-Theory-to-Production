## Estructura del Proyecto

* `main.py`: Punto de entrada principal de la aplicación.
* `index.html`: Interfaz de usuario.
* `Dockerfile`: Definición de la imagen para el contenedor.
* `docker-compose.yml`: Orquestación para levantar el servicio.
* `requirements.txt`: Dependencias de Python necesarias para el proyecto.

## Ejecución del proyecto

Una vez verificado que Docker está corriendo, puedes levantar todo el entorno con un único comando. Ejecuta en la raíz del proyecto:

```bash
sudo docker compose up --build 
