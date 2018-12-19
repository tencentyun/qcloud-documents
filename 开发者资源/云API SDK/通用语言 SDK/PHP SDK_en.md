
## Overview
Welcome to Tencent Cloud Software Development Kit (SDK). To help PHP developers debug and connect to the Tencent Cloud product API, here we introduce the Tencent Cloud SDK suitable for PHP, and provide a simple example of getting started with the SDK. Then, you can quickly get the Tencent Cloud PHP SDK and start calling.

## Supported Environment
1. Supported environment: PHP 5.3.0 or above
2. Activate the corresponding product on [Tencent Cloud Console](https://console.cloud.tencent.com).
3. [Get SecretID, SecretKey](https://console.cloud.tencent.com/capi) and the URL for calling (endpoint). The general form of endpoint is `*.api.qcloud.com`, for example, the endpoint for CVM is `cvm.api.qcloud.com`. For more information, please see product descriptions.
4. Download the relevant information and configure the relevant files.

## Installation
Before installing PHP SDK, you should obtain the security credential first. Before calling the Cloud API for the first time, you need to apply for a security credential on the Tencent Cloud console. A security credential consists of a SecretID, which is used to identify an API caller, and a SecretKey, which is used to encrypt the signature string and the key used to verify the signature string on the server end. You must keep your SecretKey strictly confidential to avoid disclosure.

### Obtaining Source Code via GitHub for Installation
Click on the GitHub address of PHP SDK provided by Tencent Cloud. [Get GitHub resources >>](https://github.com/QcloudApi/qcloudapi-sdk-php).
1. Download source code from the github address of `qcloudapi-sdk-php`
2. Extract the source code to the proper location of your project
3. You can refer to Demo.java example and reference source code for configuration

### Installing via Composer
Installing via Composer is recommended for PHP SDK. Composer is the dependency management tool of PHP, which supports the dependencies required by your project and installs them into your project. For more information on Composer, please see [Composer official website](http://www.phpcomposer.com/).
1. Install Composer
```
curl -sS https://getcomposer.org/installer | PHP
```
2. Add a line to the structure "require" of composer.json:
```
"tencentyun-api/qcloudapi-sdk-php": "dev-master":
```
3. Run composer install to download and install the PHP SDK
4. You can refer to Demo.php example and reference source code for configuration

## Quick Start Demo
Take CVM's "Create" (RunInstances) and "Query" (DescribeInstances) as examples:
```
<?php
error_reporting(E_ALL ^ E_NOTICE);
require_once './src/QcloudApi/QcloudApi.php';
$config = array('SecretId' => 'Your secretId',
'SecretKey' => 'Your secretKey',
'RequestMethod' => 'GET',
'DefaultRegion' => 'gz');
$cvm = QcloudApi::load(QcloudApi::MODULE_CVM, $config);
$package = array('offset' => 0, 'limit' => 3, 'SignatureMethod' =>'HmacSHA256');
$a = $cvm->DescribeInstances($package);
// $a = $cvm->generateUrl('DescribeInstances', $package);
if ($a === false) {
$error = $cvm->getError();
echo "Error code:" . $error->getCode() . ".\n";
echo "message:" . $error->getMessage() . ".\n";
echo "ext:" . var_export($error->getExt(), true) . ".\n";
} else {
var_dump($a);
}
echo "\nRequest :" . $cvm->getLastRequest();
echo "\nResponse :" . $cvm->getLastResponse();
echo "\n";

```

