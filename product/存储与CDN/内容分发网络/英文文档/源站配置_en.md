You can modify the configuration of the origin server for your domain name:
+ Support multiple self-owned origin servers: When multiple IPs are configured as the origin server IP, the CDN uses polling policy for origin-pull, and a random IP is selected for origin-pull. The CDN also performs origin server detection. When an origin server IP is found to be exceptional, it is blocked for a period of time and skipped during origin-pull.
+ COS bucket can be configured as the origin server.
+ You can configure hot backup origin servers for a domain name whose access method is self-owned origin. When an origin-pull request to the master origin server encounters an error (including 4XX or 5XX error codes and TCP access error), the request is directly forwarded to the hot backup origin server.
+ The switching between master/slave origin server configurations is supported.

Configuring hot backup origin server can effectively reduce failure rate of origin-pull requests and improve your service quality.
> **Note**: HTTPS origin-pull method is not supported by hot backup origin servers. Do not choose HTTPS origin-pull method when configuring certificates for domain names with hot backup origin servers.

## Configuration
Log in to [CDN Console](https://console.cloud.tencent.com/cdn), select "Domain Management" in the left navigation bar, and click "Manage" to the right of the domain name to be edited.
![](https://mc.qcloudimg.com/static/img/f2f50e0d81eb0a8c0dcb61d2ee37e6c9/manage.png)
By clicking "Basic Configuration", you can view the origin server configuration of the domain name in the **Origin server info** module.
![](https://mc.qcloudimg.com/static/img/7e218acca2ef3a4f146afe74e35bc129/host_info.png)

## Modifying Origin Server
You can modify the type of master origin server on the CDN console. Switching between self-owned origin server and COS origin server is supported.
> **Note**: Only the origin servers of the domain names accessed by users can be modified, rather than those of the CDN accelerated domain names automatically created by Bucket in [Cloud Object Storage](https://cloud.tencent.com/product/cos).

Click "Modify" button on the upper right corner of **master origin server** to modify the configuration of origin server, and switch between COS origin server and self-owned origin server.
![](https://mc.qcloudimg.com/static/img/05bbce4f60fe74c679f218de44551407/origin_change.png)

## Adding Hot Backup Origin Server
When an origin-pull request to the master origin server encounters an error (including 4XX or 5XX error codes and TCP access error), the request is directly forwarded to the hot backup origin server.
You can click "Add hot backup origin server" for configuration in **Origin server info** module of "Basic info". The hot backup origin server can only be configured as **Self-owned origin server**, and the self-owned origin domain name can be configured as origin server address.
![](https://mc.qcloudimg.com/static/img/04bcc3829b957f9f33e118b3076c817c/back_origin.png)

## Switching Between Master/Slave Origin Server Configurations
When the slave origin server is configured, click "Master/Slave Switch" icon to switch between master/slave origin server configurations.
![](https://mc.qcloudimg.com/static/img/1fd99aab6968ee200b94abb3e59bf056/switch.png)
