pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                sh 'cd /home/pi/Sources/pizzamama'
                sh 'sudo git fetch --all'
                sh 'sudo git pull'
                sh 'sudo service apache2 restart'
            }
        }
    }
}
