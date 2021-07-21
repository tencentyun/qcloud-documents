TencentOS Server（又名 Tencent Linux，简称 TS 或 tlinux）是腾讯针对云的场景研发的 Linux 操作系统，提供特定的功能及性能优化，为云服务器实例中的应用程序提供高性能及更加安全可靠的运行环境。TencentOS Server 提供免费使用，在 CentOS（及其他发行版）上开发的应用程序可直接在 TencentOS Server 上运行，用户还可持续获得腾讯云团队的更新维护和技术支持。

## 适用说明

TencentOS Server 适用于下列场景：

- 绝大部分云服务器各规格族实例，包括黑石2.0服务器。
- 启动实例时，需要通过用户数据（即 userdata 的方式）将相关操作传递到 cloud-init，以达到在实例启动时进行动态配置的目的。

## TencentOS Server 环境说明

### 用户态环境
- TencentOS Server 2用户态软件包保持与最新版 CentOS 7兼容，即 CentOS 7版本的软件包可以直接在 TencentOS Server 2.4 中使用。
- TencentOS Server 3用户态软件包保持与最新版 RHEL 8兼容，即 RHEL 8版本的软件包可以直接在 TencentOS Server 3.1 中使用。

### 系统服务与优化配置

#### 系统服务

- `tlinux-irqaffinity`：TencentOS Server 自动中断分配服务。
- `tlinux-bootlocal`：TencentOS Server bootlocal 服务，开机自动执行 `/etc/rc.d/boot.local`。

#### 系统工具

`tencent-tools`：tos（简称 t）命令，用于系统管理。支持的参数如下：

```bash
tos version 2.2
Usage:
	tos TencentOS Server System Management Toolset
	tos -u|-U| update [rpm_name]	Update the system 
	tos -i|-I| install rpm_name	install rpms
	tos -s|-S| show			Show the system version
	tos -c|-C| check [rpm_name]	Check the modified rpms
	tos -f yum | fix yum		Fix yum problems
	tos -f dns | fix dns		Fix DNS problems
	tos -a|-A | analyze		Analyze the system performance 
	tos set dns			Set DNS
	tos set irq			Set irqaffinity, restart irqaffinity service
	tos -cu| check-update		Check available package updates
	tos -b|-B| backup [ reboot ]	Backup the system online, or reboot to backup 
	tos -r|-R| recover|reinstall	Recover or Reinstall the system
	tos -h|-H| help			Show this usage
	tos -v|-V| version		Show the script version
```

#### 系统配置

- **pam**：密码复杂度增强。
- **`/etc/bashrc` 修改**：优化 bash 显示。
- **`/etc/hosts`**：添加 TENCENT64 及 TENCENT64.site。
- **`/root/.bashrc`**：优化配置。


### TencentOS Server 内核
TencentOS-kernel 提供了4.14和5.4两个版本，详情请参见 [TencentOS-kernel](https://github.com/Tencent/TencentOS-kernel)。

## 发布说明

<table>
  <tr>
	<th>发布时间</th>
	<th style="width:30%">镜像版本</th>
	<th>版本说明</th>
	<th>发布地域</th>
  </tr>
  <tr>
	<td>2021年07月13日</td>
	<td>TencentOS Server 3.1</td>
	<td>镜像 ID：<a href="https://console.cloud.tencent.com/cvm/image/detail?rid=16&id=img-eb30mz89">img-eb30mz89</a><br>内核版本：5.4.119</td>
	<td>所有地域</td>
  </tr>
  <tr>
	<td>2019年09月17日</td>
	<td>TencentOS Server 2.4，原名 Tencent linux release 2.4 (Final)</td>
	<td>镜像 ID：<a href="https://console.cloud.tencent.com/cvm/image/detail?rid=16&id=img-hdt9xxkt">img-hdt9xxkt</a><br>内核版本：4.14.105</td>
	<td>所有地域</td>
  </tr>
</table>


## 获取 TencentOS Server

您可通过下列方法获取并使用 TencentOS Server：

- 创建云服务器实例时，选择公共镜像，并选择 TencentOS Server 的相应版本。
  操作详情请参见 [创建实例](https://cloud.tencent.com/document/product/213/4855)。
- 已创建的云服务器实例，可通过重装系统将现有操作系统更换为 TencentOS Server。
  操作详情请参见 [重装系统](https://cloud.tencent.com/document/product/213/4933)。


## 技术支持

腾讯云为 TencentOS Server 提供如下技术支持：

- 在 YUM 源提供安全更新（Security Updates），运行 `yum update` 命令即可实现版本更新。
- TencentOS Server 是基于内核社区长期支持版本，为云环境定制的操作系统镜像。腾讯云将为您在使用 TencentOS Server 过程中遇到的问题提供技术支持。
