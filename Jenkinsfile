pipeline {
    agent { 
        node {
            label 'docker-agent-flask'
            }
      }
    triggers {
        pollSCM '* * * * *'
    }
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                cd send_location
                pip3 install -r requirement.txt
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                // sh '''
                // cd myapp
                // python3 hello.py
                // python3 hello.py --name=Brad
                // '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                // sh '''
                // echo "doing delivery stuff.."
                // '''
            }
        }
    }
}
