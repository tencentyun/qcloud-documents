## Calling Method
How to connect to Tencent Cloud CVM is a problem we need to solve first. Tencent Cloud server cluster contains two layers for now:
- **Access Layer:**
  It is responsible to access the calling of external request. For example, limit the call frequency to 100 times per minute, or identify Tencent Cloud client server (based on SecretId and SecrectKey).

- **Function Layer:**
  It "hides" behind the access layer. Since the security confirmation and attack blocking have been implemented at the access layer, all the function layer needs to do is function processing. The basic features such as channel management and file query are implemented in this part.
	
	![api](//mc.qcloudimg.com/static/img/963c7973a3d5a77d6bd36d1cf3fd65ca/image.png)
	
If your server is calling a Tencent Cloud server API, the request needs go through the access layer first. The requirement for this layer are as follows:
- Request protocol must be HTTPS
- Request header must conform to Tencent Cloud access format
- Request header must contain correct SecretId and Signature

Therefore...

## Server SDK
[Tencent Cloud Server SDK](https://cloud.tencent.com/doc/sdk) is recommended. The following language versions are provided:
- PHP
- Python
- Java
- .Net
- Node.js

These SDKs are designed to help you connect to the Tencent Cloud CVM in the simplest way and to protect the intermediate linkage from attack by ensuring its security and reliability.

## Troubleshooting
An error code may be returned if you call Tencent Cloud server API. It contains two parts. The first part "code" is Tencent Cloud **access layer error code**, the second part **message** indicates the detailed meaning of the error code.

### unicode
```
{"code":4600,"message":"\u534f\u8bae\u4e0d\u652f\u6301\uff0c\u8bf7\u53c2\u8003\u6587\u6863\u8bf4\u660e\u3002"}
```
"message" is shown as an Unicode string in some platforms, which can be directly escaped in Chrome browser.
> Open Chrome, press F12 to enter the developer mode, and input the following content in Console panel at the bottom right corner:
> "\u534f\u8bae\u4e0d\u652f\u6301\uff0c\u8bf7\u53c2\u8003\u6587\u6863\u8bf4\u660e\u3002" 
> "The protocol is not supported. For more information, please see the relevant document." is returned after escape.
> 

### Dual Error Codes
Generally, the message is written in standard English, as shown below:
```
{"code":5100,"message":"20108: Channel is not in an editable status"}
```
You can see two error codes here:
- **5100**: This error code is returned from access layer. For example, 4100 refers to authentication error (that is, verification failed in Tencent Cloud backend system because SecretId and Signature you entered in the request header is incorrect). In this case, your request is intercepted at the access layer instead of being sent to the function layer.
> The error code 5100 is special. It means that "No error occurs during security check at the access layer. A message from the function layer indicates that there is an error with your request."

- **20200**: This error code is returned via a specific function module from the function layer. For example, 20108 indicates "Channel is not in an editable status", which means that your request is being processed in LVB system. However, a specific error notification returned because the system considers that there is an error with your request.

For more information on error codes, please see [Error Codes](https://cloud.tencent.com/doc/api/258/4733).

