## 操作场景
消息队列 CKafka 支持用户存储消息的能力，您可以将消息存储到 COS 中，并下载分析。

## 前提条件
该功能目前处于灰度测试阶段，如需试用请通过[ 提交工单](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=335&source=0&data_title=%E6%B6%88%E6%81%AF%E9%98%9F%E5%88%97CMQ/CKAFKA/IoT%20MQ&step=1) 的方式开通白名单。

## 操作步骤
1. 登录 [消息队列 CKafka 控制台](https://console.cloud.tencent.com/ckafka)。
2. 在实例列表页，单击目标实例 ID，进入**topic 管理**标签页。
3. 在 topic 管理标签页，单击操作列的【存储消息到 COS】。
4. 单击启用图标，开启开启存储消息到 COS 功能。
![](https://main.qcloudimg.com/raw/3337eafafaf6805fa0523bc51012f67c.png)
 - 时间粒度：根据消息量的大小，选取汇聚消息的时间间隔，时间间隔为5 - 60分钟不等。
 - 存放 Bucket：针对不同的 topic，选取相应的 COS 中 Bucket，则请求消息会自动在 Bucket 下创建 instance id + topic id 为名称的文件夹进行存储。选取完成后，单击 Bucket 地址可以直接跳转到文件下载页面。

如果您还未创建对象存储的 Bucket，请在 [新建 Bucket](https://console.cloud.tencent.com/cos/bucket) 后选取相应的存储位置。

## 后置条件
开启【存储消息到 COS】功能后，CKafka 服务会在【访问管理】>【角色】中增加一个【cosCkafka_QCSRole】角色用来授权消息存储到 COS 服务。
- 如果您不再需要此项功能，请在 [CKafka 控制台](https://console.cloud.tencent.com/ckafka/index?rid=1) >【实例列表】>【topic 管理】中，单击操作列的【存储消息到cos】，禁用此功能并删除其角色。
![](https://main.qcloudimg.com/raw/cbdfa1ba141d9f3f50d9f8b639173325.png)

- 如果您需要一直使用此功能，但误删除了【cosCkafka_QCSRole】角色，将会影响消息存储到 COS，请及时重新创建角色。

具体创建步骤如下：
1. 登录【[访问管理控制台](https://console.cloud.tencent.com/cam/overview)】，在左侧导航栏中选择【角色】>【新建角色】>【腾讯云账号】，填写其他账号ID：91000000031。
![](https://main.qcloudimg.com/raw/c4b83be38d3393224c5aed37008a1c02.png)
2. 搜索策略：QcloudCOSAccessForCkafkaRole，选中后单击【下一步】。
![](https://main.qcloudimg.com/raw/787c4bde85226c5f62596aa92a9ff235.png)
3. 填写角色名称和描述。
![](https://main.qcloudimg.com/raw/53782c7cd8e66de2a4c6e261a147df32.png)
角色名称：cosCkafka_QCSRole
角色描述：	消息服务（CKafka）对对象存储服务（COS）的跨业务访问权限
4. 单击【完成】，创建的角色将显示在角色列表中。
![](https://main.qcloudimg.com/raw/a3d60e97288278d3cb6266e153a5979b.png)
5. 在 CKafka 控制台中，观察 Consumer Group 数据消费是否正常。
![](https://main.qcloudimg.com/raw/5b9a909731c654c927bb08f217330458.png)

## 产品限制和费用计算
- 该功能适用于少量数据备份到 COS 的场景，不保证数据能100%成功同步到 COS 中。
- 当前 COS 文件聚合粒度为5 - 60分钟不等，允许用户指定。
- 数据的传输会有一定的延迟。
- 当前仅支持和 CKafka 实例同个地域的 COS 进行消息存储，为保证延时，不支持跨地域存储。
- object 权限用 COS 默认的私有读写权限。
- 转储服务会占用一个 group id。
- 文件名为存放的 timestamp，存放路径为 `instance id/topic id`。
- 文件内容是 CKafka 消息里的 value 用 String 序列化拼接而成。
- 当前 CKafka 消息到 COS 服务**免费**，COS 存储可享受一定 [免费额度](https://cloud.tencent.com/document/product/436/6240)，提供50G免费存储空间。如您的消息量级较大，请及时清理数据。
- 开启转 COS 的操作人必须对目标 COS Bucket 具备写权限。
- 开启转发前，积压 Ckafka 消息不会被转存到 COS。
- 实例到期后转发 COS 也会中断，实例续费后会自动恢复转发。
