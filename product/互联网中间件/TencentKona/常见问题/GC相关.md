### 如何确认当前使用哪种 GC？
请使用命令 `jmap -heap <pid>` 获取 heap 信息，查看当前 GC。

### 如何获取 GC 日志？
在启动 Java 进程时，请为 Java 命令设置如下 flag：
`-verbose:gc -XX:+PrintGCTimeStamps -XX:+PrintGCDetails -XX:+PrintGCDateStamps -Xloggc:<gclog 文件路径>`。

### 如何设置 Java 堆大小？
请使用 `-Xmx` 设置最大堆，使用 `-Xms` 设置初始化堆大小。

### 如何查看 Java 堆中对象统计情况?
请使用 `jmap -hiso:live <pid>` 命令查看 Java 堆中对象统计情况。

### Metaspace 满造成 full gc 该如何处理？
1. 首先请使用 `-XX:+TraceClassUnloading -XX:+TraceClassLoading` Java 命令选项重新运行程序，并分析输出代码中是否存在过多类加载问题。
2. 尝试增加 `-XX:MaxMetaspaceSize`。
