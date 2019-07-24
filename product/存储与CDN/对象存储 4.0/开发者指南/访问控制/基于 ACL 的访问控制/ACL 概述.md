## 基本概念

访问控制列表（ACL）使用 XML 语言描述，是与资源关联的一个指定被授权者和授予权限的列表，每个存储桶和对象都有与之关联的 ACL，支持向匿名用户或其他腾讯云的主账号授予基本的读写权限。

>!使用与资源关联的 ACL 管理有一些限制：
>- 资源的拥有者始终对资源具备 FULL_CONTROL 权限，无法撤销或修改。
>- 匿名用户无法成为资源拥有者，此时对象资源的拥有者属于存储桶的创建者（腾讯云主账号）。
>- 仅可对腾讯云 CAM 主账号或匿名用户授予权限，无法授予子用户或用户组权限。
>- 不支持对权限附加条件。
>- 不支持显示拒绝的权限。
>- 一个资源最多可以拥有100条 ACL 策略。

## ACL 的元素

### 身份 Grantee

支持的被授权身份可以是某个 CAM 主账号，或者是某个预设的 CAM 用户组。

>!
>- 当您授予了其他腾讯云主账号访问权限时，这个被授权的主账号可以授权其名下的子用户、用户组或角色的访问权限。
>- COS 完全不建议您对匿名用户或 CAM 用户组授予 WRITE、WRITE_ACP 或 FULL_CONTROL 权限。一旦授权许可后，用户组可以对您的资源进行上传、下载、删除等行为，这将会给您带来数据丢失、扣费等风险。


在存储桶或对象的 ACL 中支持授予的身份包括：

- 跨账号：请使用主账号的 ID，通过【账号中心】的 [账号信息](https://console.cloud.tencent.com/developer) 获得账号 ID，例如398620000。
- 预设用户组：请使用 URI 标签标记预设的用户组，支持的用户组包括：
  - 匿名用户组 -`http://cam.qcloud.com/groups/global/AllUsers`该组代表了任何人都可以无需授权而访问资源，无论请求已签名或者未签名。
  - 认证用户组 -`http://cam.qcloud.com/groups/global/AuthenticatedUsers`该组代表所有经过腾讯云 CAM 账户认证的用户都可以访问资源。


### 操作 Permission

腾讯云对象存储 COS 在资源 ACL 上支持的操作实际上是一系列的操作集合，对于存储桶和对象 ACL 来说分别代表不同的含义。

**存储桶的操作**

下表列出了支持在存储桶 ACL 中设置的操作列表：

| 操作集       | 描述                 | 许可的行为                                                   |
| ------------ | -------------------- | ------------------------------------------------------------ |
| READ         | 列出对象             | GetBucket，HeadBucket，GetBucketObjectVersions，ListMultipartUploads |
| WRITE        | 上传、覆盖和删除对象 | PutObject，PutObjectCopy，PostObject，InitiateMultipartUpload， UploadPart，UploadPartCopy，CompleteMultipartUpload， DeleteObject |
| READ_ACP     | 读取存储桶的 ACL     | GetBucketAcl                                                 |
| WRITE_ACP    | 写入存储桶的 ACL     | PutBucketAcl                                                 |
| FULL_CONTROL | 以上四种权限的集合   | 以上所有行为的集合                                           |

>!请谨慎授予存储桶 WRITE、WRITE_ACP 或 FULL_CONTROL 权限。授予存储桶 WRITE 权限将允许被授权者覆盖或删除已有的任何对象。

**对象的操作**

下表列出了支持在对象 ACL 中设置的操作列表：

| 操作集       | 描述               | 许可的行为                              |
| ------------ | ------------------ | --------------------------------------- |
| READ         | 读取对象           | GetObject，GetObjectVersion，HeadObject |
| READ_ACP     | 读取对象的 ACL     | GetObjectAcl，GetObjectVersionAcl       |
| WRITE_ACP    | 写入对象的 ACL     | PutObjectAcl，PutObjectVersionAcl       |
| FULL_CONTROL | 以上四种权限的集合 | 以上所有行为的集合                      |

>?对象不支持授予 WRITE 操作集。

### 预设的 ACL

对象存储 COS 支持一系列预设的 ACL 进行授权，方便简单权限的描述。使用预设 ACL 描述时，需要在 PUT Bucket/Object 或 PUT Bucket/Object acl 中携带 x-cos-acl 头部并描述所需权限，如果同时在请求正文中携带了 XML 的描述内容，我们将优先选择头部中的描述并忽略请求正文中的 XML 描述。

**存储桶的预设 ACL**

| 预设名称           | 描述                                                               |
| ------------------ | ------------------------------------------------------------------ |
| private            | 创建者（主账号）具备 FULL_CONTROL 权限，其他人没有权限（默认）   |
| public-read        | 创建者具备 FULL_CONTROL 权限，匿名用户组具备 READ 权限           |
| public-read-write  | 创建者和匿名用户组都具备 FULL_CONTROL 权限，通常不建议授予此权限 |
| authenticated-read | 创建者具备 FULL_CONTROL 权限，认证用户组具备 READ 权限           |

**对象的预设 ACL**

| 预设名称                  | 描述                                                                         |
| ------------------------- | ---------------------------------------------------------------------------- |
| default                   | 空描述，此时根据各级目录的显式设置及存储桶的设置来确定是否允许请求（默认） |
| private                   | 创建者（主账号）具备 FULL_CONTROL 权限，其他人没有权限                     |
| public-read               | 创建者具备 FULL_CONTROL 权限，匿名用户组具备 READ 权限                     |
| authenticated-read        | 创建者具备 FULL_CONTROL 权限，认证用户组具备 READ 权限                  |
| bucket-owner-read         | 创建者具备 FULL_CONTROL 权限，存储桶拥有者具备 READ 权限                   |
| bucket-owner-full-control | 创建者和和存储桶拥有者都具备 FULL_CONTROL 权限                             |

>?对象不支持授予 public-read-write 权限。

## 示例
### 存储桶的 ACL
在创建存储桶时，COS 将创建一个默认的 ACL 以赋予资源拥有者对资源的完全控制权限（FULL_CONTROL），示例如下：

```xml
<AccessControlPolicy>
  <Owner>
    <ID>Owner-Cononical-CAM-User-Id</ID>
  </Owner>
  <AccessControlList>
    <Grant>
      <Grantee>
        <ID>Owner-Cononical-CAM-User-Id</ID>
      </Grantee>
      <Permission>FULL_CONTROL</Permission>
    </Grant>
  </AccessControlList>
</AccessControlPolicy>
```

### 对象的 ACL

**在创建对象时，COS 默认不会创建 ACL，此时对象的拥有者为存储桶拥有者。**对象继承存储桶的权限，与存储桶的访问权限一致。由于对象没有默认的 ACL，其将遵循存储桶策略（Bucket Policy）中对访问者和其行为的定义，来判断请求是否被许可。详情请参见 [访问策略语言概述](https://cloud.tencent.com/document/product/436/18023) 文档。

如果您需要对对象授予其他访问权限，您可以在此基础上添加更多的 ACL 来描述对象的访问权限。例如授予匿名用户只读单个对象的权限，示例如下：

```xml
<AccessControlPolicy>
  <Owner>
    <ID>Owner-Cononical-CAM-User-Id</ID>
  </Owner>
  <AccessControlList>
    <Grant>
      <Grantee>
        <ID>Owner-Cononical-CAM-User-Id</ID>
      </Grantee>
      <Permission>FULL_CONTROL</Permission>
    </Grant>
    <Grant>
      <Grantee>
        <URI>http://cam.qcloud.com/groups/global/AllUsers</URI>
      </Grantee>
      <Permission>READ</Permission>
    </Grant>
  </AccessControlList>
</AccessControlPolicy>
```

