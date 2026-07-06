pipeline {
    agent any

    environment {
        // Reemplaza esto con la IP pública real que te dio tu 'terraform apply'
        EC2_PUBLIC_IP = '32.197.217.181'
        // El nombre que le daremos a tu imagen de Docker
        IMAGE_NAME    = 'todo-api-fastapi'
    }

    stages {
        stage('1. Checkout Code') {
            steps {
                // Descarga el código limpio del repositorio
                checkout scm
                echo "Código descargado con éxito de GitHub."
            }
        }

        stage('2. Build Docker Image') {
            steps {
                // Compila la imagen usando el Dockerfile de tu proyecto
                sh "docker build -t ${IMAGE_NAME}:latest ."
                echo "Imagen de Docker compilada exitosamente."
            }
        }

        stage('3. Deploy to AWS EC2') {
            steps {
                // Usamos las credenciales de AWS que guardamos en Jenkins
                withAWS(credentials: 'aws-credentials-demo', region: 'us-east-1') {
                    echo "Conectando y desplegando en la instancia EC2: ${EC2_PUBLIC_IP}..."
                    
                    // Nota: En una demo real, aquí enviaríamos la imagen a un registro como Docker Hub o AWS ECR,
                    // o nos conectaríamos por SSH para levantar el contenedor. 
                    // Para esta primera prueba de flujo, simularemos el empuje exitoso al servidor.
                    echo "Despliegue simulado correctamente en http://${EC2_PUBLIC_IP}:8000"
                }
            }
        }
    }
    
    post {
        success {
            echo "¡Pipeline ejecutado con éxito total! Tu API está automatizada."
        }
        failure {
            echo "Algo falló en el Pipeline. Revisa los logs de Jenkins."
        }
    }
}