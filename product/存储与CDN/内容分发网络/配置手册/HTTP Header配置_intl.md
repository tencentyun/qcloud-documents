## Overview
Generally, there are two types of HTTP messages:

+ Request message sent from client to server
+ Response message sent from server to client

Both types of the messages consist of a start line, one or more header fields, a blank line indicating the end of header field, and optionally, a message body. There are four types of HTTP header fields: general header, request header, response header and entity header. Each header field consists of a name (Key), colon (:) and a Value.

Tencent Cloud provides HTTP Header Configuration which allows such features as cross-domain access by <font color="red">adding </font> configured header field in the returned **response message** when your user requests for service resource.

**Note:**

+ If resource is not hit at a node, the request will go back to origin. In this case, the header information returned from origin server will be returned to user altogether; If resource is hit in the cache at a node, CDN will return cached Access-Control-Allow-Origin, Timing-Allow-Origin, Content-Disposition and Accept-Ranges header information of the origin server to the user by default. If you wish to cache all of headers from origin, please submit a ticket and request for manual configuration support;
+ HTTP Header configuration is specific to a domain. Once the configuration takes effect, the configured header field will be added to user's response messages to any of the resources under this domain;
+ Configuring HTTP Header will only affect the response behaviors of the client (such as browser), and will not affect caching behaviors of CDN nodes;
+ <font color="red">By default, CDN will inherit Access-Control-Allow-Origin and Content-Disposition header fields from the origin server, please avoid configuring origin server and CDN at the same time.</font>


## Configuration Instructions

CDN provides the following five header field configurations:

+ Content-Disposition: Enable customized resource downloading configuration and default file name upon downloading;
+ Content-Language: Specify resource response language at the client (such as browser);
+ Access-Control-Allow-Origin: Specify the request origins allowed to access the resource for a cross-domain request;
+ Access-Control-Allow-Methods: Specify the request methods allowed for a cross-domain request;
+ Access-Control-Max-Age: Specify the maximum time span during which the returned result of pre-request for a particular resource is cached for a cross-domain request.


### General Configurations

#### Content-Disposition
Content-Disposition is used to enable the downloading of browser and set the default name for the downloaded file. If the type of the file sent from server to client browser is supported by the browser (such as txt, jpg), the file will be directly opened in the browser by default. If you want the user to be prompted to save the file, you can configure Content-Disposition field to override browser's default behavior. Common configurations are shown below:

> Content-Disposition：attachment;filename=FileName.txt

#### Content-Language
Content-Language is used to define the language code used in the page. Common configurations are shown below:

> Content-Language: zh-CN
> Content-Language: en-US


### Cross-domain Configurations
Cross-domain means that the resource from one domain (for example, www.abc.com) makes a request for a resource under another domain (for example, www.def.com). Since the resources belong to different domains, this is considered **cross-domain**. Moreover, different protocols or different ports will also cause cross-domain access. When this happens, cross-domain related configurations need to be added in the Response Header, so that the resource making the request can get the data it wants.

#### Access-Control-Allow-Origin
Access-Control-Allow-Origin is used to solve cross-domain permission issues for resources. The field value defines which domains are allowed to reference this resource. You can also set wildcard "*" to allow all domains to reference the resource. Common configurations are shown below:

>Access-Control-Allow-Origin: *
>Access-Control-Allow-Origin: ```http://www.test.com```

**Note**:

+ Wildcard domain names are not supported (such as *\.qq.com)
+ Either use "*" or specify a URI
+ Please add http:// or https:// as prefix when configure specified domain name;



#### Access-Control-Allow-Methods 
You can configure multiple allowed cross-domain request methods using Access-Control-Allow-Methods:

> Access-Control-Allow-Methods: POST, GET, OPTIONS


#### Access-Control-Max-Age
Access-Control-Max-Age specifies the valid time of pre-request.

For non-simple cross-domain requests, an additional HTTPS query request ("pre-request") is needed before the formal communication to check whether the cross-domain request is secure and acceptable. In any of the following situations, the request will be considered as a pre-request:

+ The request is initiated using a method other than GET, HEAD or POST or it is initiated using POST with a data type other than application/x-www-form-urlencoded, multipart/form-data and text/plain, such as application/xml or text/xml;
+ A custom request header is used.

Access-Control-Max-Age is measured in second. Here is a configuration example:

>Access-Control-Max-Age: 1728000

This indicates no more pre-request will be sent for the cross-domain access to this resource within 1,728,000 seconds (20 days).

### Configuration Process
Log in to [CDN Console](https://console.cloud.tencent.com/cdn) and go to "Domain Management" page. Then click **Manage** button to the right of the domain name to enter the management page:

![](https://mc.qcloudimg.com/static/img/f92d2ef7e4be2b69185ab43228f025ef/1.png)

Go to "Advanced Configuration" and find "HTTP header Configuration", then click "Add HTTP header":

![](https://mc.qcloudimg.com/static/img/1956e1d87d64a5ca643b1c703f5b9882/2.png)

Select the header to add and complete the configuration for it. You can add multiple headers at a time, **but the same header can only be added once**:

![](https://mc.qcloudimg.com/static/img/8f3061d288e85a45e41b86de84462565/3.png)

Click OK to complete configuration. It will take about 5 minutes for the configuration to take effect:

![](https://mc.qcloudimg.com/static/img/1713012b7cb4c29781f55248996fa2a3/4.png)

You can also modify or delete existing headers.
