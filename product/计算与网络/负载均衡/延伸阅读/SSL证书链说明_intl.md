
## What is the SSL Certificate Chain?

There are two types of CAs: Root CAs and intermediate CAs. In order for an SSL certificate to be trusted, that certificate must have been issued by a CA that is included in the trusted store of the connecting device.
	
If the certificate was not issued by a trusted CA, the connecting device (e.g. a web browser) will then check if the certificate was issued by a trusted CA until no trusted CA can be found.
	
The list of SSL certificates, from the root certificate, to intermediate certificate, to the end-user certificate, represents the SSL certificate chain.

## Example of an SSL Certificate chain
	
Let's suppose that you purchase a certificate from the Tencent Cloud Authority for the domain example.tencent-cloud.

Tencent Cloud Authority is not a root certificate authority.  In other words, its certificate is not directly embedded in your web browser and therefore it can't be explicitly trusted.

- Tencent Cloud Authority uses a certificate issued by the intermediate Tencent Cloud CA - Alpha.
- Intermediate Tencent Cloud CA Alpha uses a certificate issued by the intermediate Tencent Cloud CA - Beta.
- Intermediate Tencent Cloud CA Beta uses a certificate issued by the intermediate Tencent Cloud CA - Gamma.
- Intermediate Tencent Cloud CA Gamma uses a certificate issued by The Root of Tencent Cloud.
- The Root of Tencent Cloud is a Root CA. Its certificate is directly embedded in your web browser, therefore it can be explicitly trusted.

In the above example, the SSL certificate chain is made up of 6 certificates:
1. End-user certificate - Issued to: example.tencent-cloud; Issued By: Tencent Cloud Authority
2. Intermediate certificate 1 - Issued to: example.tencent-cloud; Issued by:   Intermediate Tencent Cloud CA, Alpha
3. Intermediate certificate 2 - Issued to: intermediate Tencent Cloud CA, Alpha; Issued by:   Intermediate Tencent Cloud CA, Beta
4. Intermediate certificate 3 - Issued to: intermediate Tencent Cloud CA, Beta. Issued by:   Intermediate Tencent Cloud CA, Gamma
5. Intermediate certificate 4 - Issued to: intermediate Tencent Cloud CA, Gamma. Issued by: The Root of Tencent Cloud
6. Root certificate:  Issued by and to: The Root of Tencent Cloud

Certificate 1 is your end-user certificate, and certificates from 2 to 5 are called intermediate certificates.  Certificate 6 is root certificate.

When you install your end-user certificate for example.tencent-cloud, you must bundle all the intermediate certificates and install them along with your end-user certificate. If the SSL certificate chain is invalid or broken, your certificate will not be trusted by some devices.







