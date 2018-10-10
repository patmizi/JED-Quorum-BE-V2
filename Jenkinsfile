pipeline {
    agent{
        docker {
            image 'python:3.6.6'
            args '-u root:sudo'
        }
    }
    environment {
        AWS_ACCESS_KEY        = credentials('aws-access-key')
        AWS_SECRET_ACCESS_KEY = credentials('aws-secret-access-key')
    }
    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install awscli'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Set Up Credentials') {
            steps {
                withCredentials([file(credentialsId:'jed-be-connection-config', variable: 'CONNECTION_STRING')]) {

                }
                sh 'echo $CONNECTION_STRING >> ./chalicelib/connection/config.py'
                sh 'aws configure set aws_access_key_id ${AWS_ACCESS_KEY}'
                sh 'aws configure set aws_secret_access_key ${AWS_SECRET_ACCESS_KEY}'
                sh 'aws configure set region ap-southeast-2'
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