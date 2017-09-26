COS 支持多地域存储，不同地区默认访问域名不同。建议根据自己的业务场景选择就近的地域存储，可以提高对象上传、下载速度。
## 可用地域及访问域名
><font color="#0000cc">**注意：** </font>
- 默认域名在创建好存储桶后，可通过 [对象存储控制台](https://console.qcloud.com/cos4) 的存储桶【域名管理】查看。
- bucketname 是在创建存储桶时为存储桶命名的名称，可通过 [对象存储控制台](https://console.qcloud.com/cos4) 的存储桶【基础配置】查看。
- APPID 是在成功申请腾讯云账户后，系统分配的账户标识之一，可通过 [腾讯云控制台](https://console.qcloud.com/developer) 【账号信息】查看。

### 适用于 XML API
| 地域 | 地域简称 | 默认域名（上传/下载/管理 ） |
| ------ | ------- | ----------------------------------- |
| 北京一区（华北） | ap-beijing-1 | &lt;bucketname&gt;-&lt;APPID&gt;.cos.ap-beijing-1.myqcloud.com |
| 北京 | ap-beijing | &lt;bucketname&gt;-&lt;APPID&gt;.cos.ap-beijing.myqcloud.com |
| 上海（华东） | ap-shanghai | &lt;bucketname&gt;-&lt;APPID&gt;.cos.ap-shanghai.myqcloud.com |
| 广州（华南） | ap-guangzhou | &lt;bucketname&gt;-&lt;APPID&gt;.cos.ap-guangzhou.myqcloud.com |
| 成都（西南） | ap-chengdu | &lt;bucketname&gt;-&lt;APPID&gt;.cos.ap-chengdu.myqcloud.com |
| 新加坡 | ap-singapore | &lt;bucketname&gt;-&lt;APPID&gt;.cos.ap-singapore.myqcloud.com |
| 香港 | ap-hongkong | &lt;bucketname&gt;-&lt;APPID&gt;.cos.ap-hongkong.myqcloud.com |
| 多伦多 | na-toronto | &lt;bucketname&gt;-&lt;APPID&gt;.cos.na-toronto.myqcloud.com |
| 法兰克福 | eu-frankfurt | &lt;bucketname&gt;-&lt;APPID&gt;.cos.eu-frankfurt.myqcloud.com |

> 例如：
APPID 为 1234567890 的用户创建了一个名为 example，所属地域为广州的存储桶，其默认访问域名则为：
```
example-1234567890.cos.ap-guangzhou.myqcloud.com
```
 
### 适用于 JSON API
| 地域 | 地域简称 | 默认下载域名 | 上传域名 | 
| ------ | ------- | ----------------------------------- | -------------------- | 
| 北京一区（华北） | tj | &lt;bucketname&gt;-&lt;APPID&gt;.costj.myqcloud.com | tj.file.myqcloud.com |
| 北京 | bj | &lt;bucketname&gt;-&lt;APPID&gt;.cosbj.myqcloud.com | bj.file.myqcloud.com |
| 上海（华东） | sh | &lt;bucketname&gt;-&lt;APPID&gt;.cossh.myqcloud.com | sh.file.myqcloud.com |
| 广州（华南） | gz | &lt;bucketname&gt;-&lt;APPID&gt;.cosgz.myqcloud.com | gz.file.myqcloud.com |
| 成都（西南） | cd | &lt;bucketname&gt;-&lt;APPID&gt;.coscd.myqcloud.com | cd.file.myqcloud.com |
| 新加坡 | sgp | &lt;bucketname&gt;-&lt;APPID&gt;.cossgp.myqcloud.com | sgp.file.myqcloud.com |
| 香港 | hk | &lt;bucketname&gt;-&lt;APPID&gt;.coshk.myqcloud.com | hk.file.myqcloud.com |
| 多伦多 | ca | &lt;bucketname&gt;-&lt;APPID&gt;.cosca.myqcloud.com | ca.file.myqcloud.com |
| 法兰克福 | ger | &lt;bucketname&gt;-&lt;APPID&gt;.cosger.myqcloud.com | ger.file.myqcloud.com |

> 例如：
APPID 为 1234567890 的用户创建了一个名为 example，所属地域为广州的存储桶，其默认下载域名则为
```
example-1234567890.cosgz.myqcloud.com
```

### 跨地域内网访问
相同地域内的不同腾讯云产品之间访问，将会自动使用内网连接，不产生流量费用。因此选购腾讯云不同产品时，建议尽量选择相同地域，减少您的费用。
> 以腾讯 CVM 访问 COS 为例，判断是否使用内网访问 COS 的方法：
在 CVM 上 ping COS 域名，若返回内网 IP，则表明 CVM 和 COS 之间是内网访问，否则为外网访问。
内网 IP 地址一般形如`10.*.*.*`、`100.*.*.*`等。

不同地域的不同腾讯云产品之间无法直接通过内网访问。如需通过内网访问，可通过 VPC 部署专属网络通道互联。具体信息，请参考 [VPC 产品介绍](https://www.qcloud.com/product/vpc.html)。
> 例如：
所在地域为广州的 CVM 访问新加坡的 COS 上的数据，可通过建立 VPC 通道可实现互联。
