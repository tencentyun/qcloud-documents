## FAQs

+ When the HTTPS certificate has been configured, the browser displays a message indicating the certificate is not trusted.
	+ Check your certificate issuing agency and browser:
		+ Google has distrusted certificates issued from WoSign and StartCom. [Learn More](https://security.googleblog.com/2016/10/distrusting-wosign-and-startcom.html);
		+ Apple has distrusted certificates issued from WoSign. [Learn More](https://support.apple.com/en-us/HT204132);
		+ Investigation report on the 13 issues of WoSign released by Mozilla: [Learn More](https://docs.google.com/document/d/1C6BlmbeQfn4a9zydVi2UvjBGv6szuSB4sMYUcVrR8vQ/preview#).
	+ You can apply for a free certificate from Tencent Cloud, or purchase a certificate on Tencent Cloud, [Click to Visit](https://console.cloud.tencent.com/ssl).

+ What types of SSL/TSL Security Protocols does HTTPS support?
	+ ssl\_protocols supported by CDN HTTPS: TLSv1, TLSv1.1, TLSv1.2.

+ A message indicating the certificate chain is incomplete appears during the configuration of certificate.
	+ CDN now supports the certificate with a PEM format. CA certificate is required to be pasted after the domain certificate before being uploaded. For instructions on how to do this, [Click to View](https://cloud.tencent.com/document/product/228 /6303#.E8.AF.81.E4.B9.A6.E9.93.BE.E8.A1.A5.E9.BD.90).

+ A message indicating certificate mismatch error appears during the configuration of certificate.
	+ After you paste the certificate using "Batch Upload" method, CDN will analyze which domains can use the certificates, and check whether wrong certificates have been uploaded, or whether the domains to be configured have not been connected to CDN.

+ Does CDN support ECC-encrypted certificates?
	+ CDN doesn't support ECC-encrypted certificates currently.

+ When the certificate has been configured, the page cannot be opened.
	+ Check whether you have set HTTPS as the back-to-origin method. Even HTTPS is set, request sent to origin server will fail if the origin server is not configured with the certificate. You can change the back-to-origin method to HTTP, or configure the certificate for origin server to fix the problem.






