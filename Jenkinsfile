pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                sh 'cd /home/pi/Sources/pizzamama'
                sh 'git pull'
                sh 'sudo service apache2 restart'
            }
        }
    }
}
