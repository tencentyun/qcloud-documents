### 如何对 LogListener 的进程进行绑核？

使用 taskset 工具进行绑核， `taskset -cp ${cpu number} ${pid>}`。

### 如何处理 LogListener 占用内存过高，控制资源的使用？

- 建议升级到最新 LogListener 版本 ，并设置 `memory_tight_mode = true`。
- 使用 CGroup 限制 CPU 和内存使用。

### LogListener 是否支持软链接方式采集？

LogListener 低于2.3.0版本不支持监听软连接方式的日志文件和 NFS、CIFS 等共享文件目录上的日志文件，以上版本均可支持。

### LogListener 可以向多个日志主题上传数据吗？

- LogListener 可以为同地域的多个日志主题采集数据，但不支持为异地多个日志主题采集。
- 同一个日志文件只支持采集到一个主题。

### LogListener 初始化的时候是否可以自动加入机器组？

标识机器组机支持, 参考文档 [管理机器组](https://cloud.tencent.com/document/product/614/17412)。

### LogListener 日志上传策略是什么？

 - 缓存的日志量超过4M。
 - 缓存的日志条数超过10000条。
 - 读到文件末尾。

### LogListener 支持的最大性能是多少？

 - 单行全文日志最大处理能力为115MB/s。
 - 多行全文日志最大处理能力为40MB/s。
 - JSON 格式日志最大处理能力为25MB/s。
 - CSV 格式日志采最大处理能力为50MB/s。
 - 完全正则格式日志最大处理能力为18MB/s (和正则的复杂度有关)。


### 服务器更换 IP 地址后，LogListener 应该如何适配？

- 若服务器通过机器标识绑定机器组，用户无需变更 LogListener 配置。若服务器 IP 需要频繁变更，建议用户使用 [机器标识](https://cloud.tencent.com/document/product/614/17412#.E9.80.9A.E8.BF.87.E9.85.8D.E7.BD.AE.E6.9C.BA.E5.99.A8.E6.A0.87.E8.AF.86.E5.88.9B.E5.BB.BA.E6.9C.BA.E5.99.A8.E7.BB.84) 配置机器组。
- 若服务器通过 IP 地址绑定机器组，用户需要完成以下配置变更：
  a. 修改配置文件中 group_ip 选项，填入变更后的 IP 地址，例如：
```shell
sed -i '' "s/group_ip *=.*/group_ip = ${group_ip}/" etc/loglistener.conf
```
 b. 重启 LogListener。
```shell
 /etc/init.d/loglistenerd restart
```
 c. 如果使用的是 IP 机器组，登录 [日志服务控制台](https://console.cloud.tencent.com/cls/overview?region=ap-guangzhou)，在左侧导航栏中，单击【机器组管理】，修改该服务器绑定的机器组配置，使用新 IP 替换原机器 IP 地址并确定。
