pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                sh '/home/pi/Sources/pizzamama'
                sh 'git pull'
            }
        }
    }
}
