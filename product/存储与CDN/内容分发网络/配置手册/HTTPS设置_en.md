## Overview
HTTPS (Hypertext Transfer Protocol Secure) is a security protocol built on HTTP protocol to be used for encrypted communication and can effectively ensure data transmission security. When configuring HTTPS, you need to provide the certificate for your domain and deploy it across all CDN nodes on the entire network to achieve encrypted data transmission across the network.

<font color="red">HTTPS configuration is now completely available for you.</font>

## Configuration Instructions

HTTPS configuration is only available to domains which meet the following conditions:

- Domain status is **Deploying** or **Activated** in "Domain Management" page;
- It is not a COS-synchronized domain with ".file.myqcloud.com" as suffix;
- Domain's connection method is **Self-owned origin**, **COS origin** or **FTP origin**;

Log in to [CDN Console](https://console.cloud.tencent.com/cdn) and go to "Domain Management" page. Then click **Manage** button to the right of the domain name to enter the management page:

![](https://mc.qcloudimg.com/static/img/f92d2ef7e4be2b69185ab43228f025ef/1.png)

Go to "Advanced Configuration" and find "HTTPS Configuration"

![](https://mc.qcloudimg.com/static/img/df38d5d35b266e96c99f4ab67732cfd8/2.png)

## Certificate Types

Tencent Cloud currently supports two certificate deployment methods:

- Self-owned certificate: Upload self-owned certificate and private key to CDN for deployment. Transmission is encrypted throughout the process to ensure security of your certificate;
- Tencent Cloud-hosted certificate: You can go to [SSL Certificate Management](https://console.cloud.tencent.com/ssl) and trust your certificate to Tencent Cloud to use it for multiple cloud products. You can also apply for a **Free Certificate** provided by TrustAsia through this platform and deploy it directly to CDN;
- Tencent Cloud certificate: The original ".qcloudcdn.com" domain suffix belongs to Tencent Cloud and uses Tencent Cloud certificate. The entrance for adding this certificate has been closed.

## Certificate Management

Go to [Certificate Management](https://console.cloud.tencent.com/cdn/tools/certificate) page to add, modify or delete certificates. For more information, refer to [Certificate Management Instructions](https://cloud.tencent.com/doc/product/228/6303).


## Forced HTTPS

The **Forced Redirect** button will appear when the certificate is successfully configured. When it is enabled, any HTTP request made by the user will be redirected to HTTPS for access:

![](https://mc.qcloudimg.com/static/img/22b01df16d9b4d50397b612b60252cfa/3.png)

<font color="blue">The feature is only available after HTTPS certificate is successfully configured</font>

## HTTP2.0

If you already obtained the qualifications of HTTP 2.0 closed beta,  you can open HTTP2.0 after finish the configuration of HTTPS certificate:

![](https://mc.qcloudimg.com/static/img/72d122326ad99bb23f1ba66690bae91c/4.png)

