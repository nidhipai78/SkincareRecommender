pipeline {

agent any

environment {
    DOCKER_IMAGE = "nidhinpai/skincarerecommender:1.0"
}

stages {

    stage('Build Docker Image') {
        steps {
            bat 'docker build -t %DOCKER_IMAGE% .'
        }
    }

    stage('Validate Docker Compose') {
        steps {
            bat 'docker compose config'
        }
    }

    stage('Push Image to Docker Hub') {
    steps {
        bat 'docker push nidhinpai/skincarerecommender:1.0'
    }
}

    stage('Deploy') {
        steps {
            bat 'docker compose pull'
            bat 'docker compose down'
            bat 'docker compose up -d'
        }
    }
}

}