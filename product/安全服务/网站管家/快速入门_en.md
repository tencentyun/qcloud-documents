## 1. Add a Domain Name
In order for Web Application Firewall (WAF) to identify domain names to be protected, you need to add the domain names to WAF. Here we take `www.qqtester.com` as an example to show you how to add a domain name.

(1). Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click **WAF** tab in the navigation bar to go to WAF console. In the left navigation pane of the WAF console, click **Protection Settings** to go to the protection setting page.
(2). Click **Add Domain Name**, and the **Add Domain Name** window appears.
(3). Enter the domain name to be protected (e.g. `www.qqtester.com`), select a protocol and port (e.g. HTTP protocol and port 80), and enter the origin server IP (i.e. the public IP of the origin server), and then click **Add**.
  ![Add domain name](https://mc.qcloudimg.com/static/img/f1a9f6e80f56d9bf17d319f228e3084d/domain_add_01.png)
(4). The added domain name is shown on the protection settings page. You can double click the domain name to enter the details page to view CNAME assigned to the site by WAF. And now the domain name has been added successfully.
  ![Add domain name](https://mc.qcloudimg.com/static/img/d0cc2aa33cc48458c5a218cf86177eb6/domain_add_02.png)

## 2. Local Test
DNS resolution is required for local devices to access a website. Before DNS resolution, local devices first obtain the IP of the target domain name from the local Hosts file. Therefore, we can direct the local access traffic to WAF by modifying the Hosts file to test the connectivity of access to the website through WAF. In this mode, public network users can be free from the inaccessibility to the site caused by directly modifying the DNS resolution records.

(1). Obtain the IP address
  The IP address added to the local Hosts file is obtained by pinging CNAME assigned by WAF.
  ![Local test](https://mc.qcloudimg.com/static/img/e4f961fc46724e01b7c2530baf2ecbdd/local_test_01.png)
(2). Modify Hosts file
 In Windows, modify `C:\Windows\System32\drivers\etc\hosts` by adding the following content
    ![Local test](https://mc.qcloudimg.com/static/img/786df96a80f335217c4e8fd6a9e2f00b/local_test_02.png)
 In Linux, modify `/etc/hosts` by adding the following context
    ![Local test](https://mc.qcloudimg.com/static/img/8658570d2c63b1bc2c4505080d84ec49/local_test_03.png)
(3). Access the website on the local device. If the site can be opened normally, the connectivity is normal for access to the Web origin server through WAF.
(4). Enter the following address in your browser:
```
http://www.qqtester.com/?test=alert(123)  
```
If the blocking page appears in the browser, WAF protection works properly.
![Local test](https://mc.qcloudimg.com/static/img/d7cc0f6ddf36d2d565cccae57f3c8d32/local_test_04.png)


## 3. Modify DNS Resolution
If you want to protect the public network traffic to the website with WAF, you need to modify the DNS resolution records. Here we show you how to modify DNS resolution by taking DNS resolution of `www.qqtester.com` on Tencent Cloud as an example.

(1). Log in to [Cloud DNS Console](https://console.cloud.tencent.com/cns/domains). Select the domain name `qqtester.com` from the domain name list, and click **Resolution** to enter the resolution configuration interface.
  ![Local test](https://mc.qcloudimg.com/static/img/19e7342d2eea6d4d943ce0d2e7464d4f/domain_exp_01.png)
(2). Click **Add Record**, and in the pop-up Add Record window, select CNAME in **Record Type**, enter the host name of corresponding website in Host Name (here is `www.qqtester.com`, i.e. `www`), and enter the CNAME domain name `***************16feb2214fc62a3.qcloudwzgj.com` assigned by WAF in **Record Value**, and then click **OK** to save.
  ![Local test](https://mc.qcloudimg.com/static/img/8a12c2aabf297c8e99e878a839b6657a/domain_exp_02.png)
(3). After the modified DNS records take effect, WAF protects traffic of all Internet users to `www.qqtester.com`. If WAF detects that the resolution of protected domain name is normal, the prompt **Normal Protection** shows on the console.

## 4.Set Security Group 
Security group, an instance-level firewall provided by Tencent Cloud, is used to control inbound/outbound traffic of CVMs. You can allow only traffic from WAF to access the website in the security group settings in order to prevent attackers from directly attacking the origin server while bypassing WAF. Here we explain the configuration process by taking the WAF origin server IP range `123.207.88.0/24` in the security group as an example.

(1). Log in to [CVM Console](https://console.cloud.tencent.com/cvm/overview), and click **Security Groups** in the left navigation pane to go to the security group page.
![Local test](https://mc.qcloudimg.com/static/img/e974185bedefc9071d4ce8ea639af578/sec_group_01.png)
(2). Click **+ New**, enter the security group name (e.g. my-security-group), select a custom template, and enter the relevant notes. ![Local test](https://mc.qcloudimg.com/static/img/7bd416c6d5df549fbdd1489ca2616944/sec_group_02.png)
(3). Click **+ New Line** in the inbound rule list. In the new configuration line, select HTTP in **Rule Protocol**, and enter the origin server IP range `123.207.88.0/24` in **Source**. And then click **Done** to finish the configuration.
![Local test](https://mc.qcloudimg.com/static/img/2326cd7793602227e0115ea4db7d373b/sec_group_03.png)
(4). In the security group list, find the new security group, and click **Operation** -> **Add Instance**, and then select CVM as the binding type, and select the CVM to be bound to complete the binding operation. You can also enter the CVM list page to view or modify the security group associated with the CVM. On the CVM list page, select the CVM for which you want to modify the security group, and click **Operation** -> **More** -> **Security Group**, and then select a security group for binding.

> **Note:**
> All origin server IP ranges to be allowed by WAF are:
```
123.207.88.0/24
123.207.124.0/24
119.29.245.0/24
139.199.169.0/24
123.207.83.0/24
119.29.218.0/24
119.29.106.0/24
118.89.61.0/24
```

