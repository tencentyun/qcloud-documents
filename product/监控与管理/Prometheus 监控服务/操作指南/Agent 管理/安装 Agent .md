本文将为您介绍如何安装 Agent。

## 前提条件

- 已创建 [ Prometheus 实例](https://cloud.tencent.com/document/product/248/48690)。
- 已 [创建 Agent](https://cloud.tencent.com/document/product/248/52951) 。

## 操作步骤
1. 登录 [ Prometheus 监控服务控制台](https://console.cloud.tencent.com/monitor/prometheus)。
2. 在实例列表中，选择对应的 Prometheus 实例，单击左侧菜单栏的 **Agent 管理**。
3. 单击 Agent 对应的 ID, 进入 Agent 安装指南页，复制 Agent 安装命令于您的云服务器或自建 IDC ，修改命令中的`<secret_id>`和`<secret_key>`后即可执行。
   ![](https://main.qcloudimg.com/raw/1b514661b252a3dd87f52f841a5496d8.png)
   执行成功示例如下：
   ![](https://main.qcloudimg.com/raw/9737c22b742419eb798f5dfa8bdb84d0.png)
4. 返回 Agent 管理页面，如果 Agent 正常运行，可以看到 Agent 上报的版本，IP 地址和心跳时间。

## 其它命令

### 重启&nbsp;Agent
执行如下命令：
```
systemctl restart prometheus
```

### 停止&nbsp;Agent
执行如下命令：

```
systemctl stop prometheus
```

### 检查&nbsp;Agent&nbsp;状态
执行如下命令：

```
systemctl status prometheus
```

### 查看&nbsp;Agent&nbsp;日志
执行如下命令：

```
journalctl -f --unit=prometheus
```

### 卸载&nbsp;Agent
执行如下命令：
```
systemctl stop prometheus && rm -rf /usr/lib/systemd/system/prometheus.service
```


