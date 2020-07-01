### 授权子帐号拥有消息服务的所有权限

企业帐号CompanyExample下有一个子账号Developer，该子账号需要拥有对企业帐号CompanyExample名下的消息队列的所有权限，无论消息队列是主题模型还是队列模型，都可以被读写。

方案A：

企业帐号CompanyExample直接将预设策略QCloudCmqQueueFullAccess和QCloudCmqTopicFullAccess授权给子账号Developer。授权方式请参考[授权管理](https://cloud.tencent.com/document/product/378/8961)。

方案B：

step1：通过策略语法方式创建以下策略
```
 {
    "version": "2.0",
    "statement":
     {
         "effect": "allow",
         "action": ["name/cmqtopic:*","name/camqueue:*"]
         "resource": "*"
     }
}
```
step2：将该策略授权给子账号。授权方式请参考[授权管理](https://cloud.tencent.com/document/product/378/8961)。

### 授权子帐号拥有其创建的消息队列的所有权限

企业帐号CompanyExample下有一个子账号Developer，该子账号希望其可以访问自己创建的消息队列。

方案A：

企业帐号CompanyExample直接将预设策略QCloudCmqQueueCreaterFullAccess和QCloudCmqTopicCreaterFullAccess授权给子账号Developer。授权方式请参[考授权管理](https://cloud.tencent.com/document/product/378/8961)。

方案B：

step1：通过策略语法方式创建以下策略

```
{
    "version": "2.0",
    "statement":
    [
       {
           "effect": "allow",
           "action": "name/cmqtopic:*",
           "resource": "qcs::cmqtopic:::topicName/uin/${uin}/*"
       },
       {
           "effect": "allow",
           "action": "name/cmqqueue:*",
           "resource": "qcs::cmqqueue:::queueName/uin/${uin}/*"
       }
    ]
}
```

step2：将该策略授权给子账号。授权方式请参考[授权管理](https://cloud.tencent.com/document/product/378/8961)。

### 授权子帐号拥有特定的主题模型的消息队列的读权限

企业帐号CompanyExample（ownerUin为1234）有一个基于主题模型的消息队列，同时他有一个子账号Developer，希望其可以访问该消息队列。

step1：通过策略语法方式创建以下策略
```
{
    "version": "2.0",
    "statement":   
     {
        "action": "name/cmqqueue:SendMessage",
        "resource":"qcs::cmqqueue:::queueName/uin/1234/test-caten",
        "effect": "allow"
     } 
}
```

step2：将该策略授权给子账号。授权方式请参考[授权管理](https://cloud.tencent.com/document/product/378/8961)。
