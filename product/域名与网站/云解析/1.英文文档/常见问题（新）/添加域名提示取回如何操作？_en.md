"Domain name is already added by another user" indicates that another developer has already added the domain name in Cloud DNS platform, as shown in the following figure:
![1](//mc.qcloudimg.com/static/img/d8bf385c475f6bee85c55c4d63794d54/image.png)
If you encounter this prompt, click "Retrieve" to open the window shown below. There are two ways to retrieve a domain name: use Whois email to retrieve or add TXT record to retrieve. Choose a method based on your demand. 
![2](https://mc.qcloudimg.com/static/img/50dba306a62d6917d4094e9344dd5fdf/image.png)
**Use Whois email to retrieve** 
First, make sure that you own this email. Click **OK**, and the verification email is sent to your email box. This verification email is valid for 30 minutes.
If the dialog box as below is shown when you use Whois email for retrieval:
![3](//mc.qcloudimg.com/static/img/452b533f0e7e9d4d0a3694d4bad0894e/image.png)
If the email displayed is "whoisprotect@dnspod.com", go to your domain name registrar first and disable "Privacy Protection" and retry the retrieval again.
>**Note:**
>Domain names registered with Tencent Cloud can only be retrieved by using Whois email.

If you cannot obtain the email, you can retrieve by adding TXT record, as shown in the following figure: 
![4](//mc.qcloudimg.com/static/img/1d34f2938a89530af95287a05a55641f/image.png)
**Add TXT record to retrieve** 
This approach is only suitable for domain names whose DNS servers are not located at DNSPod. You can configure this record at the registrar where you want to add the resolution to retrieve the domain name.
![5](//mc.qcloudimg.com/static/img/5a5534e4d61aeccd4476c5787aa8f93c/image.png)
>**Note:**
>You cannot retrieve domain names that use VIP resolution service by yourself. Contact our customer service for assistance.

If you have any questions, [submit a ticket](https://console.cloud.tencent.com/workorder/create?level1_id=16&level2_id=17&level1_name=%E5%85%B6%E5%AE%83%E6%9C%8D%E5%8A%A1&level2_name=%E5%9F%9F%E5%90%8D) to contact our customer service.

