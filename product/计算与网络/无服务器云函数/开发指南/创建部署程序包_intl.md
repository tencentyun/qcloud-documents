A deployment package is a zip file into which all codes and dependencies that are running in the SCF platform are compressed. You need to specify a deployment package when creating a function. You can create a deployment package in local environment and upload it to the SCF platform, or write code directly in the SCF console, so that the console can create and upload a package for you. Determine whether you can use the console to create a deployment package according to the following conditions:

- Simple scenario: If standard Python library and SDK library (such as COS and SCF) provided by Tencent Cloud are required to write custom code and when there is only one .py file, you can use the inline editor of the SCF console. The console can automatically compress the code and relevant configuration information into an executable deployment package.
- Advanced scenario: If other resources (such as graphic database for graphic processing, Web framework for Web programming) are required to write code, you need to create a function deployment package in local environment, and upload the package through the console.

The following example shows how to create a deployment package in local environment.

```
Notes:
1. Generally, the dependent library installed locally can run well in the SCF platform. However, the installed binary file may be incompatible in a few scenarios. If such a problem is found, please [contact us](https://cloud.tencent.com/document/product/583/9712).
2. In the example for Python, libraries and dependencies are installed using pip in local environment, so make sure that you have installed Python and pip locally.
```

## Creating a Python Deployment Package in Linux

1) Create a directory:

```
mkdir /data/my-first-scf
```

2) Store all Python source files (.py files) required to create this function into this directory. For more information on how to create a function, please see the section [Getting Started - Create DownloadImage Function](https://cloud.tencent.com/document/product/583/9211).

3) Install all dependencies in this directory using pip:

```
pip install <module-name> -t /data/my-first-scf
```

For example, you can install Pillow library in my-first-scf directory by executing the following command:

```
pip install Pillow -t /data/my-first-scf
```

4) Under my-first-scf directory, compress all the files. Note: What you need to compress is the content in the directory instead of the directory:

```
zip my_first_scf.zip /data/my-first-scf/*
```

```
Notes:
1. For libraries needing compilation, it is recommended to compress the files in CentOS 7 on which SCFs run.
2. If you have other requirements on software, compilation environment, or development library during the installation or compilation process, follow the installation prompts.
```

## Creating a Python Deployment Package in Windows

We recommend that you compress the dependencies and codes that run successfully in Linux environment into a zip file as the function execution code. For more information, please see [Practical Operation of Code - Obtain Images on COS and Create Thumbnails](https://cloud.tencent.com/document/product/583/9736).

For Windows, you can also use the `pip install <module-name> -t <code-store-path>` command to install the Python library. But for packages that need to be compiled or carry static and dynamic libraries, only libraries completely implemented in Python can be installed in Windows, because libraries compiled in Windows cannot be invoked to run in SCF's running environment (CentOS 7).

