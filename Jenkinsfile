pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                sh 'sudo cd /home/pi/Sources/pizzamama'
                sh 'sudo git pull'
                sh 'sudo service apache2 restart'
            }
        }
    }
}
