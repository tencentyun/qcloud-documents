**1. Principle of Automatic DNS Verification**

After the application for certificate is submitted, the CA will specify a CNAME record to verify the ownership of the domain name. If the domain name is resolved in Tencent Cloud DNS platform, the specified CNAME record can be added automatically and immediately for the scheduled scanning audit by CA, which is the fastest and most convenient way to complete the certificate application.

**2. Add Domain Name to Cloud DNS**

If your domain name is not resolved on the Cloud DNS platform, you can refer to the following process to add a domain name to Cloud DNS:

[Add a Domain Name to Cloud DNS](https://cloud.tencent.com/doc/product/302/3446).


**3. Modify DNS Server**

After adding the domain name, make sure to modify the DNS server of the domain name to the DNS address specified by Tencent Cloud to make the resolution effective.
For more information, please see [Change DNS Server](https://cloud.tencent.com/doc/product/302/5518).

