When there is no user request file in a Bucket, or when a specific request needs to be redirected, setting the back-to-origin can effectively meet users' needs. Back-to-origin setting is mainly used for scenarios such as hot migration of data, and redirection of specific requests.

Currently, the back-to-origin setting supports IP segments of which the origin server IP belongs to China Telecom, China Mobile, China Unicom and Great Wall Broadband. The supported ISPs are increasing.

![](//mccdn.qcloud.com/img5697c84160bd9.png)

## Configuration Instructions

Enter the COS console, and click the Bucket List on the left to enter the Bucket List page. Select the Bucket for which the origin needs to be configured. Click to enter the File List, and then switch to the tab **Basic Configuration**:

![](https://mc.qcloudimg.com/static/img/dbddd755f6b782d8f9857d6e0feb9806/image.png)

Click the **Edit** button next to the **Origin Configuration**:

![](https://mc.qcloudimg.com/static/img/b8717b14f1e94c920679655df98cc693/image.png)

Status: After the back-to-origin is enabled, the domain or IP address that needs to send requests to the origin must be filled in.

Note: Currently, only HTTP is supported, and HTTPS is not supported. Fill in the domain or IP address without the prefix "http://". The port number can be added to the address in the :[port] format, and : should be an English character.

Configure a valid address for back-to-origin requests, for example:

```
abc.qq.com
abc.qq.com:8080
123.2.4.8
123.2.4.8:8080
```

## Example
A user creates a new Bucket and enables the CDN accelerated access domain `Bucket-1250000000.file.myqcloud.com`. The user sets the address for back-to-origin requests of the Bucket to `abc.qq.com`, and stores an image `http://abc.qq.com/1.jpg` on the origin server.

When accessing `http://bucket-1250000000.file.myqcloud.com/1.jpg` for the first time, COS finds that the file was not hit, and returns 302 HTTP status code to the client and jumps to `http://abc.qq.com/1.jpg`. In this case, the file is provided by the origin server for the client to ensure successful access, and meanwhile, COS will copy the `1.jpg` at the origin server and save it to the root directory of the bucket.

When accessing `http://bucket-1250000000.file.myqcloud.com/1.jpg` for the second time, the `1.jpg` under the root directory in the COS will be hit directly.



