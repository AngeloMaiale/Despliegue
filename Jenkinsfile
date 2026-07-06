pipeline {
    agent any

    environment {
        // Tu IP pública real de AWS
        EC2_PUBLIC_IP = '32.197.217.181'
        IMAGE_NAME    = 'todo-api-fastapi'
    }

    stages {
        // Eliminamos el 'checkout scm' manual porque Jenkins ya lo hace por defecto
        stage('1. Build Docker Image') {
            steps {
                // Compila la imagen usando el Dockerfile del proyecto
                sh "docker build -t ${IMAGE_NAME}:latest ."
                echo "Imagen de Docker compilada exitosamente."
            }
        }

        stage('2. Deploy to AWS EC2') {
            steps {
                withAWS(credentials: 'aws-credentials-demo', region: 'us-east-1') {
                    echo "Conectando y desplegando en la instancia EC2: ${EC2_PUBLIC_IP}..."
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