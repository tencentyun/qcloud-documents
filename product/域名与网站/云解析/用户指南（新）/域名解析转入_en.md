First, register your Tencent Cloud account.
### Add Domain Names
Log in to Tencent [Cloud DNS Console](https://console.cloud.tencent.com/cns/domains) and add the domain name to be transferred to Tencent Cloud DNS. For more information, please see the [process for adding domain name](https://cloud.tencent.com/document/product/302/3446). You can choose to import the domain names in batch if the data is too much:
![](//mc.qcloudimg.com/static/img/a92554869b120029121faba523c1b438/image.png)
>**Note:**
>In this case, you only added the domain name to Tencent Cloud DNS but the domain name isn't resolved at Tencent Cloud yet. You need to go to your domain name registrar and modify the DNS server to complete the remaining steps.

### Upgrade DNS Package (Optional)
You can upgrade your DNS package based on your needs to improve minimum TTL, A record load balancing, sub domain name level, attack protection traffic and so on. For more information, please see the [purchase process](https://cloud.tencent.com/document/product/302/7808). This step can be ignored if you only use the free package.
### Import Resolution Record
You can add manually for a few resolution records. For more information, please see [process for adding A record](https://cloud.tencent.com/document/product/302/3449), and [process for adding CName record](https://cloud.tencent.com/document/product/302/3450). In case of a large number of resolution records, you can export the records from your original DNS service provider and import them into Tencent Cloud DNS through files. Both zone files and xls files are supported:
![](//mc.qcloudimg.com/static/img/7bbaa544587436ca13b7741ee370ac55/image.png)
![](//mc.qcloudimg.com/static/img/f640781d89ca9f1625d71153cfb06074/image.png)
Key customers may submit tickets and contact Tencent Cloud engineers to verify if the import is successful.
### Modify DNS Server
Go to the domain name registrar to modify domain name DNS server. For more information, please see [process for modifying DNS server](https://cloud.tencent.com/document/product/302/5518).
### Wait for 72 Hours
Wait until the resolution takes effect globally, confirm, and add resolution record.
### Verify if Resolution is Functional
Randomly access the domain name to verity if the resolution is functional.
### Transfer Domain Name to Tencent Cloud (Optional)
When the resolution is stable, you can transfer the domain name into Tencent Cloud. For more information, please see [process of transferring domain name to Tencent Cloud](https://cloud.tencent.com/document/product/242/3645).

