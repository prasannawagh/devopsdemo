pipeline {
  agent any
  stages {
    stage('hello') {
      steps {
         script {
            def data = readFile(file: '/config/sql/test1.sql')
            println(data)
           }
         }        
      }
    }
  }
