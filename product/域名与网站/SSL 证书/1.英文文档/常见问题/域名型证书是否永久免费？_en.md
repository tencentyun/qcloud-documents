First, regardless of whether the SSL certificate is a free DV certificate or a paid OV certificate, CAs set a valid period for security reasons. A valid website cannot be guaranteed never to become a phishing site, so CAs conduct a regular review and do not issue permanent valid certificates.

Second, if the private key of a website is lost, you can apply for a certificate revocation. Then the CA adds the revoked certificate to the certificate revocation list (CRL). Whenever a HTTPS website is accessed, the browser retrieves the CRL from a CA to determine whether to trust the certificate. However, permanently valid certificates will lead to an increasing CRL, which will increase the request traffic of browsers. Therefore, it is a more scientific approach to specify a valid period for a certificate.

Now, Tencent Cloud provides a free DV certificate with the model of **TrustAsia DV SSL CA - G5** and a valid period of **1 year**. The certificate can be re-applied **three months** before expiration. DV certificates can be issued quickly within one working day, so you have sufficient time to switch the certificate for the site.

