## 简介

对象存储 COS 提供存储数据的监控能力，用户可通过监控数据窗口了解各数据的状况及趋势。COS 的数据统计的监控窗口包括请求量、流量、数据读取等基础数据统计和返回码统计。

## 通过主账号查询操作步骤

1. 登录 [对象存储桶控制台](https://console.cloud.tencent.com/cos5)，单击左侧菜单【存储桶列表】，然后选择需要进行统计数据的存储桶，并单击对应存储桶上的监控按钮，如下图所示：
   ![img](https://main.qcloudimg.com/raw/181be97d3b8eefb9a3298f440707c0ea.png)
2. 单击监控按钮，进入监控数据界面，如下图所示：
   ![img](https://main.qcloudimg.com/raw/b3f1ff522827c42eff044abe40aac5be.png)

>?
> - 在【当前数据】视窗，可切换当前数据或本月累计的数据，包括有存储容量、读写请求次数、流量、返回码和数据读取，时间粒度分别为实时、昨天、近7天、近30天。
> - 在【本月累计】视窗中，可以查看本月日均各存储类型的存储容量以及总流量（累计外网流量、累计CDN回源流量和累计跨区域复制流量）。

## 通过子账号查询操作步骤
通过子账号查询监控报表，您需要首先授予子账号查询监控报表的权限，此后才能使用子账号通过控制台查询监控报表。您可以通过使用策略模板或者自定义访问策略的方式，授予子账号访问监控报表的权限。

### 配置子账号访问监控报表权限
<a id="celie"></a>
#### 通过策略模板配置

1. 使用主账号登录 [访问管理控制台](https://console.cloud.tencent.com/cam)，单击左侧菜单【用户】，单击已创建的子账号。
![](https://main.qcloudimg.com/raw/838e61e330336c8b68564d7b5b381c5a.png)

2. 在策略列表中搜索`QcloudMonitorFullAccess`策略，单击确定添加至该子账号中，即可使用该子账号查阅云监控报表。
![Aaron Swartz](https://main.qcloudimg.com/raw/c1ffcc2c93a36a9c565b78b549b01d9b.png)

>!策略模板将授予访问云监控的所有权限，如您需要保护账号安全，可自定义配置子账户读权限的访问策略。

#### 通过自定义访问策略配置

1. 使用主账号登录 [访问管理控制台](https://console.cloud.tencent.com/cam)，单击策略模块，新建自定义策略。
![Aaron Swartz](https://main.qcloudimg.com/raw/63c631abf08ab7c80a8fb0828cb48288.png)

2. 选择按策略语法创建。
![](https://main.qcloudimg.com/raw/5bc3f55b92f80e721a9331c96e290f46.png)

3. 选择按照空白模板创建策略。
![](https://main.qcloudimg.com/raw/43f2263d11c2684ad10d9857fd18cf2b.png)

4. 在空白模板中，将以下策略语法填充至**编辑策略内容**输入框内。您可以根据自己业务需要修改策略名字。
策略语法：
```shell
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "monitor:GetMonitorData"
            ],
            "resource": "*"
        }
    ]
}
```
编辑策略内容输入框：
![Aaron Swartz](https://main.qcloudimg.com/raw/18e892e58e8c6c9966a169ad22e1d963.png)

5. 单击创建策略。策略创建成功后，您可对子账户授权相应策略。操作步骤请参阅 [通过策略模板配置](#celie)。
