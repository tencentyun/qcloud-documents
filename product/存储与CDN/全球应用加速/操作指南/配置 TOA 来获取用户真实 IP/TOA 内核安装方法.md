## CentOS TOA 内核安装方法
### rpm 包安装方式
直接下载下面的 rpm 包：
- CentOS 6 TOA 包（[单击下载](http://toakernel-1253438722.cossh.myqcloud.com/kernel-2.6.32-220.23.1.el6.toa.x86_64.rpm)）。
- CentOS 7 TOA 包（[单击下载](http://toakernel-1253438722.cossh.myqcloud.com/kernel-3.10.0-693.el7.centos.toa.x86_64.rpm)）。  

下载安装完后，重启系统即完成安装。
也可以自己制作 rpm 包，自己制作 rpm 包步骤如下：
1. 安装 kernel-2.6.32-220.23.1.el6.src.rpm：
```
rpm -hiv kernel-2.6.32-220.23.1.el6.src.rpm
```
2. 生成内核源码目录：
```
rpmbuild -bp ~/rpmbuild/SPECS/kernel.spec
```
3. 复制一份源码目录：
```
cd ~/rpmbuild/BUILD/kernel-2.6.32-220.23.1.el6/
cp -a linux-2.6.32-220.23.1.el6.x86_64/ linux-2.6.32-220.23.1.el6.x86_64_new
```
4. 在复制出来的源码目录中打下面的 toa 补丁：
```
cd ~/rpmbuild/BUILD/kernel-2.6.32-220.23.1.el6/linux-2.6.32-220.23.1.el6.x86_64_new/
patch -p1 < /usr/local/src/linux-2.6.32-220.23.1.el6.x86_64.rs/toa-2.6.32-220.23.1.el6.patch
```
5. 编辑 .config 并拷贝到 SOURCE 目录：
```
sed -i 's/CONFIG_IPV6=m/CONFIG_IPV6=y/g' .config
echo -e '\n# toa\nCONFIG_TOA=m' >> .config
cp .config ~/rpmbuild/SOURCES/config-x86_64-generic
```
6. 删除原始源码中的 .config：
```
cd ~/rpmbuild/BUILD/kernel-2.6.32-220.23.1.el6/linux-2.6.32-220.23.1.el6.x86_64
rm -rf .config
```
7. 生成最终 patch：
```
cd ~/rpmbuild/BUILD/kernel-2.6.32-220.23.1.el6/
diff -uNr linux-2.6.32-220.23.1.el6.x86_64 linux-2.6.32-220.23.1.el6.x86_64_new/ >
~/rpmbuild/SOURCES/toa.patch
```
8. 编辑 kernel.spec ：
`vim ~/rpmbuild/SPECS/kernel.spec`
在 ApplyOptionPath 下添加如下两行（还可修改 buildid 等自定义内核包名）：
```
Patch999999: toa.patch
ApplyOptionalPatch toa.patch
```
9. 制作 rpm 包：
```
rpmbuild -bb --with baseonly --without kabichk --with firmware --without debuginfo --target=x86_64 ~/rpmbuild/SPECS/kernel.spec
```
10. 安装内核 rpm 包：
```
rpm -hiv kernel-xxxx.rpm --force
```
11. 重启，加载 toa 模块，安装完毕。

### 源码安装方式
如果您所需要的操作系统版本不是低于CentOS 6，您也可以通过下载源代码编译的方式，得到相应的安装包，步骤如下：
1. 下载打好 toa 补丁的源码包（[单击下载](http://kb.linuxvirtualserver.org/images/3/34/Linux-2.6.32-220.23.1.el6.x86_64.rs.src.tar.gz)）。
2. 解压。
3. 编辑`.config`，将`CONFIG_IPV6=M`改成`CONFIG_IPV6=y`。
4. 如果需要加上一些自定义说明，可以编辑` Makefile`。
5. `make -jn` (n 为线程数)。
6. 执行`make modules_install` 。
7. 执行`make install`。
8. 修改`/boot/grub/menu.lst`，将 default 改为新安装的内核（title 顺序从 0 开始）。
9. 执行`Reboot` 重启后即为 toa 内核。
10. 执行`lsmod | grep toa`检查 toa 模块是否加载，没有加载的话，可通过`modprobe toa`命令 开启。

## Ubuntu TOA 内核安装方法
单击下面的链接，下载内核包和 Headers 包：
- 内核包（[单击下载](http://toakernel-1253438722.cossh.myqcloud.com/linux-image-4.4.87.toa_1.0_amd64.deb)） 
- 内核 Headers 包（[单击下载](http://toakernel-1253438722.cossh.myqcloud.com/linux-headers-4.4.87.toa_1.0_amd64.deb)） 

Headers 包为选装，可在需要做相关开发时再安装。请先安装内核包，相应的操作步骤如下：
1. 执行下面的指令，安装内核包：  
```
dpkg -i linux-image-4.4.87.toa_1.0_amd64.deb
```
2. 安装完成后请重启主机。
3. 执行 `lsmod | grep toa` 检查 toa 模块是否加载，若没加载，可通过 `modprobe toa` 开启，执行命令如下：
```
echo “modprobe toa” >> /etc/rc.d/rc.local
```

## Debian TOA 内核安装方法
单击下面的链接，下载内核包和 Headers 包：
- 内核包（[单击下载](http://toakernel-1253438722.cossh.myqcloud.com/linux-image-3.16.43.toa_1.0_amd64.deb)）
- 内核 Headers 包（[单击下载](http://toakernel-1253438722.cossh.myqcloud.com/linux-headers-3.16.43.toa_1.0_amd64.deb)）

Headers 包为选装，可在需要做相关开发时再安装。请先安装内核包，相应的操作步骤如下：
1. 执行下面的指令，安装内核包：  
```
dpkg -i linux-image-4.4.87.toa_1.0_amd64.deb
```
2. 安装完成后请重启主机。
3. 执行 `lsmod | grep toa` 检查 toa 模块是否加载，若没加载，可通过 `modprobe toa` 开启，执行命令如下：
```
echo “modprobe toa” >> /etc/rc.d/rc.local
```
