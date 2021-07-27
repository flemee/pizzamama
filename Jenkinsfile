pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                sh 'cd /home/pi/Sources/pizzamama'
                sh 'pwd'
                sh 'sudo git fetch --all'
                //sh 'sudo git branch backup-main'
                sh 'sudo git reset --hard'
                sh 'pwd'
                sh 'sudo git pull'
                sh 'pwd'
                sh 'sudo service apache2 restart'
            }
        }
    }
}
