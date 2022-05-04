pipeline {
    agent any
    options { timeout(time: 1, unit: "HOURS") }
    environment {
        DOCKERHUB_CREDENTIALS = credentials("hpprediction-dockerhub")
        GITHUB_URL = "https://github.com/flow-lyze/events.git"

        IMAGE_NAME = "hpprediction/event-service"
        IMAGE_TAG = "1.0.0"
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
                sh "git clone ${GITHUB_URL}"
            }
        }
        stage("Build and Test") {
            steps {
                // dir will set directory where we'll working lately
                // dir definition is spread among other stages (all of them will operate in this dir)
                echo "================== building image =================="
                dir("events") {
                    sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
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
                sh "docker push  ${IMAGE_NAME}:${IMAGE_TAG}"
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