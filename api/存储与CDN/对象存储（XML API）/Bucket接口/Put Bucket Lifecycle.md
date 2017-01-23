## 功能描述
Put Bucket Lifecycle请求实现设置生命周期管理的功能。您可以通过该请求实现数据的冷热沉降和定期删除。此请求为覆盖操作，上传新的配置文件将覆盖之前的配置文件。生命周期管理对文件和文件夹同时生效。

（目前只支持华南园区）

## 请求

### 请求语法

```HTTP
PUT /?lifecycle HTTP 1.1
Host:<Bucketname>-<UID>.<Region>.myqcloud.com
Date:date
Content-Type:application/xml
Content-MD5:MD5
Authorization: Auth
```

### 请求参数

无特殊请求参数

### 请求头部

#### 必选头部

| 名称          | 描述                               | 类型     | 必选   |
| ----------- | -------------------------------- | ------ | ---- |
| Content-MD5 | RFC 1864 中定义的 128位 内容 MD5 算法校验值。 | String | 是    |

### 请求内容

| 名称                             | 描述                                       | 类型        | 必选             |
| ------------------------------ | ---------------------------------------- | --------- | -------------- |
| LifecycleConfiguration         | 描述此生命周期管理的所有配置信息，最大支持1000条规则。            | Container | 是              |
| Rule                           | 描述单条规则的具体信息，最大支持1000条规则<Br/>父节点：LifecycleConfiguration | Container | 是              |
| Prefix                         | 前缀匹配策略，根目录则填空；多个Rule不能同时指定相同前缀路径；父目录指定某条Rule时，子目录不能指定相同类型的Rule<Br/>父节点：LifecycleConfiguration | String    | 是              |
| Status                         | 是否生效此条策略，枚举值：Enabled, Disabled<Br/>父节点：LifecycleConfiguration | String    | 是              |
| ID                             | 标示策略名称<Br/>父节点：LifecycleConfiguration    | String    | 否              |
| Transition                     | 配置文件的冷热沉降规则<Br/>父节点：Rule                 | Container | 是              |
| Expiration                     | 配置文件的定期删除规则，过期时间必须大于转换时间<Br/>父节点：Rule    | Container | 是              |
| Days                           | 在文件创建指定天数以后执行操作。Transition操作请用自然数，Expiration操作请用正整数，不同的Rule下可使用不同的时间格式，相同Rule下冲突<Br/>父节点：Transition，Expiration | Intger    | Days与Date二选一   |
| Date                           | 在指定时间点执行操作，时间格式为ISO 8601格式，须指定东八区触发当天午夜零点零分，可以指定历史时间，例如2016-10-31T00:00:00+08:00；当前时间大于等于Date便执行操作，长期有效；不同的Rule下可使用不同的时间格式，相同Rule下冲突<Br/>父节点：Transition，Expiration | Intger    | Days与Date二选一   |
| StorageClass                   | 指定存储级别，枚举值：Standard，Standard_IA，Nearline。<Br/>父节点：Transition | String    | Transition中必须有 |
| AbortIncompleteMultipartUpload | 配置未完成分块上传的定期删除规则<Br/>父节点：Rule            | Container | 是              |
| DaysAfterInitiation            | 在初始化分块上传之后指定天数以后Abort操作                  | 正整数       | 是              |

配置文件的冷热沉降规则

```XML
<LifecycleConfiguration>
  <Rule>
    <ID></ID>
    <Prefix></Prefix>
    <Status></Status>
    <Transition>
      <Date></Date>
      <StorageClass></StorageClass>
    </Transition>
  </Rule>
  <Rule>
    <ID></ID>
    <Prefix></Prefix>
    <Status></Status>
    <Transition>
      <Days></Days>
      <StorageClass></StorageClass>
    </Transition>
  </Rule>
</LifecycleConfiguration>
```

配置文件的定期删除规则

```XML
<LifecycleConfiguration>
  <Rule>
    <ID></ID>
    <Prefix></Prefix>
    <Status></Status>
    <Expiration>
      <Date></Date>
    </Expiration>
  </Rule>
  <Rule>
    <ID></ID>
    <Prefix></Prefix>
    <Status></Status>
    <Expiration>
      <Days></Days>
    </Expiration>
  </Rule>
</LifecycleConfiguration>
```

配置未完成分块上传的定期删除规则

```XML
<LifecycleConfiguration>
  <Rule>
    <ID></ID>
    <Prefix></Prefix>
    <Status></Status>
    <AbortIncompleteMultipartUpload>
      <DaysAfterInititation></DaysAfterInititation>
    </AbortIncompleteMultipartUpload>
  </Rule>
</LifecycleConfiguration>
```

## 返回值

### 返回头部

无特殊返回头部，其他头部请参见公共返回头部

### 返回内容

无返回内容