
pipeline {

    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t skincare-recommender .'
            }
        }

        stage('Validate Docker Compose') {
            steps {
                bat 'docker compose config'
            }
        }

    }
}