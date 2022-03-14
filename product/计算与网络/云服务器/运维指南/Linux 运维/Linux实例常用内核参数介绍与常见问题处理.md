腾讯云在 Linux 公有镜像中已默认配置了部分参数，但由于 sysctl 的高度个性化配置，腾讯云建议用户按照自身业务特点单独配置 sysctl。您可通过本文了解腾讯云针对公有云 Linux 公有镜像特殊的默认优化配置及常见配置，并根据业务进行手动调优。

<dx-alert infotype="explain" title="">
- “初始化配置”项为“-”的参数项，均保持官方镜像默认配置。
- 使用 sysctl -w 命令配置为临时生效，写入 /etc/sysctl.conf 配置永久生效。
</dx-alert>



### 网络类
<table>
<tr>
<th>参数</th><th>说明</th><th>初始化配置</th>
</tr>
<tr>
<td><code>net.ipv4.tcp_tw_recycle</code></td>
<td>该参数用于快速回收 TIME_WAIT 连接。关闭时，内核不检查包的时间戳。开启时则会进行检查。<br>不建议开启该参数，在时间戳非单调增长的情况下，会引起丢包问题，高版本内核已经移除了该参数。</td>
<td>0</td>
</tr>
<tr>
<td><code>net.core.somaxconn</code></td>
<td>对应三次握手结束，还没有 accept 队列时的 establish 状态。accept 队列较多则说明服务端 accept 效率不高，或短时间内突发了大量新建连接。该值过小会导致服务器收到 syn 不回包，是由于 somaxconn 表满而删除新建的 syn 连接引起。若为高并发业务，则可尝试增大该值，但有可能增大延迟。
</td>
<td>128</td>
</tr>
<tr>
<td><code>net.ipv4.tcp_max_syn_backlog</code></td>
<td>对应半连接的上限，曾用来防御常见的 synflood 攻击，但当 tcp_syncookies=1 时半连接可超过该上限。</td>
<td>-</td>
</tr>
<tr>
<td><code>net.ipv4.tcp_syncookies</code></td>
<td>对应开启 SYN Cookies，表示启用 Cookies 来处理，可防范部分 SYN 攻击，当出现 SYN 等待队列溢出时也可继续连接。但开启后会使用 SHA1 验证 Cookies，理论上会增大 CPU 使用率。</td>
<td>1</td>
</tr>
<tr>
<td><code>net.core.rmem_default</code><br>
<code>net.core.rmem_max</code><br>
<code>net.ipv4.tcp_mem</code><br>
<code>net.ipv4.tcp_rmem</code>
</td>
<td>这些参数配置了数据接收的缓存大小。配置过大容易造成内存资源浪费，过小则会导致丢包。建议判断自身业务是否属于高并发连接或少并发高吞吐量情形，进行优化配置。<ul><li>rmem_default 的理论最优配置策略为带宽/RTT 积，其配置会覆盖 tcp_rmem，tcp_rmem 不单独配置。</li><li>rmem_max 配置约为 rmem_default 的5倍。</li><li>tcp_mem 为总的 TCP 占用内存，一般由 OS 自动配置为 CVM 可用内存的3/32、1/8或3/16，tcp_mem 及 rmem_default 也决定了最大并发链接数。</li></ul></td>
<td><code>rmem_default<br>=655360</code><br>
<code>rmem_max<br>=3276800</code></td>
</tr>
<tr>
<td><code>net.core.wmem_default</code><br>
<code>net.core.wmem_max</code><br>
<code>net.ipv4.tcp_wmem</code>
</td>
<td>这些参数用于配置数据发送缓存，腾讯云平台上数据发送通常不会出现瓶颈，可不做配置。</td>
<td>-</td>
</tr>
<tr>
<td><code>net.ipv4.tcp_keepalive_intvl</code><br>
<code>net.ipv4.tcp_keepalive_probes</code><br>
<code>net.ipv4.tcp_keepalive_time</code>
</td>
<td>这些参数与 TCP KeepAlive 有关，默认为75/9/7200。表示某个 TCP 连接在空闲7200秒后，内核才发起探测，探测9次（每次75秒）不成功，内核才发送 RST。对服务器而言，默认值比较大，可结合业务调整到30/3/1800。</td>
<td>-</td>
</tr>
<tr>
<td><code>net.ipv4.ip_local_port_range</code></td>
<td>配置可用端口的范围，请按需调整。</td>
<td>-</td>
</tr>
<tr>
<td><code>tcp_tw_reuse</code></td>
<td>该参数允许将 TIME-WAIT 状态的 socket 用于新的 TCP 连接。对快速重启动某些占用固定端口的链接有帮助，但基于 NAT 网络有潜在的隐患，高版本内核变为0/1/2三个值，并配置为2。</td>
<td>-</td>
</tr>
<tr>
<td><code>net.ipv4.ip_forward</code><br>
<code>net.ipv6.conf.all.forwarding</code>
</td>
<td>IP 转发功能，若用于 docker 的路由转发场景可将其配置为1。</td>
<td>0</td>
</tr>
<tr>
<td><code>net.ipv4.conf.default.rp_filter</code></td>
<td>该参数为网卡对接收到的数据包进行反向路由验证的规则，可配置为0/1/2。根据 RFC3704建议，推荐设置为1，打开严格反向路由验证，可防止部分 DDos 攻击及防止 IP Spoofing 等。</td>
<td>-</td>
</tr>
<tr>
<td><code>net.ipv4.conf.default.accept_source_route</code></td>
<td>根据 CentOS 官网建议，默认不允许接受含有源路由信息的 IP 包。</td>
<td>0</td>
</tr>
<tr>
<td><code>net.ipv4.conf.all.promote_secondaries</code><br>
<code>net.ipv4.conf.default.promote_secondaries</code></td>
<td>当主 IP 地址被删除时，第二 IP 地址是否成为新的主 IP 地址。</td>
<td>1</td>
</tr>
<tr>
<td><code>net.ipv6.neigh.default.gc_thresh3</code><br>
<code>net.ipv4.neigh.default.gc_thresh3</code>
</td>
<td>保存在 ARP 高速缓存中的最多记录的限制，一旦高速缓存中的数目高于设定值，垃圾收集器将马上运行。</td>
<td>4096</td>
</tr>
</table>



### 内存类

<table>
<tr>
<th>参数</th><th>说明</th><th>初始化配置</th>
</tr>
<tr>
<td><code>vm.vfs_cache_pressure</code></td>
<td>原始值为100，表示扫描 dentry 的力度。以100为基准，该值越大内核回收算法越倾向于回收内存。很多基于 curl 的业务上，通常由于 dentry 的积累导致占满所有可用内存，容易触发 OOM 或内核 bug 之类的问题。综合考虑回收频率和性能后，选择配置为250，可按需调整。</td>
<td>250</td>
</tr>
<tr>
<td><code>vm.min_free_kbytes</code></td>
<td>该值是启动时根据系统可用物理内存 MEM 自动计算出：4 * sqrt（MEM）。其含义是让系统运行时至少要预留出的 KB 内存，一般情况下提供给内核线程使用，该值无需设置过大。当机器包量出现微突发，则有一定概率会出现击穿 vm.min_free_kbytes，造成 OOM。建议大配置的机器下默认将 vm.min_free_kbytes 配置为总内存的1%左右。
</td>
<td>-</td>
</tr>
<tr>
<td><code>kernel.printk</code></td>
<td>内核 printk 函数打印级别，默认配置为大于5。</td>
<td>5 4 1 7</td>
</tr>
<tr>
<td><code>kernel.numa_balancing</code></td>
<td>该参数表示可以由内核自发的将进程的数据移动到对应的 NUMA 上，但是实际应用的效果不佳且有其他性能影响，redis 的场景下可以尝试开启。</td>
<td>0</td>
</tr>
<tr>
<td><code>kernel.shmall</code><br>
<code>kernel.shmmax</code>
</td>
<td><ul><li>shmmax 设置一次分配 shared memory 的最大长度，单位为 byte。</li><li>shmall 设置一共能分配 shared memory 的最大长度，单位为 page。</li></ul></td>
<td><code>kernel.shmmax<br>=68719476736</code><br>
<code>kernel.shmall<br>=4294967296</code>
</td>
</tr>
</table>

### 进程类
<table>
<tr>
<th>参数</th><th>说明</th><th>初始化配置</th>
</tr>
<tr>
<td><code>fs.file-max</code><br>
<code>fs.nr_open</code>
</td>
<td>分别控制系统所有进程和单进程能同时打开的最大文件数量：<ul><li>file-max 由 OS 启动时自动配置，近似为10万/GB。</li><li>nr_open 为固定值1048576，但为针对用户态打开最大文件数的限制，一般不改动这个值，通常设置 ulimit -n 实现，对应配置文件为 /etc/security/limits.conf。</li></ul></td>
<td>
<code>ulimit 的 open files 为100001</code><br>
<code>fs.nr_open=1048576</code>
</td>
</tr>
<tr>
<td><code>kernel.pid_max</code></td>
<td>系统内最大进程数，官方镜像默认为32768，可按需调整。</td>
<td>-</td>
</tr>
<tr>
<td><code>kernel.core_uses_pid</code></td>
<td>该配置决定 coredump 文件生成的时候是否含有 pid。</td>
<td>1</td>
</tr>
<tr>
<td><code>kernel.sysrq</code></td>
<td>开启该参数后，后续可对 /proc/sysrq-trigger 进行相关操作。</td>
<td>1</td>
</tr>
<tr>
<td><code>kernel.msgmnb</code><br>
<code>kernel.msgmax</code>
</td>
<td>分别表示消息队列中的最大字节数和单个最大消息队列容量。</td>
<td>65536</td>
</tr>
<tr>
<td><code>kernel.softlockup_panic</code></td>
<td>当配置了 softlockup_panic 时，内核检测到某进程 softlockup 时，会发生 panic，结合 kdump 的配置可生成 vmcore，用以分析 softlockup 的原因。</td>
<td>-</td>
</tr>
</table>


### IO 类
<table>
<tr>
<th>参数</th><th>说明</th><th>初始化配置</th>
</tr>
<tr>
<td><code>vm.dirty_background_bytes</code><br>
<code>vm.dirty_background_ratio</code><br>
<code>vm.dirty_bytes</code><br>
<code>vm.dirty_expire_centisecs</code><br>
<code>vm.dirty_ratio</code><br>
<code>vm.dirty_writeback_centisecs</code>
</td>
<td>这部分参数主要配置 IO 写回磁盘的策略：<ul><li>dirty_background_bytes/dirty_bytes 和 dirty_background_ratio/dirty_ratio 分别对应内存脏页阈值的绝对数量和比例数量，一般情况下设置 ratio。</li><li>dirty_background_ratio 指当文件系统缓存脏页数量达到系统内存百分之多少时（默认10%）唤醒内核的 flush 等进程，写回磁盘。</li><li>dirty_ratio 为最大脏页比例，当脏页数达到该比例时，必须将所有脏数据提交到磁盘，同时所有新的 IO 都会被阻塞，直到脏数据被写入磁盘，通常会造成 IO 卡顿。系统先会达到 vm.dirty_background_ratio 的条件然后触发 flush 进程进行异步的回写操作，此时应用进程仍然可以进行写操作，如果达到 vm.dirty_ratio 这个参数所设定的值，此时操作系统会转入同步地处理脏页的过程，阻塞应用进程。<br>
</li><li>vm.dirty_expire_centisecs 表示脏页能存活的时间，flush 进程会检查数据是否超过了该时间限制，单位为1/100秒。</li><li>vm.dirty_writeback_centisecs 表示 flush 进程的唤醒周期，单位为1/100秒。</li></ul>
</td>
<td>-</td>
</table>
