pipeline {
  agent any
  stages {
    stage('hello') {
      steps {
        def data = readFile(file: '/config/sql/test1.sql')
        println(data)
      }
    }
  }
}
