腾讯云自2016年4月11日起，新购买的linux操作系统CVM将不再提供2GB的SWAP盘。

Swap分区是在系统物理内存不够用时由系统内存管理程序将很长时间没有操作内存数据临时保存到Swap分区中，以提高可用内存额度的一种机制。当那些程序要再次重新运行时，会再从Swap分区恢复之前保存的数据到内存中。
　　
相关操作会导致额外的IO开销，特别是，如果内存使用率已经非常高，而同时IO性能也不是很好的情况下，该机制其实会起到相反的效果：不仅系统性能提升较小（因为内存使用率已经非常高了），而且由于频繁的内存到SWAP的切换操作，会导致产生大量额外的IO操作，导致IO性能进一步降低，最终反而降低了系统总体性能。
　　
内存与磁盘性能有10倍以上的差距。Mysql等业务当内存数据临时保存到SWAP分区时，数据库的整体服务质量会大大下降。为了保证您业务的正常运行，当服务器内存不足时，建议您增加内存空间。
　　
您亦可以通过自行配置，划分SWAP分区，配置方案如下：
- 查看系统当前的分区情况`free -m`
- 创建用于交换分区的文件`dd if=/dev/zero of=/xxx/swap bs=4096 count=1572864`
- 设置交换分区文件`mkswap /xxx/swap`
- 启用交换分区文件`swapon /xxx/swap`
- 若要想使开机时自启用，则需修改文件`/etc/fstab`中的swap行` echo “LABEL=SWAP-sda /xxx/swap swap swap defaults 0 0” >> /etc/fstab`
- 删除swap`swapoff /xxx/swap ; rm -f /Application/swap`

若已配置SWAP分区，并写入fstab，当系统重装或者新购买服务器时，我们不会保留fstab设置，您需要重新设置。

另：针对FreeBSD系统的云服务器，配置SWQP分区的方法请参见： http://www.techonia.com/1807/add-swap-file-linux-freebsd
