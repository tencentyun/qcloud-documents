## Download Links
[Kernel Packet>>](http://toakernel-1253438722.cossh.myqcloud.com/linux-image-4.4.87.toa_1.0_amd64.deb)


[Kernel Headers Packet>>](http://toakernel-1253438722.cossh.myqcloud.com/linux-headers-4.4.87.toa_1.0_amd64.deb)

## Installation Method
Headers packet is optional, which can be installed as needed for development. Install the kernel packet first.

1. Execute the following command to install the kernel packet:
`dpkg -i linux-image-4.4.87.toa_1.0_amd64.deb`

2. After the installation is completed, restart the server.

3. Check whether the toa module is loaded by executing `lsmode | grep toa`. If not, enable it using the following `modprobe toa` command:
`echo "modprobe toa" >> /etc/rc.d/rc.local`

