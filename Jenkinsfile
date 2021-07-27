pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                sh 'sudo git -C /home/pi/Sources/pizzamama fetch --all'
                sh 'sudo git -C /home/pi/Sources/pizzamama reset --hard'
                sh 'sudo git -C /home/pi/Sources/pizzamama pull'
                sh 'sudo service apache2 restart'
            }
        }
    }
}
