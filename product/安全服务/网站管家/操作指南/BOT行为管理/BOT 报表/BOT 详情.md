BOT 详情展示了不同类型的 BOT 详细数据、各个特征项的统计分布，以及相关日志。

## 前提条件
已购买[ Web 应用防火墙套餐](https://buy.cloud.tencent.com/buy/waf)，完成防护域名添加，域名处于正常防护状态，并且域名 BOT 检测功能已开通。
>? 
>- 只有 WAF 企业版和旗舰版支持 BOT 行为管理，高级版用户建议升级到企业版或旗舰版。
>- 完成 WAF 域名接入，并开启 WAF 防护开关。
>- 需开启 [BOT 防护设置](https://console.cloud.tencent.com/guanjia/bot2/config) 页面中对应域名的流量分析开关。

## 操作步骤
1. 登录 [Web 应用防火墙（WAF）控制台](https://console.cloud.tencent.com/guanjia/waf/overview)，在左侧导航栏中，选择【BOT 行为管理】>【BOT 详情】>【BOT 详情】，进入 BOT 详情页面。
2. 在BOT详情页面，单击左上角“全部域名”下拉框，选择要查看的域名，通过指定的时间范围，搜索某个域名在查询时间范围内的 BOT 防护效果数据。
![](https://main.qcloudimg.com/raw/f795b89cf53cc7f0616954b0167d2b30.png)
3. 在BOT详情页面，单击筛选器搜索框，选择所需条件，并输入文本内容。
![](https://main.qcloudimg.com/raw/82e83d0649bbfa540a0b6a4e9b431b8a.png)
4. 单击【添加】，可添加多个条件，每个类型一个。
>?筛选器可以针对多个不同的条件进行数据过滤用来生成报表，条件不限于域名，还包含 IP/URL/地理位置等信息。
5. 流量趋势对比图：单击“标签项”，可快速查看不同统计类型，在选定的时间范围内的流量趋势。
![](https://main.qcloudimg.com/raw/4e023249e948d83fd4d3408c27afcb89.png)
6. BOT 请求量 TOP5 统计：展示对应时间段内 BOT 的相关特征，所统计出的TOP5 键值及其数量。
  - 统计图受筛选器影响，受流量趋势对比图框选时间影响。
![](https://main.qcloudimg.com/raw/4dc2f380a2aed527fc33880d2fdf93c5.png)
 - 单击对应的“柱状图”，会展示对应提示框，该提示框包含该键值的信息，单击【筛选】或【排除】，可以快速添加相关的过滤器。
![](https://main.qcloudimg.com/raw/d5a9bb47f9d6236e59945901789ba5d8.png)
 - 如果数据量级大于 TOP5 ，单击【更多】，右侧弹出抽屉展示 BOT 请求量 TOP 统计列表，最多默认展示10条。单击右侧【行为分析】，会根据该路径的相关筛选项，跳转至动态行为分析页签。
![](https://main.qcloudimg.com/raw/296fedb8da396ec0880b54bc159f0b28.png)
7. BOT 日志详情：展示 BOT 的日志信息，单击![](https://main.qcloudimg.com/raw/5492e6a1a03c64ede0d9a728c743dad9.png)图标，可以展示该时间的日志详情。
![](https://main.qcloudimg.com/raw/82cbae0808c89c4f4df270ab6356b987.png)
