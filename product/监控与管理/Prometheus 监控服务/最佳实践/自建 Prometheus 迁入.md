## 操作场景

已经有自建 Prometheus 需快速迁移到 Prometheus 监控服务。

## 操作步骤

Prometheus 本身支持 Remote Write 到一个外部存储，因此沿用这个思想，在自建 Prometheus 的配置文件中加一个 Remote Write 配置指向到 Prometheus 监控服务即可。具体操作步骤如下：
1. 通过实例基本信息获取 Prometheus监控服务的 Remote Write 地址及 Token，如下：
![](https://main.qcloudimg.com/raw/8a75f9f21f391f771d3898310a8ccc0d.png)
2. 修改 `prometheus.yml`，修改完成 `重启 Prometheus`，具体配置如下，如需了解更多 Remote Write 配置参数，请参考 [remote_write](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#remote_write) 。
<dx-codeblock>
:::  yaml
remote_write:

  - name: cm_prometheus # Remote write 的名称
    url: http://ip:port/api/v1/prom/write  # 从 Prometheus 基本信息中获取 Remote Write 地址
    remote_timeout: 30s # 根据实际情况设置
    bearer_token: k32*****trR # 从 Prometheus 基本信息中获取 Token 信息
:::
</dx-codeblock>
3. 打开 Prometheus 监控服务自带的 Grafana，通过 `Explore` 来验证数据是否写入成功，如下图，也可以 [自定义 Grafana 监控大盘](https://grafana.com/docs/grafana/latest/dashboards/)。
   ![](https://main.qcloudimg.com/raw/fc6bf3f5cfbab1bbd931d418b9dddef2.png)
4. 也可以通过Prometheus API 进行自建可视化，详情请参考 [监控数据查询](https://cloud.tencent.com/document/product/1416/56026)。
