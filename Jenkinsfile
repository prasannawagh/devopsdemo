pipeline {
  agent { docker { image 'python:3.10.7-alpine' } }
  stages {
    stage('build') {
            steps {
                sh 'python --version'
            }
        }
    stage('readfile') {
      steps {
         script {
           println("${env.WORKSPACE}/${env.JOB_NAME}/config/sql/test1.sql")
           println("${env.WORKSPACE}/config/sql/test1.sql")
           def data = readFile(file: "${env.WORKSPACE}/config/sql/test1.sql")
           println(data)
          }
        }        
      }
    }
  }
