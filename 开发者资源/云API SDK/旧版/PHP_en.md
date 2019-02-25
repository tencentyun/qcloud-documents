We provide PHP based SDK to make it easy for developers to debug and access Cloud API.

Download from: https://github.com/QcloudApi/qcloudapi-sdk-php

The qcloudapi-sdk-php SDK is designed to make it easy for PHP developers to use Tencent Cloud API in their codes.


## 1. Resources
For details, refer to API common parameters, overview and error codes in different modules. For instance, [CVM API Common Parameters](http://cloud.tencent.com/document/api/213/6976), [CVM API Overview](http://cloud.tencent.com/doc/api/229/API%E6%A6%82%E8%A7%88) and [CVM API Error Codes](http://cloud.tencent.com/doc/api/229/%E9%94%99%E8%AF%AF%E7%A0%81).

## 2. Quick Start
1) [Get Security Credential](https://console.cloud.tencent.com/capi). Before calling the Cloud API for the first time, you need to apply for a security credential on the Tencent Cloud console. A security credential consists of a SecretId, which is used to identify an API caller, and a SecretKey, which is used to encrypt the signature string and verify the string on the server. You must keep your SecretKey strictly confidential to avoid disclosure.

2) [Download SDK](https://github.com/QcloudApi/qcloudapi-sdk-php), and put it in your program directory. For details, refer to the example below.

## 3. Example

```
<?php
require_once './src/QcloudApi/QcloudApi.php';

$config = array('SecretId'       => 'Your secretId',
                'SecretKey'      => 'Your secretKey',
                'RequestMethod'  => 'GET',
                'DefaultRegion'  => 'Region parameter');

// The first parameter indicates the domain in use
// List of existing modules:
// QcloudApi::MODULE_CVM      corresponds to   cvm.api.qcloud.com
// QcloudApi::MODULE_CDB      corresponds to   cdb.api.qcloud.com
// QcloudApi::MODULE_LB       corresponds to   lb.api.qcloud.com
// QcloudApi::MODULE_TRADE    corresponds to   trade.api.qcloud.com
// QcloudApi::MODULE_SEC      corresponds to   csec.api.qcloud.com
// QcloudApi::MODULE_IMAGE    corresponds to   image.api.qcloud.com
// QcloudApi::MODULE_MONITOR  corresponds to   monitor.api.qcloud.com
// QcloudApi::MODULE_CDN      corresponds to   cdn.api.qcloud.com
// QcloudApi::MODULE_WENZHI corresponds to   wenzhi.api.qcloud.com
$service = QcloudApi::load(QcloudApi::MODULE_CVM, $config);

// Request parameter. Please refer to the description of corresponding API in the product documentation
$package = array('offset' => 0,
                 'limit' => 3,
                 // 'Region' => 'gz' // If the Region value is not the same as the configured DefaultRegion one, you can re-specify the requested Region
                );


// You can reset the requested secretID/secretKey/region/method parameter using the following four methods before making a request
// Reset secretId
$secretId = 'Your secretId';
$service->setConfigSecretId($secretId);
// Reset secretKey
$secretKey = 'Your secretKey';
$service->setConfigSecretKey($secretKey);
// Reset region
$region = 'sh';
$service->setConfigDefaultRegion($region);
// Reset method
$method = 'POST';
$service->setConfigRequestMethod($method);

// The request method corresponds to the API name. Please refer to the API name of the corresponding API in the product documentation
$a = $service->DescribeInstances($package);

// Generate the requested URL, but not initiate the request
$a = $service->generateUrl('DescribeInstances', $package);

if ($a === false) {
    // Request failed, error while parsing information
    $error = $service->getError();
    echo "Error code:" . $error->getCode() . ' message:' . $error->getMessage();

    // The following method can be used to obtain the execution information of an asynchronous task API
    $detail = $error->getExt();
} else {
    // Request succeeded
    var_dump($a);
}
```
