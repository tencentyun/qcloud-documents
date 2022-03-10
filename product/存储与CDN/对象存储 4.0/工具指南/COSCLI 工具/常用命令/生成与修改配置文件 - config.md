
## 命令格式

以下 config 命令用于生成与修改配置文件：

```
./coscli config [command] [flag]
```

>? 正确填写各配置项后，您可以使用`./coscli config show`来查看配置信息。
>

<span id="config"></span>

config 命令包含以下子命令：

| command 名称 | command 用途                               |
| ------------ | ------------------------------------------ |
| add          | 添加一个新的存储桶配置。                   |
| delete       | 删除一个已经存在的存储桶配置。             |
| init         | 交互式地生成配置文件。                     |
| set          | 修改配置文件 base 组中的一个或多个配置项。 |
| show         | 打印指定配置文件中的信息。                 |

config 及其子命令包含以下可选 flag：

| flag 简写 | flag 全称     | flag 用途                  |
| --------- | ------------- | -------------------------- |
| -h        | --help        | 输出帮助信息。             |
| -c        | --config-path | 指定要使用的配置文件路径。 |

config add 子命令包含以下可选 flag：

| flag 简写 | flag 全称 | flag 用途    |
| --------- | --------- | ------------ |
| -a        | --alias   | 存储桶别名。 |
| -b        | --bucket  | 存储桶名称。 |
| -r        | --region  | 存储桶地域。 |

config delete 子命令包含以下可选 flag：

| flag 简写 | flag 全称 | flag 用途    |
| --------- | --------- | ------------ |
| -a        | --alias   | 存储桶别名。 |

config set 子命令包含以下可选 flag：

| flag 简写 | flag 全称    | flag 用途         |
| --------- | ------------ | ----------------- |
| -i        | --secret_id  | 设置 secret ID。  |
| -k        | --secret_key | 设置 secret key。 |
| -t        | --token      | 设置 token。      |

## 操作示例

### 添加一个新的存储桶配置

```
./coscli config add -b examplebucket3-1250000000 -r ap-chengdu -a bucket3
```

### 删除一个已经存在的存储桶配置

```
./coscli config delete -a bucket3
```

### 修改默认配置文件中的 session-token

```
./coscli config set -t test-token123
```

### 打印指定配置文件中的信息

```
./coscli config show -c /your/config/path.yaml
```
