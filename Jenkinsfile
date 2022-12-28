pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'python3 --version'
        sh 'pip3 --version'
        sh 'pip3 show pandas'
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
//     stage('upload_to_s3') {
//       steps {
//         script {
//           s3Upload consoleLogLevel: 'INFO', dontSetBuildResultOnFailure: false, dontWaitForConcurrentBuildCompletion: false, entries: [
//             [bucket: 'devops-bucket-demo/jenkins_test_1', excludedFile: '**/mapping/master/*.*', flatten: false, gzipFiles: false, keepForever: false, managedArtifacts: false, noUploadOnFailure: false, selectedRegion: 'us-east-1', showDirectlyInBrowser: false, sourceFile: '**/*.*', storageClass: 'STANDARD', uploadFromSlave: false, useServerSideEncryption: false]
//           ], pluginFailureResultConstraint: 'FAILURE', profileName: 'S3_jenkins_profile', userMetadata: []
//         }
//       }
//     }
  }
  post {
    always {
      cleanWs()
    }
  }
}
