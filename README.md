# Deploy a Python (Django) web app container to Azure App Service (in progress)

This Python web app is a restaurant review application using the [Django](https://www.djangoproject.com/) framework. The app is intended to be used as a container running on Azure App Service with a connection to an Azure Cosmos DB API for MongoDB. 

Following the tutorial [TBD: coming soon](TBD), you can deploy this web app Azure, hosted in a fully managed Azure App Service. Azure managed identity enables the App Service to pull container images from an Azure Container Registry. MongoDB connection info is passed to the code through environment variables. 

If you need an Azure account, you can [create on for free](https://azure.microsoft.com/free/).

A Flask sample application with similar functionality is at [Flask Container Web App](https://github.com/Azure-Samples/msdocs-python-flask-container-web-app).

## Run and deploy options

Here are some ways you can run the sample web app in this repository.

| Scenario | As-is repo code        | Containerized app |
| ----------- | ----------- | ----------|
| Local environment | Run repo code in virtual environment with *requirements.txt*. Set environment variables in shell before running. | Build image from repo and run locally in Docker container. Pass environment variables in Docker CLI command or with VS Code task definition <sup>1<sup>. |
| Azure App Service [Web App for Containers](https://azure.microsoft.com/services/app-service/containers/) | Deploy repo code to App service. Set environment variables as App Service configuration settings. See note about subpath. <sup>2</sup> | Build image locally or in Azure and push to container registry like Azure Container Registry. Configure App Service to pull from registry. Set environment variables as App Service configuration settings. |
| [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/overview) | *n/a* |  Build image locally or in Azure and push to container registry like Azure Container Registry. Create a Container App with deployment from the registry. Configure environment variables for the container. |

(1) The *.vscode* directory *settings.json* and *tasks.json* are configured either for a MongoDB local connection or an Azure Cosmos DB connection. The tasks and templates in *.vscode* are only used when using Visual Studio Code locally.

(2) This app was designed to be containerized and run on App Service. If you want to deploy to App Service without containerizing it, then be sure to set the *subpath* to the *azureporject* folder, which contains the *manage.py* file. Do that by:

* In VS Code: **F1** or **CTRL** + **SHIFT** + **P** to open the command palette.
* Type "Preferences: Open Workspace Settings" and select to open.
* In the Settings search field, enter "@id:appService.deploySubpath appser".
* Set the subpath as "azureproject".


## Environment variables

The sample code requires the following environment variables passed in as described in the scenario table above.

```
CONNECTION_STRING=<connection-string>
DB_NAME=restaurants_reviews
COLLECTION_NAME=restaurants_reviews
```

For a local MongoDB instance, the connection string is of the form `mongodb://127.0.0.1:27017`. An Azure Cosmos DB API for MongoDB connections string is of the form `mongodb://<server-name>:<password>@<server-name>.mongo.cosmos.azure.com:10255/?ssl=true&<other-parameters>`.

## Requirements

The [requirements.txt](./requirements.txt) has the following packages:

| Package | Description |
| ------- | ----------- |
| [Django](https://pypi.org/project/Django/) | Web application framework. |
| [gunicorn](https://pypi.org/project/gunicorn/) | Gunicorn ‘Green Unicorn’ is a Python WSGI HTTP Server for UNIX. |
| [pymongo](https://pypi.org/project/pymongo/) | The PyMongo distribution contains tools for interacting with MongoDB database from Python. |
| [requests](https://pypi.org/project/requests/) | An HTTP library |
| [whitenoise](https://pypi.org/project/whitenoise/) | Static file serving for WSGI applications, used in the deployed app. <br><br> This package is used in the [azureproject/settings.py](./azureproject/azureproject/settings.py) file. |

