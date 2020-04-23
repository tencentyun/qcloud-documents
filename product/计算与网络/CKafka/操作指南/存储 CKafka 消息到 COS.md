## 操作场景
消息队列 CKafka 支持用户存储消息的能力，您可以将消息存储到 COS 中，并下载分析。该白名单功能即将下线,正式功能查看[消息转储](https://cloud.tencent.com/document/product/597/43448)

## 前提条件

<span id="operation"></span>
## 操作步骤
1. 登录 [消息队列 CKafka 控制台](https://console.cloud.tencent.com/ckafka)。
2. 在实例列表页，单击目标实例 ID，进入**topic 管理**标签页。
3. 在 topic 管理标签页，单击操作列的【存储消息到 COS】。
4. 单击启用图标，开启开启存储消息到 COS 功能。
![](https://main.qcloudimg.com/raw/3337eafafaf6805fa0523bc51012f67c.png)
 - 时间粒度：根据消息量的大小，选取汇聚消息的时间间隔，时间间隔为5 - 60分钟不等。
 - 存放 Bucket：针对不同的 topic，选取相应的 COS 中 Bucket，则请求消息会自动在 Bucket 下创建 instance ID + topic ID 为名称的文件夹进行存储。选取完成后，单击 Bucket 地址可以直接跳转到文件下载页面。

如果您还未创建对象存储的 Bucket，请在 [新建 Bucket](https://console.cloud.tencent.com/cos/bucket) 后选取相应的存储位置。

<span id="postconditions"></span>
## 后置条件
开启【存储消息到 COS】功能后，CKafka 服务会在【访问管理】>【角色】中增加一个【cosCkafka_QCSRole】角色用来授权消息存储到 COS 服务。
- 如果您不再需要此项功能，请在 [CKafka 控制台](https://console.cloud.tencent.com/ckafka/index?rid=1) >【实例列表】>【topic 管理】中，单击操作列的【存储消息到 COS】，禁用此功能并删除其角色。
![](https://main.qcloudimg.com/raw/90bfbefc512b95d9e1345f2a9e58e136.png)

- 如果您需要一直使用此功能，但误删除了【cosCkafka_QCSRole】角色，将会影响消息存储到 COS，请及时重新创建角色。

具体创建步骤如下：
1. 主账号登录 [访问管理控制台](https://console.cloud.tencent.com/cam/overview)，在左侧导航栏中选择【角色】>【新建角色】>【腾讯云账号】，填写其他账号 ID：91000000031。
![](https://main.qcloudimg.com/raw/c4b83be38d3393224c5aed37008a1c02.png)
2. 搜索策略：QcloudCOSAccessForCkafkaRole，选中后单击【下一步】。
![](https://main.qcloudimg.com/raw/787c4bde85226c5f62596aa92a9ff235.png)
3. 填写角色名称和描述。
角色名称：cosCkafka_QCSRole
角色描述：	消息服务（CKafka）对对象存储服务（COS）的跨业务访问权限
![](https://main.qcloudimg.com/raw/53782c7cd8e66de2a4c6e261a147df32.png)
4. 单击【完成】，创建的角色将显示在角色列表中。
![](https://main.qcloudimg.com/raw/a3d60e97288278d3cb6266e153a5979b.png)
5. 在 CKafka 控制台中，观察 Consumer Group 数据消费是否正常。
![](https://main.qcloudimg.com/raw/d956ce9ec5f09e3dd5d8e2fd6b6f39ec.png)

>!子账号创建的实例或者 topic 使用消息存储到 COS，主帐号需要授权子帐号可以传递指定角色（Pass Role）给腾讯云 CKafka 服务（如果没有此步骤，则子帐号无法通过 CKafka 服务访问 COS 资源）。

您可以创建自定义策略并授权子账号，PassRole 策略语法如下：
```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": "cam:PassRole",
            "resource": "qcs::cam::uin/${roleOwnerUin}:roleName/cosCkafka_QCSRole"
        }
    ]
}
```

<span id="limit"></span>
## 产品限制和费用计算
- 该功能适用于少量数据备份到 COS 的场景，不保证数据能100%成功同步到 COS 中。
- 当前 COS 文件聚合粒度为5 - 60分钟不等，允许用户指定。
- 数据的传输会有一定的延迟。
- 当前仅支持和 CKafka 实例同个地域的 COS 进行消息存储，为保证延时，不支持跨地域存储。
- object 权限用 COS 默认的私有读写权限。
- 转储服务会占用一个 Group ID。
- 文件名为存放的 timestamp，存放路径为 `instance ID/topic ID`。
- 文件内容是 CKafka 消息里的 value 用 utf-8 String 序列化拼接而成，暂不支持二进制的数据格式。
- 当前 CKafka 消息到 COS 服务**免费**，COS 存储可享受一定 [免费额度](https://cloud.tencent.com/document/product/436/6240)，提供50GB免费存储空间。如您的消息量级较大，请及时清理数据。
- 开启转 COS 的操作人必须对目标 COS Bucket 具备写权限。
- 开启转发前，积压 Ckafka 消息不会被转存到 COS。
- 实例到期后转发 COS 也会中断，实例续费后会自动恢复转发。

## 旧版COS转储能力迁移说明
为提供更好的服务并全面支持更多Ckafka相关转储能力，我们将在近日对旧版白名单COS转储功能进行下线处理，并正式推出全新商业化COS转储能力。请及时做好相关迁移工作：

新版正式商业化COS转储能力有以下优势：
- 灵活转储：新版COS转储功能提供更加灵活的转储配置，创建完成后可在云函数控制台自定义较为特殊的转储逻辑，如设置特殊换行符，日志过滤等。亦可快捷方便的使用默认配置。
- 消费能力：新版转储消费能力相较旧版COS转储消费能力提升50%，是自建单节点 logstash 消费能力的15倍。
- 文件存储：新版 Ckafka 转储 COS 的单个文件最大500MB，如超过该数值，会自动分包上传。相较于之前旧版 20MB 分包，新版单包大小聚合能力提升25倍。
- 功能特性：新版 Ckafka 转储 COS 新增 "起始位置"特性，用户可自行选择历史消息的处理方式，更加方便的使用 to COS 转储功能。
- 更多支持：新版转储能力新增"通用转储"，可支持并自定义 Elasticsearch、MySQL、PostgreSQL 等通用场景的转储能力。

关于旧版COS转储能力迁移，您需要关注以下几点：

- 存储路径：为保证转储文件的可读性，新版COS转储存储路径将修改为 instance-id/topic-id/date/timestamp 。
> 说明：如相关路径如无法满足业务需要，请创建完成后在云函数控制台修改 CkafkaToCosConsumer 函数，参考下文迁移步骤。
-  时间聚合：新版Ckafka 转储 COS 为了保证转储服务的可用性防止消息堆积，故支持 1-15 分钟粒度。
-  费用相关：新版转储功能基于云函数 SCF 服务提供。SCF 为用户提供了一定量 [免费额度](https://cloud.tencent.com/document/product/583/12282) ，超额部分产生的收费，请以 SCF 服务的 [计费规则](https://cloud.tencent.com/document/product/583/17299) 为准。

更多说明参考  [消息转储文档](https://cloud.tencent.com/document/product/597/43448) 。

### 迁移步骤

1. 创建新版 消息转储
![](https://main.qcloudimg.com/raw/edf5b4726e84b0612df8a7dbd8ce2b3d.png)

2. 设置时间粒度，选择与之前相同的 Bucket 信息
![](https://main.qcloudimg.com/raw/b942d6e09a545493413c54e4def8f243.png)

> 注意：新版 COS 转储新增“起始位置”，可根据迁移需求自行选择 Topic 消费位置。

3. 如新版相关存储路径无法满足业务需要，可点击函数管理内的 CkafkaToCosConsumer 函数进行修改
![](https://main.qcloudimg.com/raw/2581f23de103e24279cbaf699eb2faaf.png)
![](https://main.qcloudimg.com/raw/cba941837c732f250599ca36b9734531.png)
将 CkafkaToCosConsumer 函数第49行 -56行内容替换为如下代码，点击保存即可与旧版存储路径保持一致
```
    # Generating file name. 生成写入文件名
    def object_key_generate(self):
        logger.info("start to generate key name")
        file_name = str(int(round(time.time())))
        dir_name = "{}/{}".format(str(self.kafka_instance_id), str(self.topic_id))
        object_key = '{}/{}'.format(dir_name, file_name)
        return object_key
```

4. 为避免重复存储数据，请关闭旧版COS转储功能
![](https://main.qcloudimg.com/raw/834c509f374f85f4326f450f97b6671b.png)
