
du 命令用于列出某存储桶或某文件夹下，每一种存储类型文件的统计信息。统计信息包括不同存储类型的文件总数、每种类型文件的总大小。

## 命令格式
使用桶别名访问：
```plaintext
./coscli du cos://<bucketAlias>[/prefix/] [flag]
```

如果您希望使用桶全称访问桶，则需要额外携带 `endpoint` flag。命令格式如下：

```plaintext
./coscli du cos://<BucketName-APPID>[/prefix/] -e <endpoint> [flag]
```

>? 
>- 有关 bucketAlias 的说明，请参见 [下载与安装配置](https://cloud.tencent.com/document/product/436/63144#alias)。
>- 关于此命令的其他通用选项（例如切换存储桶、切换用户账号等），请参见 [通用选项](https://cloud.tencent.com/document/product/436/71763) 文档。
>

du 命令包含以下参数：

| 参数格式          | 参数用途       | 示例                 |
| ----------------- | -------------- | -------------------- |
 cos://&lt;bucketAlias&gt; | 需要进行操作的存储桶别名。别名需要在配置文件中提前配置好。添加配置请参考 [修改配置文档](https://cloud.tencent.com/document/product/436/63679)  |example-alias  |
| cos://&lt;BucketName-APPID&gt; | 需要进行操作的存储桶名称  |examplebucket-1250000000  |
| /prefix/          | 可选参数。指定某一文件夹 | /picture/ |


du 命令包含以下可选 flag：

| flag 简写 | flag 全称     | flag 用途                |
| --------- | ------------- | ------------------------ |
| -h |  --help |   查看该命令的具体用法  |
|    无       | --include     | 包含特定模式的文件       |
|      无       | --exclude     | 排除特定模式的文件       |

>? 
>- `--include` 和 `--exclude` 支持标准正则表达式的语法，您可以使用它来过滤出符合特定条件的文件。
>- 使用 zsh 时，您可能需要在 pattern 串的两端加上双引号。
> ```plaintext
> ./coscli du cos://bucket1/picture/ --include ".*.mp4"
> ```

## 操作示例

### 列出 bucket1 存储桶内文件的统计信息

```plaintext
./coscli du cos://bucket1
```
返回的结果示例如下，输出的信息包括：该桶各存储类型下的对象数量和大小，桶内对象总数，桶内对象总容量。
```plaintext
       STORAGE CLASS      | OBJECTS COUNT | TOTAL SIZE
--------------------------+---------------+-------------
                 STANDARD |             2 |     164  B
              STANDARD_IA |             0 |       0  B
      INTELLIGENT_TIERING |             0 |       0  B
                  ARCHIVE |             0 |       0  B
             DEEP_ARCHIVE |             0 |       0  B
             MAZ_STANDARD |             0 |       0  B
          MAZ_STANDARD_IA |             0 |       0  B
  MAZ_INTELLIGENT_TIERING |             0 |       0  B
              MAZ_ARCHIVE |             0 |       0  B
--------------------------+---------------+-------------
INFO[2022-12-14 17:35:41] Total Objects Count: 2
INFO[2022-12-14 17:35:41] Total Objects Size:  164  B
```

### 列出 bucket1 存储桶 picture 文件夹下文件的统计信息

```plaintext
./coscli du cos://bucket1/picture/
```

### 列出 bucket1 存储桶 picture 文件夹下所有 .mp4 类型文件的统计信息

```plaintext
./coscli du cos://bucket1/picture/ --include .*.mp4
```

### 列出 bucket1 存储桶 picture 文件夹下所有非 .md 类型文件的统计信息

```plaintext
./coscli du cos://bucket1/picture/ --exclude .*.md
```
