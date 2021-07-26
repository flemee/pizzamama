pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                sh 'cd /home/pi/Sources/pizzamama'
                sh 'sudo git fetch --all'
                //sh 'sudo git branch backup-main'
                sh 'sudo git reset --hard origin/main'
                sh 'sudo service apache2 restart'
            }
        }
    }
}
