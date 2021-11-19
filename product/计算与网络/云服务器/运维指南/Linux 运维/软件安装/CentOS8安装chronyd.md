## 操作场景
目前原生 CentOS 8 不支持安装 ntp 服务，因此会发生时间不准的问题，需使用 chronyd 来调整时间服务。本文介绍了如何在 CentOS 8 操作系统的腾讯云服务器上安装并配置 chronyd 时间服务。

## 操作步骤
### 安装配置 chronyd 服务
1. 登录云服务器实例，详情请参见 [使用标准方式登录 Linux 实例（推荐）](https://cloud.tencent.com/document/product/213/5436)。
2. 执行以下命令，安装 chronyd 服务。
```
yum -y install chrony
```
3. 执行以下命令，修改配置文件 `chrony.conf`。
```
vim /etc/chrony.conf
```
4. 按 **i** 进入编辑模式，并在 `#log measurements statistics tracking` 后另起一行，输入以下内容。
```
server time1.tencentyun.com iburst
server time2.tencentyun.com iburst
server time3.tencentyun.com iburst
server time4.tencentyun.com iburst
server time5.tencentyun.com iburst
```
编辑完成后如下图所示：
![](https://main.qcloudimg.com/raw/578e072599f8d50ea188d3911a9d76c7.png)
5. 按 **Esc** 输入 **:wq** 保存后退出编辑模式。
6. 依次执行以下命令，设置 chronyd 服务为开机自启动并重启服务。
```
systemctl restart chronyd
```
```
systemctl enable chronyd
```

### 检查服务配置
1. 执行以下命令，检查时间是否同步。
```
date
```
2. 执行以下命令，看时间同步源状态。
```
chronyc sourcestats -v
```
若返回类似如下结果，则表示配置成功。
![](https://main.qcloudimg.com/raw/6a5f584638de922f5e80b5b138541c9e.png)

## 附录
### 常用命令
<table>
<tr>
<th>命令</th><th>说明</th>
</tr>
<tr>
<td>
<code>chronyc sources -v</code>
</td>
<td>查看时间同步源。</td>
</tr>
<tr>
<td>
<code>chronyc sourcestats -v</code>
</td>
<td>查看时间同步源状态。</td>
</tr>
<tr>
<td>
<code>timedatectl set-local-rtc 1</code>
</td>
<td>设置硬件时间，硬件时间默认为 UTC。
</td>
</tr>
<tr>
<td>
<code>timedatectl set-ntp yes</code>
</td>
<td>启用 NTP 时间同步。</td>
</tr>
<tr>
<td>
<code>chronyc tracking</code>
</td>
<td>校准时间服务器。</td>
</tr>
<tr>
<td>
<code>chronyc -a makestep</code>
</td>
<td>强制同步系统时钟。</td>
</tr>
</table>


