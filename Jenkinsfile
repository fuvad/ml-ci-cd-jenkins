pipeline {
    agent any
    
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/fuvad/ml-ci-cd-jenkins.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r reequirements.txt'
            }
        }

        stage('Train Model') {
            steps {
                bat 'python train.py'
            }
        }

        stage('Test Model') {
            steps {
                bat 'python test_model.py'
            }
        }

        stage('Deploy Model') {
            when {
                expression { currentBuild.result == null || currentBuild.result == 'SUCCESS'}
            }
            steps {
                echo 'Model passed all tests. Deploying model...'
                bat 'python deploy.py'
            }
        }
    }
}

