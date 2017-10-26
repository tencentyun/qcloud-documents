## Configuration Item Overview
### What is Configuration Item

Configuration is used to specify the read-in settings of some programs when they start. You can apply different configurations to different objects.

Configuration item is a collection of multiple configurations. The value of configuration item can be a string or a file.
Configuration item supports YAML format and visual editing. Click to view [YAML Syntax](https://zh.wikipedia.org/wiki/YAML).
Configuration item supports only new versions instead of modified versions.

### Benefits of Configuration Item

1. Configuration item feature can help you manage configurations of different businesses under different environments. It supports multiple versions and YAML format.
2. Configuration item enables you to configure different environments for the same application. It supports multiple versions, which allows you to update and roll back application.
3. With this feature, you can quickly import your configurations into the container in the form of files.

## How to Use and Work With Configuration Item
### Creation of Configuration File

1. Go to configuration file list page, and click "New"
2. Enter basic information and the content of configuration file. YAML format and visual editing are supported.
3. Step 2: Set a mount path for the volume in the container configuration.
![Alt text](https://mc.qcloudimg.com/static/img/608b0501fdc822a00cf0e57142beaafc/%7B4D979ED1-07C6-421C-9364-93CEC4082E44%7D.png)
![Alt text](https://mc.qcloudimg.com/static/img/dde52abbf61fccb9b5b0c2249e6b2692/%7BABDEC50C-9DF0-4CF8-84A6-5652DF87D38A%7D.png)

### Revised Version of Configuration File

1. Click configuration file ID to go to configuration file details page.
2. Select one of the versions and click "Generate New Version". A new version is generated based on the revision of this version.
![Alt text](https://mc.qcloudimg.com/static/img/780f58ee32be0c6a97cd0c94cca459c0/%7B69848654-B721-4460-A6CA-600B20FE361C%7D.png)

### Deletion of Configuration File
1. You can delete a specified version in configuration file details page
2. You can delete a configuration file in configuration file list page and delete all versions under this file

## Usage of Configuration File
Method 1:  Mount the configurations in the configuration file to a container in the form of data volume. [View details](https://cloud.tencent.com/document/product/457/11034)
Method 2:  Deploy multiple environments using configuration file and application template. [View details](https://cloud.tencent.com/document/product/457/11033)
Method 3:  When you create a service, import configurations to environment variable using configuration file. [View details](https://cloud.tencent.com/document/product/457/11034)





