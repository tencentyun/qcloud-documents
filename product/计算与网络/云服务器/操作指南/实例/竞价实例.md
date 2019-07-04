目前已上线竞价实例的两种使用方式。
* **云 API** 
[CVM RunInstance 接口](/document/api/213/15730) 已增加竞价实例相关参数。
* **批量计算控制台** 
批量计算已支持提交作业和创建计算环境时选择竞价实例。

## 云 API
接口 RunInstance 内参数 [InstanceMarketOptionsRequest](https://cloud.tencent.com/document/api/213/15753#InstanceMarketOptionsRequest) 可指定使用竞价实例模式和配置相关信息。
![](https://main.qcloudimg.com/raw/8e3dc464e202ed3355b6bb3b4fe72566.png)
![](https://main.qcloudimg.com/raw/281df8c2b655876f612c8ae34f1e2951.png)
* **同步接口**：目前 RunInstance 提供的是一次性的同步请求接口，即申请失败（库存不足、请求价格低于市场价格）则马上返回失败，且不再继续申请。
* **固定价格（公测）**：公测期间采用固定折扣模式，所以您必须设置参数为大于等于当前市场价格，详细市场价格请查阅 [竞价实例 - 竞价实例支持地域和类型](/doc/product/213/17817)。

### 云 API 示例
#### 场景描述
实例所在地域为广州三区，付费模式为按小时后付费竞价模式，最高竞价出价：0.6元/小时，竞价请求模式：一次性请求，镜像 ID 为：img-pmqg1cw7，选择机型为：2C4G 二代标准型（S2.MEDIUM4），购买数量为1台。

#### 请求参数
```
https://cvm.tencentcloudapi.com/?Action=RunInstances
&Placement.Zone=ap-guangzhou-3
&InstanceChargeType=SPOTPAID
&InstanceMarketOptions.MarketType=spot
&InstanceMarketOptions.SpotOptions.MaxPrice=0.60
&InstanceMarketOptions.SpotOptions.SpotInstanceType=one-time
&ImageId=img-pmqg1cw7
&InstanceType=S2.MEDIUM4
&InstanceCount=1
&<公共请求参数>
```

#### 返回参数
```
{
  "Response": {
    "InstanceIdSet": [
      "ins-1vogaxgk"
    ],
    "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
  }
}
```

## 批量计算（Batch）控制台
* **异步接口**：提交作业或者创建计算环境、修改计算环境期望数量时，批量计算将以异步的形式处理您的请求，也就是在当前请求因为库存、价格等原因无法满足时，持续申请竞价实例型资源直到满足为止。（所以当您需要释放实例的时候，需要在批量计算控制台调整计算环境实例数量，若在云服务器控制台释放，批量计算会自动帮您再次创建直到满足期望数量）
* **集群模式**：批量计算的计算环境支持以集群的模式维护一批竞价实例，您只需要提交需要的数量、配置和最高出价，计算环境将自动持续发起申请直到满足期望数量，发生中断后也会自动再次发起申请补充数量
* **固定价格（公测）**：同云 API，必须大于等于当前市场价格。

### 批量计算控制台使用步骤

#### I.打开批量计算控制台
![](https://main.qcloudimg.com/raw/77c64f7632e04183d598bbb8af9211cd.jpg)

首先进入 [批量计算控制台](https://console.cloud.tencent.com/batch/env)。

#### II. 进入创建计算环境
单击【新建】即可进入新建计算环境的页面。

![](https://main.qcloudimg.com/raw/84c0019c5f2cd090a829f2bd35f06d03.jpg)

确认您已获得竞价实例使用资格：任意选择一个已支持竞价实例的可用区（例如广州三区），如果可以在图中标识的下拉菜单里查看到【竞价实例】选项，即表示已在白名单内。如果没有【竞价实例】选项，请先提交使用申请并等待审批通过。

#### III. 创建采用竞价实例的计算环境

![](https://main.qcloudimg.com/raw/f9db70d48dedf80f4977efb88c008f60.jpg)

选择【竞价实例】类型，同时选择好您需要的机型、镜像、名称、期望实例数量等信息，单击【确定】。

#### IV. 查看创建好的计算环境

![](https://main.qcloudimg.com/raw/086852467032fa4cf9e209e4afe86c96.jpg)

创建完成，会回到 [批量计算控制台](https://console.cloud.tencent.com/batch/env)，可以看到刚才创建的计算环境，计算环境内的云服务器也在同步创建中，您可以通过【活动日志】和【实例列表】来查看创建情况。
