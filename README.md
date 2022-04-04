# kalinka

Kalinka nace como un proyecto de prática realizado con el simple propósito de tener una pequeña aplicación funcional. No pretende ser un producto comercial ni mucho menos.

Consiste en tablero para la gestión de tareas personales. Todas las funcionalidades fueron definidas por por una persona agena al proyecto, quien me aguantó varias horas hablando de códigos.

## Demo

Puedes probar la aplicación en su versión demo.

- [Kalinka](http://kalinka.cultivoiot.com.ar:3900/).
- usr: demo.
- pss: demo.2022

## Estructura

El proyecto está estructurado en 3 contenedores.

- Kalinka: Aplicación.
- postgreSQL: Base de datos.
- nginx: Servicio de proxy.

En la raiz del proyecto se encuentra el archivo Docker-compose.yml  para ejecutar en el servidor.


## Variables de entorno
Para la ejecución del proyecto se deben especificar las variables de entorno de cada contenedor.

__

### Kalinka
- SECRET_KEY=
- ALLOWED_HOSTS=0.0.0.0,127.0.0.1
- DB_USER=
- DB_PASSWORD=
- EMAIL_HOST=
- EMAIL_PORT=
- EMAIL_USE_TLS=
- EMAIL_HOST_USER=
- EMAIL_HOST_PASSWORD=

__
### PostgreSQL
- POSTGRES_DB=
- POSTGRES_USER=
- POSTGRES_PASSWORD=

__
### nginx
Sin variables de entorno.

## Despliegue

Se detallan los pasos recomendados.

- Clonar el repositorio.

        'git clon https://github.com/lucrohatsch/kalinka.git'
- Definir las variables de entorno
        
- Iniciar contenedores con Docker-compose

        'docker-compose up'
- Iniciar bash interactiva

        'docker exec -it kalinka_app /bin/sh'
- Colectar archivos estaticos

        'python manage.py collectstatic'
- Crear super usuario del proyecto

        'python manage.py createsuperuser'
