pipeline {
  agent any
  stages {
    stage('intall python') {
      agent {
        docker {
          image 'python:alpine3.17'
        }
      }
      steps {
        sh 'python3 --version'
      }
    }
    stage('version') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('hello') {
      steps {
        sh 'python3 hello.py'
      }
    }
  }
}
