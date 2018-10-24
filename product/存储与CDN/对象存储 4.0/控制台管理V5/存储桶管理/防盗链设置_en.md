## Basic Concepts

To prevent malicious programs from cheating in public network traffic through resource URLs, thus causing unnecessary losses to you, and prevent them from stealing the website's resources by malicious means, Bucket provides hotlink protection configurations. We recommend that you configure the blacklist and whitelist through the console for safety protection by constraining the value of the referer field in the HTTP request header.

## Configuration Instructions

Enter the COS console, click **Basic Configuration** above the Bucket for which hotlink protection needs to be configured:

![](https://mc.qcloudimg.com/static/img/7affe351956ede6c475d349f380f6a2b/image.png)

Configuring hotlink protection:

![](https://mc.qcloudimg.com/static/img/665340c9b36cd513f8a8f4f8a131b394/image.png)


Status: After the hotlink protection is enabled, the corresponding domain must be filled in.

List type: You can set the domains to the blacklist or whitelist.

> Blacklist: The domains in the list are not allowed in the HEADER's Referer field, otherwise a failure will be returned.
>
> Whitelist: Only the domains in the list are allowed in the HEADER's Referer field, otherwise a failure will be returned.

*Note: If a CDN domain is used to accelerate the access, the hotlink protection rules of CDN are matched first, and then the hotlink protection rules of Cloud Object Storage are matched.*

## Note
The list supports multiple domains and prefix match. Each domain occupies one line, for example:

> If www.qq.com is set, the following values of Referer all match the list:
>
> `http://www.qq.com/123`
>
> `http://www.qq.com.cn`

Domains and IPs with ports are supported, for example:

> abc.qq.com:8080
>
> 123.2.4.8:8080

The asterisk wildcard (*) is supported for secondary domain or multi-level domain wildcarding, for example:

> If *.qq.com is set, the following values of Referer all match the list:
>
>` http://a.b.qq.com/123`
>
> `http://a.qq.com`

If Referer is blank (in the case of access via browser), no matching rule is used by default:

> If the user set a blacklist: the blank referer request will not be blocked by the blacklist rules, and COS returns the requested information;
>
> If the user set a whitelist: the blank referer request will not hit the whitelist rules, and COS rejects returning the requested information;

*Note: If a CDN domain is used to accelerate the access, the hotlink protection rules of CDN are matched first, and then the hotlink protection rules of Cloud Object Storage are matched.*

## Example

A user creates a Bucket, and places an image 1.jpg under the root directory. An access address `testbucket-1250000000.file.myqcloud.com/1.jpg` is generated based on the rules.

The user has a website www.example.com, and embeds the image in the home page index.html.

A webmaster who holds www.fake.com wants to put this image in his website, but he does not want to pay for the traffic, so he cites this image directly through the address `testbucket-1250000000.file.myqcloud.com/1.jpg` and places it on his home page index.html.

**Before enabled**

> Visit `http://www.example.com/index.html`, and the image displays normally.
>
> Visit `http://www.fake.com/index.html`, and the image also displays normally.

**Enabling method 1**

> The user configures Referer to the **blacklist** mode in COS, fills in *.fake.com and saves it to make it effective.
>
> Visit `http://www.example.com/index.html`, and the image displays normally.
>
> Visit `http://www.fake.com/index.html`, and the image cannot be displayed.

**Enabling method 2**

> The user configures Referer to the **whitelist** mode in COS, fills in *.example.com and saves it to make it effective.
>
> Visit `http://www.example.com/index.html`, and the image displays normally.
>
> Visit `http://www.fake.com/index.html`, and the image cannot be displayed.


