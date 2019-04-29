## 1. How to apply for common certificates

- Generate private key locally: openssl genrsa -out privateKey.pem 2048, where privateKey.pem is your private key file. Please keep it well.
- Generate certificate request file: openssl req -new -key privateKey.pem -out server.csr, where server.csr is your certificate request file which is used to apply for certificate.
- Obtain the content of the request file and go to the CA site to apply for the certificate.

## 2. Certificate format

- The format of the certificate to be applied for is a .pem file under Linux environment. Load balancer does not support the certificates of other formats. For more information, please see "the certificate format supported by load balancer and conversion method" in this document.

- The certificate issued by root CA is unique. Without additional certificates, your configured site will be considered trusted by the browser and other accessing devices.

- The certificate file issued by an intermediate CA can contain multiple certificates. In this case, you need to manually concatenate the server certificate and intermediate certificates before uploading them.

- If your certificate has a certificate chain, convert its content into PEM format, and upload it along with the certificate content.

- Concatenation rule: The server certificate comes first, followed by the intermediate certificate. No blank line is allowed in between. Note: Generally, a CA provides instructions when issuing certificates. Make sure to carefully read the instructions.

Here are examples of certificate format and certificate chain format. Confirm that the formats are correct before uploading:

1. Certificate issued by root CA: Certificate is in the pem format under Linux environment. Example:

![](//mccdn.qcloud.com/static/img/b5eb2ee933723e3171d48377f354bc95/image.jpg)

Rules for certificate:
- [--- BEGIN CERTIFICATE ---, --- END CERTIFICATE ---] are the beginning and end, which should be uploaded with the content.
- Each line contains 64 characters, and the last line is limited to 64 characters.

2. Certificate chain issued by intermediate CA:
---BEGIN CERTIFICATE---
---END CERTIFICATE---
---BEGIN CERTIFICATE---
---END CERTIFICATE---
---BEGIN CERTIFICATE---
---END CERTIFICATE---

Rules for certificate chain:
- No blank line is allowed between certificates.
- Each certificate should comply with the certificate format rules described in Item 1.

## 3. RSA private key format

Example:

![](//mccdn.qcloud.com/static/img/6fd4309a24b9f969cd76950712fe8868/image.jpg)

RSA private key can include all private keys (RSA and DSA), public keys (RSA and DSA), and (x509) certificates. It stores DER data encoded with Base64 and is enclosed by ASCII header, thus is suitable for textual transfer between systems.

Rules for RSA private key:
- [---BEGIN RSA PRIVATE KEY---, ---END RSA PRIVATE KEY---] are the beginning and end, which should be uploaded with the content.
- Each line contains 64 characters, and the last line can contain less than 64 characters.

If the private key is not generated using the above method or has a format of [--- BEGIN PRIVATE KEY ---, --- END PRIVATE KEY ---], you can convert the format as follows:
```
openssl rsa -in old_server_key.pem -out new_server_key.pem
```
Then upload the content of new_server_key.pem along with the certificate.

## 4. How to convert certificate into PEM format

Load balancer only supports PEM certificates. Any certificate with other format must be converted to PEM format before being uploaded to load balancer. It is recommended to use openssl tool for the conversion. Here are some common methods for converting the certificate format to PEM.

### 4.1. Certificate conversion from DER format to PEM format

DER certificates are generally used on Java platforms.

Certificate conversion: ```openssl x509 -inform der -in certificate.cer -out certificate.pem```

Private key conversion: ```openssl rsa -inform DER -outform PEM -in privatekey.der -out privatekey.pem```

### 4.2. Certificate conversion from P7B format to PEM format

P7B certificates are generally used in Windows Server and Tomcat.

Certificate conversion: ```openssl pkcs7 -print_certs -in incertificat.p7b -out outcertificate.cer```

Obtain [--- BEGIN CERTIFICATE ---, --- END CERTIFICATE ---] content in outcertificat.cer as a certificate for upload.

Private key conversion: Private key can be exported from IIS server

### 4.3. Certificate conversion from PFX format to PEM format

PFX certificates are generally used in Windows Server.

Certificate conversion: ```openssl pkcs12 -in certname.pfx -nokeys -out cert.pem```

Private key conversion: ```openssl pkcs12 -in certname.pfx -nocerts -out key.pem -nodes```	

### 4.4. Certificate conversion from CER/CRT format to PEM format

You can convert CER/CRT certificates by directly modifying the certificate file extension. For example, directly rename the certificate file "servertest.crt" to "servertest.pem" to complete the conversion.

