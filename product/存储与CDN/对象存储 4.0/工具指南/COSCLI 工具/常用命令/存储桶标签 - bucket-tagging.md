bucket-tagging 命令用于创建（修改）、获取、删除存储桶标签。每个存储桶下最多支持50组标签。

## 命令格式
使用桶别名访问：
```plaintext
./coscli bucket-tagging --method [method] cos://bucketAlias [tag_key]#[tag_value]
```
如果您希望使用桶全称访问桶，则需要额外携带 `endpoint` flag。命令格式如下：

```plaintext
./coscli bucket-tagging --method [method] cos://<BucketName-APPID> -e <endpoint> [tag_key]#[tag_value]
```

>? 
>- 有关 bucketAlias 的说明，请参见 [下载与安装配置](https://cloud.tencent.com/document/product/436/63144#alias)。
>- 关于此命令的其他通用选项（例如切换存储桶、切换用户账号等），请参见 [通用选项](https://cloud.tencent.com/document/product/436/71763) 文档。
>

bucket-tagging 命令包含以下参数：
| 参数格式  | 参数用途     | 示例                |
| --------- | ------------- | ------------------------ |
 cos://&lt;bucketAlias&gt; | 需要进行操作的存储桶别名。别名需要在配置文件中提前配置好。添加配置请参考 [修改配置文档](https://cloud.tencent.com/document/product/436/63679)  |example-alias  |
| cos://&lt;BucketName-APPID&gt; | 需要进行操作的存储桶名称  |examplebucket-1250000000  |

bucket-tagging 命令包含以下可选 flag：

|flag 简写|flag 全称| flag 用途|
|----|----|----|
| -h |  --help |   查看该命令的具体用法  |
|无|--method|指定需要进行的操作，包括 put（添加标签）、get（查询标签）、delete（删除标签）   |


## 添加或修改存储桶标签

存储桶标签用一组健值对（Key-Value）来表示，只有存储桶所有者及拥有 PutBucketTagging 权限的用户才可以添加或修改存储桶标签，否则会返回错误码 403 AccessDenied。

### 命令格式

```plaintext
./coscli bucket-tagging --method put cos://bucketAlias key1#value1 key2#value2
```
其中，`key#value`表示标签键值对 Key-Value，key 和 value 之间以`#`分割。若存储桶未设置标签，此命令将为存储桶添加指定的标签；若存储桶已设置标签，此命令将覆盖原有的标签。

### 操作示例

为别名为 example-alias 的存储桶配置两组标签，其中一组标签的 key 为1，value 为111，一组标签的 key 为2，value 为222。命令如下：

```plaintext
./coscli bucket-tagging --method put cos://exmaple-alias 1#111 2#222
```

## 查询存储桶标签
### 命令格式

```plaintext
./coscli bucket-tagging --method get cos://bucketAlias
```

### 操作示例

```plaintext
./coscli bucket-tagging --method get cos://exmaple-alias
```

以下输出结果表明别名问 exmaple-alias 的存储桶配置了两组标签，其中一组标签的 key 为1，value 为111，一组标签的 key 为2，value 为222。

```plaintext
  KEY | VALUE  
------+--------
    1 |   111  
    2 |   222 
```

## 删除存储桶标签

### 命令格式
```plaintext
./coscli bucket-tagging --method delete cos://bucketAlias


### 操作示例

```plaintext
./coscli bucket-tagging --method delete cos://exmaple-alias
```
