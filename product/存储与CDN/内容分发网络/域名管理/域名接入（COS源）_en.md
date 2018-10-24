If you wish to use Tencent Cloud's [Cloud Object Storage](https://cloud.tencent.com/product/cos.html) due to limited capacity of your business server, or if you're already using Tencent Cloud's Cloud Object Storage, you can directly use COS origin as the origin type and connect your domain to CDN.

## STEP One: Connect a Domain
Log in to [CDN Console](https://console.cloud.tencent.com/cdn) and click **Create a distribution** in the **Domain Management** page:
![](https://mc.qcloudimg.com/static/img/fd1298d36e50a667aecae4ca6bdab9eb/%5B1%5D+cdn_access_create_a_distribution.png)

Step 1. Enter the acceleration domain in the **Domain** field. The following conditions must be met:

+ The domain has been recorded by MIIT;
+ The domain has not yet connected to any Tencent Cloud CDN.

Support batch connection, up to 10 domains at a time.

![](https://mc.qcloudimg.com/static/img/5a1a96eeccbe218aaf0d09b1045eea13/2.png)

Step 2. Select a content type in the **Content type** field. In the **Project** field, select the corresponding project for the domain to manage sub-projects. The projects here are shared for all Tencent Cloud products, you can add projects in [Project Management](https://console.cloud.tencent.com/project);

Step 3. Select **Object storage (COS)** in **Origin type** and select the corresponding origin server bucket:

+ Once you have selected bucket as the origin server, you can manage the content of the origin server in [COS Console](https://console.cloud.tencent.com/cos);
+ If there is no bucket in the corresponding project when you select the COS origin, you will need to log in to [COS Console](https://console.cloud.tencent.com/cos) to create a bucket.

![](https://mc.qcloudimg.com/static/img/ab9889fc2079a65d713bb0445861ac01/3.png)

Step 4. Select a content type in the **Content type** field and its corresponding configuration:

- Static content: Domains of this content type will be placed into the CDN static acceleration pool. This is recommended if your origin server falls into the category of website, e-commerce, game or image;
- Media streaming: Domains of this content type will be placed into the CDN streaming media acceleration pool. This is recommended if your origin server falls into the category of LVB or ILVB;
- Downloading: Domains of this content type will be placed into the large file downloading acceleration pool. This is recommended if your origin server falls into the category of mobile phone firmware, audio & video source file or game installer distribution.

![](https://mc.qcloudimg.com/static/img/194b11ed28ac620b19476a125d4cbb4d/3.png)

Step 5. Click "Submit" to add domain

![](https://mc.qcloudimg.com/static/img/0a03db953d30949addab41f3c7078a45/4.png)

## STEP Two: Confirm the Status
You can go to **Domain Management** page to check the current status of your connected domain:

![](https://mc.qcloudimg.com/static/img/2cdcd2ac2041dd8473013a4b7c9d6191/4.png)

## STEP Three: Configure CNAME
You can view the acceleration CNAME (suffixed with **.cdn.dnsv1.com**) that CDN has assigned to your domain in the status displayed in step 5. You will need to go to the DNS service provider of the connection domain (such as Dnspod) and add a CNAME record for the domain. Acceleration service will become available once **this DNS configuration takes effect**. (How to configure? [Click here](https://cloud.tencent.com/doc/product/228/3121)). 
