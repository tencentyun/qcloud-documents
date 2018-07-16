腾讯云 TencentDB for MySQL 数据库目前支持实例包年包月和按量计费两种模式（按量计费购买前需要实名认证，详见 <a href="https://cloud.tencent.com/document/product/378/3629" target="_blank">实名认证指引</a>）。  
包年包月是一种预付费计费模式，详情请参见 <a href="https://cloud.tencent.com/document/product/555/9618" target="_blank">预付费计费说明</a>。  
按量计费是一种后付费计费模式，详情请参见 <a href="https://cloud.tencent.com/document/product/555/9617" target="_blank">按量计费说明</a>。  
计费流程请参见 <a href="https://cloud.tencent.com/document/product/555/7437" target="_blank">计费流程说明</a>。
## 按量计费阶梯价格
为惠及用户，云数据库 MySQL 自 2016 年 7 月 15 日起支持按量计费阶梯价，用得久更便宜。
按量计费根据使用时长不同，共分为三个阶梯：
- 0~4 天（4\*24 小时内），适用按量计费第一阶梯价格。
- 4 天~ 15 天（4\*24 小时起，至15\*24 小时内），适用按量计费第二阶梯价格。
- 15 天以上（15\*24 小时起），适用按量计费第三阶梯价格  。

具体的价格请参见【[各地域国内价格](#document_price)】。<span id="https://cloud.tencent.com/document/product/236/18334"></span>
具体的价格请参见【[各地域国际价格](#document_price)】。
<span id="https://cloud.tencent.com/document/product/236/18327"></span>
## 实例续费管理
在续费管理页面提供实例的【批量资源续费】、【设置自动续费】、【设置统一到期日】、【取消不续费】等功能 ，详见 <a href="https://cloud.tencent.com/document/product/555/7454" target="_blank">续费管理</a>。

## 实例升级费用
假设该实例的到期时间 T 天，计算您升级到目标配置与现有配置的月预付费差额 C，升级总费用的公式就是 T/30\*C。
例如：您有个实例 1 G 内存 100 G 硬盘（预付费 174 元/月），还有 15 天时间到期，现在您需要升级到 1 G 内存 200 G 硬盘（预付费 246 元/月），升级总费用 = 15/30\*(246-174) = 36 元。

>**注意：**
为保障您业务正常进行，当硬盘空间快要满时，请及时升级数据库实例规格或者购买硬盘空间。详情请参见 [升级数据库实例规格](https://cloud.tencent.com/document/product/236/7271)。
实例存储数据量超过实例，实例会被锁住，仅能读取数据不能写入，需**扩容或在控制台删除部分数据库表**解除只读。
为避免数据库重复触发锁定状态，仅当实例剩余空间大于 20% 或大于 50 G （满足两个条件其中之一即可）时，实例会解除锁定状态，恢复正常读写功能。

## 灾备实例同步流量费用
推广期 TencentDB for MySQL 数据库灾备同步流量暂不收费。商业化收费时间将另行通知。 

[2]:	https://cloud.tencent.com/document/product/555/9618
[3]:	https://cloud.tencent.com/document/product/555/9617
[4]: https://cloud.tencent.com/document/product/555/7437
[5]: https://buy.cloud.tencent.com/calculator/cdb
