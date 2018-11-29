## 云缓存 Memcached 定价

云缓存 Memcached 根据分配空间进（使用空间 + 预留缓冲空间）计费，不足1G时按1G收费。

- 表缩容指的是减少表的占用空间，也即存储缩容。因为需要预留缓冲空间，缩容后表使用率不会超过80%。表缩容的最小粒度是1GB，如果缩容会造成使用率超过80%，则不能进行缩容。

目前云缓存 Memcached 的表暂不支持自动缩容，如表需要缩容则可提交工单申请，之后需运维人员操作缩容。

在申请缩容之前，计费时仍然会按照原占用空间（包括在原使用空间的基础上自动扩容的缓冲空间）的峰值进行计算。

### 定价详情

<table class="t" style="display:table;width:80%;">
<tbody><tr>
<th>  资源
</th><th>  配置说明
</th><th>  单价（GB日）
</th></tr>
<tr>
<td> 云缓存Memcached
</td><td> 有热备<br>
<p>每G存储量最大支持10000次/秒的访问量（例如如果申请10G存储，那么访问量上限是100000次/秒）<br>
</p>
</td><td> 2.00元 /GB日
</td></tr></tbody></table>

## 购买指导

### 购买新表
1.登录腾讯云首页cloud.tencent.com

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/NoSQLBuy1.png)

2.在产品服务模块，选择云缓存Memcached，点击“立即购买”进入购买流程。

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/NoSQLBuy2.jpg)

【注意事项】

- 如果需要新建大量的表且初始表总空间大于100GB，或者单个表初始空间大于20GB，请[提交工单](http://console.cloud.tencent.com/ticket)。如果访问量超过10000次/秒/GB，则新建表成功后，请填写[工单](/doc/product/282/联系我们#4-开发者运维需求申请)**接口/端口扩容**进行申请。

3.购买成功后，可在“管理中心 - 控制台 - 云缓存Memcached”看到购买的表。单击表名称可以修改名称。

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/NoSQLBuy3.png)

4.确定是否开启expire过期删除功能。请参见[开启expire过期删除功能](/doc/product/439/6806)。
