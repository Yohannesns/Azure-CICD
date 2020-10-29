# Overview

This project demonstrate how to deploy a pre-trained Sklearn model machine learning application on
microsoft azure by implemanting CICD using Github, GitHub acctions and azure pipeline.

## Project Plan
the preoject is diveded in to a quarterly and weekly deliverbles. Excell is used for time management and
a trello board for task tracking

* A link to a Trello board for the project
   https://trello.com/b/uhZ6GdYt/azure-devops-ml-app
* A link to a spreadsheet that includes the original and final project plan>

https://github.com/Yohannesns/Azure-CICD/blob/master/project-management-template.xlsx

## Instructions
  
* Architectural Diagram (Shows how key parts of the system work)>

https://app.diagrams.net/#HYohannesns%2FAzure-CICD%2Fmaster%2FArchitectural%20Diagram

Instructions for running the Python project.  
1. Create GitHub Repo
2.Launch an Azure cloud Shell environment and create ssh-keys upload these keys to your Github account
  ** on azure cloude shell Create your SSH keys with the ssh-keygen 
 ** git clone <your git repo>
** python3 -m venv ~/.flask-ml-azure
** source ~/.flask-ml-azure/bin/activate
* Project cloned into Azure Cloud Shell
https://github.com/Yohannesns/Azure-CICD/blob/master/RepoCloneWithAzure.PNG
3. Create project scaffolding Makefile, hello.py, test_hello.py, requirements.txt
  navigate to project directory edit permition  Chmod +x <directory> then run make all
* Passing tests that are displayed after running the `make all` command from the `Makefile`
https://github.com/Yohannesns/Azure-CICD/blob/master/Make.PNG

* Output of a test run
https://github.com/Yohannesns/Azure-CICD/blob/master/Make.PNG
5. configure Github acctions
6. verfiy remote test pass (enable Github actions)
https://github.com/Yohannesns/Azure-CICD/blob/master/GithubActions.PNG

7. continues delivery using azure pipelines and deploy flask code
 az webapp up --SKU F1 -n <appname>
https://github.com/Yohannesns/Azure-CICD/blob/master/Deploy.PNG
  
* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).

* Running Azure App Service from Azure Pipelines automatic deployment
8. call ./make_prediction.sh
9. inspect the log file
* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
The output should look similar to this:
https://github.com/Yohannesns/Azure-CICD/blob/master/predict.PNG

## Enhancements

 The project can be improved by using other frameworks and machine learning model.

## Demo 

https://youtu.be/fMg-tjzJ1GQ


