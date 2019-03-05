### 1. What is HTTPS?
HTTPS refers to Hypertext Transfer Protocol Secure, which is a security protocol that encrypts and transfers data based on the HTTP protocol to ensure the security of data transfer. When configuring HTTPS, you need to provide the certificate for the domain name and deploy it on the CDN nodes across the network to implement the encrypted data transfer across the network.

### 2. Does CDN support HTTPS configuration?
Tencent Cloud CDN fully supports HTTPS configuration. You can either upload your own certificate for deployment or go to [Certificate Management Console](https://console.cloud.tencent.com/ssl) to apply for a third party certificate that is provided by TrustAsia free of charge.

### 3. How to configure HTTPS certificate?
You can configure the HTTPS certificate in the CDN console. For more information, please see [HTTPS Configuration](https://cloud.tencent.com/document/product/228/6295).

### 4. Do the HTTPS certificates on CDN nodes need to be synchronized with the updates of HTTPS certificate on origin server?
This depends on your origin-pull method.
Origin-pull based on HTTP: Synchronization is not needed.
Origin-pull based on HTTPS: When the certificate on origin server is updated, the certificates on the CDN nodes need to be updated synchronously. The certificate between client and node must be identical to the one between node and origin server. Otherwise, a failure of origin-pull will occur.

### 5. Is there any way for users to allow only HTTPS access and forbid HTTP access?
You can use forced HTTPS. After the certificate is configured successfully, the [Forced Redirect] switch is displayed. When the switch is enabled, even if you initiate an HTTP request, it will be forced to redirect to HTTPS for access.
![](https://mc.qcloudimg.com/static/img/8dc758129896bef56c85a8528371e9e7/force_https.png)
