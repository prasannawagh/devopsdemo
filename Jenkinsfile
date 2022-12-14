pipeline {
  agent any
  stages {
    stage('hello') {
      steps {
         script {
           println('${env.WORKSPACE}/${env.JOB_NAME}/config/sql/test1.sql')
            def data = readFile(file: '${env.WORKSPACE}/config/sql/test1.sql')
            println(data)
           }
         }        
      }
    }
  }
