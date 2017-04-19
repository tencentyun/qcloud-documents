# Python sdk
## 开发准备

### 相关资源
-[GitHub地址](https://github.com/tencentyun/cmq-python-sdk) ,欢迎贡献代码以及反馈问题。

-[python sdk 本地下载]()
### 环境依赖
python2.7 目前不支持python3

获取python版本的方法：

linux shell 

```

    $python -V

    Python 2.7.11
```

windows cmd

```
   
    D:>python -V
    Python 2.7.11
```

如果提示不是内部或者外部命令，请先在window环境变量PATH里面添加上python的绝对路径

### 历史版本

## 生成客户端对象

``` 
    secretId='xxxxxx'    #替换为用户的secretId
    secretKey = 'xxxxxx' #替换为用户的secretKey
    endpoint = 'https://cmq-queue-region.api.tencentyun.com' # 替换为用户的region , 例如 sh 表示上海， gz表示广州，bj表示北京
    account = Account(endpoint,secretId,secretKey)
```
### 初始化客户端配置
客户端默认使用sha1 签名算法，可以调用签名算法修改签名方式

```
    account.set_sign_method('sha256')
```

## 队列模式
### 队列相关接口
#### 创建队列
##### 方法原型

```
    def create(self, queue_meta)
```

##### 参数说明

| 参数名 | 类型 | 默认值 | 参数描述 |
|---------|---------|---------|---------|
|queue_meta|QueueMeta|无|队列属性|

QueueMeta结构体 描述如下：

| 属性名称 | 类型 | 含义 |
|---------|---------|---------|
|queueName|string|队列名称|
|maxMsgHeapNum|int|队列中最大的消息堆积数量|
|pollingWaitSeconds|int|队列消费消息时默认轮训时间，单位：秒|
|visibilityTimeout|int|消息可见性超时， 单位：秒|
|maxMsgSize|int|消息最大长度，单位：Byte|
|msgRetentionSeconds|int|消息在队列中的保留周期，单位：秒|
|rewindSeconds|int|队列允许回溯时间，单位：秒|
|activeMsgNum|int|队列中，可消费消息数，近似值|
|inactiveMsgNum|int|队列中，正在被消费的消息数，近似值|
|createTime|unix time| 队列创建时间， unix时间戳|
|lastModifyTime|unix time|最近一次修改队列属性时间，unix时间戳|
|rewindmsgNum|int|已经删除，但是还在回溯保留时间内的消息数量|
|minMsgTime|int|消息最小未消费时间，单位：秒|
|delayMsgNum|int|延时消息数量|

##### 使用示例

```
    queue_name ="MySampleQueue"
    my_queue = my_account.get_queue(queue_name)
    # 创建队列, 具体属性请参考cmq/queue.py中的QueueMeta结构
    queue_meta = QueueMeta()
    queue_meta.queueName = queue_name
    queue_meta.pollingWaitSeconds = 10
    queue_meta.visibilityTimeout = 10
    queue_meta.maxMsgSize = 1024
    queue_meta.msgRetentionSeconds = 3600
    my_queue.create(queue_meta)
```

#### 获取队列属性
##### 方法原型

```
    def get_attributes(self)
```

##### 参数说明


无入参


返回值 QueueMeta结构体 描述如下：

| 属性名称 | 类型 | 含义 |
|---------|---------|---------|
|queueName|string|队列名称|
|maxMsgHeapNum|int|队列中最大的消息堆积数量|
|pollingWaitSeconds|int|队列消费消息时默认轮训时间，单位：秒|
|visibilityTimeout|int|消息可见性超时， 单位：秒|
|maxMsgSize|int|消息最大长度，单位：Byte|
|msgRetentionSeconds|int|消息在队列中的保留周期，单位：秒|
|rewindSeconds|int|队列允许回溯时间，单位：秒|
|activeMsgNum|int|队列中，可消费消息数，近似值|
|inactiveMsgNum|int|队列中，正在被消费的消息数，近似值|
|createTime|unix time| 队列创建时间， unix时间戳|
|lastModifyTime|unix time|最近一次修改队列属性时间，unix时间戳|
|rewindmsgNum|int|已经删除，但是还在回溯保留时间内的消息数量|
|minMsgTime|int|消息最小未消费时间，单位：秒|
|delayMsgNum|int|延时消息数量|

##### 使用示例

```
   queue_meta = my_queue.get_attributes()
```

#### 设置队列属性
##### 方法原型

```
    def set_attributes(self, queue_meta)
```

##### 参数说明

| 参数名 | 类型 | 默认值 | 参数描述 |
|---------|---------|---------|---------|
|queue_meta|QueueMeta|无|队列属性|

QueueMeta结构体 描述如下：

| 属性名称 | 类型 | 含义 |
|---------|---------|---------|
|queueName|string|队列名称|
|maxMsgHeapNum|int|队列中最大的消息堆积数量|
|pollingWaitSeconds|int|队列消费消息时默认轮训时间，单位：秒|
|visibilityTimeout|int|消息可见性超时， 单位：秒|
|maxMsgSize|int|消息最大长度，单位：Byte|
|msgRetentionSeconds|int|消息在队列中的保留周期，单位：秒|
|rewindSeconds|int|队列允许回溯时间，单位：秒|
|activeMsgNum|int|队列中，可消费消息数，近似值|
|inactiveMsgNum|int|队列中，正在被消费的消息数，近似值|
|createTime|unix time| 队列创建时间， unix时间戳|
|lastModifyTime|unix time|最近一次修改队列属性时间，unix时间戳|
|rewindmsgNum|int|已经删除，但是还在回溯保留时间内的消息数量|
|minMsgTime|int|消息最小未消费时间，单位：秒|
|delayMsgNum|int|延时消息数量|

返回值 无

##### 使用示例

```
    queue_meta = QueueMeta()
    queue_meta.maxMsgSize = 65536
    my_queue.set_attributes(queue_meta)
```

#### 获取队列列表
##### 方法原型

```
    def list_queue(self, searchWord="", limit=-1, offset="")
```

##### 参数说明

| 参数名 | 类型 | 默认值 | 参数描述 |
|---------|---------|---------|---------|
|searchWord|string|""|搜索关键字。|
|offset|int|""|返回列表偏移值。|
|limit|int|-1|本次返回列表限制个数，不填写默认为返回20个。|

返回值 为三元组 描述如下：
(totalCount, queueList,next_offset)

| 参数名 | 类型 | 参数描述 |
|---------|---------|---------|
|totalCount|int|表示所有的队列个数。|
|queueList|array|queue数组。|
|next_offset|int|本次列出队列列表结尾位置，用户可以使用该值作为下一次列出队列的偏移量。|

##### 使用示例

```
    totalCount, queueList, next_offset= account.list_queue()
```
#### 回溯队列
##### 方法原型

```
    def rewindQueue(self, backTrackingTime)
```

##### 参数说明

|参数名|类型|默认值|参数描述|
|---------|---------|---------|---------|
|backTrackingTime|unix time|无|队列回溯时间点。队列可回溯时间范围可以通过获取队列属性查询。|

返回值  无

##### 使用示例

```
    my_queue.rewindQueue(1492506197)
```

#### 删除队列
##### 方法原型

```
    def delete(self)
```

##### 参数说明

入参 无

返回值 无

##### 使用示例

```
    my_queue.delete()
```

### 消息相关接口
#### 发送消息
##### 方法原型

```
    def send_message(self, message, delayTime=0)
```

##### 参数说明

|参数名|类型|默认值|参数描述|
|---------|---------|---------|---------|
|message|Message|None|消息|
|delayTime|int|0|延时时间，默认为0。|


返回值 Message  Message.msgId 表示该消息的消息Id

##### 使用示例

```
    msg_body = "I am test message."
    msg = Message(msg_body)
    re_msg = my_queue.send_message(msg)
    print "Send Message Succeed! MessageBody:%s MessageID:%s" % (msg_body, re_msg.msgId)
```


#### 批量发送消息
##### 方法原型

```
    def batch_send_message(self, messages, delayTime=0)
```

##### 参数说明

|参数名|类型|默认值|参数描述|
|---------|---------|---------|---------|
|messages|Message 数组|无|消息数组|
|delayTime|int|0|延时时间。|

返回值 Message 数组  Message.msgId 表示该消息的消息Id

##### 使用示例

```
    msg_count=3
    messages=[]
    for i in range(msg_count):
        msg_body = "I am test message %s." % i
        msg = Message(msg_body)
        messages.append(msg)
		
    re_msg_list = my_queue.batch_send_message(messages)	
    print "Batch Send Message Succeed! Messages\n%s" % ('\n'.join(['MessageBody:%s MessageID:%s' % (msg.msgBody, msg.msgId) for msg in re_msg_list]))
```

#### 消费消息
##### 方法原型

```
    def disable_key(self, KeyId=None)
```

##### 参数说明

|参数名|类型|默认值|参数描述|
|---------|---------|---------|---------|
|KeyId|string|None|主密钥Id|

返回值 无
##### 使用示例

```
    kms_account.disable_key(KeyId)
```

#### 删除消息
##### 方法原型

```
    def disable_key(self, KeyId=None)
```

##### 参数说明

|参数名|类型|默认值|参数描述|
|---------|---------|---------|---------|
|KeyId|string|None|主密钥Id|

返回值 无
##### 使用示例

```
    kms_account.disable_key(KeyId)
```

#### 批量消费消息
##### 方法原型

```
    def disable_key(self, KeyId=None)
```

##### 参数说明

|参数名|类型|默认值|参数描述|
|---------|---------|---------|---------|
|KeyId|string|None|主密钥Id|

返回值 无
##### 使用示例

```
    kms_account.disable_key(KeyId)
```

#### 批量删除消息
##### 方法原型

```
    def disable_key(self, KeyId=None)
```

##### 参数说明

|参数名|类型|默认值|参数描述|
|---------|---------|---------|---------|
|KeyId|string|None|主密钥Id|

返回值 无
##### 使用示例

```
    kms_account.disable_key(KeyId)
```


## 主题模式
### 主题相关接口
#### 创建主题
##### 方法原型

```
    def create_key(self, Description=None, Alias="", KeyUsage='ENCRYPT/DECRYPT')
```

##### 参数说明

| 参数名 | 类型 | 默认值 | 参数描述 |
|---------|---------|---------|---------|
|Description|string|None|主密钥描述|
|Alias|string|空字符串|主密钥别名|
|KeyUsage|string|'ENCRYPT/DECRYPT'|主密钥用途：默认是加解密|

返回值 KeyMetadata结构体 描述如下：

| 属性名称 | 类型 | 含义 |
|---------|---------|---------|
|KeyId|string|密钥id|
|CreateTime|uinx time|创建时间|
|Description|string|密钥描述|
|KeyState|string|密钥状态|
|KeyUsage|string|密钥用途|
|Alias|string|密钥别名|

##### 使用示例

```
    description ='for test'
    alias = 'kms_test'
    kms_meta = kms_account.create_key(description,alias)
```

#### 获取队列属性
##### 方法原型

```
    def get_key_attributes(self, KeyId=None)
```

##### 参数说明

| 参数名 | 类型 | 默认值 | 参数描述 |
|---------|---------|---------|---------|
|KeyId|string|None|主密钥Id|

返回值 KeyMetadata结构体 描述如下：

| 属性名称 | 类型 | 含义 |
|---------|---------|---------|
|KeyId|string|密钥id|
|CreateTime|uinx time|创建时间|
|Description|string|密钥描述|
|KeyState|string|密钥状态|
|KeyUsage|string|密钥用途|
|Alias|string|密钥别名|

##### 使用示例

```
    keyId=''  # 请填写你的keyId
    key_meta = kms_account.get_key_attributes("kms-awy8dndb")
    print key_meta
```

#### 修改主题属性
##### 方法原型

```
    def set_key_attributes(self, KeyId=None, Alias=None)
```

##### 参数说明

| 参数名 | 类型 | 默认值 | 参数描述 |
|---------|---------|---------|---------|
|KeyId|string|None|主密钥Id|
|Alias|string|None|主密钥别名|

返回值 无

##### 使用示例

```
    keyId=''  # 请填写你的keyId
    Alias=''  # 请填写你的主密钥别名
    kms_account.get_key_attributes(keyId,Alias)
```

#### 获取主题列表
##### 方法原型

```
    def list_key(self, offset=0, limit=10)
```

##### 参数说明

| 参数名 | 类型 | 默认值 | 参数描述 |
|---------|---------|---------|---------|
|offset|int|0|返回列表偏移值。|
|limit|int|10|本次返回列表限制个数，不填写默认为返回10个。|

返回值 KeyMetadata结构体 描述如下：

|属性名称|类型|含义|
|---------|---------|---------|
|totalCount|int|表示所有的密钥个数。|
|keys|array|key数组。|

##### 使用示例

```
    totalCount, keys = kms_account.list_key()
    print keys
```
#### 删除主题
##### 方法原型

```
    def generate_data_key(self, KeyId=None, KeySpec=None, NumberOfBytes=None, EncryptionContext=None)
```

##### 参数说明

|参数名|类型|默认值|参数描述|
|---------|---------|---------|---------|
|KeyId|string|None|主密钥Id。|
|KeySpec|string|None|生成数据密钥算法。|
|NumberOfBytes|int|None|生成指定长度的数据密钥。|

返回值 
(plaintext, ciphertextBlob)

plaintext 表示生成的数据密钥明文

ciphertextBlob：表示生成的数据密钥密文
##### 使用示例

```
        KeySpec = "AES_128"
        Plaintext, CiphertextBlob = kms_account.generate_data_key(KeyId, KeySpec)
        print "the data key : %s \n  the encrypted data key :%s\n" % (Plaintext, CiphertextBlob)
```


### 消息相关接口
#### 发布消息
##### 方法原型

```
    def disable_key(self, KeyId=None)
```

##### 参数说明

|参数名|类型|默认值|参数描述|
|---------|---------|---------|---------|
|KeyId|string|None|主密钥Id|

返回值 无
##### 使用示例

```
    kms_account.disable_key(KeyId)
```

#### 批量发布消息
##### 方法原型

```
    def disable_key(self, KeyId=None)
```

##### 参数说明

|参数名|类型|默认值|参数描述|
|---------|---------|---------|---------|
|KeyId|string|None|主密钥Id|

返回值 无
##### 使用示例

```
    kms_account.disable_key(KeyId)
```

#### 消费消息
##### 方法原型

```
    def disable_key(self, KeyId=None)
```

##### 参数说明

|参数名|类型|默认值|参数描述|
|---------|---------|---------|---------|
|KeyId|string|None|主密钥Id|

返回值 无
##### 使用示例

```
    kms_account.disable_key(KeyId)
```

#### 投递消息
##### 方法原型

```
    def disable_key(self, KeyId=None)
```

##### 参数说明

|参数名|类型|默认值|参数描述|
|---------|---------|---------|---------|
|KeyId|string|None|主密钥Id|

返回值 无
##### 使用示例

```
    kms_account.disable_key(KeyId)
```

### 订阅相关接口
#### 创建订阅
##### 方法原型

```
    def disable_key(self, KeyId=None)
```

##### 参数说明

|参数名|类型|默认值|参数描述|
|---------|---------|---------|---------|
|KeyId|string|None|主密钥Id|

返回值 无
##### 使用示例

```
    kms_account.disable_key(KeyId)
```

#### 获取订阅属性
##### 方法原型

```
    def disable_key(self, KeyId=None)
```

##### 参数说明

|参数名|类型|默认值|参数描述|
|---------|---------|---------|---------|
|KeyId|string|None|主密钥Id|

返回值 无
##### 使用示例

```
    kms_account.disable_key(KeyId)
```

#### 获取订阅属性
##### 方法原型

```
    def disable_key(self, KeyId=None)
```

##### 参数说明

|参数名|类型|默认值|参数描述|
|---------|---------|---------|---------|
|KeyId|string|None|主密钥Id|

返回值 无
##### 使用示例

```
    kms_account.disable_key(KeyId)
```

#### 设置订阅属性
##### 方法原型

```
    def disable_key(self, KeyId=None)
```

##### 参数说明

|参数名|类型|默认值|参数描述|
|---------|---------|---------|---------|
|KeyId|string|None|主密钥Id|

返回值 无
##### 使用示例

```
    kms_account.disable_key(KeyId)
```

#### 获取订阅列表
##### 方法原型

```
    def disable_key(self, KeyId=None)
```

##### 参数说明

|参数名|类型|默认值|参数描述|
|---------|---------|---------|---------|
|KeyId|string|None|主密钥Id|

返回值 无
##### 使用示例

```
    kms_account.disable_key(KeyId)
```

#### 清空订阅标签
##### 方法原型

```
    def disable_key(self, KeyId=None)
```

##### 参数说明

|参数名|类型|默认值|参数描述|
|---------|---------|---------|---------|
|KeyId|string|None|主密钥Id|

返回值 无
##### 使用示例

```
    kms_account.disable_key(KeyId)
```

#### 删除订阅
##### 方法原型

```
    def disable_key(self, KeyId=None)
```

##### 参数说明

|参数名|类型|默认值|参数描述|
|---------|---------|---------|---------|
|KeyId|string|None|主密钥Id|

返回值 无
##### 使用示例

```
    kms_account.disable_key(KeyId)
```


