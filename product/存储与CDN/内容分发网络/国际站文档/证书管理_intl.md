You can configure HTTPS certificate for a domain that has been connected to CDN. You can upload your existing certificate for deployment, or directly deploy the certificate hosted or issued by SSL Certificate Management platform.

You can apply for a free third party certificate from TrustAsia on SSL Certificate Management page.

## Configuring Certificate

If you already have a certificate, you can upload it directly to the CDN page for configuration. Log in to [CDN Console](https://console.cloud.tencent.com/cdn), and go to **Certificates** page in **Advanced** and click "Configure Certificate":
![](//mc.qcloudimg.com/static/img/2ee4c1d3e538986546ccbc7c167fd772/image.png)

### 1. Selecting a Domain
Select the accelerated domain for which you want to configure a certificate. Note:

+ The domain is required to be connected to CDN with a status of **Deploying** or **Activated**. For a deactivated domain, certificate deployment is not allowed; 
+ When CDN acceleration has been activated for COS or Cloud Image, certificate cannot be deployed for domain `.file.myqcloud.com` or `.image.myqcloud.com` by default; 
+ Certificate cannot be deployed for SVN hosted origin currently.

![](//mc.qcloudimg.com/static/img/77f74050757ce3fbd0fea195e3fcd877/image.png)

### 2. Origin-Pull Method
After the certificate is configured, you can select the back-to-origin method by which CDN nodes get resources from origin server:

![](//mc.qcloudimg.com/static/img/8209ac4d41b103bfa8866e021f076b8e/image.png)

+ If HTTP is selected, the requests sent from users to CDN nodes support HTTPS/HTTP, and the requests sent from CDN nodes to origin server all use HTTP;
+ If HTTPS is selected, the origin server is required to be already configured with a certificate, otherwise back-to-origin failure may occur. When this is checked, if the requests sent from users to CDN nodes use HTTP, the requests sent from CDN nodes to origin server also use HTTP; if the requests sent from users to CDN nodes use HTTPS, the requests sent from CDN nodes to origin server also use HTTPS;
+ Currently, domains connected with COS origin or FTP origin do not support using HTTPS as the back-to-origin method;
+ For the configuration of HTTPS, your origin server is required to have no port constraint or to be configured with port 443, otherwise the configuration may fail.

#### 3. Finishing Configuration

Once the configuration is finished, you can see the domain and certificate that have been configured successfully on "Certificate Management" page.

## Editing Certificate
For certificates that have been configured successfully, you can seamlessly update the certificates with "Edit" button.
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

CA agency mainly provide the following three certificates: Apache, IIS, Nginx.

CDN uses **Nginx**. Select the certificates with an extension of .crt or .key under  **Nginx** folder. A certificate of PEM format can be directly opened in text editor. You just need to copy and upload it.

You can also complete the certificate chain by pasting the content of CA certificate (PEM format) to the bottom of domain certificate (PEM format).
