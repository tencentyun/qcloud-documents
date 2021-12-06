## 功能介绍
线程池（Thread_pool）采用一定数量的工作线程来处理连接请求，通常比较适应于 OLTP 工作负载的场景。但线程池的不足在于当请求偏向于慢查询时，工作线程阻塞在高时延操作上，难以快速响应新的请求，导致系统吞吐量反而相较于传统 one-thread-per-connection（Per_thread）模式更低。

Per_thread 模式与 Thread_pool 模式各有优缺点，系统需要根据业务类型灵活地进行切换。遗憾的是，当前两种模式的切换必须重启服务器才能完成。通常而言，两种模式相互转换的需求都是出现在业务高峰时段，此时强制重启服务器将对业务造成严重影响。

为了提高 Per_thread 模式与 Thread_pool 模式切换的灵活程度，云数据库 MySQL 提出了线程池动态切换的优化，即在不重启数据库服务的情况下，动态开启或关闭线程池。

## 支持版本
- 内核版本 MySQL 8.0 20201230 及以上
- 内核版本 MySQL 5.7 20201230 及以上

## 适用场景
对性能敏感，需要根据业务类型灵活调整数据库工作模式的业务。

## 性能影响
- pool-of-threads 切换为 one-thread-per-connection 过程本身不会带来 query 堆积，以及性能影响。
- one-thread-per-connection 切换为 pool-of-threads 过程由于之前线程池处于休眠状态，在 QPS 极高并且有持续高压的情况下，可能存在一定的请求累积。解决方案如下：
  - 方案1：适当增大 thread_pool_oversubscribe，并适当调小 thread_pool_stall_limit，快速激活线程池。待消化完堆积 SQL 再视情况还原上述修改。
  - 方案2：出现 SQL 累积时，短暂暂停或降低业务流量几秒钟，等待 pool-of-threads 完成激活，再恢复持续高压业务流量。

## 使用说明
新增 thread_handling_switch_mode 用于控制线程池动态切换功能，可选值及其含义如下：

| 可选值   | 含义                                               |
| -------- | -------------------------------------------------- |
| disabled | 禁止模式动态迁移                                   |
| stable    | 只有新连接迁移                                     |
| fast       | 新连接 + 新请求都迁移，默认模式                      |
| sharp    | kill 当前活跃连接，迫使用户重连，达到快速切换的效果 |

在 `show threadpool status` 中新增如下状态：
- connections_moved_from_per_thread 表示从 Per_thread 迁移至 Thread_pool 的 connections 数量。
- connections_moved_to_per_thread 表示从 Thread_pool 迁移至 Per_thread 的 connections 数量。
- events_consumed 表示每个线程池工作线程组消费的 events 总数，当 Thread_pool 迁移至 Per_thread 后，events 总数不再增加。
- average_wait_usecs_in_queue 表示每个 event 平均在 queue 中等待的时间。

在 `show full processlist` 中新增如下状态：
- Moved_to_per_thread 表示该连接迁移到 Per_thread 的次数。
- Moved_to_thread_pool 表示该连接迁移到 Thread_pool 的次数.

## 相关参数状态说明
线程池相关参数的介绍：

| 参数名                          | 动态         | 类型 | 默认            | 参数值范围                  | 说明                             |
| ------------------------------- | ------------ | ---- | --------------- | --------------------------- | ------------------------------- |
| thread_pool_idle_timeout        | Yes          | uint | 60              | [1, UINT_MAX]               | worker 线程在没有需要处理的网络事件时，最多等待此时间（单位秒）后销毁 |
| thread_pool_oversubscribe       | Yes          | uint | 3               | [1,1000]                    | 在一个工作组中最多允许多少个 worker                          |
| thread_pool_size                | Yes          | uint | 当前机器 CPU 个数 | [1,1000]                    | 线程组个数                  |
| thread_pool_stall_limit         | Yes          | uint | 500             | [10, UINT_MAX]              | 每间隔此时间（单位毫秒）timer 线程负责遍历检查一次所有线程组。<br>当线程组没有 listener、高低优先级队列非空并且没有新增的 IO 网络事件时，认为线程组处于 stall 状态，timer 线程负责唤醒或创建新的 worker 线程来缓解该线程组的压力 |
| thread_pool_max_threads         | Yes          | uint | 100000          | [1,100000]                  | 线程池中所有 worker 线程的总数                               |
| thread_pool_high_prio_mode      | Yes, session | enum | transactions    | transactions\statement\none | 高优先级队列工作模式，包括三种：<li>transactions：只有一个已经开启了事务的 SQL，并且 thread_pool_high_prio_tickets 不为0，才会进入到高优先级队列中，每个连接在 thread_pool_high_prio_tickets 池被放到优先队列中后，会移到普通队列中<li>statement：所有连接都被放入高优先级队列中<li>none：与 statement 相反，所有连接都被放入低优先级队列中</li> |
| thread_pool_high_prio_tickets   | Yes, session | uint | UINT_MAX        | [0, UINT_MAX]               | transactions 工作模式下，给每个连接授予的 tickets 大小        |
| threadpool_workaround_epoll_bug | Yes          | bool | false           | true/false                  | 是否绕过 linux2.x 中的 epoll bug，该 bug 在 linux3 中修复          |

`show threadpool status` 命令展示的相关状态介绍：

| 状态名                            | 说明                                                         |
| --------------------------------- | ------------------------------------------------------------ |
| groupid                               | 线程组 ID                                                     |
| connection_count                | 线程组用户连接数                                             |
| thread_count                      | 线程组内工作线程数                                           |
| havelistener                       | 线程组当前是否存在 listener                                   |
| active_thread_count               | 线程组内活跃 worker 数量                                       |
| waiting_thread_count              | 线程组内等待中的 worker 数量（调用 wait_begin 的 worker）         |
| waiting_threads_size              | 线程组中无网络事件需要处理，进入休眠期等待被唤醒的 worker 数量（等待 thread_pool_idle_timeout 秒后自动销毁） |
| queue_size                             | 线程组普通优先级队列长度                                     |
| high_prio_queue_size              | 线程组高优先级队列长度                                       |
| get_high_prio_queue_num           | 线程组内事件从高优先级队列被取走的总次数                     |
| get_normal_queue_num              | 线程组内事件从普通优先级队列被取走的总次数                   |
| create_thread_num                  | 线程组内创建的 worker 线程总数                                 |
| wake_thread_num                    | 线程组内从 waiting_threads 队列中唤醒的 worker 总数              |
| oversubscribed_num                | 线程组内 worker 发现当前线程组处于 oversubscribed 状态，并且准备进入休眠的次数 |
| mysql_cond_timedwait_num     | 线程组内 worker 进入 waiting_threads 队列的总次数                |
| check_stall_nolistener             | 线程组被 timer 线程 check_stall 检查中发现没有 listener 的总次数   |
| check_stall_stall                     | 线程组被 timer 线程 check_stall 检查中被判定为 stall 状态的总次数  |
| max_req_latency_us                | 线程组中用户连接在队列等待的最长时间（单位毫秒）             |
| conns_timeout_killed               | 线程组中用户连接因客户端无新消息时间超过阈值（net_wait_timeout）被 killed 的总次数 |
| connections_moved_in               | 从其他线程组中迁入该线程组的连接总数                         |
| connections_moved_out             | 从该线程组迁出到其他线程组的连接总数                         |
| connections_moved_from_per_thread | 从 one-thread-per-connection 模式中迁入该线程组的连接总数      |
| connections_moved_to_per_thread     | 从该线程组中迁出到 one-thread-per-connection 模式的连接总数    |
| events_consumed                          | 线程组处理过的 events 总数                                     |
| average_wait_usecs_in_queue       | 线程组内所有 events 在队列中的平均等待时间                     |



