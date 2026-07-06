# 🚀 FastAPI TODO API - Automated CI/CD Cloud Deployment

Este proyecto consiste en una **API REST reactiva para la gestión de tareas (TODO)** desarrollada con **FastAPI** y conectada a **Amazon DynamoDB**. La aplicación está completamente contenerizada con **Docker** y su infraestructura en la nube está automatizada de extremo a extremo utilizando **Terraform** (Infraestructura como Código) y un Pipeline de Integración y Despliegue Continuos (CI/CD) en **Jenkins**.

---

## 🏗️ Arquitectura del Sistema

El flujo de despliegue y operación sigue el siguiente modelo de arquitectura en la nube:

* **Infraestructura (AWS):** Una instancia virtual **EC2 (Ubuntu)** actúa como servidor web, protegida por un *Security Group* que expone el puerto `8000`. Los datos se almacenan de forma persistente y asíncrona en una tabla NoSQL de **Amazon DynamoDB**.
* **Orquestación:** La API de FastAPI se ejecuta de forma aislada dentro de un contenedor de **Docker** para garantizar la paridad entre los entornos de desarrollo y producción.
* **Automatización (CI/CD):** **Jenkins** monitorea el repositorio de **GitHub**, automatizando la limpieza del espacio de trabajo, la clonación del código y la validación de las imágenes de Docker.

---

## 🛠️ Tecnologías Utilizadas

* **Backend:** Python 3.11+ / FastAPI / Uvicorn / Boto3 (SDK de AWS).
* **Base de Datos:** Amazon DynamoDB (NoSQL).
* **Infraestructura como Código (IaC):** Terraform.
* **Contenerización:** Docker.
* **Servidor de CI/CD:** Jenkins Pipelines (Groovy).
* **Cloud Provider:** Amazon Web Services (AWS EC2 & IAM).

---

## 📦 Estructura del Repositorio

```text
├── .github/               # Configuraciones opcionales de GitHub
├── terraform/             # Scripts de Infraestructura como Código (IaC)
│   ├── main.tf            # Definición de EC2, DynamoDB y Security Groups
│   ├── variables.tf       # Variables de configuración de AWS
│   └── outputs.tf         # Salidas del despliegue (IPs, IDs)
├── src/                   # Código fuente de la API
│   ├── main.py            # Inicialización de FastAPI y Endpoints
│   └── database.py        # Conexión y configuración con DynamoDB
├── Dockerfile             # Instrucciones de empaquetado del contenedor
├── Jenkinsfile            # Pipeline de automatización de CI/CD
├── requirements.txt       # Dependencias de Python
└── README.md              # Documentación del proyecto
🚀 Ciclo de Vida del Despliegue (Guía de Uso)
1. Inicializar la Infraestructura en la Nube
Para levantar los servidores en AWS desde tu máquina local, navega a la carpeta de Terraform y ejecuta:

Bash
cd terraform
terraform init
terraform apply -auto-approve
2. Ejecutar el Pipeline en Jenkins
Accede a tu servidor local de Jenkins (http://localhost:8080).

Crea o selecciona el proyecto de tipo Pipeline conectado a este repositorio de GitHub.

Asegúrate de configurar las credenciales de AWS (aws-credentials-demo) en el gestor de Jenkins.

Modifica las variables de entorno al inicio del Jenkinsfile con la IP y el ID asignados por AWS:

Groovy
environment {
    INSTANCE_ID   = 'i-084100026076b6ce2'
    EC2_PUBLIC_IP = '32.197.217.181'
}
Haz clic en Build Now (Construir ahora). El pipeline limpiará el entorno, validará el build localmente e interactuará con la infraestructura para preparar el despliegue.

3. Ejecución del Contenedor en la EC2
Con la infraestructura lista, conéctate a la terminal de tu instancia EC2 (vía EC2 Instance Connect) para levantar el contenedor en producción:

Bash
git clone -b master [https://github.com/AngeloMaiale/Despliegue.git](https://github.com/AngeloMaiale/Despliegue.git) /home/ubuntu/Despliegue
cd /home/ubuntu/Despliegue
sudo docker build -t todo-api-fastapi:latest .
sudo docker run -d -p 8000:8000 --name todo-api todo-api-fastapi:latest
Una vez encendido, puedes validar el estado del contenedor con:

Bash
sudo docker ps -a
4. Acceso al Servicio e Interfaz Interactiva
La API expone una documentación completamente interactiva autogenerada (Swagger UI). Puedes consumirla ingresando desde cualquier navegador a la siguiente ruta:

👉 http://<TU_IP_PUBLICA_DE_AWS>:8000/docs

5. Destrucción de Recursos (Control de Costos)
Al finalizar las pruebas de desarrollo, es una buena práctica destruir los recursos en la nube para evitar consumos del Free Tier:

Bash
cd terraform
terraform destroy -auto-approve
⚠️ Posibles Puntos de Falla en Producción
Cambio de IP Pública: Al apagar y encender la EC2, AWS asignará una IP dinámica nueva. Solución productiva: Asociar una Elastic IP (IP Estática) mediante Terraform.

Crash Loops de Python: Si el código tiene un error de sintaxis o faltan dependencias en requirements.txt, el contenedor Docker fallará inmediatamente tras el arranque. Validar logs con sudo docker logs todo-api.

Falta de Permisos IAM: Si el servidor de Jenkins pierde acceso a las claves secretas o los roles de AWS, las etapas de despliegue automatizado fallarán por error de autenticación (Código de error 127/No autenticado).
