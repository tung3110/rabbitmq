	pipeline {
		 agent any
		 environment { 
			  registry = "tung3110/apiHello" 
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
			 
		 }
		 
	}