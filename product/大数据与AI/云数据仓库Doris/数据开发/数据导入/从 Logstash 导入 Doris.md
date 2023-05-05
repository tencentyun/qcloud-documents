从 Logstash 导入 Doris 需要使用 Logstash的Doris output plugin。该插件使用 HTTP 协议与 Doris FE HTTP 接口交互，并通过 Doris 的 stream load 的方式进行数据导入。

## 安装和编译
### 1. 下载源码
插件源码在 Doris 源码中，下载 Doris 源码。

### 2. 编译 
在 doris 源码的 extension/logstash/ 目录下执行：
```
gem build logstash-output-doris.gemspec
```
您将在同目录下得到 logstash-output-doris-{version}.gem 文件。

### 3. 插件安装
`copy logstash-output-doris-{version}.gem` 到 logstash 安装目录下，执行命令：
```
./bin/logstash-plugin install logstash-output-doris-{version}.gem
```
安装 logstash-output-doris 插件。

## 配置
### 示例
在 config 目录下新建一个配置配置文件，命名为 logstash-doris.conf，具体配置如下：
```
    output {
        doris {
            http_hosts => [ "http://fehost:8030" ]
            user => user_name
            password => password
            db => "db_name"
            table => "table_name"
            label_prefix => "label_prefix"
            column_separator => ","
        }
    }
```
### 配置说明

连接相关配置：

配置 | 说明
--- | ---
`http_hosts` | FE的HTTP交互地址。 例如：  ["http://fe1:8030", "http://fe2:8030"]
`user` | 用户名，该用户需要有 doris 对应库表的导入权限
`password` | 密码
`db` | 数据库名
`table` | 表名
`label_prefix` | 导入标识前缀，最终生成的标识为 *{label\_prefix}\_{db}\_{table}\_{time_stamp}*


导入相关配置参考 [Stream Load 手册](https://doris.apache.org/zh-CN/docs/dev/data-operate/import/import-way/stream-load-manual?_highlight=stream&_highlight=load)。

配置 | 说明
--- | ---
`column_separator` | 列分割符，默认为\t。
`columns` | 用于指定导入文件中的列和 table 中的列的对应关系。
`where` | 导入任务指定的过滤条件。
`max_filter_ratio` | 导入任务的最大容忍率，默认零容忍。
`partition` | 待导入表的 Partition 信息。
`timeout` | 超时时间，默认为600s。
`strict_mode` | 严格模式，默认为 false。
`timezone` | 指定本次导入所使用的时区，默认为东八区。
`exec_mem_limit` | 导入内存限制，默认为 2GB，单位为字节。

其他配置：

配置 | 说明
--- | ---
`save_on_failure` | 如果导入失败是否在本地保存，默认为 true
`save_dir` | 本地保存目录，默认为 /tmp
`automatic_retries` | 失败时重试最大次数，默认为3
`batch_size` | 每批次最多处理的 event 数量，默认为100000
`idle_flush_time` | 最大间隔时间，默认为20（秒）


## 启动
执行命令启动 doris output plugin：
```
{logstash-home}/bin/logstash -f {logstash-home}/config/logstash-doris.conf --config.reload.automatic
```

## 完整使用示例
### 1. 编译 doris-output-plugin
1. 下载 ruby 压缩包，自行到 [ruby 官网](https://www.ruby-lang.org/en/downloads/)下载，这里使用的2.7.1版本。
2. 编译安装，配置ruby的环境变量.
3. 到 doris 源码 extension/logstash/ 目录下，执行：
```
gem build logstash-output-doris.gemspec
```
得到文件 logstash-output-doris-0.1.0.gem，至此编译完成。

### 2. 安装配置 filebeat
 >? 此处使用 filebeat 作为 input。
 >
1. [es 官网](https://www.elastic.co/) 下载 filebeat tar 压缩包并解压。
2. 进入 filebeat 目录下，修改配置文件 filebeat.yml 如下：
```yaml
filebeat.inputs:
- type: log
paths:
    - /tmp/doris.data
output.logstash:
hosts: ["localhost:5044"]
```
/tmp/doris.data 为 doris 数据路径。
3. 启动 filebeat：
```
./filebeat -e -c filebeat.yml -d "publish"
```

### 3. 安装 logstash 及 doris-out-plugin
1. 从 [es官网](https://www.elastic.co/) 下载 logstash tar 压缩包并解压。
2. 将步骤1中得到的 logstash-output-doris-0.1.0.gem copy 到 logstash 安装目录下。
3. 执行：
```
./bin/logstash-plugin install logstash-output-doris-0.1.0.gem
```
安装插件。
4. 在 config 目录下新建配置文件 logstash-doris.conf 内容如下：
```sql
input {
    beats {
        port => "5044"
    }
}

output {
    doris {
        http_hosts => [ "http://127.0.0.1:8030" ]
        user => doris
        password => doris
        db => "logstash_output_test"
        table => "output"
        label_prefix => "doris"
        column_separator => ","
        columns => "a,b,c,d,e"
    }
}
```
这里的配置需按照配置说明自行配置。
5. 启动 logstash：
```
./bin/logstash -f ./config/logstash-doris.conf --config.reload.automatic
```

### 4. 测试功能
向/tmp/doris.data追加写入数据：
```
echo a,b,c,d,e >> /tmp/doris.data
```
观察 logstash 日志，若返回 response的Status 为 Success，则导入成功，此时可在 logstash_output_test.output 表中查看已导入的数据。

