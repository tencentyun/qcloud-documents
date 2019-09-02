## iOS Certificate Command
#### Certificate validity period
```
openssl x509 -in xxx.pem -noout -dates
```
#### Connecting to APNS to test whether the certificate is valid
1. Development environment:
```
openssl s_client -connect gateway.sandbox.push.apple.com:2195 -cert xxx.pem -key xxx.pem
```
2. Production environment:
```
openssl s_client -connect gateway.push.apple.com:2195 -cert xxx.pem -key xxx.pem
```

## About This Guide
This guide describes how to set up an iOS certificate. After configuring the certificate, go to Full Connection to iOS SDK.
### Procedure

**Step 1:** Log in to the Apple Developer website, and then click **Certificates, Identifiers & Profiles**.
![](//mc.qcloudimg.com/static/img/13a636325558df6da436d28301e907e3/image.jpg)

**Step 2:** Click **Certificates**.
![](//mc.qcloudimg.com/static/img/13a636325558df6da436d28301e907e3/image.jpg)

**Step 3:** Select the App for which a Push certificate is needed, and then check **Push Notifications**.
![](//mc.qcloudimg.com/static/img/47598fc9cf98c77fed1c91aa55c1b88e/image.jpg)

**Step 4:** The following example shows how to create a development certificate.
Click **Create Certificate...**
![](//mc.qcloudimg.com/static/img/912a8d77242160b02ef102ebb4e3307c/image.png)
![](//mc.qcloudimg.com/static/img/2f8ba124babf0a925c3f0aa96bfd1bdb/image.jpg)
And then open the Keychain Access tool
![](//mc.qcloudimg.com/static/img/eee2ebb09a60acfb9509fe30c02b9e2d/image.jpg)
Select **Request a Certificate From a Certificate Authority...** 
![](//mc.qcloudimg.com/static/img/66e99c2d806d0d1d59f9fd93d940bc3a/image.jpg)
Enter the e-mail address and leave other fields empty. Click **Continue** to save the certificate locally.
![](//mc.qcloudimg.com/static/img/61f00eed1371c2ef791dff672545e899/image.png)
Return to the website and select the file you just created to upload.
![](//mc.qcloudimg.com/static/img/c62bc18cdcb019a62f4ef73cedff8691/image.jpg)
After the certificate is generated, download it locally.![](//http://developer.qq.com/wiki/xg/imgs/20151118170536_85822.jpg) 

Open Keychain Access again. Select the Push certificate to export by selecting a line. The exported format is p12.
![](//mc.qcloudimg.com/static/img/cadb2f416989d37fa517fa27defb21b6/image.jpg)

### Generating a certificate in pem format
After completing the above operations, open the terminal to enter the folder where p12 file is located, and execute the following command:
```
openssl pkcs12 -in CertificateName.p12 -out CertificateName.pem -nodes
```
A CertificateName.pem certificate is generated. Upload it to XGPush to push messages.
For more information on the development using iOS SDK, go to [Full Connection to iOS SDK V2.5.0](https://cloud.tencent.com/document/product/548/13270) or [Full Connection to iOS SDK V3.0.0](https://cloud.tencent.com/document/product/548/13274).





