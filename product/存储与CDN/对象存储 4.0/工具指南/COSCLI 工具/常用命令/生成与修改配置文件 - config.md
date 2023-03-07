
## 命令格式

以下 config 命令用于生成与修改配置文件：

```
./coscli config [command] [flag]
```

>? 
>- 正确填写各配置项后，您可以使用`./coscli config show`来查看配置信息。
>- 关于此命令的其他通用选项（例如切换存储桶、切换用户账号等），请参见 [通用选项](https://cloud.tencent.com/document/product/436/71763) 文档。
>- 生成的配置文件，默认网络传输协议为 https。如需更改为 http，可直接进入配置文件进行修改即可。

<span id="config"></span>

config 命令包含以下子命令：

| command 名称 | command 用途                               |
| ------------ | ------------------------------------------ |
| add          | 添加一个新的存储桶配置。                   |
| delete       | 删除一个已经存在的存储桶配置。             |
| init         | 交互式地生成配置文件。                     |
| set          | 修改配置文件 base 组中的一个或多个配置项。base 组包含 `secretid`、`secretkey`、`sessiontoken` 信息。 |
| show         | 打印指定配置文件中的信息。                 | 

config 及其子命令包含以下可选 flag：

| flag 简写 | flag 全称     | flag 用途                  |
| --------- | ------------- | -------------------------- |
| -h |  --help |   查看该命令的具体用法  |
| -c        | --config-path | 指定要使用的配置文件路径。 |

config add 子命令包含以下可选 flag：

| flag 简写 | flag 全称 | flag 用途    |
| --------- | --------- | ------------ |
| -h |  --help |   查看该命令的具体用法  |
| -a        | --alias   | 存储桶别名。 |
| -b        | --bucket  | 存储桶名称。 |
| -r        | --region  | 存储桶地域。 |
| -o |  --ofs |   元数据加速桶标记。详情请参见 [元数据加速概览](https://cloud.tencent.com/document/product/436/56971)。  |

>! 如果您需要指定存储桶的 endpoint，可以使用通用 flag `-e`  或 `--endpoint`，详见 [通用选项介绍](https://cloud.tencent.com/document/product/436/71763)。

config delete 子命令包含以下可选 flag：

| flag 简写 | flag 全称 | flag 用途    |
| --------- | --------- | ------------ |
| -h |  --help |   查看该命令的具体用法  |
| -a        | --alias   | 存储桶别名。 |

config set 子命令包含以下可选 flag：

| flag 简写 | flag 全称    | flag 用途         |
| --------- | ------------ | ----------------- |
| -h |  --help |   查看该命令的具体用法  |
| 无      | --secret_id  | 设置 secret ID。可从 [访问管理控制台](https://console.cloud.tencent.com/cam/capi) 中创建并获取。  |
| 无       | --secret_key | 设置 secret key。可从 [访问管理控制台](https://console.cloud.tencent.com/cam/capi) 中创建并获取。 |
| -t        | --session_token      | 设置临时密钥 token。关于临时密钥的更多信息，详见 [使用临时密钥访问 COS](https://cloud.tencent.com/document/product/436/68283)。   |

## 操作示例

### 添加一个新的存储桶配置

```
./coscli config add -b examplebucket3-1250000000 -r ap-chengdu -e cos.ap-chengdu.myqcloud.com -a bucket3
```

### 删除一个已经存在的存储桶配置

```
./coscli config delete -a bucket3
```

### 修改默认配置文件中的 session-token

```
./coscli config set --session_token test-token123
```

### 打印指定配置文件中的信息

```
./coscli config show -c /your/config/path.yaml
```
