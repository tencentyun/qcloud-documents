You can configure HTTPS certificate for a domain that has been connected to CDN. You can upload your existing certificate for deployment, or directly deploy the certificate hosted or issued by [SSL Certificate Management](https://console.cloud.tencent.com/ssl) platform.

You can apply for a free third party certificate from TrustAsia on SSL Certificate Management page.

## Configuring Certificate

If you already have a certificate, you can upload it directly to the CDN page for configuration. Log in to [CDN Console](https://console.cloud.tencent.com/cdn), and go to **Certificates** page and click "Configure Certificate":
![](//mc.qcloudimg.com/static/img/4b6dc524595e3ac1c605676210901659/image.png)

### 1. Selecting a Domain
Select the accelerated domain for which you want to configure a certificate. Note:

+ The domain is required to be connected to CDN with a status of **Deploying** or **Activated**. For a deactivated domain, certificate deployment is not allowed; 
+ When CDN acceleration has been activated for COS or Cloud Image, certificate cannot be deployed for domain `.file.myqcloud.com` or `.image.myqcloud.com` by default; 
+ Certificate cannot be deployed for SVN hosted origin currently.

![](https://mc.qcloudimg.com/static/img/ac1c0f73c7a497cb998491672635adee/2.png)

### 2. Selecting a Certificate
#### 2.1 Using external certificate

Select "External Certificate", and paste the certificate content and private key to the corresponding text boxes. You can optionally add a remark for identifying the certificate.

![](//mc.qcloudimg.com/static/img/4b6dc524595e3ac1c605676210901659/image.png)

+ The certificate content must take a PEM format. For non-PEM certificates, please refer to the instructions below for format conversion;
+ If your certificate has a certificate chain, please convert its content into PEM format, and upload it with the certificate content. The instructions on the completion of certificate chain is described later in this chapter.

#### 2.2 Using Tencent Cloud Hosted Certificate
You can apply for a free third-party certificate from TrustAsia on [SSL Certificate Management](https://console.cloud.tencent.com/ssl) page or trust an existing certificate to Tencent Cloud to use it for such Cloud products as CDN, Cloud Load Balance.

By selecting "Tencent Cloud Hosted Certificate", you can view the list of certificates available for the domain in SSL Certificate Management:

![](https://mc.qcloudimg.com/static/img/aacbfb543f25cbebb1c7eef984cf42bb/4.png)

+ Select the certificate to use from the List of Certificates;
+ The certificates are displayed as Certificate IDs (Remark) in the list . You can learn more about the certificates by going to [SSL Certificate Management](https://console.cloud.tencent.com/ssl).

### 3. Origin-Pull Method
After the certificate is configured, you can select the back-to-origin method by which CDN nodes get resources from origin server:

![](https://mc.qcloudimg.com/static/img/5ea84cece3dbb0d0956b850fa3db71d4/5.png)

+ If HTTP is selected, the requests sent from users to CDN nodes support HTTPS/HTTP, and the requests sent from CDN nodes to origin server all use HTTP;
+ If HTTPS is selected, the origin server is required to be already configured with a certificate, otherwise back-to-origin failure may occur. When this is checked, if the requests sent from users to CDN nodes use HTTP, the requests sent from CDN nodes to origin server also use HTTP; if the requests sent from users to CDN nodes use HTTPS, the requests sent from CDN nodes to origin server also use HTTPS;
+ Currently, domains connected with COS origin or FTP origin do not support using HTTPS as the back-to-origin method;
+ For the configuration of HTTPS, your origin server is required to have no port constraint or to be configured with port 443, otherwise the configuration may fail.

#### 4. Finishing Configuration

Once the configuration is finished, you can see the domain and certificate that have been configured successfully on "Certificate Management" page:

![](https://mc.qcloudimg.com/static/img/064b82a67639f0b730fd6869f479426d/6.png)

## Batch Configuration of Certificate

If you have a multi-domain certificate or wildcard-domain certificate applicable to multiple CDN accelerated domains, you can configure such certificate for multiple domains at a time using batch configuration.

### 1. Uploading certificate

Paste PEM-encoded certificate content and private key to corresponding text boxes. You can modify the Remark to identify the configured certificate, and then click **Next**:

![](https://mc.qcloudimg.com/static/img/3b9ee17d804d79b23d045542d26bbd51/7.png)


### 2. Associating with domains

The CDN system can recognize the CDN accelerated domains that can use the uploaded certificate (with a status of Deploying or Activated). You can check the domains in batch:

+ A maximum of 10 accelerated domains are allowed to be checked at a time; 
+ You can configure the certificate for the domains that have been successfully configured with a certificate. Users can switch between the certificates seamlessly without affecting the use of HTTPS;
+ If among the checked domains there is any domain connected with COS origin or FTP origin, only HTTP is supported;
+ If among the checked domains there is any origin server that has been configured with a port other than 443, the configuration will fail.

### 3. Submitting Configuration

Once the configuration is submitted, CDN will configure the certificate for the selected domains. It will take about 5 minutes to configure certificate for each domain. Please wait a moment:

![](https://mc.qcloudimg.com/static/img/3e8b51a5718f5cb9c893f71c6d81220c/8.png)

You can check the certificate configuration status on "Certificate Management" page.

**Note:**

+ If the configuration fails, you can re-configure the certificate with "Edit" button.
+ If an overwriting operation exists but failed, the status will be changed to "Update Failed", and the original configuration remains valid. You can click "Edit" to perform the overwriting again.

## Editing Certificate
For certificates that have been configured successfully, you can seamlessly update the certificates with "Edit" button:
![](https://mc.qcloudimg.com/static/img/142e7deeae4cfc2178b36382428fbd8a/9.png)

+ Seamless switching between self-owned certificate and Tencent Cloud hosted certificate is supported;
+ Once the edited certificate is submitted, it will be deployed by seamlessly overwriting the original one without affecting your use of service.


### PEM Certificate Format

The certificate issued by Root CA agency has a PEM format as show below:

![](https://mccdn.qcloud.com/static/img/b5eb2ee933723e3171d48377f354bc95/image.jpg)

- [--- BEGIN CERTIFICATE ---, --- END CERTIFICATE ---] are the beginning and end, which should be uploaded with the content;

- Each line contains 64 characters, but the last line can contain less than 64 characters;

The certificate chain issued by intermediate agency:

>---BEGIN CERTIFICATE---
>---END CERTIFICATE---
>---BEGIN CERTIFICATE---
>---END CERTIFICATE---
>---BEGIN CERTIFICATE---
>---END CERTIFICATE---

Rules for certificate chain:

- No blank line is allowed between certificates;
- Each certificate shall comply with the certificate format rules described above; 

### PEM Private Key Format

RSA private key can include all private keys (RSA and DSA), public keys (RSA and DSA), and (x509) certificates. It stores DER data encoded with Base64 and is enclosed by ascii header, being suitable for textual transfer between systems. Example:

![](https://mccdn.qcloud.com/static/img/6fd4309a24b9f969cd76950712fe8868/image.jpg)

RSA private key rules:

- [---BEGIN RSA PRIVATE KEY---, ---END RSA PRIVATE KEY---] are the beginning and end, which should be uploaded with the content;
- Each line contains 64 characters, but the last line can contain less than 64 characters;

If the private key is generated using other methods than the one described above and has a format of [--- BEGIN PRIVATE KEY ---, --- END PRIVATE KEY ---], you can convert the format as follows:

```
openssl rsa -in old_server_key.pem -out new_server_key.pem
```

Then upload the content of new_server_key.pem and the certificate.

### PEM Format Conversion

Currently, CDN only supports the certificate with a PEM format. Any non-PEM certificates are required to be converted to PEM format before being uploaded to Cloud Load Balance. It is recommended to use openssl tool for the conversion. Here are some common methods for converting the certificate format to PEM format.

#### Converting DER to PEM
DER format generally occurs in Java platform.

Certificate conversion:

```
openssl x509 -inform der -in certificate.cer -out certificate.pem`
```

Private key conversion:

```
openssl rsa -inform DER -outform PEM -in privatekey.der -out privatekey.pem
```

#### Converting P7B to PEM

P7B format generally occurs in Windows Server and Tomcat.

Certificate conversion:

```
openssl pkcs7 -print_certs -in incertificat.p7b -out outcertificate.cer
```

Obtain [--- BEGIN CERTIFICATE ---, --- END CERTIFICATE ---] content in outcertificat.cer as a certificate for upload.

Private key conversion: no private key

#### Converting PFX to PEM

PFX format generally occurs in Windows Server.

Certificate conversion:

```
openssl pkcs12 -in certname.pfx -nokeys -out cert.pem
```

Private key conversion:

```
openssl pkcs12 -in certname.pfx -nocerts -out key.pem -nodes
```



### Completion of Certificate Chain

CA agency mainly provide the following three certificates:

![](https://mc.qcloudimg.com/static/img/b6aa91178ad952913f2a797b2f52bc93/cer_type.png)

CDN uses **Nginx**. Select the certificates with an extension of .crt or .key under  **Nginx** folder. A certificate of PEM format can be directly opened in text editor. You just need to copy and upload it.

![](https://mc.qcloudimg.com/static/img/a282abe9154c5e78b2ba771289e52c7f/cer_nginx.png)

You can also complete the certificate chain by pasting the content of CA certificate (PEM format) to the bottom of domain certificate (PEM format):

![](https://mc.qcloudimg.com/static/img/53927ba56ceba5d0a3ed0c5d80257c8a/cer_add.png)
