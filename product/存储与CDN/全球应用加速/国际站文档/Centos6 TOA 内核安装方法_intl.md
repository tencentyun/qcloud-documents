## Method 1: Installation via rpm Packet
Download one of the following rpm packets:

- CentOS 6 TOA ([Click to download](http://toakernel-1253438722.cossh.myqcloud.com/kernel-2.6.32-220.23.1.el6.toa.x86_64.rpm));
- CentOS 7 TOA ([Click to download](http://toakernel-1253438722.cossh.myqcloud.com/kernel-3.10.0-693.el7.centos.toa.x86_64.rpm));  

After the packet has been installed, restart the system to complete the installation process.

You can also create a rpm packet as follows:
1. Install kernel-2.6.32-220.23.1.el6.src.rpm:
`rpm -hiv kernel-2.6.32-220.23.1.el6.src.rpm`

2. Generate a kernel source code directory:
`rpmbuild -bp ~/rpmbuild/SPECS/kernel.spec`

3. Copy the source code directory:
```
cd ~/rpmbuild/BUILD/kernel-2.6.32-220.23.1.el6/
cp -a linux-2.6.32-220.23.1.el6.x86_64/ linux-2.6.32-220.23.1.el6.x86_64_new
```

4. Attach the following toa patch to the copied source code directory:
```
cd ~/rpmbuild/BUILD/kernel-2.6.32-220.23.1.el6/linux-2.6.32-220.23.1.el6.x86_64_new/
patch -p1 < /usr/local/src/linux-2.6.32-220.23.1.el6.x86_64.rs/toa-2.6.32-220.23.1.el6.patch
```

5. Edit .config and copy it to the SOURCE directory:
```
sed -i 's/CONFIG_IPV6=m/CONFIG_IPV6=y/g' .config
echo -e '\n# toa\nCONFIG_TOA=m' >> .config
cp .config ~/rpmbuild/SOURCES/config-x86_64-generic
```

6. Delete .config from the source code:
```
cd ~/rpmbuild/BUILD/kernel-2.6.32-220.23.1.el6/linux-2.6.32-220.23.1.el6.x86_64
rm -rf .config
```

7. Generate the final patch:
```
cd ~/rpmbuild/BUILD/kernel-2.6.32-220.23.1.el6/
diff -uNr linux-2.6.32-220.23.1.el6.x86_64 linux-2.6.32-220.23.1.el6.x86_64_new/ >
~/rpmbuild/SOURCES/toa.patch
```

8. Edit kernel.spec:
`vim ~/rpmbuild/SPECS/kernel.spec`
Add the following lines to ApplyOptionPath (the buildid and the names of other custom kernel packets can also be modified)
```
Patch999999: toa.patch
ApplyOptionalPatch toa.patch
```

9. Create a rpm packet:
`rpmbuild -bb --with baseonly --without kabichk --with firmware --without debuginfo --target=x86_64 ~/rpmbuild/SPECS/kernel.spec`

10. Install the kernel rpm packet:
`rpm -hiv kernel-xxxx.rpm --force`

11. Restart the system to load TOA module.


## Method 2: Installation via Source Code
1. Download the source code package patched with TOA ([Click to download](http://kb.linuxvirtualserver.org/images/3/34/Linux-2.6.32-220.23.1.el6.x86_64.rs.src.tar.gz)）.
2. Decompress the package.
3. Edit .config, and change CONFIG_IPV6=M to CONFIG_IPV6=y.
4. You can edit Makefile to add a custom description.
5. make -jn (n is the number of threads).
6. Execute `make modules_install` ；.
7. Execute `make install`；.
8. Modify `/boot/grub/menu.lst`, and change default to the new kernel ("title" starts from 0).
9. toa kernel is loaded after `Reboot`.
10. Check whether the toa module is loaded by executing `lsmode | grep toa`. If not, enable it using the `modprobe toa` command.


