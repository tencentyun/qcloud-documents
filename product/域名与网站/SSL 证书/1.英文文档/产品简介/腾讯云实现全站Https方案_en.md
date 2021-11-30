## Overview

Tencent Cloud, in cooperation with authoritative digital certificate authorities (CAs) and expert certificate agents, provides application and upload management services of Domain Validation (DV), Organization Validated (OV) and enterprise Extended Validated (EV) SSL certificates. Tencent Cloud CDN and CLB services support rapid SSL certificate deployment.

You can implement full HTTPS using the one-stop solution of Tencent Cloud. Here are detailed instructions:

## 1. Obtain a Certificate
Tencent Cloud SSL certificate service supports free application of DV SSL certificates, and offline purchase and application for OV, EV and other paid certificates.

### 1.1 Application Entry for DV Certificate
Enter the [SSL Certificate Console](https://console.cloud.tencent.com/ssl), and click **Apply for Certificate**.

![](https://mc.qcloudimg.com/static/img/4efe78b416cc29cacba1cbc2ba475bb6/2.png)

### 1.2 Fill in Application

Fill in the applied domain. Note that it is not supported to apply for top-level domains (e.g. qcloud com) for free certificates, please enter second-level, third-level domains such as cloud.tencent.com and demo.test.qlcoud.com.
If you need to deploy it to

![](https://mc.qcloudimg.com/static/img/4961164252cd488c9695475e173c0b8c/4.png)

### 1.3 DNS Domain Name Verification

Certificates support manual DNS verification by default, please see [instructions on domain name verification](https://cloud.tencent.com/doc/product/400/4142#2.-.E6.89.8B.E5.8A.A8dns.E9.AA.8C.E8.AF.81) for detailed verification method.

![](https://mc.qcloudimg.com/static/img/2f90c6cdf51ec98ba0fd7a112a891e13/5.png)

If the applied domain is successfully resolved on [Cloud DNS platform](https://console.cloud.tencent.com/cns/domains), the domain will support automatic DNS verification. Please see [instructions on domain name verification](https://cloud.tencent.com/doc/product/400/4142#1.-.E8.87.AA.E5.8A.A8dns.E9.AA.8C.E8.AF.81) for detailed verification method.

![](https://mc.qcloudimg.com/static/img/8c10bfb9fa50a520e0b8b45f3b7a9f74/6.png)

When the application is successfully submitted, you need to go to the certificate detail page to obtain the CName record and add resolution. The process of obtaining the CName record is shown in Tips. Please add resolution as soon as possible in order for the application to be approved by CAs:

![](https://mc.qcloudimg.com/static/img/1f0d7d113cd4ee14cda423a32e853fe4/8.png)

### 1.4 Failed to Submit Application

The pop-up window shown below indicates that the submitted domain is not approved by CA's security verification. See [Why Would Security Review Fail?](https://cloud.tencent.com/doc/product/400/5439) for detailed reasons.

![](https://mc.qcloudimg.com/static/img/25451d24cf3c717454830a44925642ec/1.png)

## 2. Deploy a Certificate to Cloud Load Balancer
### 2.1 Select a Certificate
Apply for a certificate (see [DV Certificate Application](https://cloud.tencent.com/document/product/400/6814) or select a certificate to upload, click **More**, and select **Deploy to CLB**.
![](https://mc.qcloudimg.com/static/img/f63593c744fe88e386ce1157526b468f/1.png)

### 2.2 Select a CLB Instance
Select only one CLB instance according to the project and region (South China region - Shenzhen Finance not supported).
![](https://mc.qcloudimg.com/static/img/b6261451a354dac96679737014938e52/2.png)

### 2.3 Create a Listener
Redirect to the CLB console, open the **Create a Listener** pop-up window, switch the protocol port to Https, select the specified server certificate , and then complete the rest configurations.
![](https://mc.qcloudimg.com/static/img/e997310524fd15288fca7c91ae7a2e6c/3.png)

### 2.4 Complete Other Configurations
Go on to complete other configurations to create a listener, and then you can get a CLB with HTTPS.

## 3. Deploy a Certificate to CDN
### 3.1 Select a Domain Name
Select the accelerated domain name for which you want to configure a certificate. Note:

+ The domain needs to be connected to CDN with a status of **Deploying** or **Activated**. For deactivated domains, certificate deployment is not allowed;
+ When CDN acceleration has been enabled for COS or Cloud Image, certificates cannot be deployed for domain .file.myqcloud.com or .image.myqcloud.com by default;
+ Certificates cannot be deployed for SVN hosted origin for now.

![](https://mc.qcloudimg.com/static/img/973e75c6a0b1672f1a1f11f9667bf6f0/image.png)

#### 3.2 Use Tencent Cloud Hosted Certificates
After a certificate applied on the [Certificate Management](https://console.cloud.tencent.com/ssl) page is issued successfully, select **Tencent Cloud Hosted Certificate** to view the list of certificates available for the domain name on the **Certificate Management** page:

![](https://mc.qcloudimg.com/static/img/8e6c6afcfa701fa4cdd3dc0711780c2b/image.png)

+ Select the certificate to use from the certificate list;
+ The certificates are displayed as certificate IDs (Remark) in the list. You can learn more about the certificates by going to [Certificate Management](https://console.cloud.tencent.com/ssl).

### 3.3 Origin-Pull Method
After the certificate is configured, you can select the origin-pull method by which CDN nodes get resources from origin server:

![](https://mc.qcloudimg.com/static/img/ba856a03ab0709f6befaafc7840e1cc9/image.png)

+ If HTTP is selected, the requests sent from users to CDN nodes support HTTPS/HTTP, and the requests sent from CDN nodes to origin server all use HTTP;
+ If HTTPS is selected, the origin server must have a certificate configured, otherwise origin-pull may fail. If the configuration is completed and the requests sent from users to CDN nodes use HTTP, the requests sent from CDN nodes to origin server also use HTTP; if the requests sent from users to CDN nodes use HTTPS, the requests sent from CDN nodes to origin server also use HTTPS;
+ Now, domains connected with COS origin or FTP origin do not support using HTTPS as the origin-pull method;
+ For the configuration of HTTPS, your origin server needs to have no port constraint or to be configured with port 443, otherwise the configuration may fail.

#### 3.4 Complete Configuration

Once the configuration is finished, you can see the domain name and certificate that have been configured on the **Certificate Management** page:

![](https://mc.qcloudimg.com/static/img/ec3d8d968918cd3e190c4f01194a6236/2.png)

