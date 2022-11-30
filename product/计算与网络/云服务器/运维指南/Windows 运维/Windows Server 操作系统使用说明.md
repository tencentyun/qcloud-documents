## Windows Server操作系统使用建议
1. 由于 Windows 操作系统本身可能存在的不稳定性，您在执行升级系统、更新补丁等操作前，请务必进行完整备份，备份方式包括制作 [自定义镜像](https://cloud.tencent.com/document/product/213/4942) 、[创建快照](https://cloud.tencent.com/document/product/362/5755) 等；若出现不兼容或者报错的情况，您可以可以通过备份回滚；Windows Server 操作系统自身的问题带来的损失与腾讯云无关。
2. Windows 系统使用便利、受众广泛，但也是网络攻击和黑客入侵的重灾区，养成良好的使用习惯尤其备份数据的习惯是非常重要的，最好是能安装杀毒防护软件，如 [微软电脑管家](https://pcmanager.microsoft.com/)（适用于 Windows Server 2019 及以上版本），并配合加强 [安全组](https://cloud.tencent.com/document/product/213/12452) 设置， 例如只放行需要外网访问的端口，像数据库端口一般只需服务器本机能访问就可以，不需要外网放行安全组入站（视业务具体情况而定）；对远程端口，建议修改默认远程端口号，在安全组放行新端口号时只放行客户端 IP 或 IP 段，建议不要范围放的太大。
3. 建议您选用新版本 Windows Sercer 镜像，如 Windows Server 2022，新版本系统相对老版本系统其稳定性、健壮性、整体性都会更好。
## 标准型 SA2.45XLARGE464 机型不推荐使用 Windows Server 2016
为了机型与操作系统更好的兼容性，实例规格 SA2.45XLARGE464（180核464GB）不推荐使用 Windows Server 2016 操作系统，可能会出现实例开机时间长达10分钟～1小时的情况；推荐您使用 Windows Server 2019 及更高版本的操作系统。
## 标准型SA3高配机型不推荐使用Windows Server 2016
为了机型与操作系统更好的兼容性，实例规格 SA3 高配置机型不推荐使用 Windows Server 2016 操作系统，可能会出现实例开机时间长达10分钟～1小时的情况；推荐您使用 Windows Server 2019 及更高版本的操作系统。
标准型 SA3 高配机型包括以下实例规格：

| 实例规格 | CPU | 内存 |
|---------|---------|---------|
| SA3.29XLARGE470| 116| 470|
| SA3.40XLARGE640| 160| 640|
| SA3.58XLARGE432| 232| 432|
| SA3.58XLARGE940| 232| 940|



