## Basic Concepts

Users can access the objects in the Bucket via the following addresses:

- Default domain


- CDN accelerated domain


- Custom domain

The COS default domain is defined by Tencent Cloud and is unchangeable. If users use the domain to access COS resources through Tencent Cloud internal services, the request will be sent and received in the private network environment; if users use the domain to access COS resources from the public network, the request for the files will be sent from the public network to COS. CDN accelerated domain is initialized by Tencent Cloud and is changeable (CNAME is required). An access request will travel through more than 500 CDN accelerated nodes. The custom domain can be mapped with the CNAME by users and is suitable for the scenarios where the Tencent Cloud address identifier "qcloud" needs to be shielded.


## Default Domain

The COS default domain is defined by Tencent Cloud and is unchangeable. It can be used for the request for Tencent Cloud internal services and direct access from the public network. After a Bucket is created, Tencent Cloud will automatically generate a default domain name with the format:

`[bucketname]-[appid].cos[area].myqcloud.com`
`For example: test-1250000000.cosgz.myqcloud.com`

This domain name is unchangeable.

To obtain the URL corresponding to the resource in each Bucket, you just need to add the relative path after the Bucket domain name, for example:

`http://testbucket-1250000000.cosgz.myqcloud.com/test.txt`

If the permission to the resource is private, you need to add the signature suffix after the above URL

Enter the COS Console, click the Bucket name to enter the management page, then click "Domain Management" tab to view the default domain

![](https://mc.qcloudimg.com/static/img/4fd194c09b5a2c994867238878649d77/image.png)

**Default domain - cross-region access in private network: Default domain can be used for the access among different Tencent Cloud products in the same region. However, to achieve cross-region access in private network, for example, if a CVM in Guangzhou needs to use the data on the Singapore COS, you need to use a VPC to deploy a dedicated network tunnel to achieve high-speed access.  [Click to view information on VPC](https://cloud.tencent.com/product/vpc.html)**


## CDN Accelerated Domain

CDN accelerated domain is initialized by Tencent Cloud and is changeable (CNAME is required). An access request will travel through more than 500 CDN accelerated nodes which can give a higher bandwidth and lower latency. After a Bucket is created, Tencent Cloud will automatically generate a default domain name with the format:

`[bucketname]-[appid].file.myqcloud.com`

You can enable CDN acceleration when creating the Bucket. You can also enable CDN acceleration in "Domain Management" on COS Console later. In this case, direct access from the public network to the CDN accelerated domain can be achieved, for example:

`http://testbucket-1250000000.file.myqcloud.com/testdir/test.txt`

At the same time, a new domain, which is the CDN accelerated domain, will be added in the CDN Console.

**Note: A maximum of 100 CDN accelerated domains can be created under an APPID.**

Users can also modify the CDN accelerated domain:

Enter the COS Console, select "Bucket List" page, and click a Bucket.

![](https://mc.qcloudimg.com/static/img/297fc0dfb01119f83f1fe788a868e45f/image.png)

Enter the **Domain Management** page, select **Accelerated Domain**, and click **Edit** to enable CDN acceleration.

![](https://mc.qcloudimg.com/static/img/1ccf623ef070b8d689825090ea32ceb7/image.png)

## Custom Domain

In some cases, users don't want such domains as "qcloud.com" to be shown on the website or in any services. For example, to host a website on Tencent Cloud COS, a user may choose `http://myblog.net/`, instead of `http://myblog-1250000000.file.myqcloud.com`.

You can achieve this by customizing domain. You need to create a CNAME record on CDN Console to map `http://myblog.net/` to `http://myblog-1250000000.file.myqcloud.com`.

You can directly point to the Bucket by adding a custom domain, and directly access the content in the Bucket using the bound custom domain. After adding the custom domain, you can also enable CDN acceleration to accelerate access. To avoid any security issues involved in the services, you're recommended to use a custom domain to access COS;

- To ensure the normal access to COS using the custom domain, you need to change the DNS record CNAME to the specified address to make the domain take effect.
- The bound custom domain must be licensed by MIIT, otherwise the access from the domain will not work.

Enter the COS Console, select "Bucket List" page, and click a Bucket

![](https://mc.qcloudimg.com/static/img/297fc0dfb01119f83f1fe788a868e45f/image.png)

## Example 1 (Enabling CDN Acceleration)

### Selecting a Bucket

Enter the COS Console, select "Bucket List" page, and click a Bucket

![](//mccdn.qcloud.com/static/img/ac01c306c5314d64b1afce45e7c0a093/image.png)

### Adding a Domain

Enter the **Domain Management** page, select *Custom domain**, and click **Add a domain** to add an existing domain.

![](//mccdn.qcloud.com/static/img/00c00593d5dfc71feef320d226bd18b6/image.png)

Copy **CNAME address**,

![](//mccdn.qcloud.com/static/img/c620574738d836d2a4ba96b26a3eef51/image.png)

### Domain Resolution

Enter the cloud resolution console, and click the bound custom domain.

![](//mccdn.qcloud.com/static/img/706dbd1854f7ac85768a8dffc58e130c/image.png)

Add a CNAME record.

![](//mccdn.qcloud.com/static/img/56678b11886365cff3c9c258076d3424/image.png)

*Note: The record value is the CNAME address you just copied. It will take about 15 minutes for the record added to take effect, please wait a moment.*

### Result Validation

After the binding of custom domain, you can download the files in the Bucket using the custom domain address. Let's suppose that there is an index.htm file in your testnew Bucket, and the bound custom domain is www.srcostest.com:

**Before Binding**

The access URL can be the combination of default domain for public network access with file path: testnew-10014284.cos.myqcloud.com/index.htm

![](//mccdn.qcloud.com/static/img/939165a47b8da3c678577a9ff945e80a/image.png)

**After Binding**

The access URL can be the combination of custom domain with file path: www.srcostest.com/index.htm

![](//mccdn.qcloud.com/static/img/32e0a9be3c5fc82754014ccc497c4b1d/image.png)

> Note: If static website feature is enabled, you can directly open and view the file using the custom domain. For the instructions on how to enable the static website feature, please refer to [Static Website Hosting](/doc/product/430/5896).

## Example 2 (Disabling CDN Acceleration)

### Selecting a Bucket

Enter the COS Console, select "Bucket List" page, and click a Bucket.

![](//mccdn.qcloud.com/static/img/ac01c306c5314d64b1afce45e7c0a093/image.png)

Copy the **public network access address**

![](//mc.qcloudimg.com/static/img/38bbe6419e5df31cee3e8d083e620de5/image.png)

### Domain Resolution

Enter the cloud resolution console, and click the bound custom domain.

![](//mccdn.qcloud.com/static/img/706dbd1854f7ac85768a8dffc58e130c/image.png)

Add a CNAME record.

![](//mc.qcloudimg.com/static/img/a626c5a09f1e12c8bb772c6238d1b812/image.png)

*Note: The record value is the public network access address you just copied. It will take about 15 minutes for the record added to take effect, please wait a moment.*

### Adding a Domain

Enter the **Domain Management** page, select *Custom domain**, and click **Add a domain** to add an existing domain.

![](//mc.qcloudimg.com/static/img/d653a13cfd55c55b1e88baabef37cf36/image.png)

*Note: You need to disable CDN acceleration when adding a domain. After several minutes, the domain status will become "Enabled".

### Result Validation

After the binding of custom domain, you can download the files in the Bucket using the custom domain address. Let's suppose that there is an index.htm file in your testnew Bucket, and the bound custom domain is www.srcostest.com:

**Before Binding**

The access URL can be the combination of default domain for public network access with file path: testnew-10014284.cos.myqcloud.com/index.htm

![](//mccdn.qcloud.com/static/img/939165a47b8da3c678577a9ff945e80a/image.png)

**After Binding**

The access URL can be the combination of custom domain with file path: www.srcostest.com/index.htm

![](//mccdn.qcloud.com/static/img/32e0a9be3c5fc82754014ccc497c4b1d/image.png)

> Note: If static website feature is enabled, you can directly open and view the file using the custom domain. For the instructions on how to enable the static website feature, please refer to [Static Website Hosting](/doc/product/430/5896).

