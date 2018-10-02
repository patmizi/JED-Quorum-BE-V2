pipeline {
    agent {
        image: 'python:3.6.6-slim-stretch',
        label: 'python-slave',
        // args: '' //TODO: We attach configuration file as a volume to the container so that we have a portable container and we don't need to maintain an image
    }
    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
                // copy configuration to /chalicelib/connection/config.py
                // TODO: configure AWS credentials using credential binding block
            }
        }
        stage('Test') {
            steps {
                sh 'python --version'
                sh 'pip --version'
                sh './test.sh'
            }
        }
        stage('Build and Deploy') {
            steps {
                sh 'source ./environment/prod_setup.sh'
                sh 'chalice deploy'
            }
        }
    }
}