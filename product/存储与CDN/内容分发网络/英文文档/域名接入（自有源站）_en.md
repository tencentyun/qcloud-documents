If you already have a stable business server (origin server), you can connect to the CDN using own origin without modifying the origin server and enjoy acceleration service after completing CDN console connection process and DNS configuration. Please proceed as follows:

## STEP One: Connect a Domain
Log in to [CDN Console](https://console.cloud.tencent.com/cdn) and click **Create a distribution** in the **Domain Management** page:

![](https://mc.qcloudimg.com/static/img/fd1298d36e50a667aecae4ca6bdab9eb/%5B1%5D+cdn_access_create_a_distribution.png)

Enter the acceleration domain in the **Domain** field. The following conditions must be met:

+ The domain has been recorded by MIIT;
+ The domain has not yet connected to any Tencent Cloud CDN.

Support batch connection, up to 10 domains at a time.

![](https://mc.qcloudimg.com/static/img/5a1a96eeccbe218aaf0d09b1045eea13/2.png)

In the **Project** field, select the corresponding project for the domain to manage sub-projects. The projects here are shared for all Tencent Cloud products, you can add projects in [Project Management](https://console.cloud.tencent.com/project).

Select **Own origin** in the **Origin type** and enter origin information at the origin IP address or domain field. The IP address and origin domain need to meet the following conditions:

- For origin domain, the domain **must not** be the same as the connecting domain (the connected acceleration domain) and the ports (**1-65535**) using "domain:port" is supported;
- For origin IP, multiple origin IPs and custom ports (**1-65535**) using "IP:port" are supported. When entering multiple IPs, back-to-origin requests will access each IP in sequence;
- Cannot enter private IPs.

Select a content type in the **Content type** field:

+ Static content: Domains of this content type will be placed into the CDN static acceleration pool. This is recommended if your origin server falls into the category of website, e-commerce, game or image;
+ Media streaming: Domains of this content type will be placed into the CDN streaming media acceleration pool. This is recommended if your origin server falls into the category of LVB or ILVB;
+ Downloading: Domains of this content type will be placed into the large file downloading acceleration pool. This is recommended if your origin server falls into the category of mobile phone firmware, audio & video source file or game installer distribution.

![](https://mc.qcloudimg.com/static/img/194b11ed28ac620b19476a125d4cbb4d/3.png)

Click "Submit":

![](https://mc.qcloudimg.com/static/img/0a03db953d30949addab41f3c7078a45/4.png)


## STEP Two: Configure CNAME
You can view the acceleration CNAME that CDN has assigned to your domain in the page of domain management. You will need to go to the DNS service provider of the connection domain (such as Dnspod) and add a CNAME record for the domain. Acceleration service will become available once **this DNS configuration takes effect**. (How to configure? [Click here](https://cloud.tencent.com/doc/product/228/3121)).
