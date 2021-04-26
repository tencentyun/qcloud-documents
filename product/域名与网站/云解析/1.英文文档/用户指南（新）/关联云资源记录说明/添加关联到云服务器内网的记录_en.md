Do you often add records into "/etc/hosts" of your CVM, and configure private network domain names for other CVMs to make the access more convenient through private network? Are you having a headache because hosts are both troublesome to configure and difficult to manage in a unified manner?

You no longer need to worry about it with the help of Tencent Cloud DNS. By configuring the records that are associated to CVM private network, you can easily configure domain names for a group of CVMs in private network. An example is provided below.

Suppose you already added domain name "qcloud-example.com" in Cloud DNS (this is only used as an example. Please use the domain name you added during actual operation), our goal is to add a private network sub-domain name "internal.qcloud-example.com" for "qcloud-example.com" and direct this sub-domain name to a group of specified CVM private network IPs.

### Click **Add Record** in the record management page
![](//mc.qcloudimg.com/static/img/946e83baba710ad61e51263551870afd/image.png)
### Select the type for Associate Cloud Resource of A record
In the **Add Record** tab, record type" is A, choose "Yes" for "Associate Cloud Resource", enter "internal" as the host name. A pop-up window will list all CVMs you have purchased. Select a group of CVMs and click **OK** to submit. The newly added record will appear in the record list, and the sub-domain name is only resolved in the private network, as shown in the figure below.
![](//mc.qcloudimg.com/static/img/2a807321f1e64bdd40555269d3cec389/image.png)
![](//mc.qcloudimg.com/static/img/d9f61a3464e523a44ed17be17b386d29/image.png)
![](//mc.qcloudimg.com/static/img/310e795ca0d0136397357c7a97888c8b/image.png)
### Test
Now, log in to any of your CVMs and try accessing "internal.qcloud-example.com". You can also execute "dig internal.qcloud-example.com -t A" on any CVM, if the two private IPs 10.104.117.138 and 10.104.125.171 are included in the query result, then the resolution of this private network sub-domain name is functional.

