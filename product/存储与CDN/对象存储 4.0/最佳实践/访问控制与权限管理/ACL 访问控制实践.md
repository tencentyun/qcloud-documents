## ACL 概述
访问控制列表（ACL）是基于资源的访问策略选项之一 ，可用来管理对存储桶和对象的访问。使用 ACL 可向其他主账号、子账号和用户组，授予基本的读、写权限。

**与访问策略有所不同的是，ACL 的管理权限有以下限制：**
- 仅支持对腾讯云的账户赋予权限
- 仅支持读对象、写对象、读 ACL、写 ACL 和全部权限等五个操作组
- 不支持赋予生效条件
- 不支持显式拒绝效力

**ACL 支持的控制粒度：**
- 存储桶（Bucket）
- 对象键前缀（Prefix）
- 对象（Object）

## ACL 的控制元素
当创建存储桶或对象时，其资源所属的主账号将具备对资源的全部权限，且不可修改或删除。您可以使用 ACL 赋予其他腾讯云账户的访问权限。
如下提供了一个存储桶的 ACL 示例。其中的100000000001表示主账号，100000000011为主账号下的子账号，100000000002表示另一个主账号。ACL 包含了识别该存储桶所有者的 Owner 元素，该存储桶所有者具备该存储桶的全部权限。同时 Grant 元素授予了匿名的读取权限，其表述形式为`http://cam.qcloud.com/groups/global/AllUsers`的 READ 权限。

```shell
<AccessControlPolicy>
  <Owner>
    <ID>qcs::cam::uin/100000000001:uin/100000000001</ID>
    <DisplayName>qcs::cam::uin/100000000001:uin/100000000001</DisplayName>
  </Owner>
  <AccessControlList>
    <Grant>
      <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="RootAccount">
        <ID>qcs::cam::uin/100000000001:uin/100000000001</ID>
        <DisplayName>qcs::cam::uin/100000000001:uin/100000000001</DisplayName>
      </Grantee>
      <Permission>FULL_CONTROL</Permission>
    </Grant>
    <Grant>
      <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="Group">
        <URI>http://cam.qcloud.com/groups/global/AllUsers</URI>
      </Grantee>
      <Permission>READ</Permission>
    </Grant>
  </AccessControlList>
</AccessControlPolicy>
```



#### 权限被授予者
**主账号**
您可以对其他主账号授予用户访问权限，使用 CAM 中对委托人（principal）的定义进行授权。描述为：
```bash
qcs::cam::uin/100000000002:uin/100000000002
```

**子账号**
您可以对您的主账号下的子账号（如100000000011），或其他主账号下的子账号授权，使用 CAM 中对委托人（principal）的定义进行授权。描述为：
```bash
qcs::cam::uin/100000000001:uin/100000000011
```

**匿名用户**
您可以对匿名用户授予访问权限，使用 CAM 中对委托人（principal）的定义进行授权。描述为：
```bash
http://cam.qcloud.com/groups/global/AllUsers
```

#### 权限操作组
以下表格提供了 ACL 支持的权限操作组。

| 操作组          | 授予存储桶             | 授予前缀             | 授予对象      |
| ------------ | ----------------- | ---------------- | --------- |
| READ         | 列出和读取存储桶中的对象      | 列出和读取目录下的对象      | 读取对象      |
| WRITE        | 创建、覆盖和删除存储桶中的任意对象 | 创建、覆盖和删除目录下的任意对象 | 不支持  |
| READ_ACP     | 读取存储桶的 ACL        | 读取目录下的 ACL       | 读取对象的 ACL |
| WRITE_ACP    | 修改存储桶的 ACL        | 修改目录下的 ACL       | 修改对象的 ACL |
| FULL_CONTROL | 对存储桶和对象的任何操作      | 对目录下的对象做任何操作     | 对对象执行任何操作 |

#### 标准 ACL 描述
COS 支持一系列的预定义授权，称之为标准 ACL，下表列出了标准 ACL 的授权含义。

>!由于主账号始终拥有 FULL_CONTROL 权限，以下表格中不再对此特别说明。

| 标准 ACL            | 含义                                      |
| ----------------- | --------------------------------------- |
| (空)               | 此为默认策略，其他人无权限，资源继承上级权限                 |
| private           | 其他人没有权限                               |
| public-read       | 匿名用户组具备 READ 权限                        |
| public-read-write | 匿名用户组具备 READ 和 WRITE 权限，通常不建议在存储桶赋予此权限 |

## 使用方法

### 使用控制台操作 ACL

**对存储桶设置 ACL**
以下示例表示允许另一个主账号对某个**存储桶**有读取权限：
![](https://main.qcloudimg.com/raw/4a9cc8ba30fe072f19b1eb0e6a6bd3d1.png)

**对对象设置 ACL**
以下示例表示允许另一个主账号对某个**对象**有读取权限：
![](https://main.qcloudimg.com/raw/647e3551603ae5e0e5e072a1d94ff3d2.png)


>!如使用子账号访问存储桶或对象出现**无权限访问**的提示，请先通过主账号为子账号授权以便能够正常访问存储桶，操作步骤请参见 [子账号访问存储桶列表](https://cloud.tencent.com/document/product/436/17061)。

### 使用 API 操作 ACL

**存储桶 ACL**

| API                                                          | 操作名         | 操作描述                                |
| :----------------------------------------------------------- | :------------- | :-------------------------------------- |
| [PUT Bucket acl](https://cloud.tencent.com/document/product/436/7737) |   设置存储桶 ACL |设置指定存储桶访问权限控制列表 |
| [GET Bucket acl](https://cloud.tencent.com/document/product/436/7733) | 查询存储桶 ACL | 	查询存储桶的访问控制列表 |

**对象 ACL**

| API                                                          | 操作名       | 操作描述                                      |
| :----------------------------------------------------------- | :----------- | :-------------------------------------------- |
| [PUT Object acl](https://cloud.tencent.com/document/product/436/7748) | 设置对象 ACL | 设置存储桶中某个对象的访问控制列表 |
| [GET Object acl](https://cloud.tencent.com/document/product/436/7744) | 查询对象 ACL | 查询对象的访问控制列表             |

