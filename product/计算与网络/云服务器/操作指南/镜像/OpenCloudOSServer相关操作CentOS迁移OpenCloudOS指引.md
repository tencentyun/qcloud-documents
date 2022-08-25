
## 操作场景
CentOS 8已于2022年01月01日停止维护，后续将无法获得包括问题修复和功能更新在内的任何软件维护和支持，详情请参见 [CentOS](https://blog.centos.org/2020/12/future-is-centos-stream/?spm=a2c4g.11174386.n2.3.348f4c07hk46v4)。若您正在使用 CentOS 8操作系统实例，可参考本文替换为 OpenCloudOS Server。

## 版本说明
- 源端主机支持操作系统版本：CentOS 8系列，包括 CentOS 8.0 64位、CentOS 8.2 64位、CentOS 8.3 64位、CentOS 8.4 64位
- 目标主机建议操作系统版本：CentOS 8系列建议迁移至 OpenCloudOS Server 8

## 注意事项
- 以下情况不支持迁移：
 - 安装了图形界面。
 - 安装了i686的 rpm 包。
 - 使用 CentOS 8 stream 公共镜像的实例暂时不支持迁移操作。
- 以下情况可能会影响业务在迁移后无法正常运行：
 - 业务程序安装且依赖了第三方的 rpm 包。
 - 业务程序依赖于某个固定的内核版本，或者自行编译了内核模块。
 迁移后的目标版本是 tkernel4，基于5.4的内核。该版本较CentOS 8的内核版本更新，一些较旧的特性在新版本可能会发生变化。建议强依赖于内核的用户了解所依赖的特性，或可咨询 [腾讯云助手](https://cloud.tencent.com/product/tca)。
 - 业务程序依赖某个固定的 gcc 版本。目前 OpenCloudOS 8默认安装 gcc 8.5。
- 迁移结束后，需重启才能进入OpenCloudOS 内核。
- 迁移不影响数据盘，仅 OS 层面的升级，不会对数据盘进行任何操作。

## 资源要求
- 空闲内存大于500MB。
- 系统盘剩余空间大于10GB。


## 操作步骤

### 迁移准备
1. 迁移操作不可逆，为保障业务数据安全，建议您在执行迁移前通过 [创建快照](https://cloud.tencent.com/document/product/362/5755) 备份系统盘数据。
2. 检查并手动卸载 i686 的 rpm 包。
3. 检查是否安装 Python3。若未安装，则请通过以下方式进行安装。
 - 方式1：执行以下命令，通过 yum 源安装。
```shell
yum install -y python3
```
 - 方式2：若 yum 源不可用，则请依次执行以下命令，使用 centos-vault 源安装。
```shell
cat <<EOF | sudo tee /tmp/centos8_vault.repo
[c8_vault_baseos]
name=c8_vault - BaseOS
baseurl=http://mirrors.cloud.tencent.com/centos-vault/8.5.2111/BaseOS/\$basearch/os/
gpgcheck=0
enabled=1
[c8_vault_appstream]
name=c8_vault - AppStream
baseurl=http://mirrors.cloud.tencent.com/centos-vault/8.5.2111/AppStream/\$basearch/os/
gpgcheck=0
enabled=1
EOF
```
```shell
yum -y install python3 --disablerepo=* -c /tmp/centos8_vault.repo --enablerepo=c8_vault*
```


### 执行迁移
1. 登录目标云服务器，详情i请参见 [使用标准登录方式登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436)。
2. 点击 [链接](https://drive.weixin.qq.com/s?k=AJEAIQdfAAo3qIKRaJAboAJgaKAEM#/preview?fileId=i.1970325010981265.1688855288358586_f.661329633xdFh)，下载迁移工具包。
3. 执行以下命令，安装迁移工具。该命令会在 /usr/sbin 下创建 migrate2tencentos.py。
```shell
rpm -ivh migrate2opencloudos-1.0-4.oc8.noarch.rpm
```
4. 执行以下命令，开始迁移。
```shell
python3 /usr/sbin/migrate2opencloudos-1.0-4.oc8.noarch.rpm -v 8
```
迁移需要一定时间，请耐心等待。脚本执行完成后，输出如下图所示信息，表示已完成迁移。
![](https://qcloudimg.tencent-cloud.cn/raw/5436031a629a5cb451864388036bba0d.png)
5. 重启实例，详情请参见 [重启实例](https://cloud.tencent.com/document/product/213/4928)。


### 检查迁移结果
1. 执行以下命令，检查 os-release。
```shell
cat /etc/os-release
```
返回如下图所示信息：
![](https://qcloudimg.tencent-cloud.cn/raw/49ff5c508a4715e34ac97b34350ac180.png)
2. 执行以下命令，检查内核。
```shell
uname -r
```
返回如下图所示信息：
![](https://qcloudimg.tencent-cloud.cn/raw/0221b3623231a9c3fb2f1c71ffd8c7b8.png)
<dx-alert infotype="explain" title="">
内核默认为 yum 最新版本，请以您的实际返回结果为准，本文以图示版本为例。
</dx-alert>
3. 执行以下命令，检查 yum。
```shell
yum makecache
```
返回如下图所示信息：
![](https://qcloudimg.tencent-cloud.cn/raw/e2b08a96846403f064e006aa61eb3dd0.png)

至此已成功迁移，若您在迁移过程中遇到问题，请联系 [腾讯云助手](https://cloud.tencent.com/product/tca)。



