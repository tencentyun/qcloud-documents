## 概述
本文介绍容器服务 TKE 的日志功能中的日志采集、存储、查询各种功能的用法，并结合实际应用场景提供建议。您可结合实际情况，参考本文进行日志采集实践。
>?
>- 本文仅适用于 TKE 集群。
>- 关于 TKE 集群如何启用日志采集及其基础用法，请参见 [日志采集](https://cloud.tencent.com/document/product/457/36771)。


## 技术架构
TKE 集群开启日志采集后，tke-log-agent 作为 DaemonSet 部署在每个节点上。会根据采集规则采集节点上容器的日志，并上报至日志服务 CLS，由 CLS 进行统一存储、检索与分析。示意图如下：
<img style="width:60%" src="https://main.qcloudimg.com/raw/8bcd3f7ebad3c6d6e60f22ed50c8c38f.png" data-nonescope="true">

## 采集类型使用场景
当使用 TKE 日志采集功能时，需在新建日志采集规则时确定采集的目标数据源。TKE 支持“采集标准输出”、“采集容器内文件”及“采集宿主机文件”3种采集类型。请参考下文了解各类型使用场景及建议：

### 采集标准输出
“采集标准输出”是将 Pod 内容器日志输出到标准输出，日志内容会由容器运行时（docker 或 containerd）来管理。“采集标准输出”较于其他方式最简单，推荐选择。具备以下优势：
- 不需要额外挂载 volume。
2. 可直接通过 `kubectl logs` 查看日志内容。
3. 业务无需关注日志轮转，容器运行时会对日志进行存储和自动轮转，避免因个别 Pod 日志量大将磁盘写满。
4. 无需关注日志文件路径，可以使用较统一的采集规则，用更少的采集规则数量覆盖更多的工作负载，减少运维复杂度。

采集配置示例如下图所示，如何配置请参见 [采集容器标准输出日志](https://cloud.tencent.com/document/product/457/36771#.E9.85.8D.E7.BD.AE.E6.97.A5.E5.BF.97.E8.A7.84.E5.88.99)。
<img style="width:70%" src="https://main.qcloudimg.com/raw/adcdcd8414e493f60d02a0536d11f19c.png">

### 采集容器内的文件
通常业务会使用写日志文件的方式来记录日志，当使用容器运行业务时，日志文件被写在容器内。请了解以下事项：
- 若日志文件所在路径未挂载 volume：
日志文件会被写入容器可写层，落盘到容器数据盘里，通常路径是 `/var/lib/docker`。建议挂载 volume 至该路径，避免与系统盘混用。容器停止后日志会被清理。
- 若日志文件所在路径已挂载 volume：
日志文件会落盘到对应 volume 类型的后端存储，通常用 emptydir。容器停止后日志会被清理，运行期间日志文件会落盘到宿主机的 `/var/lib/kubelet` 路径下，此路径通常没有单独挂盘，即会使用系统盘。由于使用了日志采集功能，有统一存储的能力，不推荐再挂载其它持久化存储来存日志文件（例如云硬盘 CBS、对象存储 COS 或共享存储 CFS）。


大部分开源日志采集器需给 Pod 日志文件路径挂载 volume 后才可采集，而 TKE 的日志采集无需挂载。若将日志输出到容器内的文件，则无需关注是否挂载 volume。采集配置示例如下图所示，如何配置请参见 [采集容器内文件日志](https://cloud.tencent.com/document/product/457/36771#.E9.85.8D.E7.BD.AE.E6.97.A5.E5.BF.97.E8.A7.84.E5.88.99)。
<img style="width:70%" src="https://main.qcloudimg.com/raw/cd58e8a4e206888dcd07a50dcd217607.png">

### 采集宿主机上的文件
若业务需将日志写入日志文件，但期望在容器停止后仍保留原始日志文件作为备份，避免采集异常时日志完全丢失。此时可以给日志文件路径挂载 hostPath，日志文件会落盘到宿主机指定目录，并且容器停止后不会清理日志文件。
由于不会自动清理日志文件，可能会发生 Pod 调度走再调度回来，日志文件被写在相同路径，从而重复采集的问题。采集分以下两种情况：
- 文件名相同：
例如，固定文件路径 `/data/log/nginx/access.log`。此时不会重复采集，采集器会记住之前采集过的日志文件的位点，只采集增量部分。
- 文件名不同：
通常业务用的日志框架会按照一定时间周期自动进行日志轮转，一般是按天轮转，并自动为旧日志文件进行重命名，加上时间戳后缀。如果采集规则里使用了 <code>*</code> 为通配符匹配日志文件名，则可能发生重复采集。日志框架对日志文件重命名后，采集器则会认为匹配到了新写入的日志文件，就又对其进行采集一次。
>?通常情况下不会发生重复采集，若日志框架会对日志进行自动轮转，建议采集规则不要使用通配符 <code>*</code> 来匹配日志文件。
>
采集配置示例如下图所示，如何配置请参见 [采集节点文件日志](https://cloud.tencent.com/document/product/457/36771#.E9.85.8D.E7.BD.AE.E6.97.A5.E5.BF.97.E8.A7.84.E5.88.99)。
<img style="width:70%" src="https://main.qcloudimg.com/raw/d4a658f3e769d0e369f10883e4f4d2b0.png">

## 日志输出
TKE 日志采集与云上的 CLS 日志服务集成，日志数据也将统一上报到日志服务。CLS 通过日志集和日志主题来对日志进行管理，日志集是 CLS 的项目管理单元，可以包含多个日志主题。一般将同一个业务的日志放在一个同一日志集，同一业务中的同一类的应用或服务使用相同日志主题。
在 TKE 中，日志采集规则与日志主题一一对应。TKE 创建日志采集规则时选择消费端，则需要指定日志集与日志主题。其中，日志集通常提前创建好，日志主题通常选择自动创建。如下图所示：
<img style="width:70%" src="https://main.qcloudimg.com/raw/74c61944d6f1943350a9776f030d48c3.png">
自动创建日志主题后，可前往 [日志集管理](https://console.cloud.tencent.com/cls/logset) 的对应日志集详情页面，进行重命名操作，以便后续检索时快速找到日志所在的日志主题。



## 配置日志格式解析
在创建日志采集规则时，需配置日志的解析格式，以便后续对其进行检索。请参考以下内容，对应实际情况进行配置。

### 选择提取模式
TKE 支持单行文本、JSON、分隔符、多行文本和完全正则5种提取模式。如下图所示：
![](https://main.qcloudimg.com/raw/46dfb1fddbddfaa3aad085ffa0ff86f4.png)


<dx-tabs>
::: JSON\s模式
选择 “JSON 模式”需日志本身是以 JSON 格式输出的，推荐选择该模式。JSON 格式本身已将日志结构化，CLS 可以提取 JSON 的 key 作为字段名，value 作为对应的字段值，不再需要根据业务日志输出格式配置复杂的匹配规则。日志示例如下：
```
{"remote_ip":"10.135.46.111","time_local":"22/Jan/2019:19:19:34 +0800","body_sent":23,"responsetime":0.232,"upstreamtime":"0.232","upstreamhost":"unix:/tmp/php-cgi.sock","http_host":"127.0.0.1","method":"POST","url":"/event/dispatch","request":"POST /event/dispatch HTTP/1.1","xff":"-","referer":"http://127.0.0.1/my/course/4","agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0","response_code":"200"}
```
:::
::: 单行文本及多行文本模式
如果日志没有固定的输出格式，则考虑使用“单行文本”或“多行文本”的提取模式。使用这两种模式，不会对日志内容本身进行结构化处理及提取日志字段，每条日志的时间戳固定由日志采集的时间决定，检索时仅能进行简单的模糊查询。两种模式的区别在于日志内容为单行还是多行：
 - 单行：无需设置任何匹配条件，每行为一条单独的日志。
 - 多行：需设置首行正则表达式，即匹配每条日志第一行的正则。当某行日志匹配上预先设置的首行正则表达式，即认为是一条日志的开头，而下一个行首出现作为该条日志的结束标识符。假设多行日志内容是：
<dx-codeblock>
:::  log
10.20.20.10 - - [Tue Jan 22 14:24:03 CST 2019 +0800] GET /online/sample HTTP/1.1 127.0.0.1 200 628 35 http://127.0.0.1/group/1 
Mozilla/5.0 (Windows NT 10.0; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0 0.310 0.310
:::
</dx-codeblock>则首行正则表达式就可以设置为：`\d+\.\d+\.\d+\.\d+\s-\s.*`。如下图所示：
![](https://main.qcloudimg.com/raw/20d59a46cee1651a4fcd0643eb878976.png)
:::
::: 分隔符及完全正则模式
如果日志内容是以固定格式输出的单行文本，则考虑使用“分隔符”或“完全正则”提取模式：
- “分隔符”适用简单格式，日志中每个字段值都以固定的字符串分隔开。例如，用 `:::` 隔开，某一条日志内容为：
<dx-codeblock>
:::  log
10.20.20.10 ::: [Tue Jan 22 14:49:45 CST 2019 +0800] ::: GET /online/sample HTTP/1.1 ::: 127.0.0.1 ::: 200 ::: 647 ::: 35 ::: http://127.0.0.1/
:::
</dx-codeblock>则可以配置 `:::` 自定义分隔符，并且为每个字段按顺序配置字段名。如下图所示：
![](https://main.qcloudimg.com/raw/958a71bdee32a7346fd88646a2cbecbf.png)
- “完全正则”适用复杂格式，使用正则表达式来匹配日志的格式。例如日志内容为：
<dx-codeblock>
:::  log
10.135.46.111 - - [22/Jan/2019:19:19:30 +0800] "GET /my/course/1 HTTP/1.1" 127.0.0.1 200 782 9703 "http://127.0.0.1/course/explore?filter%5Btype%5D=all&filter%5Bprice%5D=all&filter%5BcurrentLevelId%5D=all&orderBy=studentNum" "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0"  0.354 0.354
:::
</dx-codeblock>则正则表达式就可以设置为：
<dx-codeblock>
:::  log
(\S+)[^\[]+(\[[^:]+:\d+:\d+:\d+\s\S+)\s"(\w+)\s(\S+)\s([^"]+)"\s(\S+)\s(\d+)\s(\d+)\s(\d+)\s"([^"]+)"\s"([^"]+)"\s+(\S+)\s(\S+).*
:::
</dx-codeblock>CLS 会使用 `()` 捕获组来区分每个字段，还需要为每个字段设置字段名。如下图所示：
<img src="https://main.qcloudimg.com/raw/fa23705c9d715ae2609405f10669a5e3.png">
:::
</dx-tabs>









### 配置过滤内容
可选择过滤无需使用的日志信息，降低成本。
- 若使用 “JSON”、“分隔符”或“完全正则”的提取模式，日志内容会进行结构化处理，可以通过指定字段来对要保留的日志进行正则匹配。如下图所示：
<img style="width:70%" src="https://main.qcloudimg.com/raw/ec8a53187b3068c7b0fda3c73ce3abbe.png">
- 若使用“单行文本”和“多行文本”的提取模式，由于日志内容没有进行结构化处理，无法指定字段来过滤，通常直接使用正则来对要保留的完整日志内容进行模糊匹配。如下图所示：
>!匹配内容需使用正则而不是完整匹配。例如，需仅保留 `a.test.com` 域名的日志，匹配的表达式应为 `a\.test\.com` 而不是 `a.test.com`。
>
<img style="width:70%" src="https://main.qcloudimg.com/raw/4dc0a910bfbc2b9aa302108f514bc724.png">

### 自定义日志时间戳
每条日志都需要具备主要用于检索的时间戳，可在检索时选择时间范围。默认情况下，日志的时间戳由采集的时间决定，您也可以进行自定义，选择某个字段作为时间戳，在有些场景下会更加精确。例如，在创建采集规则前，服务已运行一段时间，若不设置自定义时间格式，采集时会将之前的旧日志的时间戳设置为当前的时间，导致时间不准确。

“单行文本”和“多行文本”提取模式不会对日志内容进行结构化处理，无字段可指定为时间戳，即不支持此功能。其他提取模式均支持此功能，需关闭“使用采集时间”、选取需作为时间戳的字段名称并配置时间格式。例如，使用日志的 `time` 字段作为时间戳，其中一条日志 `time` 的值为 `2020-09-22 18:18:18`，时间格式即可设置为 `%Y-%m-%d %H:%M:%S`。如下图所示：
>!日志服务时间戳目前支持精确到秒，若业务日志的时间戳字段精确到毫秒，则将无法使用自定义时间戳，只能使用默认的采集时间作为时间戳。

<img style="width:70%" src="https://main.qcloudimg.com/raw/8699955609c5237c6d9379d05bef961d.png"></img>

更多时间格式配置信息请参见 [配置时间格式](https://cloud.tencent.com/document/product/614/38614)。



## 查询日志
完成日志采集规则配置后，采集器会自动开始采集日志并上报到 CLS。您可在 [日志服务控制台](https://console.cloud.tencent.com/cls) 的**检索分析**中查询日志，开启索引后支持 Lucene 语法。有以下3类索引：
- 全文索引。用于模糊搜索，不用指定字段。如下图所示：
![](https://main.qcloudimg.com/raw/b4635a9c0956c6d3f43ac555e4284110.png)
- 键值索引。索引结构化处理过的日志内容，可以指定日志字段进行检索。如下图所示：
<img style="width:70%" src="https://main.qcloudimg.com/raw/049e9da5c98be0dcfa4ddf2df81df941.png"></img>
- 元字段索引。上报日志时额外自动附加的一些字段。例如 pod 名称、namespace 等，方便检索时指定这些字段进行检索。如下图所示：
<img style="width:70%" src="https://main.qcloudimg.com/raw/6dd367f57c2bc34f2f56cd639c685a31.png"></img><br>

查询示例如下图所示：
<img style="width:70%" src="https://main.qcloudimg.com/raw/1099e600a88bb47371e0a9274ba5c302.png">

## 投递日志至 COS 及 Ckafka
CLS 支持将日志投递到对象存储 COS 和消息队列 CKafka，您可在日志主题里进行设置。如下图所示：
![](https://main.qcloudimg.com/raw/fe010223240e554a25337527084f9743.png)
可用于以下场景：
- 需对日志数据进行长期归档存储。日志集默认存储7天的日志数据，可以调整时长。数据量越大，成本就越高，通常只保留几天的数据，如果需要将日志存更长时间，可以投递到 COS 进行低成本存储。
- 需要对日志进行进一步处理（例如离线计算），可以投递到 COS 或 Ckafka，由其它程序消费来处理。

## 参考资料

* TKE ：[日志采集用法指引](https://cloud.tencent.com/document/product/457/36771) 
* 日志服务：[配置时间格式](https://cloud.tencent.com/document/product/614/38614) 
* 日志服务： [投递至 COS](https://cloud.tencent.com/document/product/614/37908) 
* 日志服务 ：[投递至 Ckafka](https://cloud.tencent.com/document/product/614/33342)
