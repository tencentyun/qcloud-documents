When your domain name accesses the CDN, the system automatically assigns a CNAME (suffixed with "```.cdn.dnsv1.com```") to you. It cannot be directly accessed. You need to complete the CNAME configuration at the domain name service ISP. After the configuration takes effect, you can use the CDN acceleration service.
![](https://mc.qcloudimg.com/static/img/1ad97c3a92340219c728f25290ca1f78/CNAME.png)
## Setting on Tencent Cloud
If your DNS service ISP is Tencent Cloud, you can add a CNAME record as follows.
1. Log in to [Domain Name Management](https://console.cloud.tencent.com/domain) console and click "Resolve" to the right of the domain name to which you want to add the CNAME record.
![](https://mc.qcloudimg.com/static/img/d736722a9a2f0788f55c3ea10320baab/mydomain.png)
2. After you are directed to the **Record Management** page of the specified domain name, click "Add Record".
![](https://mc.qcloudimg.com/static/img/280a9f09e37eeb5938a8b10b7e671b9c/add_record.png)
3. In the pop-up window, set the **Record Type** to CNAME, enter the domain name prefix (such as: www) in **Server Record**, enter the CNAME domain name in **Record Value**, and a CNAME record is added after you click "OK".
![](https://mc.qcloudimg.com/static/img/398f272e255e7645c7a170c483a29f68/record_info.png)

## Setting on DNSPod
If your DNS service ISP is DNSPod, you can add a CNAME record as follows.
![](https://mccdn.qcloud.com/static/img/5104d2605864556a130cac06b87e8187/image.png)

## Setting on Wanwang
If your DNS service ISP is Wanwang, you can add a CNAME record as follows.
![](https://mccdn.qcloud.com/static/img/f0eff3c6e223575b91322a49c1138ddf/image.png)
![](https://mccdn.qcloud.com/static/img/93e3eeef133d305dcc80433a168ee75a/image.png)

## Setting on Xinnet
If your DNS service ISP is Xinnet, you can add a CNAME record as follows.
![](https://mccdn.qcloud.com/static/img/301f06bf3f6f107fec5295f69f8c0ad3/image.png)

## Verifying Whether CNAME is in Effect
The time needed for the CNAME to take effect varies with different DNS service ISPs (usually within 30 minutes). You can also check the effectiveness of CNAME by using PING command in command line. If a domain name suffixed with "```.sp.spcdntip.com```" is pinged, then the CNAME has taken effect.
