
### 如何查看 agent 状态？
登录 [DBbrain 控制台](https://console.cloud.tencent.com/dbbrain/instance?product=mysql)，在左侧导航选择【实例管理】页，在上方选择对应数据库，在列表可查看 agent 状态。
![](https://main.qcloudimg.com/raw/8c72cb85a2f27e2d769672de8fcb2f04.png)

### agent 状态异常，如何解决？
- 若在实例管理页面发现 agent 连接异常，在主机上输入如下命令，查看 agent 进程：
   ```
ps aux|grep dbbrain-agent
   ```
- 若无任何输出，说明 agent 意外停止了，需要在主机上转到 agent 安装目录，然后重新启动 agent，操作命令如下：
   ```
cd /path/to/dbbrain-agent
./bin/start.sh
   ```
若输出 `Successfully start agent`，说明启动成功。

