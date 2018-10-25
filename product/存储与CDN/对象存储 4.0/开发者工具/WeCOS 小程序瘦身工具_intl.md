## Feature Description
To improve smoothness of Mini Programs, WeChat only supports uploading compiled code packages with a size smaller than 1 MB. However, during development of Mini Programs, image resources often take up large space, and code packages may exceed 1 MB. WeCOS allows you to shift your focus from image resource size to logic development.

With WeCOS, image resources in Mini Programs can be automatically uploaded to COS, and then removed from the project directory with the image resource address in codes replaced by online address. As a result, the size of the code package is reduced to the allowed limit.

## Service Limits

Only applicable to COS V4. Not available in Chongqing (ap-chongqing), Seoul (ap-seoul), and Mumbai (ap-mumbai).

## Preparations
1. Sign up for a Tencent Cloud account at [Tencent Cloud official website](https://cloud.tencent.com/). For more information, please see [Sign up for Tencent Cloud](/doc/product/378/9603).
- Log in to [COS Console](https://console.cloud.tencent.com/cos4), activate COS service, and then create a bucket. For more information, please see [Create Bucket](/doc/product/436/6232).
- Download WeCOS at [GitHub address](https://github.com/tencentyun/wecos).
- Download the environment at [Node.js official website](https://nodejs.org/) and install it.

## Installation
Execute the following command to install WeCOS:
```
npm install -g wecos
```
## Basic Configuration
Create the `wecos.config.json` file under a directory at the same level as the Mini Program directory. The file configuration example and configuration items are described as follows:
```
{
  "appDir": "./app",
  "cos": {
    "secret_id": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    "secret_key": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "bucket": "wxapp-1251902136",
    "region": "ap-guangzhou", //创建bucket时选择的地域简称
    "folder": "/" //资源存放在bucket的哪个目录下
  }
}
```
| Configuration Item | Type | Description |
| ------ | ------------ | ---------------------------------------- |
| appDir | **[String]** | The directory of a Mini Program project. Default: `./app`. |
| cos | **[Object]** | Configuration information of the bucket on COS (required). Some of the information can be found in the [Console](https://console.cloud.tencent.com/cos4/secret). |
## Usage
Execute the following command under a directory at the same level as the configuration file:
```
wecos
```
> <font color="#0000cc">**Note:** </font>
 Before executing the command, you need to create the `wecos.config.json` file under a directory at the same level as the configuration file.

## Advanced Configuration
| Configuration Item | Type | Description |
| ------------------- | ------------- | --------------------------------------- |
| backupDir | **[String]** | Backup directory. Default: `./wecos_backup`. |
| uploadFileSuffix | **[Array]** | Suffix of the uploaded image. Default: .jpg	&#166;	.png	&#166;	.gif |
| uploadFileBlackList | **[Array]** | Blacklist of image resources. Default: [] |
| replaceHost | **[String]** | Replacing the specified domain name with targetHost. Default: '' |
| targetHost | **[String]** | Custom domain name is used. Default: '' |
| compress | **[Boolean]** | Whether to compress images. Default: false |
| watch | **[Boolean]** | Whether to listen to the project directory in real time. Default: true |
#### Configuring Backup Directory
WeCOS deletes the images under a project after uploading them to COS, which may result in risks of source file loss. Therefore, the backup feature is provided to back up each uploaded image to a directory at the same level as the project directory. You can modify the name of the backup directory using the following configurations. If you want to disable the feature, set the value to null:
```
  "backupDir": "./wecos_backup"
```
#### Configuring Image Suffix
You can use image suffix provided by WeCOS to define the format of images allowed to be uploaded. Images in jpg, png, and gif are supported by WeCOS by default. If you want to upload images in other formats (such as webp), add the format in the configuration item, as shown below:
```
  "uploadFileSuffix": [".jpg",".png",".gif",".webp"]
```
#### Configuring Image Blacklist
During the development, you can use WeCOS blacklist to prevent some images from being uploaded to COS. You can add either a directory or a file name to the blacklist.
```
  "uploadFileBlackList": ["./images/logo.png","./logo/"]
```
#### Custom Domain Name
If you want to use your domain name as the file link in COS, replace the default domain name with targetHost (`http://` can be omitted):
```
  "targetHost": "http://example.com"
```
If you want to change the domain name for the image link in codes, configure replaceHost targetHost.
```
  "replaceHost": "http://wx-12345678.myqcloud.com",
  "targetHost": "https://example.com"
```
#### Enabling Image Compression
Although the program package size decreases significantly with images uploaded to COS, excessive image dimension may also cause access delay, thus affecting user experience.
Apart from uploading images to the cloud, WeCOS also provides image compression based on [Tencent Cloud's Cloud Image](https://cloud.tencent.com/product/ci). On [Cloud Image Console](https://console.cloud.tencent.com/ci), create a bucket that has the same name with the bucket used to store the uploaded resource in COS, enter the bucket and enable image compression in the style page, and then the resources will be compressed before being uploaded.
```
  "compress": true
```
#### Configuring Real-time Listener
By default, WeCOS listens to project directory in real time and automatically process image resources. During the development, if you want to disable the real-time listener after one-off processing, modify the configuration by executing the following the command line, and then the listener will be disabled after one execution.
```
  "watch": false
```
## Advanced Usage
If the command line still cannot meet your demands, you can use other methods, such as customizing your modules. We also provides the direct referencing mode to satisfy your requirements. The configuration example is as follows:
```
var wecos = require('wecos');

// option is optional (String|Object)
// Enter a string to specify the configuration file path
// Pass an object to specify the configuration item
wecos([option]);

// Specify the configuration file path
wecos('./wecos-config.js');

// Specify the configuration item
wecos({
    appDir: './xxx',
    cos: {
        ...
    }
});
```
## Related Resources
- [WeCOS-UGC-DEMO](https://github.com/tencentyun/wecos-ugc-upload-demo) - Demo on Uploading Resources of Mini Programs to COS
- [COS-AUTH](https://github.com/tencentyun/cos-auth) - Demo on the COS Authentication Server

