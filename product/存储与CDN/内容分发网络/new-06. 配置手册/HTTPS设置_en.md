## Overview
HTTPS (Hypertext Transfer Protocol Secure) is a security protocol built on HTTP protocol to be used for encrypted communication and can effectively ensure data transmission security. When configuring HTTPS, you need to provide the certificate for your domain and deploy it across all CDN nodes on the entire network to achieve encrypted data transmission across the network.

<font color="red">HTTPS configuration is now completely available for you.</font>

## Configuration Instructions

HTTPS configuration is only available to domains which meet the following conditions:

- Domain status is **Deploying** or **Activated** in "Domain Management" page;
- It is not a COS-synchronized domain with ".file.myqcloud.com" as suffix;
- Domain's connection method is **Self-owned origin**, **COS origin** or **FTP origin**;

Log in to [CDN Console](https://console.qcloud.com/cdn) and go to "Domain Management" page. Then click **Manage** button to the right of the domain name to enter the management page:

![](https://mc.qcloudimg.com/static/img/70a01c53cfaa997013da2cb4b699bbf1/donmai_management.png)

Go to "Advanced Configuration" and find "HTTPS Configuration"

![](https://mc.qcloudimg.com/static/img/fa28d53a7eba792519986e88ea5bcef8/https.png)

## Certificate Types

Tencent Cloud currently supports two certificate deployment methods:

- Self-owned certificate: Upload self-owned certificate and private key to CDN for deployment. Transmission is encrypted throughout the process to ensure security of your certificate;
- Tencent Cloud-hosted certificate: You can go to [SSL Certificate Management](https://console.qcloud.com/ssl) and trust your certificate to Tencent Cloud to use it for multiple cloud products. You can also apply for a **Free Certificate** provided by TrustAsia through this platform and deploy it directly to CDN;
- Tencent Cloud certificate: The original ".qcloudcdn.com" domain suffix belongs to Tencent Cloud and uses Tencent Cloud certificate. The entrance for adding this certificate has been closed.

## Certificate Management

Go to [Certificate Management](https://console.qcloud.com/cdn/tools/certificate) page to add, modify or delete certificates. For more information, refer to [Certificate Management Instructions](https://www.qcloud.com/doc/product/228/6303).


## Forced HTTPS

The **Forced Redirect** button will appear when the certificate is successfully configured. When it is enabled, any HTTP request made by the user will be redirected to HTTPS for access:

![](https://mc.qcloudimg.com/static/img/16abdcd52cbc8072881a2b40b05ccfee/https_set.png)

<font color="blue">The feature is only available after HTTPS certificate is successfully configured</font>

