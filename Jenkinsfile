pipeline {
    agent { 
        node {
            label 'docker-agent-location'
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
