### 1. Does Tencent Cloud CDN have international acceleration capability?
International acceleration is already available in Tencent Cloud CDN. With nodes established over ten years, Tencent Cloud CDN has deployed over 100 acceleration nodes in more than 30 countries worldwide, which allow it to provide international acceleration capabilities.

### 2. Does the origin server need to make some changes before user enjoys acceleration service after accessing CDN?
Basically, no change is needed. However, in order to achieve a better acceleration, we recommend that you assign static and dynamic files to different domain names and only accelerate the static resources.

### 3. Does Tencent Cloud CDN support cross-domain access?
No restriction is imposed on the cross-domain access in Tencent Cloud CDN. If cross-domain access is needed for your website, you simply need to configure the Access-Control-Allow-Origin field in your website, or configure cross-domain headers for your domain name in the CDN. For more information, please see [HTTP Header Configuration](https://cloud.tencent.com/doc/product/228/6296).

### 4. Where can I download the CDN access log?
You can download the CDN access log in the CDN console. For more information, please see [Download Log](https://cloud.tencent.com/document/product/228/6316#.E6.97.A5.E5.BF.97.E4.B8.8B.E8.BD.BD).

### 5. How to use the self-troubleshooting tool?
The self-troubleshooting tool provides a range of diagnostic features such as testing for DNS resolution, link quality, site availability and data access consistency for accessing domain name. For more information, please see [Self-Troubleshooting](https://cloud.tencent.com/document/product/228/6304).

### 6. What is the difference between local access diagnostics and user access diagnostics?
Local Access Diagnostics: When you find an error with one of your resource accesses, you can initiate a test with "Local Access Diagnostics".
User Access Diagnostics: When your user reports an error with resource access, you can pinpoint the problem through "User Access Diagnostics" and solve the problem by performing the actions suggested by Tencent Cloud.

### 7. Does CDN support POST requests?
Yes. CDN supports POST requests.

### 8. Does CDN support the origin server's Cache-Control setting?
By default, Tencent Cloud CDN supports origin server's Cache-Control setting.

### 9. Does CDN support GZIP compression?
In order to save your traffic, CDN compresses the files with a size between 256 Byte and 2048 KB and a filename extension of .js, .html, .css, .xml, .json, .shtml, and .htm to Gzip files by default.

### 10. Does CDN accelerator support non-80 ports?
CDN accelerator supports ports 80, 443 and 8080.

### 11. What is CDN intermediate origin server?
CDN intermediate origin server is an intermediate-layer origin-pull server located between the business server and CDN node. The intermediate origin server converges the node's origin-pull requests to reduce the origin-pull pressure on your origin server.

