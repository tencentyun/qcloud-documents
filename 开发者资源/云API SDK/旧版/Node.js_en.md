We provide Node.js based SDK to make it easy for developers to debug and access Cloud API.

Download from: https://github.com/CFETeam/qcloudapi-sdk

qcloudapi-sdk is a node.js SDK for Tencent Cloud API 2.0.

## 1. Resources

For details, refer to API common parameters, overview and error codes in different modules. For instance, [CVM API Common Parameters](http://cloud.tencent.com/document/api/213/6976), [CVM API Overview](http://cloud.tencent.com/doc/api/229/API%E6%A6%82%E8%A7%88) and [CVM API Error Codes](http://cloud.tencent.com/doc/api/229/%E9%94%99%E8%AF%AF%E7%A0%81).

## 2. Installation

```
npm i qcloudapi-sdk --save
```


## 3. Quick Start

1) [Get Security Credential](https://console.cloud.tencent.com/capi). Before calling the Cloud API for the first time, you need to apply for a security credential on the Tencent Cloud console. A security credential consists of a SecretId, which is used to identify an API caller, and a SecretKey, which is used to encrypt the signature string and verify the string on the server. You must keep your SecretKey strictly confidential to avoid disclosure.

2) Install and use this SDK. For details, refer to the example below.

## 4. Example

```
var Capi = require('qcloudapi-sdk')

// The parameter input via the Constructor will be treated as a new default parameter
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

// Input the parameter to overwrite the original default parameter
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

## 5. SDK API
For details, refer to [api.md](https://github.com/CFETeam/qcloudapi-sdk/blob/master/api.md)
