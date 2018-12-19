You usually need to configure a public network sub-domain name for a group of CVMs, which can be easily done in Cloud DNS. An example is provided below.

Suppose you already added a domain name called "qcloud-example.com" (this is only used as an example. Please use the domain name you added during actual operation), our goal is to configure a public network sub-domain name `www.qcloud-example.com` for a group of CVMs.

### Click **Add Record** in the record management page
![](//mc.qcloudimg.com/static/img/946e83baba710ad61e51263551870afd/image.png)
### Select the type for Associate Cloud Resource of A record
In the **Add Record** tab, enter "www" as host name (the "www" in `www.qcloud-example.com` is called the host name), record type is A, then choose **Associate Cloud Resource**. A pop-up window will list all CVMs you have purchased with public IPs. Select a group of CVMs and click **OK** to submit, and the newly added record will appear in the record list, with the sub-domain name's line type being "default", as shown in this figure:
![](//mc.qcloudimg.com/static/img/9fa144ec34bea93527d22b1555d108a0/image.png)
![](//mc.qcloudimg.com/static/img/b3db9a0a7a8b3c0b3e28a3ada5c4b371/image.png)
![](//mc.qcloudimg.com/static/img/2f4c31232aef6185e03bf0c8121fce6f/image.png)
### Test
Now, try to access `www.qcloud-example.com`. You can also execute "dig www.qcloud-example.com -t A", if the two cloud service public IPs 123.207.67.60 and 123.207.43.183 are included in the returned result, then the resolution of this record is functional.

