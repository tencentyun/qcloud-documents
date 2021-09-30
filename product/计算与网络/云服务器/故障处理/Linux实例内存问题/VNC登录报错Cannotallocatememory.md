## 现象描述
使用 VNC 登录云服务器时，无法正常进入系统，且出现 “Cannot allocate memory” 报错信息。如下图所示：
![](https://main.qcloudimg.com/raw/0a31fdd909701c27c9923b2fff24668a.png)

## 可能原因[](id:PossibleCauses)
可能是系统中存在多个大页内存导致。一个大页内存默认占用2048KB，根据 `/etc/sysctl.conf` 里的大页内存个数计算，以下图为例，1280个大页内存等于2.5G。如果实例的配置较低，但仍将2.5G分配给大页内存池（Huge Pages pool），则将导致系统没有可用内存，重启后无法进入系统。
![](https://main.qcloudimg.com/raw/1978a0b2a85fc828674f720c108c48a3.png)


## 解决思路
1. 参考 [处理步骤](#ProcessingSteps)，查看总进程数是否超限。 
2. 核实大页内存配置，并修改为合适的配置。


## 处理步骤[](id:ProcessingSteps)
1. 参考 [日志报错 fork：Cannot allocate memory](https://cloud.tencent.com/document/product/213/54645)，核实进程数是否超限。若进程数未超限，则执行下一步。
2. 使用单用户模式登入云服务器，详情请参见 [设置 Linux 云服务器进入单用户模式](https://cloud.tencent.com/document/product/213/33321)。
3. 执行以下命令，参考 [可能原因](#PossibleCauses) 核实大页内存配置。
```
cat /etc/sysctl.conf | grep hugepages
```
若存在多个大页内存，则请按照以下步骤修改配置。
4. 执行以下命令，使用 VIM 编辑器打开 `/etc/sysctl.conf` 配置文件。
```
vim /etc/sysctl.conf
```
5. 按 **i** 进入编辑模式，结合实例实际配置将 `vm.nr_hugepages` 配置项调低至合理数值。
6. 按 **Esc** 并输入 **:wq** 后，按 **Enter** 保存并退出 VIM 编辑器。
7. 执行以下命令，使配置立即生效。
```
sysctl -p
```
8. 配置完成后，重启云服务器即可恢复登录。
