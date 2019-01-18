
By using WeCOS, image resources in mini-app projects will be automatically uploaded to COS. In addition, WeCOS will automatically replace the address references of image resources in the codes with online addresses to remove the image resources from the project directories, which will reduce the size of mini-app packages and prevent the packages from going over the size limit. 


## Why Use WeCOS?

    
```
To make the user experience of mini-apps more fluent, compiled code packages need to be smaller than 1 MB. Code packages larger than 1 MB cannot be uploaded successfully.
```

When developing mini-apps, image resources usually take up a great deal of space, which will make it more likely for the packages to go beyond the official size limit (1 MB). In this case, you can use WeCOS so that you won't need to worry about storage occupied by image resources during development process and concentrate on your logic development.



## Preparation
* Go to [Tencent Cloud Official Site](https://cloud.tencent.com) and register an account
* Log in to [Cloud Object Storage Service (COS) Console](https://console.cloud.tencent.com/cos4), activate COS service and create Bucket
* Download the [WeCOS Tool](https://github.com/tencentyun/wecos)
* Install [Node.js](https://nodejs.org) environment



## Installation

```js
npm install -g wecos
```



## Basic Configuration
Create `wecos.config.json` file in a sibling directory as your mini-app directory

Example of the configurations in `wecos.config.json`:
```json
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

| Configuration | Type | Description |
|:-- |:-- |:-- |
| appDir | **[String]** | Default `./app`, project directory of the mini-app |
| cos | **[Object]** | (Required) configuration information of the COS to upload resources to. You can view some of the information from the [COS Console](https://console.cloud.tencent.com/cos4/secret) |


## Use

Execute the following command from the sibling directory as the configuration file 
```js 
wecos
```
Note that you need to create the `wecos.config.json` file in this directory before executing the command


## Advanced Configuration

| Configuration | Type | Description |
|:-- |:-- |:-- |
| backupDir | **[String]** | Default is `./wecos_backup`. Backup directory |
| uploadFileSuffix | **[Array]** | Default is `[".jpg", ".png", ".gif"]`. Suffix configuration for uploaded image files |
| uploadFileBlackList | **[Array]** | Default is `[]`, image resource blacklist |
| replaceHost | **[String]** | Default is `''`. Replace specified host with targetHost |
| targetHost | **[String]** | Default is `''`. Use custom domain |
| compress | **[Boolean]** | Default is `false`. Whether to enable image compression |
| watch | **[Boolean]** | Default is `true`. Whether to enable project directory real-time listening |

</br>
#### Configure Backup Directory

When running, WeCOS will automatically upload images under projects onto COS, then delete them, so it is possible to lose the source files. We provide source file backup feature, each time an image is uploaded, it will be backed up in a certain sibling directory of the project

To make it more convenient, you can change the name of the backup directory by modifying the following configuration. Leave the value empty if you do not wish to use this feature
```json
  "backupDir": "./wecos_backup"
```

#### Configure Image File Suffix

Sometimes we need to restrict the format of uploaded images (for example, only allow `jpg` format). You can define this restriction by using image file suffix configuration provided by WeCOS

WeCOS supports three formats `jpg, png, gif` by default. You can add other formats to this configuration if necessary (such as webp)

```json
  "uploadFileSuffix": [".jpg",".png",".gif",".webp"]
```

#### Configure Image Blacklist

During development, there can be certain images which we do not wish to be uploaded. You can use the blacklist configuration of WeCOS to solve this problem. Once configured, the program will automatically ignore these images when uploading

You can either configure directories or enter specific file names for the blacklist configuration
```json
  "uploadFileBlackList": ["./images/logo.png","./logo/"]
```

#### Custom Domain

If you wish to use custom domain in COS file links, you can configure targetHost to replace the default domain. (`http://` can be omitted):

```json
  "targetHost": "http://example.com"
```

If you want to change the domain for the image link in the codes, you can configure replaceHost targetHost.

```json
  "replaceHost": "http://wx-12345678.myqcloud.com",
  "targetHost": "https://example.com"
```

#### Enable Image Compression

Uploading images onto COS will reduce the size of app packages, but this will also reduce access speed if the images are too large, which will in turn affect user experience

In addition to uploading images to the cloud, WeCOS also provides image compression feature which is base on [Tencent Cloud Image](https://cloud.tencent.com/product/ci).

First, you need to create a bucket with the same name that of COS in the [Cloud Image Console](https://console.cloud.tencent.com/ci)

Next, enable this option, after which the resources will be uploaded after being compressed (Note: Compression may not reduce the size of certain images that are already small enough)

```json
  "compress": true
```

#### Configure Real-time Listening

WeCOS listens to the changes of project directories in real-time and automatically processes the image resources by default. During development, if you find this feature inconvenient, or you only need to process the resources once, you may modify this configuration to exit the app after one execution
```json
  "watch": false
```


## Advanced Use
Apart from the execution method by using command lines mentioned above, if you wish to use other methods (for example, customizing your own modules), we also provide direct reference to satisfy your personalization demands

```js
var wecos = require('wecos');

/**
* option, optional [String|Object]
* Pass String, specify the path of configuration file
* Pass Object, specify configuration item
*/
wecos([option]);

//Specify the path of configuration file
wecos('./wecos-config.js');

//Specify configuration item
wecos({
	appDir: './xxx',
	cos: {
		...
	}
});

```


## Relevant Resource

* [WeCOS-UGC-DEMO](https://github.com/tencentyun/wecos-ugc-upload-demo)--DEMO: Uploading resources to COS for mini-app user

* [COS-AUTH](https://github.com/tencentyun/cos-auth)--DEMO: COS authentication server








