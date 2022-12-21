pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'python3 --version'
        sh 'pip --version'
        sh 'pip show pandas'
      }
    }
    stage('readfile') {
      steps {
         script {
           println("${env.WORKSPACE}/${env.JOB_NAME}/config/sql/test1.sql")
           println("${env.WORKSPACE}/config/sql/test1.sql")
           def data = readFile(file: "${env.WORKSPACE}/config/sql/test1.sql")
           println(data)
           sh 'python3 hello.py'
         }
      }       
    }
    stage('transform') {
      steps {
        script {
          sh 'python3 transform_pp_custom.py "1.15" "version_komodo"'
        }
      }        
    }
  }
  post { 
      always { 
          cleanWs()
      }
  }
}
