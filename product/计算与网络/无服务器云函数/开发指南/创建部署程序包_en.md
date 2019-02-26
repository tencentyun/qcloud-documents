Deployment package is a zip file into which all codes and dependencies that are running in SCF platform are compressed. You need to specify a deployment package when creating a function. You can create a deployment package in local environment and upload it to SCF platform, or write code directly in SCF console, so that the console can create and upload a package for you. Determine whether you can use the console to create a deployment package according to the following conditions:

- Simple scenario: If standard Python library and SDK library (such as COS, SCF, etc.) provided by Tencent Cloud are required to write custom code and when there is only one .py file, you can use the inline editor of SCF console. The console can automatically compress the code and relevant configuration information into a deployment package that is able to run.
- Advanced scenario: If other resources (such as graphic database for graphic processing, Web framework for Web programming, etc.) are required to write code, you need to create a function deployment package in local environment, and upload the package through the console.

The following example shows how to create deployment package in local environment.
```
Note:
1. Generally, the dependent library installed locally can run well in SCF platform. However, in few scenarios where the installed binary file may be incompatible. If such a problem is found, please [contact us](https://cloud.tencent.com/document/product/583/9712).
2. In the example, dependencies are installed using pip in local environment, so please make sure that you have installed Python and pip locally.
```
## Creating Deployment Package in Linux
1) Create a directory:
```
mkdir /data/my-first-scf
```
2) Store all Python source files (.py files) required to create this function into this directory. For more information on how to create a function, please see the section [Getting Started - Create DownloadImage Function](https://cloud.tencent.com/document/product/583/9211).

3) Install all dependencies in this directory using pip:

```
pip install <module-name> -t /data/my-first-scf
```
For example, you can install PIL library in my-first-scf directory by executing the following command:
```
pip install Pillow -t /data/my-first-scf
```

4) Under my-first-scf directory, compress all the files. Note: What you need to compress is the content in the directory instead of the directory:
```
zip my_first_scf.zip /data/my-first-scf/*
```

## Creating Deployment Package in Windows
We recommend that you compress the dependencies and codes that run successfully under Linux environment into a zip file as the function execution code. For more information, please see [Practical Operation of Code - Acquire Image on COS and Create a Thumbnail](https://cloud.tencent.com/document/product/583/9736)


