COS supports multi-region storage, and different regions have different access domains by default. It is recommended to choose the nearest storage region according to your own business scenarios, so as to improve the object upload and download speed.
## Available Regions and Access Domain Names
><font color="#0000cc">**Note:** </font>
- After creating the bucket, the default domain name can be viewed through the bucket "Domain Management" of [Object Storage Console](https://console.cloud.tencent.com/cos4).
- bucketname is the name given upon creating a bucket, and it can be viewed through the bucket "Basic Configuration" of [Object Storage Console](https://console.cloud.tencent.com/cos4).
- APPID is one of the account identifiers assigned by the system after the successful application of Tencent Cloud account, which can be viewed through "Account Information" of [Tencent Cloud Console](https://console.cloud.tencent.com/developer).

#### For XML API
| Region | Abbreviation | Default Domain Name (Upload/Download/Management) |
| ------ | ------- | ----------------------------------- |
| Beijiing Zone 1 (North China) | ap-beijing-1 | &lt;bucketname&gt;-&lt;APPID&gt;.cos.ap-beijing-1.myqcloud.com |
| Beijing | ap-beijing | &lt;bucketname&gt;-&lt;APPID&gt;.cos.ap-beijing.myqcloud.com |
| Shanghai (East China) | ap-shanghai | &lt;bucketname&gt;-&lt;APPID&gt;.cos.ap-shanghai.myqcloud.com |
| Guangzhou (South China) | ap-guangzhou | &lt;bucketname&gt;-&lt;APPID&gt;.cos.ap-guangzhou.myqcloud.com |
| Chengdu (Southwest China) | ap-chengdu | &lt;bucketname&gt;-&lt;APPID&gt;.cos.ap-chengdu.myqcloud.com |
| Singapore | ap-singapore | &lt;bucketname&gt;-&lt;APPID&gt;.cos.ap-singapore.myqcloud.com |
| Hong Kong | ap-hongkong | &lt;bucketname&gt;-&lt;APPID&gt;.cos.ap-hongkong.myqcloud.com |
| Toronto | na-toronto | &lt;bucketname&gt;-&lt;APPID&gt;.cos.na-toronto.myqcloud.com |
| Frankfurt | eu-frankfurt | &lt;bucketname&gt;-&lt;APPID&gt;.cos.eu-frankfurt.myqcloud.com |

For example:
A user with APPID of 1234567890 creates a bucket under the name example and region Guangzhou, and the default access domain name is:
```
example-1234567890.cos.ap-guangzhou.myqcloud.com
```
 
#### For JSON API
| Region | Abbreviation | Default Download Domain Name | Upload Domain Name | 
| ------ | ------- | ----------------------------------- | -------------------- | 
| Beijing Zone 1 (North China) | tj | &lt;bucketname&gt;-&lt;APPID&gt;.costj.myqcloud.com | tj.file.myqcloud.com |
| Beijing | bj | &lt;bucketname&gt;-&lt;APPID&gt;.cosbj.myqcloud.com | bj.file.myqcloud.com |
| Shanghai (East China) | sh | &lt;bucketname&gt;-&lt;APPID&gt;.cossh.myqcloud.com | sh.file.myqcloud.com |
| Guangzhou (South China) | gz | &lt;bucketname&gt;-&lt;APPID&gt;.cosgz.myqcloud.com | gz.file.myqcloud.com |
| Chengdu (Southwest China) | cd | &lt;bucketname&gt;-&lt;APPID&gt;.coscd.myqcloud.com | cd.file.myqcloud.com |
| Singapore | sgp | &lt;bucketname&gt;-&lt;APPID&gt;.cossgp.myqcloud.com | sgp.file.myqcloud.com |
| Hong Kong | hk | &lt;bucketname&gt;-&lt;APPID&gt;.coshk.myqcloud.com | hk.file.myqcloud.com |
| Toronto | ca | &lt;bucketname&gt;-&lt;APPID&gt;.cosca.myqcloud.com | ca.file.myqcloud.com |
| Frankfurt | ger | &lt;bucketname&gt;-&lt;APPID&gt;.cosger.myqcloud.com | ger.file.myqcloud.com |

 For example:
 A user with APPID of 1234567890 creates a bucket under the name example and region Guangzhou, and the default download domain name is:
 ```
 example-1234567890.cosgz.myqcloud.com
 ```
 
**Suggestions on cross-region access in private network:
As different Tencent Cloud Services in different regions cannot be accessed directly through private network. You can deploy an exclusive network channel through VPC when necessary. For more information, please see [VPC Product Introduction](https://cloud.tencent.com/product/vpc.html).**
For example:
A CVM in the region Guangzhou can access the data on Singapore COS through a VPC channel.

