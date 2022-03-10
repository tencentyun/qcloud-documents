自 Java 9 发布以来，Java 已经在诸多方面进行了显著的改进和增强，并伴随着一些针对 API 的修改，这其中的许多功能都可以改善您应用的启动速度、性能和内存占用。

## Java 8 与 Java 11 之间的显著更改

### 模块系统

模块系统 [JSR 376](http://openjdk.java.net/projects/jigsaw/spec/) 自 Java 9 引入 Java，它解决了在大型应用程序中，类路径的混乱、配置复杂和难以有效的封装问题 。

模块是 Java 类和接口以及相关资源的集合。模块可以定制应用程序的运行时配置。它占用空间更小，并允许使用 [jlink](https://docs.oracle.com/en/java/javase/11/tools/jlink.html) 将应用链接到自定义运行时以进行部署。较小的占用空间在微服务架构中十分实用。JVM 在加载模块中的类时，也会比直接从类路径中加载时更快。

模块需要明确声明它导出哪些包以及它需要哪些组件，并且通过限制私有模块的反射访问来实现强封装。这种封装级别使应用更安全且更易于维护。

对于从 Java 8 过度来的开发者来说，模块并不是必选的，应用程序可以继续使用类路径在 Java 11 上运行。

您可以参见 [The State of the Module System](http://openjdk.java.net/projects/jigsaw/spec/sotms) 来了解模块系统的工作方式。

### JVM 的分析诊断工具

#### Java Flight Recorder 和 Java Mission Control

Java Flight Recorder (JFR) [JEP 328](http://openjdk.java.net/jeps/328) 从正在运行的 Java 应用程序收集诊断和分析数据。JFR 对正在运行的 Java 应用程序几乎没有影响。开发者可以使用 Java Mission Control (JMC) 和其他工具分析收集到的数据。 JFR 和 JMC 在 Java 8 中是商业功能，但它们在 Java 11 中都是开源的。

#### JVM 日志系统

Java 11 为 JVM 的所有组件提供了一个通用的日志记录系统 [JEP 158](http://openjdk.java.net/jeps/158)。这个统一的日志系统允许用户定义想要记录的组件，以及记录到什么级别。这种细粒度的日志能帮助开发者在 JVM 崩溃时进行根因分析，以及诊断生产环境中的性能问题。

#### 低开销的堆分析

Java 虚拟机工具接口 (JVMTI) 中添加了新的 API，用于对 Java 堆分配进行采样 [JEP 331](http://openjdk.java.net/jeps/331)。采样具有低开销的特性。

### 垃圾回收

Java 11 中提供了以下垃圾收集器：串行（Serial）、并行（Parallel）、G1（Garbage-First）和 Epsilon。Java 11 中的默认垃圾收集器是 G1。

- G1 的目标是在延迟和吞吐量之间取得平衡。G1 旨在避免 Full GC，但是当并发收集不能足够快地回收内存时，仍然会产生 Full GC。
- 并行GC 是 Java 8 中的默认收集器，它是一种吞吐量优先的收集器，它使用多个线程来加速垃圾收集。
- Epsilon 垃圾收集器处理分配但不回收任何内存。当堆内存耗尽时，JVM 将关闭。Epsilon 对于短期服务和无垃圾的应用程序会很有用。

除此之外，Java 11 还提供其他三种垃圾回收器：

- ZGC 是一个并发、低延迟的收集器，它试图将暂停时间保持在 10 毫秒以下。ZGC 作为 Java 11 中的一项实验性功能提供。
- Shenandoah 是一种低暂停收集器，它会与正在运行的 Java 程序同时执行，并以此来减少 GC 暂停时间。Shenandoah 是 Java 12 中的一项实验性功能，但已经移植到 Java 11。
- CMS 虽然在Java 11 中仍然可用，但自 Java 9 以来已被标记为弃用。

### 容器环境的改进

在 Java 10 之前，JVM 无法识别在容器上设置的内存和 CPU 限制。例如，在 Java 8 中，JVM 默认最大堆为底层主机物理内存的 1/4。从 Java 10 开始，JVM 使用 cgroups 来设置内存和 CPU 限制。例如，默认的最大堆是容器内存的 1/4。

此外，Java 10 中还提供了新的 JVM 参数，以便 Docker 容器用户可以细粒度地控制将用于 Java 堆的系统内存量。

>?从 jdk8u191 开始，大部分 cgroup 支持工作都被向后移植到 Java 8。

## 从 Java 8 迁移到 Java 11

在应用从 Java 8 迁移到 Java 11 的过程中，并不存在万能的解决方案，开发者可能会面临的潜在问题包括：已删除的 API、已弃用的包、内部 API 的使用、类加载器的更改以及垃圾回收器的更改。

### 尝试直接编译运行

一般来说，最简单的方法是尝试在不重新编译的情况下，直接在 Java 11 上运行使用 Java 8 编译的应用，或者先使用 Java 11 进行编译后，再运行。如果目标是让应用程序尽快启动并运行，那么这种简单的尝试通常是最好的方法。

### 其他工具

Java 11 提供了两个工具，jdeprscan 和 jdeps，可用于发现潜在问题。这些工具可以针对现有的类文件或 jar 包运行，您无需重新编译即可使用。

#### jdeprscan

[jdeprscan](https://docs.oracle.com/en/java/javase/11/tools/jdeprscan.html) 用于查找程序中是否有使用已弃用或已删除的 API 。使用已弃用的 API 并不会阻塞您的迁移，但您仍需要注意，因为他们有可能在未来的版本中被删除。

若要使用 [jdeprscan](https://docs.oracle.com/en/java/javase/11/tools/jdeprscan.html)，最简单的方法是提供一个现成的 jar 包，您可以为其指定目录或是某个类名。 使用 `--release 11` 参数可获取使用已弃用 API 的最完整列表。例如 `jdeprscan --release 11 my-application.jar`。

如果您遇到 `error: cannot find class XXX` 的错误，则需要优先检查此依赖类文件是否存在于 jar 包的类路径中。如此依赖类并非第三方依赖，则有可能是您使用了在 Java 11 中已被删除的 API。

运行 `jdeprscan --release 11 --list` 即可了解自 Java 8 后弃用的具体 API。 若要获取已删除 API 的列表，请运行 `jdeprscan --release 11 --list --for-removal` 。

#### jdeps

[jdeps](https://docs.oracle.com/en/java/javase/11/tools/jdeps.html)，是一个 Java 类依赖分析器。当此工具与 `--jdk-internals` 参数一起使用时，jdeps 会告诉您的哪个类依赖内部 API。我们也建议添加`--multi-release 11`参数来支持多版本构建的 jar 包。例如 `jdeps --jdk-internals --multi-release 11 --class-path log4j-core-2.13.0.jar my-application.jar`。

您可以继续在 Java 11 中使用内部 API，但这种方式已经不在推荐。OpenJDK wiki [Java Dependency Analysis Tool](https://wiki.openjdk.java.net/display/JDK8/Java+Dependency+Analysis+Tool) 推荐了一些常用 JDK 内部 API 的替代品。

您应该尽量避免使用来自 jdk.unsupported 中的任何 API 。尽管在替代的 API 可用之前，使用内部 API 仍将被支持，但在未来，它们有可能被彻底弃用或删除。[JEP 260](http://openjdk.java.net/jeps/260) 提供了一些替代方案。

Gradle 和 Maven 都有 jdeps 和 jdeprscan 插件。我们建议将这些工具添加到您的构建脚本中。

| 工具      | Gradle 插件                                                  | Maven 插件                                                   |
| --------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| jdeps     | [jdeps-gradle-插件](https://github.com/kordamp/jdeps-gradle-plugin) | [Apache Maven JDeps 插件](https://maven.apache.org/plugins/maven-jdeps-plugin/index.html) |
| jdeprscan | [jdeprscan-gradle-插件](https://github.com/kordamp/jdeprscan-gradle-plugin) | [Apache Maven JDeprScan 插件](https://maven.apache.org/plugins/maven-jdeprscan-plugin/index.html) |

jdeprscan 和 jdeps 无法检查使用反射访问的 API。因此，您需要在运行时检查您代码中的反射访问。

### 运行时检查

#### 检查 JVM 参数

在 Java 11 上运行之前，请检查 JVM 参数。 使用已删除的 JVM 参数将导致 JVM 崩溃退出（`Error: Could not create the Java Virtual Machine`）。如果您开启了 GC 日志，则此检查尤其重要，因为 GC 日志与 Java 8 相比发生了巨大变化。您可以使用 JaCoLine 工具来检测 JVM 参数。

#### 检查第三方依赖类库

您需要让您的所有第三方依赖类库都更新为支持 Java 11 的版本。对此，OpenJDK Quality Group 维护了一个 [Quality Outreach](https://wiki.openjdk.java.net/display/quality/Quality+Outreach) wiki 页面，其中列出了许多免费开源软件 (FOSS) 项目针对 OpenJDK 版本的测试状态。

#### 检查垃圾回收参数

并行垃圾回收器（Parallel GC）是 Java 8 中的默认 GC。自 Java 9 开始，默认的垃圾回收器更改为 G1GC。您需要检查您的垃圾回收参数是否正确设置。

#### 类加载器注意事项

- 在 Java 11 中的类加载器层次结构发生了变化。`SystemClassloader`（也称为`AppClassloader`）现在是一个内部类。强制转换成 `URLClassLoader` 会抛出  `ClassCastException` 异常。 Java 11 没有在运行时动态增加 classpath 的 API，但您仍然可以通过反射来完成获取。
- 在 Java 11 中，`BootstrapClassloader` 只加载核心模块。如果您创建一个没有父级加载器的 classloader，它可能无法找到所有平台类。在 Java 11 中，您需要传递  `ClassLoader.getPlatformClassLoader()` 作为其父级加载器。

#### 语言环境数据更改

Java 11 中语言环境数据的默认源已随 [JEP 252](http://openjdk.java.net/jeps/252) 更改为 Unicode 的通用区域资料库。这可能会对本地化产生影响。如有必要，设置系统属性 `java.locale.providers=COMPAT,SPI` 以恢复为 Java 8 语言环境行为。

### 一些常见的问题

#### Unrecognized options

如果 JVM 参数已被删除，应用程序将打印 `Unrecognized option:` 或 `Unrecognized VM option` 。无法识别的参数将导致 JVM 崩溃退出（`Error: Could not create the Java Virtual Machine`）。已弃用但未删除的选项将产生 JVM 警告（`VM Warning: Option <option> was deprecated`）。

通常情况下，您需要删除这些不能识别的 JVM 参数。GC 日志参数除外。GC 日志在 [jep 271](http://openjdk.java.net/jeps/271) 中重新实现。请参见 [oracle 官方文档](https://docs.oracle.com/en/java/javase/11/tools/java.html#GUID-BE93ABDC-999C-4CB5-A88B-1994AAAC74D5) 进行重新配置。

#### WARNING: An illegal reflective access operation has occurred

当 Java 代码使用反射访问 JDK 内部 API 时，运行时会发出非法反射访问警告。

#### java.lang.reflect.InaccessibleObjectException

此异常表明您正在试图通过 `setAccessible(true)` 的方式来反射获取一个包/模块中私有的类的字段或方法。使用 `--add-opens` 参数可让您的代码访问包/模块的非公共成员。

#### java.lang.NoClassDefFoundError

如果应用程序在 Java 8 上正常运行，但在Java 11中抛出 `java.lang.NoClassDefFoundError` 或 `java.lang.ClassNotFoundException`，那么很可能应用程序正在使用来自 Java EE 或 CORBA 模块的包。这些模块在 Java 9 中被弃用并在 Java 11 中被删除 [jep 320](https://openjdk.java.net/jeps/320)。

要解决此问题，请向您的项目添加运行时依赖。

| 移除模块 | 受影响的包             | 建议的依赖                                                   |
| -------- | ---------------------- | ------------------------------------------------------------ |
| JAX-WS   | java.xml.ws            | [JAX WS RI 运行时](https://mvnrepository.com/artifact/com.sun.xml.ws/jaxws-rt) |
| JAXB     | java.xml.bind          | [JAXB 运行时](https://mvnrepository.com/artifact/org.glassfish.jaxb/jaxb-runtime) |
| JAV      | java.activation        | [JavaBeans (TM) 激活框架](https://mvnrepository.com/artifact/javax.activation/activation) |
| 注解     | java.xml.ws.annotation | [Javax 注解 API](https://mvnrepository.com/artifact/javax.annotation/javax.annotation-api) |
| CORBA    | java.corba             | [GlassFish CORBA ORB](https://mvnrepository.com/artifact/org.glassfish.corba/glassfish-corba-orb) |
| JTA      | java.transaction       | [Java 事务 API](https://mvnrepository.com/artifact/javax.transaction/jta) |

#### UnsupportedClassVersionError

此异常意味着您正在尝试在早期的 Java 版本上运行使用更高版本的 Java 编译的代码。例如，您在 Java 11 上运行一个使用 JDK 13 编译的 jar。

| Java版本 | 类文件版本 |
| -------- | ---------- |
| 8        | 52         |
| 9        | 53         |
| 10       | 54         |
| 11       | 55         |
| 12       | 56         |
| 13       | 57         |
