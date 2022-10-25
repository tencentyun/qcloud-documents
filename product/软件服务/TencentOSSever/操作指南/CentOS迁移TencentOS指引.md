## 操作场景
CentOS 官方计划停止维护 CentOS Linux 项目，CentOS 8及 CentOS 7维护情况如下表格。如需了解更多信息，请参见 [CentOS 官方公告](https://blog.centos.org/2020/12/future-is-centos-stream/?spm=a2c4g.11174386.n2.3.348f4c07hk46v4)。
<table>
<tr>
<th>操作系统版本</th>
<th>停止维护时间</th>
<th>使用者影响</th>
</tr>
<tr>
<td>CentOS 8</td>
<td>2022年01月01日</td>
<td rowspan=2>停止维护后将无法获得包括问题修复和功能更新在内的任何软件维护和支持。</td>
</tr>
<tr>
<td>CentOS 7</td>
<td>2024年06月30日</td>
</tr>
</table>

针对以上情况，若您需新购云服务器实例，建议选择使用 TencentOS Server 镜像。若您正在使用 CentOS 实例，则可参考本文替换为 TencentOS Server。


## 版本说明
**源端主机支持操作系统版本**：
- 支持 CentOS 7系列操作系统版本：
  - CentOS 7.2 64位、CentOS 7.3 64位、CentOS 7.4 64位、CentOS 7.5 64位、CentOS 7.6 64位、CentOS 7.7 64位、CentOS 7.8 64位、CentOS 7.9 64位
- 支持 CentOS 8系列操作系统版本：
  - CentOS 8.0 64位、CentOS 8.2 64位、CentOS 8.4 64位

**目标主机建议操作系统版本**：
- CentOS 7系列建议迁移至 TencentOS Server 2.4 (TK4)。
- CentOS 8系列建议迁移至 TencentOS Server 3.1 (TK4)。

<dx-alert infotype="notice" title="">
CentOS 7.2、CentOS 7.3公共镜像可能默认包含了32位的软件包，需要手动移除后再执行升级操作。
</dx-alert>



## 注意事项
- 以下情况不支持迁移：
 - 安装了图形界面。
 - 安装了i686的 rpm 包。
- 以下情况可能会影响业务在迁移后无法正常运行：
 - 业务程序安装且依赖了第三方的 rpm 包。
 - 业务程序依赖于某个固定的内核版本，或者自行编译了内核模块。
迁移后的目标版本是 tkernel4，基于5.4的内核。该版本较 CentOS 7及 CentOS 8的内核版本更新，一些较旧的特性在新版本可能会发生变化。建议强依赖于内核的用户了解所依赖的特性，或可咨询 [腾讯云助手](https://cloud.tencent.com/product/tca)。
 - 业务程序依赖某个固定的 gcc 版本。
目前 TencentOS 2.4默认安装 gcc 4.8.5，TencentOS 3.1默认安装 gcc 8.5。
- 迁移结束后，需重启才能进入TencentOS 内核。
- 迁移不影响数据盘，仅 OS 层面的升级，不会对数据盘进行任何操作。

## 资源要求
-  空闲内存大于500MB。
- 系统盘剩余空间大于10GB。

## 操作步骤

### 迁移准备
1. 迁移操作不可逆，为保障业务数据安全，建议您在执行迁移前通过 [创建快照](https://cloud.tencent.com/document/product/362/5755) 备份系统盘数据。
2. 检查并手动卸载i686的 rpm 包。

### 执行迁移
<dx-tabs>
::: CentOS 7系列迁移至 TencentOS 2.4（TK4）
1. 登录目标云服务器，详情请参见 [使用标准登录方式登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436)。
2. 执行以下命令，安装 Python 3。
```shell
yum install -y python3
```
3. 执行以下命令，获取迁移工具。
```shell
wget http://mirrors.tencent.com/tencentos/2.4/tlinux/x86_64/RPMS/migrate2tencentos-1.0-4.tl2.noarch.rpm
```
4. 执行以下命令，安装迁移工具。该命令会在 /usr/sbin 下创建 migrate2tencentos.py。
```shell
rpm -ivh migrate2tencentos-1.0-4.tl2.noarch.rpm
```
5. 执行以下命令，开始迁移。
```shell
python3 /usr/sbin/migrate2tencentos.py -v 2.4
```
迁移需要一定时间，请耐心等待。脚本执行完成后，输出如下图所示信息，表示已完成迁移。
![](https://qcloudimg.tencent-cloud.cn/raw/a5d1a2cc65970b98b51071f6c90a40f5.png)
6. 重启实例，详情请参见 [重启实例](https://cloud.tencent.com/document/product/213/4928)。
7. 检查迁移结果。 
   1. 执行以下命令，检查 os-release。
```shell
cat /etc/os-release
```
返回如下图所示信息：
![](https://qcloudimg.tencent-cloud.cn/raw/11ae97a1ed88d3a6e6ddfddc369b2574.png)
   2. 执行以下命令，检查内核。
```shell
uname -r
```
返回如下图所示信息：
![](https://qcloudimg.tencent-cloud.cn/raw/cb34dbe478757069a4d3136a9384f711.png)
<dx-alert infotype="explain" title="">
内核默认为 yum 最新版本，请以您的实际返回结果为准，本文以图示版本为例。
</dx-alert>
  3. 执行以下命令，检查 yum。
```shell
yum makecache
```
返回如下图所示信息：
![](https://qcloudimg.tencent-cloud.cn/raw/88b9468bed347c567223385b3df161b4.png)


:::
::: CentOS 8系列迁移至 TencentOS 3.1（TK4）
1. 登录目标云服务器，详情请参见 [使用标准登录方式登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436)。
2. 执行以下命令，安装 Python 3。
```shell
yum install -y python3
```
3. 执行以下命令，获取迁移工具。
```shell
wget http://mirrors.tencent.com/tlinux/3.1/Updates/x86_64/RPMS/migrate2tencentos-1.0-4.tl3.noarch.rpm
```
4. 执行以下命令，安装迁移工具。该命令会在 /usr/sbin 下创建 migrate2tencentos.py。
```shell
rpm -ivh migrate2tencentos-1.0-4.tl3.noarch.rpm
```
5. 执行以下命令，开始迁移。
```shell
python3 /usr/sbin/migrate2tencentos.py -v 3.1
```
迁移需要一定时间，请耐心等待。脚本执行完成后，输出如下图所示信息，表示已完成迁移。
![](https://qcloudimg.tencent-cloud.cn/raw/e272e5f6e5eba50a1e9bc74db536a592.png)
6. 重启实例，详情请参见 [重启实例](https://cloud.tencent.com/document/product/213/4928)。
7. 检查迁移结果。 
   1. 执行以下命令，检查 os-release。
```shell
cat /etc/os-release
```
返回如下图所示信息：
![](https://qcloudimg.tencent-cloud.cn/raw/eb7333c8badf5d7a4852a66084fcc190.png)
   2. 执行以下命令，检查内核。
```shell
uname -r
```
返回如下图所示信息：
![](https://qcloudimg.tencent-cloud.cn/raw/9bba4c6112c4bec1482d827ad02a39d6.png)
<dx-alert infotype="explain" title="">
内核默认为 yum 最新版本，请以您的实际返回结果为准，本文以图示版本为例。
</dx-alert>
  3. 执行以下命令，检查 yum。
```shell
yum makecache
```
返回如下图所示信息：
![](https://qcloudimg.tencent-cloud.cn/raw/83a6ec7fc69ab6bd26e9ff1cf0f443da.png)

:::
</dx-tabs>

若您在迁移过程中遇到问题，请联系 [腾讯云助手](https://cloud.tencent.com/product/tca)。
