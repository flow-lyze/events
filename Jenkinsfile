pipeline {
    agent any
    options { timeout(time: 1, unit: "HOURS") }
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
        stage("Build") {
            steps {
                // dir will set directory where we'll working lately
                // dir definition is spread among other stages (all of them will operate in this dir)
                echo "================== building image =================="
                dir("events") {
                    sh "docker build ."
                }
            }
        }
        stage("Test") {
            steps {
                echo "Testing Code"
                sh "docker images"
            }
        }
    }
}