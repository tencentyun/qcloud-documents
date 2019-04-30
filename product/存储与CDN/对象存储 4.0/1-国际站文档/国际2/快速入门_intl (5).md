## Preparations for Development

### Obtain SDK

Download XML JS SDK resources for COS service on Github from: [tencentyun/cos-js-sdk-v5](https://github.com/tencentyun/cos-js-sdk-v5).

Download Demo from [XML JS SDK Demo](https://github.com/tencentyun/cos-js-sdk-v5/tree/master/demo).

### Preparations for development

1. First, JS SDK requires the browser to support basic HTML5 features in order to support uploading files using ajax and computing md5 values of files.
2. Go to the [COS Console](https://console.cloud.tencent.com/cos4) to create a bucket and obtain Bucket (bucket name) and [Region (region name)](https://cloud.tencent.com/document/product/436/6224).
3. Go to [Key Management](https://console.cloud.tencent.com/capi) on the console to obtain SecretId and SecretKey of your project.
4. Configure CORS rules, as shown below:
![cors](//mc.qcloudimg.com/static/img/2e7791e9274ce3ebf8b25bbeafcd7b45/image.png)


> For more information on the definitions of SecretId, SecretKey, Bucket and other terms and how to obtain them, please see [COS Glossary](https://cloud.tencent.com/document/product/436/7751).
    
## Getting Started		
### Computing signature

If the signature computing is implemented at frontend, SecretId and SecretKey can be exposed. For this reason, the signature computing is performed at backend. The frontend obtains the signature computing result via ajax. Add a permission verification at backend for your website during the deployment.For other languages, please see the relevant [XML SDK](https://cloud.tencent.com/document/product/436/6474).

### Example for upload

1. Create test.html, fill in the following code, and modify the Bucket and Region in it.
2. Deploy the backend signature service and modify the signature service address in getAuthorization.
3. Place test.html on the Web server, then visit the page in the browser to test the file upload.

```html
<input id="file-selector" type="file">
<script src="dist/cos-js-sdk-v5.min.js"></script>
<script>
var Bucket = 'test-1250000000';
var Region = 'ap-guangzhou';

// Initialize the instance
var cos = new COS({
    getAuthorization: function (options, callback) {
        // Obtain the signature asynchronously
        $.get('../server/sts.php', {
            bucket: options.Bucket,
            region: options.Region,
        }, function (data) {
            callback({
                TmpSecretId: data.TmpSecretId,
                TmpSecretKey: data.TmpSecretKey,
                XCosSecurityToken: data.XCosSecurityToken,
                ExpiredTime: data.ExpiredTime,
            });
        });
    }
});

// Listen on the selected file
document.getElementById('file-selector').onchange = function () {
    
    var file = this.files[0];
    if (!file) return;

    // Upload the file in multipart
    cos.sliceUploadFile({
        Bucket: Bucket,
        Region: Region,
        Key: file.name,
        Body: file,
    }, function (err, data) {
        console.log(err, data);
    });

};
</script>
```


## Introducing Webpack

In the scenarios where webpack is supported, it can be introduced as a module using npm.
```shell
npm i cos-js-sdk-v5 --save
```

## Other Documents and Examples

1. For more examples, please see [XML JavaScript SDK Demo](https://github.com/tencentyun/cos-js-sdk-v5/blob/master/demo).
2. For the complete API documentation, please see [XML JavaScript SDK API documentation](https://cloud.tencent.com/document/product/436/12260).

