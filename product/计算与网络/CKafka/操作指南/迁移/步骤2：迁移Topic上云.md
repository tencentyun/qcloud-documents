## 操作场景
本文档为您介绍如何利用 CKafka 提供的迁移工具将自建 Kafka 集群的 Topic 迁移到 CKafka 的实例中。

## 前提条件

- 已 [购买云上实例](https://cloud.tencent.com/document/product/597/57775)
- [下载 Python2](https://www.python.org/downloads/)


## 操作步骤
1. 下载 [迁移工具](https://ckafka-1300957330.cos.ap-guangzhou.myqcloud.com/ckafka-demo/migrateToCkafkaTool.zip) 并解压到可以连通自建实例的 broker 和 zk 的机器上。
2. 在 ckafka-migrate.py 文件中填写配置参数。
>?
>- 请保证后面迁移操作所在的机器和 CKafka 以及自建 Kafka 集群的网络互通。
>- yunapi 的密钥对应的用户需要拥有 CKafka 的写权限，建议使用主账号的密钥对。
<dx-codeblock>
:::  python
   # your local broker ip:port list
   # 自建实例的broker列表 ["broker1:port1","ip2:port2"]
   bootstrapServers = ["$ip:$port"]
   
   # your local zk ip:port list
   # 自建实例的zk列表 ["zk1:port1","zk2:port2"]
   sourceZk = ["$ip:$port"]
   
   # your cloud instanceId
   # 云上实例id  "ckafka-xxx"
   instanceId = "$yourinstanceId"
   
   # topic regex,just migrate match topics
   # topic名称正则表达式,非空则只迁移匹配到的topic
   topicRegex = ""
   
   # your secretId and secretKey
   # 账号的密钥对
   secretId = "$yoursecretId"
   secretKey = "$yoursecretKey"
   
   # your cloud instance region
   # 云上实例的地域  ckafka已开区地域码：
   # 广州 ap-guangzhou;上海 ap-shanghai;南京 ap-nanjing;北京 ap-beijing; 成都 ap-chengdu;重庆 ap-chongqing;
   # 中国香港 ap-hongkong;新加坡 ap-singapore;印度孟买 ap-mumbai;日本东京 ap-tokyo;美西硅谷 na-siliconvalley;
   # 美东弗吉尼 na-ashburn;北美多伦多 na-toronto;中国台北 ap-taipei;天津 ap-tianjin;上海金融 ap-shanghai-fsi;
   # 深圳金融 ap-shenzhen-fsi;深圳 ap-shenzhen;德国法兰克 eu-frankfur;首尔 ap-seoul;清远 ap-qingyuan;
   # 北京金融 ap-beijing-fsi;莫斯科 eu-moscow;曼谷 ap-bangkok;长沙 ap-changsha-ec;雅加达 ap-jakarta
   region = "ap-changsha-ec"
   
   # if you make sure the migrate topic List,please modify checkFlag = 1
   # 检查标记,设0只显示将要迁移的topic列表不做真正迁移,请先以0运行检查将要迁移的topic列表，确认无误后修改为1开始迁移
   # 0:列出迁移topic列表后脚本终止
   # 1:列出迁移topic列表并开始迁移
   checkFlag = 0
   
   # force transfor your topic config to cloude
   # 如果为0转换本地topic到云上topic时，属性不一致不会迁移上云。如果为1，会强制转换topic属性和云上最近的值
   # 例如云上topic的副本只支持2，3副本，如果本地的某topic副本数为5，则不会迁移上云。如果设置为1，则会取和5最接近的3副本，在云上创建3副本topic。
   # 0:本地和云上topic副本数或topic属性不兼容时，跳过不兼容的topic或者topic属性
   # 1:本地和云上topic副本数或topic属性不兼容时，强制迁移至云上，云上修正不兼容的topic副本数或topic属性并 （不会修改本地自建kafka的任何数据）
   force = 0
:::
</dx-codeblock>


   | 参数             | 说明                                                         |
   | ---------------- | ------------------------------------------------------------ |
   | bootstrapServers | 自建实例的broker列表，["ip1:port1","ip2:port2"]。            |
   | sourceZk         | 自建实例的zookeeper列表， ["zk1:port1","zk2:port2"]。        |
   | instanceId       | 您在 [购买云上实例](https://cloud.tencent.com/document/product/597/57775) 中购买的 CKafka 实例的 ID，在控制台的**实例列表**页面复制。 |
   | secretId         | 账号的密钥对-ID。                                            |
   | secretKey        | 账号的密钥对-密码。                                          |
   | region           | 您在 [购买云上实例](https://cloud.tencent.com/document/product/597/57775) 中选择的部署地域，脚本内注释附带各地域码。   |
   | checkFlag        | 检查标记，设置为0时只显示将要迁移的 Topic 列表并不开始迁移，设置为非0时开始迁移 Topic。 |
   | topicRegex       | Topic 名称正则表达式，设置为空时迁移所有的 Topic，非空时则只迁移匹配到的 Topic。 |
   | force            | 是否强制迁移，如果为0转换本地 Topic 到云上 Topic 时，属性不一致不会迁移上云。如果为1，会强制转换 Topic 属性和云上规定最接近的值。 |

3. 将 ckafka-migrate.py 的 checkFlag 参数设为0，运行脚本 python ckafka-migrate.py，根据输出结果检查需要迁移的Topic列表。
>?如果缺少部分自建的 Topic，可能是自建Topic命名不符合规则或者Topic副本数、Topic属性数值与云上数值范围无法兼容。
>
![](https://main.qcloudimg.com/raw/4566352387f69b71e6fb7ab1b44780b9.png)

4. 把 ckafka-migrate.py 的 checkFlag 参数设为1，运行脚本 python ckafka-migrate.py，开始迁移 Topic。
   ![](https://main.qcloudimg.com/raw/eed68b25e287092fc370b7b91b09a35c.png)

5. 登录 [CKafka 控制台](https://console.cloud.tencent.com/ckafka)，在**迁移上云**页面查看任务列表，等待 Topic 迁移完毕。
	任务列表如下：
	<img src="https://main.qcloudimg.com/raw/d064a541d46505746b3a9e81c4cb5e99.png" width="600px">
	
	迁移成功界面如下：
	<img src="https://main.qcloudimg.com/raw/574f0dd1ead9397a7da91f26f82c9bc8.png" width="600px">


