## 操作场景
TSF 为用户现存的 Dubbo 应用提供了两种插件，分别适合不同场景下的使用：
- 当前只是轻度使用 Dubbo，希望使用 TSF 的治理能力，可以使用**完整版插件**。完整版插件提供完整的治理能力（可能会和用户以有的治理能力冲突）。
- 当前已经使用了 Dubbo 的治理能力，只是希望注册到 TSF，可以使用**轻量级插件**。轻量级插件只提供注册和发现的能力。

>?
>- 两款插件目前均只支持 Alibaba Dubbo，版本为2.6.8（其余低版本只要和2.6.8兼容即可）。
>- 两款插件不会实时同步更新全部的 TSF 能力，具体能力支持以文档为准。

## 完整版插件接入
完整版插件通过 Dubbo filter 的机制，将 TSF 的全部能力适配至 Dubbo 上，允许用户只修改几行依赖和配置即可体验完整的治理和监控体验。

>?TSF 对治理能力的定义和 Dubbo 原生的略有区别，包括但不限于路由，负载均衡等，如果用户已经使用并依赖了 Dubbo 自身的治理能力，并且不希望行为变化，可以采用轻量级的框架接入 TSF。

### 操作步骤
#### 1. Maven 环境安装
详细操作请参考 [Maven 安装](https://cloud.tencent.com/document/product/649/20231#2.-.E5.AE.89.E8.A3.85-maven)。

#### 2. 注册中心配置
Dubbo 官网 Demo：
```xml
<dubbo:registry address="multicast://224.5.6.7:1234"/>
```

TSF Demo（**注册中心地址使用注册中心 IP 和端口替换**）：
```xml
<dubbo:registry address="tsfconsul://127.0.0.1:8500">
    <dubbo:parameter key="router" value="tsfrouter"/>
</dubbo:registry>
```
- 协议名为 tsfconsul。
- "注册中心地址:端口" 可以填写 127.0.0.1:8500。在 TSF 控制台部署时，SDK 会替换为正确的地址。

#### 3. 添加依赖
根据业务使用的对应的 TSF Dubbo 版本 SDK 如下：

3.1 在 pom 中增加插件依赖：
```xml
<dependency>
  <groupId>com.tencent.tsf</groupId>
  <artifactId>atom-extension-dubbo</artifactId>
  <!-- 修改为对应的版本号 -->
  <version>1.0.0-RELEASE</version>
</dependency>
```

3.2 在 pom 中剔除其他 brave 依赖，否则可能会造成类加载冲突。

>?由于完整版插件支持了全套的 TSF 能力、包括监控，依赖了一些开源包，这里如果在之前使用 Dubbo 试也依赖了一些开源包的话，建议删除之前的依赖。

#### 4. 打包 FatJar
和 Spring Boot 结合的时候，您可以通过 **spring-boot-maven-plugin** 构建一个包含所有依赖的 jar 包（FatJar），执行命令`mvn clean package`。详情请参考 [Dubbo Demo 工程概述](https://cloud.tencent.com/document/product/649/35577)。

如果是单纯的 Dubbo 应用，可以使用 Maven 的 FatJar 插件。

```xml
<plugins>
    <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-jar-plugin</artifactId>
        <configuration>
            <archive>
                <manifestEntries>
                    <Implementation-Version>${project.version}</Implementation-Version>
                </manifestEntries>
            </archive>
        </configuration>
    </plugin>
    <plugin>
        <artifactId>maven-assembly-plugin</artifactId>
        <configuration>
            <archive>
                <manifest>
                    <!--这里指定要运行的main类-->
                    <mainClass>com.tencent.tsf.atom.example.alibaba.dubbo.client.ConsumerApplication</mainClass>
                </manifest>
            </archive>
            <descriptorRefs>
                <descriptorRef>jar-with-dependencies</descriptorRef>
            </descriptorRefs>
        </configuration>
        <executions>
            <execution>
                <id>make-assembly</id>
                <phase>package</phase>
                <goals>
                    <goal>single</goal>
                </goals>
            </execution>
        </executions>
    </plugin>
</plugins>
```

#### 5. 使用自定义 Tag
完整版插件支持 TSF 平台的自定义 Tag 能力。

```java
// 引入 TsfContext
import com.tencent.tsf.atom.adaptor.tsf.common.TsfContext;

/**
 * 放入将自定义的 Tag 放入 Context 中
 * Context 会将该 Tag 往下传递
 * 用户可以对某个 Tag 进行查询和删除操作
 */
TsfContext.putTag("local", "yes");
```

>?Tag 会自动往下传递，如果不希望某个 Tag 继续传递可以在代码中手动删除。

#### 6. 使用自定义 Filter
Dubbo 框架中如果要实现自定义 Filter 需要 resources 目录下建立特定名称的文件夹。
官方推荐目录为 META-INF/dubbo，用户如果在此文件夹下声明自定义 Filter 则不需要任何改动。

TSF 将自定义插件目录设置为 META-INF/services，如果用户希望在 services 目录下实现自定义 filter，
则需要在 filter 的文件中显示加入 TSF 的三个插件。

>?Maven 打包时会把相同目录的文件保留一份，所以推荐用户不要使用 services，而是采用 Dubbo 目录。

```xml
// 自定义 filter
logFilter=com.alibaba.dubbo.demo.consumer.LogFilter

// Tsf 系统 filter，需要显示加入
localAddressFilter=com.tencent.tsf.atom.extensions.dubbo.filter.LocalAddressFilter
atomConsumerFilter=com.tencent.tsf.atom.extensions.dubbo.filter.AtomConsumerFilter
atomProviderFilter=com.tencent.tsf.atom.extensions.dubbo.filter.AtomProviderFilter
```

### 兼容性说明
- 提供对 TSF 平台的兼容支持。
- 部分后续新增能力暂时不支持。
- 暂不支持全局命名空间。
- 部分系统 Tag 暂不支持。
- 部分监控能力暂时不支持，具体已实际展示为准。
- 暂不支持对非 Restful 协议的 API 进行调试。
- Dubbo 应用的其他能力（如 filter 机制），可以继续使用。
- 可能会和 Dubbo 自身的治理能力冲突，推荐二选一，如果需要 Dubbo 的治理能力，可以使用轻量级插件。

### 常见错误
- 问题1：启动时报 ClassNotFound 异常。
解决方案：一般是类加载冲突，可以将 pom中DUBBO 相关的依赖删除。

- 问题2：路由治理不生效。
解决方案：查看配置中心中是否指定了 tsfrouter 作为路由器。

## 轻量级插件接入
轻量级框架为 DUBBO 应用提供服务注册中心，Dubbo 应用可通过依赖 jar 包的方式接入该项服务。下文将介绍 Dubbo 应用从接入TSF 到部署应用的操作方法及相关注意事项。

### 操作步骤
#### 1. Maven 环境安装
详细操作请参考 [Maven 安装](https://cloud.tencent.com/document/product/649/20231#2.-.E5.AE.89.E8.A3.85-maven)。

#### 2. 注册中心配置
Dubbo 官网 Demo：
```xml
<dubbo:registry address="multicast://224.5.6.7:1234"/>
```

TSF Demo（**注册中心地址使用注册中心 IP 和端口替换**）：
```xml
<dubbo:registry address="tsfconsul://注册中心地址:端口"/>
```
- 协议名为 tsfconsul。
- "注册中心地址:端口" 可以填写 127.0.0.1:8500。在 TSF 控制台部署时，SDK 会替换为正确的地址。

#### 3. 添加依赖
根据业务使用的对应的 TSF Dubbo 版本 SDK 如下：  
```xml
<dependency>
  <groupId>com.tencent.tsf</groupId>
  <artifactId>tsf-dubbo-registry</artifactId>
  <!-- 修改为对应的版本号 -->
  <version>1.1.7-alibaba-RELEASE</version>
</dependency>
```
>?目前只支持 Alibaba Dubbo。 

#### 4. 打包 FATJAR
和 Spring Boot 结合的时候，您可以通过 **spring-boot-maven-plugin** 构建一个包含所有依赖的 jar 包（FatJar），执行命令`mvn clean package`。
详情请参考 [Dubbo Demo 工程概述](https://cloud.tencent.com/document/product/649/35577)。

### 兼容性说明
- TSF 提供服务注册中心，Dubbo 应用通过依赖 jar 包的方式使用。
- TSF 支持 Dubbo 应用的 Dubbo 服务注册、Dubbo 服务调用。
- Dubbo 应用的其他能力（如 filter 机制），可以继续使用。

### 常见错误
部分包对版本有要求，如果发生**包冲突**，请尝试主动依赖以下版本：
 ```xml
 <dependency>
  <groupId>com.ecwid.consul</groupId>
  <artifactId>consul-api</artifactId>
  <version>1.4.2</version>
</dependency>
```
