## 基本结构

跨地域规则的配置使用 XML 描述方法，通过跨地域复制规则配置能够为存储桶配置和编辑跨地域复制规则，对象存储（Cloud Object Storage，COS）中的每个存储桶支持配置一条跨地域复制规则。配置元素的基本结构如下：

```
<ReplicationConfiguration>
	<Role>qcs::cam::uin/[UIN]:uin/[Subaccount]</Role>
	<Rule>
        <Status></Status>
        <ID></ID>
        <Prefix></Prefix>
        <Destination>
            <Bucket>qcs::cos:[Region]::[Bucketname-Appid]</Bucket>
            <StorageClass></StorageClass>
        </Destination>
	</Rule>
	<Rule>
	...
	</Rule>
</ReplicationConfiguration>
```

其中，`<Role>` 代表跨地域复制发起者的身份标示，`<Rule>`为配置的跨地域复制规则，每一条规则下包含以下内容：

- Status：可选择规则启用 Enabled 或禁用 Disabled 的状态。
- ID：用来标注具体 Rule 的名称。
- Prefix：前缀匹配策略，不可重叠，重叠返回错误。前缀为空时，代表复制存储桶内全部对象。前缀有值时，复制具有前缀值的对象内容。
- Destination：目标存储桶信息，包括`Bucket`和`StorageClass`两个信息：
	1. Bcuket：目标存储桶的命名和存储地域信息。
	2. StorageClass：对象复制到目标存储桶后的存储类型。

## 规则描述

### 复制内容元素

#### 复制存储桶内所有对象内容

指定空的`<Prefix>`参数，该条跨地域复制规则将会复制存储桶中的所有对象。

```
<ReplicationConfiguration>
	<Role>qcs::cam::uin/[UIN]:uin/[Subaccount]</Role>
	<Rule>
        <Status></Status>
        <ID></ID>
        <Prefix></Prefix>
        <Destination>
            <Bucket>qcs::cos:[Region]::[Bucketname-Appid]</Bucket>
            <StorageClass></StorageClass>
        </Destination>
	</Rule>
</ReplicationConfiguration>
```

#### 复制存储桶内指定前缀对象内容

指定对象前缀，可以对一部分符合前缀描述的对象执行跨地域复制操作，例如设置以 logs/ 为前缀的所有对象。

```
<ReplicationConfiguration>
	<Role>qcs::cam::uin/[UIN]:uin/[Subaccount]</Role>
	<Rule>
        <Status></Status>
        <ID></ID>
        <Prefix>logs</Prefix>
        <Destination>
            <Bucket>qcs::cos:[Region]::[Bucketname-Appid]</Bucket>
            <StorageClass></StorageClass>
        </Destination>
	</Rule>
</ReplicationConfiguration>
```

### 目标存储桶元素

#### 目标存储桶地域及命名

通过修改`<Bucket>`参数，可以指定不同地域的存储桶作为目标存储桶。需要注意的是，目标存储桶需与源存储桶处于不同的存储地域，且目前 COS 要求源存储桶和目标存储桶均在同一个账户下。

```
<ReplicationConfiguration>
	<Role>qcs::cam::uin/[UIN]:uin/[Subaccount]</Role>
	<Rule>
        <Status></Status>
        <ID></ID>
        <Prefix></Prefix>
        <Destination>
            <Bucket>qcs::cos:cn-south::sevenyousouthtest-7319456</Bucket>
            <StorageClass></StorageClass>
        </Destination>
	</Rule>
</ReplicationConfiguration>
```

#### 目标存储桶内对象副本类别

通过修改`<StorageClass>`参数，可以指定源存储桶中的对象复制到目标存储桶后的存储类型。COS 目前支持的对象副本存储类型为标准和低频两类，用户如需将副本存储为归档类型，需要自行开启目标存储桶内的生命周期以实现对象管理。COS 默认对象副本存储类型跟随源存储桶对象的存储类型。

```
<ReplicationConfiguration>
	<Role>qcs::cam::uin/[UIN]:uin/[Subaccount]</Role>
	<Rule>
        <Status></Status>
        <ID></ID>
        <Prefix></Prefix>
        <Destination>
            <Bucket>qcs::cos:cn-south::sevenyousouthtest-7319456</Bucket>
            <StorageClass>Standard</StorageClass>
        </Destination>
	</Rule>
</ReplicationConfiguration>
```

