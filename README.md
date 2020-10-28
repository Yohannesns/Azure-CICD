# Overview

<TODO: complete this with an overview of your project>

## Project Plan
<TODO: Project Plan

* A link to a Trello board for the project
* A link to a spreadsheet that includes the original and final project plan>

## Instructions
  
* Architectural Diagram (Shows how key parts of the system work)>

https://app.diagrams.net/#HYohannesns%2FAzure-CICD%2Fmaster%2FArchitectural%20Diagram

Instructions for running the Python project.  
1. Create GitHub Repo
2.Launch an Azure cloud Shell environment and create ssh-keys upload these keys to your Github account
* Project cloned into Azure Cloud Shell
https://github.com/Yohannesns/Azure-CICD/blob/master/Deploy.PNG
3. Create project scaffolding Makefile, hello.py, test_hello.py, requirements.txt
* Passing tests that are displayed after running the `make all` command from the `Makefile`

* Output of a test run
https://github.com/Yohannesns/Azure-CICD/blob/master/Deploy.PNG
5. configure Github acctions
6. verfiy remote test pass (enable Github actions)
https://github.com/Yohannesns/Azure-CICD/blob/master/Deploy.PNG

7. continues delivery using azure pipelines and deploy flask code

* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).

* Running Azure App Service from Azure Pipelines automatic deployment
8. call ./make_prediction.sh
9. inspect the log file
* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
The output should look similar to this:
https://github.com/Yohannesns/Azure-CICD/blob/master/Deploy.PNG

## Enhancements

 

## Demo 

<TODO: Add link Screencast on YouTube>


