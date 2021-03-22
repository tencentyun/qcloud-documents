### 探针是否会影响应用性能？

探针（Agent）工作原理是在原有业务代码中动态插入采集性能的相关代码，并且随着原有代码执行而执行。因此探针不可避免、或多或少都会产生额外的性能消耗。
在业务高峰期，为了把性能问题带来的影响降到最低，我们在探针端引入了熔断机制，即根据预设置的阈值（例如 CPU、GC 等），探针会判断当前系统资源使用情况并采取相应措施。例如，当高于阈值时，探针会停止采集工作，减少对资源的消耗。低于阈值探针会恢复采集工作。



### Java 探针采集原理是什么？

Java Agent 基于Java JDK 提供的 Instrumentation 机制，在 class 文件被加载时，调用 transform 方法，通过字节码技术，动态对 Framework、数据库、NoSQL、Web Service、组件等特定方法实施监控，从而获得方法执行时间、数据库调用时间、NoSQL 响应时间以及外部服务响应时间；并在这部分时间超过一定阈值时，抓取调用堆栈来进行进一步问题诊断。

>?Instrumentation JDK 中介绍 Java Agent 如下：Instrumentation 类为 JVM 上运行时的程序提供测量手段。大多数工具通过 Instrumenation 修改方法字节码实现收集数据目的。这部分通过 Instrumentaion 搜集数据的工具（包括 monitoring agents、profilers、coverage analyzers 和 event loggers）不会改变程序的状态和行为。



### PHP 探针采集原理是什么？

Php agent 是一个 PHP 扩展，使用 PHP 扩展技术替换 zend_execute 的函数指针，在 Zend 引擎循环执行操作码的过程中追踪获得调用各类函数的性能及错误信息。



### .NET 探针采集原理是什么？

.Net 探针通过 CLR 提供的一系列的接口函数，在 JIT 开始编译某个函数期间，通过 ILRewrite 技术替换和修改正在被编译的函数， 从而达到 .NET 探针嵌码目的，实现对 IIS .net 应用性能和其他数据的采集。



### Java 探针如何实现执行的慢 SQL 的抓取？

Java 探针通过对数据库驱动的适配，来实现对数据库数据的采集。在数据库驱动 getConnection 时采集数据库相关的信息，并通过对 statement 和 PreparedStatement 等相关接口方法的适配，实现对数据库相关操作数据的抓取。



