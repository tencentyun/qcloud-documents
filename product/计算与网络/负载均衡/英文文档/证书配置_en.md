## Common Procedure for Applying for Certificates

- Generate private key locally: openssl genrsa -out privateKey.pem 2048, where privateKey.pem will be your private key file. Make sure to place the file in a secure place for safekeeping
- Generate certificate request file: openssl req -new -key privateKey.pem -out server.csr, where server.csr will be your certificate request file which is used to apply for certificate
- Acquire the content of the request file and go to authorities (such as CA) to apply for certificate

## Certificate Format Requirement

- The format of the certificate to be applied by the user is a .pem file under linux environment. Cloud load balancer does not support certificates of other types. If your certificate is of another type, please refer to the "Certificate Types Supported by Cloud Load Balancers and Conversion Method" section of this document.

- A certificate issued by root CA is unique, in which case you will not need  additional certificates and your configured site will be considered as trusted by accessing devices such as browsers.

- A certificate file issued by intermediate CA includes multiple certificates, you need to concatenate server certificate and intermediate certificate manually before uploading.

- If your certificate has a certificate chain, please convert its content into PEM format, and upload it with the certificate content.

- Concatenation rule: The server certificate comes first, followed by the intermediate certificate. No blank lines in between. Note: CAs will usually provide corresponding instructions when issuing certificates, make sure to read the rules.

Here are examples of certificate format and certificate chain format. Please confirm the format before uploading:

1. Certificate issued by root CA: Certificate is pem format under linux environment. Example:

![](//mccdn.qcloud.com/static/img/b5eb2ee933723e3171d48377f354bc95/image.jpg)

Rules for certificate:
- [--- BEGIN CERTIFICATE ---, --- END CERTIFICATE ---] are the beginning and end, which should be uploaded with the content;
- Each line contains 64 characters, but the last line can contain less than 64 characters;

2. Certificate chain issued by intermediate CA:
---BEGIN CERTIFICATE---
---END CERTIFICATE---
---BEGIN CERTIFICATE---
---END CERTIFICATE---
---BEGIN CERTIFICATE---
---END CERTIFICATE---

Rules for certificate chain:

- No blank line is allowed between certificates;
- Each certificate shall comply with the certificate format rules described above;

## RSA Private Key Format Requirement

Example:

![](//mccdn.qcloud.com/static/img/6fd4309a24b9f969cd76950712fe8868/image.jpg)

RSA private key can include all private keys (RSA and DSA), public keys (RSA and DSA), and (x509) certificates. It stores DER data encoded with Base64 and is enclosed by ascii header, being suitable for textual transfer between systems.

Rules for RSA private key:
- [---BEGIN RSA PRIVATE KEY---, ---END RSA PRIVATE KEY---] are the beginning and end, which should be uploaded with the content;
- Each line contains 64 characters, but the last line can contain less than 64 characters;

If the private key is generated using other methods than the one described above and has a format of [--- BEGIN PRIVATE KEY ---, --- END PRIVATE KEY ---], you can convert the format as follows:
```
openssl rsa -in old_server_key.pem -out new_server_key.pem
```
Then upload the content of new_server_key.pem with the certificate.

## How to Convert Certificate into PEM Format

Currently, cloud load balance only supports certificates of PEM format. Any non-PEM certificates are required to be converted to PEM format before being uploaded to cloud load balance. It is recommended to use openssl tool for the conversion. Here are some common methods for converting the certificate format to PEM format.

### Converting DER to PEM

DER format generally occurs in Java platform.

Certificate conversion:```openssl x509 -inform der -in certificate.cer -out certificate.pem```

Private key conversion:```openssl rsa -inform DER -outform PEM -in privatekey.der -out privatekey.pem```

### Converting P7B to PEM

P7B format generally occurs in Windows Server and Tomcat.

Certificate conversion:```openssl pkcs7 -print_certs -in incertificat.p7b -out outcertificate.cer```

Obtain [--- BEGIN CERTIFICATE ---, --- END CERTIFICATE ---] content in outcertificat.cer as a certificate for upload.

Private key conversion: no private key

### Converting PFX to PEM

PFX format generally occurs in Windows Server.

Certificate conversion:```openssl pkcs12 -in certname.pfx -nokeys -out cert.pem```

Private key conversion:```openssl pkcs12 -in certname.pfx -nocerts -out key.pem -nodes```	

