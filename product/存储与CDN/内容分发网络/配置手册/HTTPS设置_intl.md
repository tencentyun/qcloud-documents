HTTPS (Hypertext Transfer Protocol Secure) is a security protocol built on HTTP protocol to be used for encrypted communication and can effectively ensure data transmission security. When configuring HTTPS, you need to provide the certificate for your domain name and deploy it across all CDN nodes on the entire network to achieve encrypted data transmission across the network.

**Notes:**
-  When CDN acceleration is enabled for **Cloud Object Storage** or **Cloud Image**, you can directly enable HTTPS support for domain names suffixed with ```.file.myqcloud.com``` or ```.image.myqcloud.com``` by default, without having to configure any certificate.
- Tencent Cloud CDN has entered public beta and is open to anyone who requires HTTP 2.0 support.

## Configuration Guide
- Your domain name is not the one suffixed with ```.file.myqcloud.com``` or ```.image.myqcloud.com``` by default.
- Connection to your domain name is implemented by means of **Self-owned origin**, **COS origin** or **FTP origin**.

Tencent Cloud CDN supports two certificate deployment methods:
- Self-owned certificate: Upload self-owned certificate and private key to CDN for deployment. Transmission is encrypted throughout the process to ensure security of your certificate.
- Tencent Cloud-hosted certificate: You can go to [SSL Certificate Management](https://console.cloud.tencent.com/ssl) and trust your certificate to Tencent Cloud to use it for multiple cloud products. You can also apply for a free third-party certificate provided by TrustAsia through this platform and deploy it directly to CDN.

Log in to [CDN Console](https://console.cloud.tencent.com/cdn), and click **Domain Management** in the left navigation bar to enter the **Domain Management** page. Click the **Manage** button on the right of the domain name to enter the management page.
![](https://main.qcloudimg.com/raw/667013013f17c055f0cb3cec4580c4ef.png)
Click **Advanced Configuration** and find **HTTPS Configuration**. Click **Configure Now**, and you will be taken to the **Configure Certificate** page where you can configure your certificate. For more information on how to make the configurations, please see [Certificate Management](https://cloud.tencent.com/document/product/228/6303).
![](https://main.qcloudimg.com/raw/1efff7b5b6909863e0849ae6cf9f65a7.png)
After the certificate is **successfully configured**, a **Forced HTTPS Redirection** toggle button appears. Switching this toggle button to "ON" will force any HTTP request to redirect to HTTPS:
![](https://main.qcloudimg.com/raw/8ccfdda9898a09a95d702e9162ff95d6.png)

## HTTP 2.0 Configuration
If you are eligible for an HTTP 2.0 internal trial, you can enable HTTP 2.0 support after having successfully configured an HTTPS certificate for your domain name.
![](https://main.qcloudimg.com/raw/19b5892f7cf04b93e37f63eef75a94d8.png)
For more information on the features in HTTP 2.0, please see [New Features in HTTP 2.0](https://cloud.tencent.com/community/article/541321).

## Algorithms supported by HTTPS origin-pull
The algorithms supported by HTTPS origin-pull are shown in the following table (in no particular order):

<table ><tbody>
<tr><td >ECDHE-RSA-AES256-SHA</td>
<td >ECDHE-RSA-AES256-SHA384</td>
<td >ECDHE-RSA-AES256-GCM-SHA384</td></tr>
<tr><td >ECDHE-ECDSA-AES256-SHA</td>
<td >ECDHE-ECDSA-AES256-SHA384</td>
<td >ECDHE-ECDSA-AES256-GCM-SHA384</td></tr>
<tr><td >SRP-AES-256-CBC-SHA</td>
<td >SRP-RSA-AES-256-CBC-SHA</td>
<td >SRP-DSS-AES-256-CBC-SHA</td></tr>
<tr><td >DH-RSA-AES256-SHA</td>
<td >DH-RSA-AES256-SHA256</td>
<td >DH-RSA-AES256-GCM-SHA384</td></tr>
<tr><td >DH-DSS-AES256-SHA</td>
<td >DH-DSS-AES256-SHA256</td>
<td >DH-DSS-AES256-GCM-SHA384</td></tr>
<tr><td >DHE-RSA-AES256-SHA</td>
<td >DHE-RSA-AES256-SHA256</td>
<td >DHE-RSA-AES256-GCM-SHA384</td></tr>
<tr><td >DHE-DSS-AES256-SHA</td>
<td >DHE-DSS-AES256-SHA256</td>
<td >DHE-DSS-AES256-GCM-SHA384</td></tr>
<tr><td >CAMELLIA256-SHA</td>
<td >DH-RSA-CAMELLIA256-SHA</td>
<td >DHE-RSA-CAMELLIA256-SHA</td></tr>
<tr><td >PSK-3DES-EDE-CBC-SHA</td>
<td >DH-DSS-CAMELLIA256-SHA</td>
<td >DHE-DSS-CAMELLIA256-SHA</td></tr>
<tr><td >ECDH-RSA-AES256-SHA</td>
<td >ECDH-RSA-AES256-SHA384</td>
<td >ECDH-RSA-AES256-GCM-SHA384</td></tr>
<tr><td >ECDH-ECDSA-AES256-SHA</td>
<td >ECDH-ECDSA-AES256-SHA384</td>
<td >ECDH-ECDSA-AES256-GCM-SHA384</td></tr>
<tr><td >AES256-SHA</td><td >AES256-SHA256</td>
<td >AES256-GCM-SHA384</td></tr>
<tr><td >ECDHE-RSA-AES128-SHA</td>
<td >ECDHE-RSA-AES128-SHA256</td>
<td >ECDHE-RSA-AES128-GCM-SHA256</td></tr>
<tr><td >ECDHE-ECDSA-AES128-SHA</td>
<td >ECDHE-ECDSA-AES128-SHA256</td>
<td >ECDHE-ECDSA-AES128-GCM-SHA256</td></tr>
<tr><td >SRP-AES-128-CBC-SHA</td>
<td >SRP-RSA-AES-128-CBC-SHA</td>
<td >SRP-DSS-AES-128-CBC-SHA</td></tr>
<tr><td >DH-RSA-AES128-SHA</td>
<td >DH-RSA-AES128-SHA256</td>
<td >DH-RSA-AES128-GCM-SHA256</td></tr>
<tr><td >DH-DSS-AES128-SHA</td>
<td >DH-DSS-AES128-SHA256</td>
<td >DH-DSS-AES128-GCM-SHA256</td></tr>
<tr><td >DHE-RSA-AES128-SHA</td>
<td >DHE-RSA-AES128-SHA256</td>
<td >DHE-RSA-AES128-GCM-SHA256</td></tr>
<tr><td >DHE-DSS-AES128-SHA</td>
<td >DHE-DSS-AES128-SHA256</td>
<td >DHE-DSS-AES128-GCM-SHA256</td></tr>
<tr><td >ECDH-RSA-AES128-SHA</td>
<td >ECDH-RSA-AES128-SHA256</td>
<td >ECDH-RSA-AES128-GCM-SHA256</td></tr>
<tr><td >ECDH-ECDSA-AES128-SHA</td>
<td >ECDH-ECDSA-AES128-SHA256</td>
<td >ECDH-ECDSA-AES128-GCM-SHA256</td></tr>
<tr><td >CAMELLIA128-SHA</td>
<td >DH-RSA-CAMELLIA128-SHA</td>
<td >DHE-RSA-CAMELLIA128-SHA</td></tr>
<tr><td >PSK-RC4-SHA</td>
<td >DH-DSS-CAMELLIA128-SHA</td>
<td >DHE-DSS-CAMELLIA128-SHA</td></tr>
<tr><td >AES128-SHA</td>
<td >AES128-SHA256</td>
<td >AES128-GCM-SHA256</td></tr>
<tr><td >SEED-SHA</td>
<td >DH-RSA-SEED-SHA</td>
<td >DH-DSS-SEED-SHA</td></tr>
<tr><td >DES-CBC3-SHA</td>
<td >DHE-RSA-SEED-SHA</td>
<td >DHE-DSS-SEED-SHA</td></tr>
<tr><td >IDEA-CBC-SHA</td>
<td >PSK-AES256-CBC-SHA</td>
<td >PSK-AES128-CBC-SHA</td></tr>
<tr><td >EDH-RSA-DES-CBC3-SHA</td>
<td >ECDH-RSA-DES-CBC3-SHA</td>
<td >ECDHE-RSA-DES-CBC3-SHA</td></tr>
<tr><td >EDH-DSS-DES-CBC3-SHA</td>
<td >ECDH-ECDSA-DES-CBC3-SHA</td>
<td >ECDHE-ECDSA-DES-CBC3-SHA</td></tr>
<tr><td >RC4-SHA</td>
<td >ECDH-RSA-RC4-SHA</td>
<td >ECDHE-RSA-RC4-SHA</td></tr>
<tr><td >RC4-MD5</td>
<td >ECDH-ECDSA-RC4-SHA</td>
<td >ECDHE-ECDSA-RC4-SHA</td></tr>
<tr><td >SRP-3DES-EDE-CBC-SHA</td>
<td >SRP-RSA-3DES-EDE-CBC-SHA</td>
<td >SRP-DSS-3DES-EDE-CBC-SHA</td></tr>
<tr><td >DH-DSS-DES-CBC3-SHA</td>
<td >DH-RSA-DES-CBC3-SHA</td>
<td >-</td></tr>
</tbody></table>

