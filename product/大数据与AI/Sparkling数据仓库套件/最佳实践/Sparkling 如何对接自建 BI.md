自建 BI 的 VPC 和 Sparkling 的 VPC 不相同，需要先打通网络。打通网络的方案主要包括对等连接、云联网等。下文以对等连接为例，介绍 Sparkling 如何对接 BI，整体流程如下：
![](https://main.qcloudimg.com/raw/3283eee40de5f15a4ab915af3b25b6b3.png)

### 第一步：BI 创建私有网络
>?本步骤是使用 BI 账号登录进行以下操作。若 BI 端已创建私有网络可以复用，直接跳过此步。

具体步骤如下：
1. 使用 BI 账号登录 [腾讯云控制台](https://console.cloud.tencent.com/)，选择【云产品】>【网络】>【私有网络】，进入私有网络控制台。
2. 单击左侧目录中的【私有网络】，进入管理页面。
3. 在管理页上方选择地域，例如广州，单击【新建】，创建私有网络。
   ![](https://main.qcloudimg.com/raw/5b545a32b89c0cc979e055195415e9e4.png)
   新建私有网络步骤如下：
   a. 填写私有网络名称
   b. 填写私有网络 CIDR
   c. 填写子网名称
   d. 填写子网 CIDR
   e. 选择子网可用区
![](https://main.qcloudimg.com/raw/4f60959b89c4c60490ecd6ffbd2e2635.jpg)

### 第二步：Sparkling 创建私有网络
>?本步骤是使用 Sparkling 账号登录进行以下操作。若 Sparkling 端已创建私有网络可以复用，直接跳过此步。
>
具体步骤如下：
1. 使用 Sparkling 账号登录 [腾讯云控制台](https://console.cloud.tencent.com/)，选择【云产品】>【网络】>【私有网络】，进入私有网络控制台。
2. 单击左侧目录中的【私有网络】，进入管理页面。
2. 在管理页上方选择地域，例如广州，单击【新建】，创建私有网络。
   ![](https://main.qcloudimg.com/raw/5b545a32b89c0cc979e055195415e9e4.png)
   新建私有网络步骤如下：
   a. 填写私有网络名称
   b. 填写私有网络 CIDR
   c. 填写子网名称
   d. 填写子网 CIDR
   e. 选择子网可用区
![](https://main.qcloudimg.com/raw/4f60959b89c4c60490ecd6ffbd2e2635.jpg)

### 第三步：BI 创建对等连接
具体步骤如下：
1. 使用 BI 账号单击控制台左侧目录中的【对等连接】，进入管理页面。
2. 在列表上方选择地域和已创建的私有网络，单击【新建】，创建对等连接。
![](https://main.qcloudimg.com/raw/5c521be875990964201c517e762c56cf.jpg)
3. 填写对等连接信息。
a. 对等连接名称（如：PeerConn）
b. 选择其他账户
c. 选择对端地域（如：广州）
d. 对端账户：填入 Sparkling 用户账号 ID，可在用户的 [个人中心](https://console.cloud.tencent.com/developer) 查看。
![](https://main.qcloudimg.com/raw/0be60e3505401e5c4d857f154772b312.jpg)
e. 对端网络：填入 Sparkling 私有网络 ID，可在 Sparking 端登录 [私有网络控制台](https://console.cloud.tencent.com/vpc) 查看。
![](https://main.qcloudimg.com/raw/be13b24659b8c433990dca0a3984b768.jpg)
4. 选择带宽上限
>!若 BI 端私有网络与 Sparkling 端私有网络所在地区不同，其中产生的费用由发起对等连接方承担。
>
 - 同地域对等连接带宽无上限，不可修改 。
 - 跨地域对等连接可以选择带宽上限。如需更大的跨地域带宽，请提 [工单](https://console.cloud.tencent.com/workorder/category) 申请。
![](https://main.qcloudimg.com/raw/0e525b591343b4ad30c2170405006ffd.jpg)
5. 单击【创建】。**同一账户内 VPC 进行连接，新建后对等连接立即生效。**

### 第四步：BI 新增路由策略
具体步骤如下：
1. 使用 BI 账号单击控制台左侧目录中的【子网】，进入管理页面。
2. 单击对等连接本端指定子网（子网 A）的关联路由表 ID（路由表 A），进入路由表的详情页。
![](https://main.qcloudimg.com/raw/7210f931dc919da05fd1fbb1e7dc36cd.jpg)
3. 单击【+新增路由策略】。
![](https://main.qcloudimg.com/raw/a375d7506b8e7075bdbd6f62661216d4.jpg)
4. 目的端中填入对端 Sparkling 私有网络 CIDR。【下一跳类型】选择【对等连接】，【下一跳】选择已建立的对等连接（PeerConn）。
![](https://main.qcloudimg.com/raw/6dfb18cede3e94bfbef4a1d57b953bcd.png)
 Sparkling 私有网络 CIDR，可在 Sparking 端选择【云产品】>【网络】>【私有网络】，进入私有网络控制台，私有网络 CIDR 如下图：
 ![](https://main.qcloudimg.com/raw/6e87dd28bc99c0a20c6edf6e6deff27a.png)
5. 单击【确定】。**路由表配置完成后，不同 VPC 的网段之间即可进行通信。**

### 第五步：Sparkling 接受由 BI 创建的对等连接
具体步骤如下：
1. 使用 Sparkling 账号登录 [腾讯云控制台](https://console.cloud.tencent.com/)，选择【云产品】>【网络】>【私有网络】，进入私有网络控制台。
2. 单击左侧目录中的【对等连接】，进入管理页面。
3. 在列表上方选择对应的地域，如广州， 找到列表中待接受的对等连接：PeerConn，单击【接受】。
![](https://main.qcloudimg.com/raw/b0c5a1c457ade0e5edd4c97c7a85e8a8.png)

### 第六步：Sparkling 新增路由策略
具体步骤如下：
1. 使用 Sparkling 账号单击控制台左侧目录中的【子网】，进入管理页面。
2. 单击对等连接本端指定子网（子网 A）的关联路由表 ID（路由表 A），进入路由表的详情页。
![](https://main.qcloudimg.com/raw/7210f931dc919da05fd1fbb1e7dc36cd.jpg)
3. 单击【+新增路由策略】。
![](https://main.qcloudimg.com/raw/a375d7506b8e7075bdbd6f62661216d4.jpg)
4. 目的端中填入 BI 私有网络 CIDR。【下一跳类型】选择【对等连接】，【下一跳】选择已建立的对等连接（PeerConn）。
![](https://main.qcloudimg.com/raw/6dfb18cede3e94bfbef4a1d57b953bcd.png)
 BI 私有网络 CIDR，可在 BI 端选择【云产品】>【网络】>【私有网络】，进入私有网络控制台，私有网络 CIDR 如下图：
![](https://main.qcloudimg.com/raw/4472dc4f0b58a7de33f90e1ba29f1b30.png)
5. 单击【确定】。**路由表配置完成后，不同 VPC 的网段之间即可进行通信。**

### 第七步：Sparkling 创建集群
使用 Sparkling 账号登录 [控制台 ](https://console.cloud.tencent.com/sparkling)，具体步骤可参考 [创建集群](https://cloud.tencent.com/document/product/1002/30551)。

### 第八步：BI 端添加 Sparkling 数据源
具体步骤如下：
1. 使用 BI 账号在自建 BI 界面操作单击左侧目录中的【添加数据源】 。
![](https://main.qcloudimg.com/raw/dd889a95a54fa35bff1379a4bee4d15f.png)
2. 单击数据源中的【SPARK】。
![](https://main.qcloudimg.com/raw/d59c6a329404bb483a0e48b87ce34b60.png)
3. 填写数据源内容。
 - 【URL】：将“Databaseserver”修改为 sparkling 集群的 JDBC SERVER 的 IP。查询 JDBC SERVER 的 IP 需提交 [工单](https://console.cloud.tencent.com/workorder/category)，并提供创建 Sparkling 集群的截图。
 - 【服务器登录】：选择【用户名】。
 - 【用户名】：填入“hadoop”，密码为空 。 
![](https://main.qcloudimg.com/raw/6c9f6f81dc4fc1e7abd3a6caebaf8376.png)
4. 单击【测试连接】。页面显示“测试成功”后，即可保存数据源，创建 BI 的数据集。
