You may modify the origin server configuration for your domain:



+ Switching between own origin and COS origin is supported;

+ You can configure hot slave origin servers for a domain whose connection method is own origin. When a back-to-origin request towards the master origin encounters an error (including 4XX or 5XX error codes and TCP connection error), the request will be forwarded to the slave origin server;

+ The switching between master and slave origin configurations is supported.



Configuring hot slave origin server can effectively reduce failure rate of back-to-origin requests and improve your business.

<font color="red">HTTPS back-to-origin method is currently not supported by slave origin servers. Please do not choose HTTPS back-to-origin method when configuring certificates for domains with hot slave origin servers.</font>



## Modifying Origin Server



Switching between own origin and COS origin is supported to provide a higher flexibility.



Log in to [CDN Console](https://console.qcloud.com/cdn) and go to "Domain Management" page. Then click **Manage** button to the right of the domain name to enter the management page:



![](https://mc.qcloudimg.com/static/img/70a01c53cfaa997013da2cb4b699bbf1/donmai_management.png)



Go to **Origin Server Info** under "Basic Configuration" to view the current origin server configuration of the domain:



![](https://mc.qcloudimg.com/static/img/6fb7c96bdd79b1ee3b45b4961972e163/change_origin.png)



Click the modify button at the top-right corner of the origin server configuration to make changes. **Switching between COS origin and own origin is supported**:



![](https://mc.qcloudimg.com/static/img/8c30c6b8c0a38f9afa14c78f29bd9a0a/change_origin_cos.png)



## Adding Hot Slave Origin Server



You can add hot slave origin servers for a domain **whose connection method is own origin**. When a back-to-origin request towards the master origin encounters an error (including 4XX or 5XX error codes and TCP connection error), the request will be forwarded to the slave origin server.



![](https://mc.qcloudimg.com/static/img/cd704a8f4742c94847621a327880fee0/back-up.png)



Hot slave origin servers can only be configured as **own origins**:



![](https://mc.qcloudimg.com/static/img/7cd5ee81ef3a61c69890cd8dcaea4eaf/set_back_up.png)





## Switching between master and slave origin configurations



Once slave origin server is configured, you can witch between the master and slave origin server configurations with one click:



![](https://mc.qcloudimg.com/static/img/fb6c82e8f703b1248624a8e865c95854/switch_backup.png)






