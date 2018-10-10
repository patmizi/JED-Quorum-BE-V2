pipeline {
    agent{
        docker { image 'python:3.6.6' }
    }
    environment {
        CONNECTION_CONFIG     = credentials('jed-be-connection-config')
        AWS_ACCESS_KEY        = credentials('aws-access-key')
        AWS_SECRET_ACCESS_KEY = credentials('aws-secret-access-key')
    }
    stages {
        stage('Install Dependencies') {
            steps {
                sh 'echo $(ls)'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Set Up Credentials') {
            steps {
                sh 'cat ${env.CONNECTION_CONFIG} >> ./chalicelib/connection/config.py'
                sh 'aws configure set aws_access_key_id ${env.AWS_ACCESS_KEY}'
                sh 'aws configure set aws_secret_access_key ${env.AWS_SECRET_ACCESS_KEY}'
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