CSR is short for Certificate Signing Request. To obtain an SSL certificate, you need to generate a CSR file first and submit it to a certificate authority (CA). The CSR includes a public key and a distinguished name. CSR is typically generated from a web server and a public/private key pair for encryption and decryption will be created at the same time.

Relevant organization information is required to create a CSR. The web server creates a distinguished name based on the information provided to identify the certificate. The organization information contains the following contents:

**Country/Region Code**
The code of the country/region where your organization is legally registered, in the format of two-letter defined by the International Organization for Standardization (ISO).

**Province/City/Autonomous Region**
The province/city/autonomous region where your organization is located.

**City/Region**
The city/region where your organization is registered or located.

**Organization**
The name of your business registered according to law.

**Department of Organization**
This field is used to differentiate departments within an organization, such as "Engineering Department " or "Human Resources".

**Generic Name**

The name entered in the generic name field of CSR must be the fully qualified domain name (FQDN) of the website for which you want to use the certificate, for example `www.domainnamegoeshere`.


However, Tencent Cloud applies the method of generating CSR online to simplify the application process. You only need to submit a generic name for a domain validation (DV) certificate application and do not need to generate and submit CSR files.

