The following prompt in the domain name record management page indicates that the DNS server is incorrect, and you need to modify domain name DNS according to the prompt to make the resolution functional.
![1](//mc.qcloudimg.com/static/img/461b3011772da9f667c9e54dd45ef660/image.png)
>**Note:**
>The corresponding DNS addresses are different for different DNS service packages. Please modify them according to the prompt.

### Modify DNS for Domain Name Registered with Tencent Cloud
If your domain name is registered with Tencent Cloud, or the domain name is transferred to Tencent Cloud, you can modify its DNS server by following the steps below:
1. Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/). Choose **Cloud Products** > **Domain Names and Websites** > **Domain Name Management**.
![1](//mc.qcloudimg.com/static/img/c2f4a6cb3572143b1fbaffb23bc58510/image.png)
2. Choose the corresponding domain name and click **Manage**.
![2](//mc.qcloudimg.com/static/img/1dbc9f9c19eb5543fcde41577e817ff0/image.png)
3. Modify DNS server.
![3](//mc.qcloudimg.com/static/img/f4178f07026b20d51e6cf7ae7a41c07c/image.png)
4. Enter the specified DNS server address.
![4](https://mc.qcloudimg.com/static/img/0b866d917b994eb84eab2a58b6cd16e3/5.png)

If the domain name is managed at another registrar, you need to go to the domain name management page provided by this registrar and modify the domain name DNS into the specified one.
The following takes Alibaba Cloud (net.cn) and GoDaddy as examples to explain how to modify DNS.

### Modify DNS When Domain Name Registrar is Alibaba Cloud (net.cn)
1. Choose the domain name to be resolved at Tencent Cloud and go to **DNS Modification/Creation** on its management page. Click **Modify Domain Name DNS**;
![](https://mccdn.qcloud.com/static/img/2ade9bc496f296f14186df348835ed8e/image.png)
2. Enter "f1g1ns1.dnspod.net" and "f1g1ns2.dnspod.net" respectively, save, and wait for up to 72 hours for the DNS to take effect globally.
![](https://mccdn.qcloud.com/static/img/bca1fc5a448568567c3498b3d2c0da4d/image.png)

### Modify DNS When Domain Name Registrar is GoDaddy
1. Log in to [GoDaddy](http://www.godaddy.com), click **Manage** of **DOMAINS**.
![1](https://mccdn.qcloud.com/static/img/857a65f25a4c950dab04f36c6773bf20/GD-1.png)
2. Find the domain name whose DNS is to be modified from the domain name list and click **Set NameServers** in the drop-down list of the domain name.
![2](https://mccdn.qcloud.com/static/img/d692fab785a928ebbfc183637bdd9c31/GD-2.png)
3. Select **Custom** and click **Add Nameserver** at the lower left corner.
![3](https://mccdn.qcloud.com/static/img/2b5194f50b656d4d75666d2357f784b6/GD-3.png)
4. Enter "f1g1ns1.dnspod.net" and "f1g1ns2.dnspod.net" respectively, click **Add Nameserver** -> **Save**, and wait for the global recursive DNS server to refresh (72 hours at most).
![4](https://mccdn.qcloud.com/static/img/bed919b5d4fe0b33b6bc9f537dce1a8d/GD-4.png)
![5](https://mccdn.qcloud.com/static/img/8c4f15a5fa913037a06f752ac62ac22b/GD-5.png)


