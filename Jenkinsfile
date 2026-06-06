pipeline {

agent any

environment {
    DOCKER_IMAGE = "nidhinpai/skincare-recommender:1.0"
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
            withCredentials([usernamePassword(
                credentialsId: 'dockerhub',
                usernameVariable: 'DOCKER_USER',
                passwordVariable: 'DOCKER_PASS'
            )]) {

                bat 'echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin'
                bat 'docker push %DOCKER_IMAGE%'
            }
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