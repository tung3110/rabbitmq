	pipeline {
		 agent any
		 environment { 
			  registry = "tungnh2022/apihello" 
			  registryCredential = 'dockerhub_id' 
			  dockerImage = '' 
		 }
		 stages {
			 stage('Cloning Git') {
				 steps {
					 git branch: 'develop', url: 'https://github.com/tung3110/apiHello.git'
				 }
			 }
			 stage('Building image') { 
			  steps { 
				  script { 
					  dockerImage = docker.build registry + ":latest" 
				  }
			  } 
			 }
			 stage('Deploy image') { 
				  steps { 
					  script { 
						  docker.withRegistry( '', registryCredential ) { 
							  dockerImage.push() 
						  }
					  } 
				  }
			 } 
			 stage('Cleaning up') { 
				  steps { 
					  sh "docker rmi $registry:latest" 
				  }
			 }
			 stage('Setting the variables values') {
				steps {
					 sh '''#!/bin/bash
							 sudo bash apijenkins.sh
					 '''
				}
			 }
		 }
		 
	}