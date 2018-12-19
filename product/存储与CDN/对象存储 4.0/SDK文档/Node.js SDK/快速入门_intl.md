## Preparations for Development
### Obtain SDK

Download XML JS SDK resources for COS service on Github from: [tencentyun/cos-nodejs-sdk-v5](https://github.com/tencentyun/cos-nodejs-sdk-v5) .

Download Demo from [XML Node.js SDK Demo](https://github.com/tencentyun/cos-nodejs-sdk-v5/tree/master/demo) .

### Introduce npm
Before development, you need to install environment dependencies: [npm address](https://www.npmjs.com/package/cos-nodejs-sdk-v5)
 
```
npm i cos-nodejs-sdk-v5 --save
```

### Development environment

1. The use of SDK requires that your operating environment includes nodejs and npm. Nodejs 7.0 or above is recommended.
2. After installing npm, be sure to install npm install once under SDK's decompressed directory (install dependency package).
3. Go to [Key Management](https://console.cloud.tencent.com/capi) on the console to obtain SecretId and SecretKey of your project.

> For more information on the definitions of SecretId, SecretKey, Bucket and other terms and how to obtain them, please see [COS Glossary](https://cloud.tencent.com/document/product/436/7751).

## Getting Started	

1. Go to the [COS Console](https://console.cloud.tencent.com/cos4) to create a bucket and obtain Bucket (bucket name) and [Region (region name)](https://cloud.tencent.com/document/product/436/6224).
2. Go to [Key Management](https://console.cloud.tencent.com/capi) on the console to obtain SecretId and SecretKey of your project.
3. Modify the SecretId, SecretKey, Bucket and Region to test the file upload by referring to the following code.

```javascript
// Introduce the module
var COS = require('cos-nodejs-sdk-v5');
// Create an instance
var cos = new COS({
    AppId: '1250000000',
    SecretId: 'AKIDxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    SecretKey: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
});
// Multipart upload
cos.sliceUploadFile({
    Bucket: 'test',
    Region: 'ap-guangzhou',
    Key: '1.zip',
    FilePath: './1.zip'
}, function (err, data) {
    console.log(err, data);
});
```

## Related Documents 

1. For more examples, please see [XML Node.js SDK Demo](https://github.com/tencentyun/cos-nodejs-sdk-v5/blob/master/demo/).
2. For the complete API documentation, please see [XML Node.js SDK API documentation](https://cloud.tencent.com/document/product/436/12264).


