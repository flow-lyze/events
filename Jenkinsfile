pipeline {
    agent any
    options { timeout(time: 1, unit: "HOURS") }
    environment {
        DOCKERHUB_CREDENTIALS = credentials("hpprediction-dockerhub")
    }
    stages {
        stage("Clean Up") {
            steps {
                deleteDir()
            }
        }
        stage("Clone Repository") {
            steps {
                echo "Cloning repository..."
                sh "git clone https://github.com/flow-lyze/events.git"
            }
        }
        stage("Build and Test") {
            steps {
                // dir will set directory where we'll working lately
                // dir definition is spread among other stages (all of them will operate in this dir)
                echo "================== building image =================="
                dir("events") {
                    sh "docker build -t hpprediction/event-service:latest ."
                }
            }
        }
        stage("Login") {
            steps {
                echo "================== docker authorization =================="
                sh "echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin"
            }
        }
        stage("Push") {
            steps {
                echo "================== docker pushing =================="
                sh "docker push hpprediction/event-service:latest"
            }
        }
    }
    post {
        always {
            echo "================== docker logout =================="
            sh "docker logout"
        }
    }
}