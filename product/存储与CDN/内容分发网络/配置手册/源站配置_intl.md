You may modify the origin server configuration for your domain:



+ Switching between own origin and COS origin is supported;

+ You can configure hot slave origin servers for a domain whose connection method is own origin. When a back-to-origin request towards the master origin encounters an error (including 4XX or 5XX error codes and TCP connection error), the request will be forwarded to the slave origin server;

+ The switching between master and slave origin configurations is supported.



Configuring hot slave origin server can effectively reduce failure rate of back-to-origin requests and improve your business.

<font color="red">HTTPS back-to-origin method is currently not supported by slave origin servers. Please do not choose HTTPS back-to-origin method when configuring certificates for domains with hot slave origin servers.</font>



## Modifying Origin Server



Switching between own origin and COS origin is supported to provide a higher flexibility.



Log in to [CDN Console](https://console.cloud.tencent.com/cdn) and go to "Domain Management" page. Then click **Manage** button to the right of the domain name to enter the management page:

![](https://mc.qcloudimg.com/static/img/f92d2ef7e4be2b69185ab43228f025ef/1.png)



Go to **Origin Server Info** under "Basic Configuration" to view the current origin server configuration of the domain:

![](https://mc.qcloudimg.com/static/img/3d4ec364b6c1f09a064cce3e65ba378a/CDN-Configuration+management-+Basic+Configurations-Origin+Config.png)



Click the modify button at the top-right corner of the origin server configuration to make changes. **Switching between COS origin and own origin is supported**:



![](https://mc.qcloudimg.com/static/img/5e83d9cde4f15cdd6d4a56274a520980/3.png)



## Adding Hot Slave Origin Server



You can add hot slave origin servers for a domain **whose connection method is own origin**. When a back-to-origin request towards the master origin encounters an error (including 4XX or 5XX error codes and TCP connection error), the request will be forwarded to the slave origin server.



![](https://mc.qcloudimg.com/static/img/600a79eb7c31038e02308ebde0a8af28/4.png)



Hot slave origin servers can only be configured as **own origins**:



![](https://mc.qcloudimg.com/static/img/8e67e4f369eef169113f101d24e16051/5.png)





## Switching between master and slave origin configurations



Once slave origin server is configured, you can witch between the master and slave origin server configurations with one click:



![](https://mc.qcloudimg.com/static/img/bc30ebce0cc78569066aab8588453516/6.png)


