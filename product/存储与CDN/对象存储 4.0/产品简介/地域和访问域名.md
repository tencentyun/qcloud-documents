腾讯云对象存储 COS 支持多地域存储，不同地区的默认访问域名不同。创建存储桶时选定的地域不可修改，建议根据自己的业务场景选择就近的地域存储，可以提高对象上传、下载速度。

## 可用地域及访问域名
>!
>- 默认域名在创建好存储桶后，可通过 [对象存储控制台](https://console.cloud.tencent.com/cos5) 的存储桶【域名管理】查看。
>- bucketname 是在创建存储桶时为存储桶命名的名称，可通过 [对象存储控制台](https://console.cloud.tencent.com/cos5) 的存储桶【基础配置】查看。
>- APPID 是在成功申请腾讯云账户后，系统分配的账户标识之一，可通过 [腾讯云控制台](https://console.cloud.tencent.com) 【账号信息】查看。
>- 历史版本的可用地域说明，请参阅 [历史版本地域列表](https://cloud.tencent.com/document/product/436/7777)。
>- 有关内网与外网访问的相关信息，请参阅 [创建请求概述](https://cloud.tencent.com/document/product/436/31315) 文档。

| 地域       | 地域简称         | 默认域名（上传/下载/管理 ）                          |
| -------- | ------------ | ---------------------------------------- |
| 北京一区（华北） | ap-beijing-1 | &lt;bucketname-APPID&gt;.cos.ap-beijing-1.myqcloud.com |
| 北京       | ap-beijing   | &lt;bucketname-APPID&gt;.cos.ap-beijing.myqcloud.com |
| 上海（华东）   | ap-shanghai  | &lt;bucketname-APPID&gt;.cos.ap-shanghai.myqcloud.com |
| 广州（华南）   | ap-guangzhou | &lt;bucketname-APPID&gt;.cos.ap-guangzhou.myqcloud.com |
| 成都（西南）   | ap-chengdu   | &lt;bucketname-APPID&gt;.cos.ap-chengdu.myqcloud.com |
| 重庆       | ap-chongqing | <bucketname-APPID&gt;.cos.ap-chongqing.myqcloud.com |
| 新加坡      | ap-singapore | &lt;bucketname-APPID&gt;.cos.ap-singapore.myqcloud.com |
| 香港       | ap-hongkong  | &lt;bucketname-APPID&gt;.cos.ap-hongkong.myqcloud.com |
| 多伦多      | na-toronto   | &lt;bucketname-APPID&gt;.cos.na-toronto.myqcloud.com |
| 法兰克福     | eu-frankfurt | &lt;bucketname-APPID&gt;.cos.eu-frankfurt.myqcloud.com |
| 孟买       | ap-mumbai    | <bucketname-APPID&gt;.cos.ap-mumbai.myqcloud.com |
| 首尔       | ap-seoul     | <bucketname-APPID&gt;.cos.ap-seoul.myqcloud.com |
| 硅谷       | na-siliconvalley     | <bucketname-APPID&gt;.cos.na-siliconvalley.myqcloud.com |
| 弗吉尼亚       | na-ashburn     | <bucketname-APPID&gt;.cos.na-ashburn.myqcloud.com |
| 曼谷       | ap-bangkok     | <bucketname-APPID&gt;.cos.ap-bangkok.myqcloud.com |
| 莫斯科       | eu-moscow     | <bucketname-APPID&gt;.cos.eu-moscow.myqcloud.com |
|东京       |ap-tokyo  |     <bucketname-APPID&gt;.cos.ap-tokyo.myqcloud.com |

> 示例：
> 用户在所属地域广州创建了一个存储桶，存储桶名中用户自定义字符串部分为 example，系统自动为用户生成的数字串 APPID 为1250000000，则其默认访问域名为：
```
example-1250000000.cos.ap-guangzhou.myqcloud.com
```
