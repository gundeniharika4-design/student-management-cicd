pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building Student Management System'
            }
        }

        stage('Test') {
            steps {
                bat '"C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pytest test_app.py -v'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Student Management System deployment completed'
            }
        }
    }
}
