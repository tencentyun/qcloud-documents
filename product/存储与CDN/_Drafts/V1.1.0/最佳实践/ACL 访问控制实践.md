## ACL 概述

访问控制列表 (ACL) 是基于资源的访问策略选项之一 ，可用来管理对存储桶和对象的访问。使用 ACL 可向其他根账户、子账户和用户组授予基本的读、写权限。

与访问策略有所不同的是，ACL 的管理权限有一些限制：

- 仅支持对腾讯云的账户赋予权限
- 仅支持读、写、读权限、写权限和完整权限等五个操作组
- 不支持赋予生效条件
- 不支持显示拒绝效力

ACL 支持的控制粒度：

- 存储桶 (Bucket)
- 对象键前缀 (Prefix)
- 对象 (Object)

## ACL 的控制元素

当创建存储桶或对象时，其资源所属的主账户将具备对资源的完全权限，且不可修改或删除。您可以使用 ACL 赋予其他腾讯云账户的访问权限。如下提供了一个存储桶的 ACL 示例。

```xml
<AccessControlPolicy>
  <Owner>
    <ID>qcs::cam::uin/12345:uin/12345</ID>
    <DisplayName>qcs::cam::uin/12345:uin/12345</DisplayName>
  </Owner>
  <AccessControlList>
    <Grant>
      <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="RootAccount">
        <ID>qcs::cam::uin/12345:uin/12345</ID>
        <DisplayName>qcs::cam::uin/12345:uin/12345</DisplayName>
      </Grantee>
      <Permission>FULL_CONTROL</Permission>
    </Grant>
    <Grant>
      <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="RootAccount">
        <ID>qcs::cam::uin/54321:uin/54321</ID>
        <DisplayName>qcs::cam::anyone:anyone</DisplayName>
      </Grantee>
      <Permission>READ</Permission>
    </Grant>
  </AccessControlList>
</AccessControlPolicy>
```

如上 ACL 包含了识别该存储桶所有者的 Owner 元素，其具备该存储桶的完整权限。同时 Grant 元素授予了匿名的读取权限，其表述为 qcs::cam::anyone:anyone 的 READ 权限。

### 权限被授予者

#### 根账户

您可以授予其他根账户的用户访问权限，其使用 CAM 中对委托人 (principal) 的定义。例如：

```
qcs::cam::uin/1238423:uin/1238423
```

#### 子账户

您可以授权您的根账户下的子账户，亦可以授权给其他根账户下的子账户，其使用 CAM 中对委托人 (principal) 的定义。例如：

```
qcs::cam::uin/1238423:uin/3232
```

#### 匿名用户

您可以授权匿名用户的访问权限，其使用 CAM 中对委托人 (principal) 的定义。描述为：

```
qcs::cam::anyone:anyone
```

### 权限操作组

以下表格提供了 ACL 支持的权限操作组。

| 操作组          | 授予存储桶             | 授予前缀             | 授予对象      |
| ------------ | ----------------- | ---------------- | --------- |
| READ         | 列出和读取存储桶中的对象      | 列出和读取目录下的对象      | 读取对象      |
| WRITE        | 创建、覆盖和删除存储桶中的任意对象 | 创建、覆盖和删除目录下的任意对象 | 覆盖和删除对象   |
| READ_ACP     | 读取存储桶的 ACL        | 读取目录下的 ACL       | 读取对象的 ACL |
| WRITE_ACP    | 修改存储桶的 ACL        | 修改目录下的 ACL       | 修改对象的 ACL |
| FULL_CONTROL | 对存储桶和对象的任何操作      | 对目录下的对象做任何操作     | 对对象执行任何操作 |

### 标准 ACL 描述

COS 支持一系列的预定义授权，称之为标准 ACL，下表列出了标准 ACL 的授权含义。

*注意：由于主账户始终拥有 FULL_CONTROL 权限，以下表格中不再对此特别说明。*

| 标准 ACL            | 含义                                      |
| ----------------- | --------------------------------------- |
| (空)               | 此为默认策略，其他人无权限，资源继承上级权限。                 |
| private           | 其他人没有权限。                                |
| public-read       | 匿名用户组具备 READ 权限。                        |
| public-read-write | 匿名用户组具备 READ 和 WRITE 权限，通常不建议在存储桶赋予此权限。 |

## ACL 示例

### 为存储桶设置 ACL

以下示例对存储桶授予了另一个根账户的读取权限：

![](//mc.qcloudimg.com/static/img/7088f7b6c3336668b4b04f63392e069d/image.jpg)

### 为对象设置 ACL

以下示例对某个对象授予了另一个根账户的读取权限：

![](//mc.qcloudimg.com/static/img/7088f7b6c3336668b4b04f63392e069d/image.jpg)