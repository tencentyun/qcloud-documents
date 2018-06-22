
##  CAM 基本概念
根账户通过给子账户绑定策略实现授权，策略设置可精确到**[API，资源，用户/用户组，允许/拒绝，条件]**维度。

**1、 账户**
- **根账号**：腾讯云资源归属、资源使用计量计费的基本主体，可登录腾讯云服务。
- **子账号**：由根账号创建账号，有确定的身份ID和身份凭证，且能登录到腾讯云控制台。根账号可以创建多个子账号(用户)。**子账号默认不拥有资源，必须由所属根账号进行授权。**
- **身份凭证**：包括登录凭证和访问证书两种，**登录凭证**是指用户登录名和密码，**访问证书**是指云API密钥(SecretId和SecretKey)。

**2、资源与权限**

- **资源**：资源是云服务中被操作的对象，如一个云服务器实例，COS存储桶，VPC实例等。
- **权限**：权限是指允许或拒绝某些用户执行某些操作。默认情况下，**根账号拥有其名下所有资源的访问权限**，而**子账号没有根账号下任何资源的访问权限**。
- **策略**：策略是定义和描述一条或多条权限的语法规范。**根账号**通过将**策略关联**到用户/用户组完成授权。
[单击查看更多CAM介绍](https://cloud.tencent.com/document/product/378/9028)

##  相关文档
| 目标 | 链接 | 
|---------|---------|
|了解策略和用户之间关系|[策略管理](https://cloud.tencent.com/document/product/378/8955)|
|了解策略的基本结构| [策略语法](https://cloud.tencent.com/document/product/378/8962) | 
|了解还有哪些产品支持CAM|[支持CAM的云服务列表](https://cloud.tencent.com/document/product/378/9029)|

##  访问控制策略示例 

### CKafka全读写策略
授权一个子用户以CKafka服务的完全管理权限（创建、管理等全部操作）。
```
{
  "version": "2.0",
  "statement": [
    {
      "action": [
            "name/ckafka:*",
      ],
      "resource": "*",
      "effect": "allow"
    }
  ]
}
```

### CKafka单个实例读写策略
授权一个子用户某个特定实例的CKafka服务的完全管理权限（创建、管理等全部操作）。
```
{
  "version": "2.0",
  "statement": [
    {
      "action": [
            "name/ckafka:*",
      ],
      "resource": "qcs::ckafka:$region:uin/:ckafkaId/uin/$createUin/$instanceId",
      "effect": "allow"
    }
  ]
}
```





