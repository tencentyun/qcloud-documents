## GC 线程调度优化 Optimized Work Stealing Threads
### 开启方式
默认开启。可在启动参数中添加 `-XX:-UseOWSTTaskTerminator` 关闭。

### 原理
GC 并行线程通过 Work Stealing 进行负载均衡，减少 GC 停顿时间。原有 Work Stealing 算法中所有空闲 GC 线程都会频繁尝试 work stealing，造成 CPU 资源浪费，新算法采用一个 master 线程监控是否进行 work stealing 并在适当时机唤醒其它空闲 GC 线程，极大减少 CPU 资源浪费和进程间的 CPU 资源竞争。OWST 在 OpenJDK 社区版本12以后支持，大数据 Hibench 测试有最多30%的性能提升，平均提升8%。

## CMS FullGC 并行化
### 开启方式
在启动参数中设置 `-XX:+CMSParallelFullGC`参数为 false。

### 原理
官方默认是 CMS FullGC 是单线程全停机的 gc，停机时间很长。20GB的堆使用 CMS 算法时，一旦触发 FullGC，停机时间可能在50s左右。EMR-TianQiong-V1.0.0 版本发布的 FullGC 并行化功能，可以部分阶段多线程执行 gc，最多可降低 FullGC 的停机时间40%左右，改善系统最坏情况下的性能。

## 物理内存释放优化
### 开启方式
- 在启动参数中添加 `-XX:+FreeHeapPhysicalMemory`，针对 PS、CMS 和 G1 算法，在触发 FullGC（G1 算法触发 concurrent cycle 和 FullGC）时，JVM 做完内存碎片整理后，会通过调用 madvise 释放不包含对象的 old 区的后半部分虚拟地址空间对应的物理内存。
- 在上述参数开启的情况下，如果在启动参数中指定 `-XX:PeriodicGCInterval=x`，则 JVM 会每隔5min，自动判断当前进程的 load，如果连续3次低于该进程 load 的 P99 的话，则会触发一次 FullGC 进行物理内存回收，PeriodicGCInterval（单位 ms）时间间隔内最多只会触发一次 FullGC，默认 PeriodicGCInterval=0。
- 上面两个参数对应的功能默认都是关闭的。

## Default CDS Archive
Tencent Kona 默认打开 Default CDS Archive 功能，用户可以通过以下启动标志关闭该功能：
```
java -Xshare:off
```

## 支持国密算法
### 使用方式
国密算法在 KonaJDK 中的 API 是符合 JCE CipherAPI 的标准的。用户只要使用 KonaJDK 即可无缝使用国密算法。

### 原理
- 国密算法是国家密码局制定标准的一系列算法。其中包括了对称加密算法、椭圆曲线非对称加密算法和杂凑算法。具体包括 SM1、SM2、SM3 等。
- 为提高 Konajdk 的易用性，降低现有业务转换密码算法为国密算法的门槛，KonaJDK 与 TencentSM 合作将国密算法引入到 jdk 库中进行支持。KonaJDK 中国密算法的使用遵循 JCE 标准，定义了 SMCSProvider 来提供国密算法 API。

## JFR 使用
### Java Flight Recorder
可收集 Java 应用在运行过程中的诊断及性能数据，后端口来自 OpenJDK11。如果使用的是默认的配置，理论上 JFR 开销是小于2%的，因此必要情况下可用在现网收集数据。

### 简要用法
#### 启动 JFR
```
//默认关闭，需要使用时，在应用启动命令中带上 -XX:+FlightRecorder 参数开启 JFR
$JAVA_HOME/bin/java -XX:+FlightRecorder YourApplication
```
#### 开始记录 JFR
```
//当需要开始记录时先获取 YourApplication 的 pid，使用 jcmd pid JFR.start 开始记录，当 java 应用正常停止时会自动将运行数据记录在 filename 参数指定的文件中
$JAVA_HOME/bin/jcmd <your_pid> JFR.start name=anyname_for_dump filename=anyname_for_your_record.jfr
 
可用参数如下:
    name=name
    指定记录的名称
    
    defaultrecording=true/false
    是否在初始化时启动记 录事件，默认为 false，对于反应分析，应设置为 true
    
    settings=path
    JFR 配置文件的路径
    
    delay=time
    开始记录前的延时
    
    duration=time
    记录持续时间
    
    filename=path
    保存记录事件的文件路径
    
    compress=true/false
    是否使用 gzip 压缩记录数据，默认为 false
    
    maxage=time
    环形缓存中保存记录的数据的最长时间
     
    maxsize=size
    环形缓存占用的最大空间
```

#### 导出记录

```
//如果JFR.start后，打算导出截止目前为止的记录就用jcmd JFR.dump 可以通过filename指定导出数据的位置，注意name要与JFR.start中指定的name一致
$JAVA_HOME/bin/jcmd <your_pid> JFR.dump name=anyname_for_your_record filename=anyname_for_dump_record.jfr
 
 
可用参数如下：
    name=name
    指定导出数据的事件记录名
    
    recording=n
    JFR 事件记录号
    
    filename=path
    导出文件的路径
```

#### 停止记录

```
//停止记录(注意这个停止如果没有带后面的 name 和 filename 参数，将不会执行 dump 直接停止记录)
$JAVA_HOME/bin/jcmd <your_pid> JFR.stop name=anyname_for_your_record filename=anyname_for_dump_record.jfr
 
可用参数如下：
    name=name
    需要停止的事件记录名
    
    recording=n
    需要停止的事件记录号
    
    discard=Boolean
    如果为 true，舍弃之前保存的数据
    
    filename=path
    保存数据的文件路径
```

#### 查看当前所有事件记录

```
//一个进程下可能有多个 JFR 事件记录在运行，可以通过下面的命令查看当前所有的事件记录：
$JAVA_HOME/bin/jcmd <your_pid> JFR.check 
```

 
