
## Overview
Welcome to Tencent Cloud Software Development Kit (SDK). To help Node.js developers debug and connect to the Tencent Cloud product API, here we introduce the Tencent Cloud development kit suitable for Node.js, and provide a simple example of getting started with the development kit. Then, you can quickly get the Tencent Cloud Node.js SDK and start calling.

## Supported Environment
1. Activate the corresponding product on [Tencent Cloud Console](https://console.cloud.tencent.com).
2. [Get SecretID and SecretKey](https://console.cloud.tencent.com/capi). For more information, please see product descriptions.
3. Download the relevant information and configure the relevant files.

## Installation
Before installing Node.js SDK, you should obtain the security credential first. Before calling the Cloud API for the first time, you need to apply for a security credential on the Tencent Cloud console. A security credential consists of a SecretID, which is used to identify an API caller, and a SecretKey, which is used to encrypt the signature string and the key used to verify the signature string on the server end. You must keep your SecretKey strictly confidential to avoid disclosure.

### Obtaining Source Code via GitHub for Installation
Click on the GitHub address of PHP SDK provided by Tencent Cloud. [Get GitHub resources >>](https://github.com/CFETeam/qcloudapi-sdk).
1. Download source code from the Github address of `qcloudapi-sdk`
2. Extract the source code to the proper location of your project
3. Install the source code to the project:
```
    npm i qcloudapi-sdk --save
```

## Quick Start Demo
Take CVM's "Query" (DescribeInstances) as an example:
```
var Capi = require('qcloudapi-sdk')

// The parameter passed via the constructor is used as a default parameter
var capi = new Capi({
    SecretId: 'Your SecretId here',
    SecretKey: 'Your SecretKey here',
    serviceType: 'account'
});

capi.request({
    Region: 'gz',
    Action: 'DescribeProject',
    otherParam: 'otherParam'
}, function(error, data) {
    console.log(data)
})

// Pass the parameter to overwrite the original default parameter
capi.request({
    Region: 'gz',
    Action: 'DescribeInstances',
    otherParam: 'otherParam'
}, {
    serviceType: 'cvm'
}, function(error, data) {
    console.log(data)
});

// Generate querystring
var qs = capi.generateQueryString({
    Region: 'gz',
    Action: 'DescribeInstances',
    otherParam: 'otherParam'
}, {
    serviceType: 'cvm'
});
// 'Region=gz&SecretId=&Timestamp=1449461969&Nonce=20874&Action=DescribeInstances&otherParam=otherParam&Signature=r%2Fa9nqMxEIn5RsMjqmIksQ5XcYc%3D'
```

