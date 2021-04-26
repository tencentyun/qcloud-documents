## 服务注册发现

### 名词解释

**FatJar**：FatJar (也称作可执行 jars ) 是包含编译后的类及代码运行所需依赖 jar 的存档，可以使用 java -jar 命令运行该应用程序。

### 实现服务注册和发现

#### 1. 服务提供者
**Maven 依赖**
~~~ xml
<dependency> 
	<groupId>com.tencent.tsf</groupId> 
	<artifactId>dubbo-registry-consul</artifactId> 
	<version>1.1.0-SNAPSHOT</version> 
</dependency> 
<dependency> 
	<groupId>com.tencent.tsf</groupId> 
	<artifactId>dubbo-filter-brave</artifactId> 
	<version>1.1.0-SNAPSHOT</version> 
</dependency>
~~~

**XML 配置**
~~~ xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:dubbo="http://code.alibabatech.com/schema/dubbo"
       xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans-2.5.xsd
	http://code.alibabatech.com/schema/dubbo http://code.alibabatech.com/schema/dubbo/dubbo.xsd">

    <!-- 提供方应用信息，用于计算依赖关系 -->
    <dubbo:application name="demo-provider"/>

    <!-- 使用consul注册中心暴露发现服务地址 -->

    <dubbo:registry address="consul://127.0.0.1:8500"/>

    <!-- 用dubbo协议在20880端口暴露服务 -->
    <dubbo:protocol name="dubbo" port="20885"/>

    <!-- 声明需要暴露的服务接口 -->
    <bean id="demoService" class="com.alibaba.dubbo.demo.provider.DemoServiceImpl" />

    <!-- 和本地bean一样实现服务 -->
    <dubbo:service interface="com.alibaba.dubbo.demo.DemoService" ref="demoService"/>

    <bean id="demoService2" class="com.alibaba.dubbo.demo.provider.DemoService2Impl"/>

    <dubbo:service interface="com.alibaba.dubbo.demo.DemoService2" ref="demoService2"/>

</beans>
~~~

#### 2. 服务消费者
**Maven 依赖**
~~~
<dependency> 
<groupId>com.tencent.tsf</groupId> 
<artifactId>dubbo-registry-consul</artifactId> 
<version>1.1.0-SNAPSHOT</version> 
</dependency> 
<dependency> 
<groupId>com.tencent.tsf</groupId> 
<artifactId>dubbo-filter-brave</artifactId> 
<version>1.1.0-SNAPSHOT</version> 
</dependency>
~~~

**XML 配置**
~~~ xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:dubbo="http://code.alibabatech.com/schema/dubbo"
       xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans-2.5.xsd
	http://code.alibabatech.com/schema/dubbo http://code.alibabatech.com/schema/dubbo/dubbo.xsd">

    <!-- 消费方应用名，用于计算依赖关系，不是匹配条件，不要与提供方一样 -->
    <dubbo:application name="demo-consumer"/>

    <!-- 使用consul注册中心暴露发现服务地址 -->
    <dubbo:registry address="consul://127.0.0.1:8500"/>

    <!-- 生成远程服务代理，可以和本地bean一样使用demoService -->

    <dubbo:reference id="demoService" check="false" interface="com.alibaba.dubbo.demo.DemoService"
                     loadbalance="roundrobin"/>
    <dubbo:reference id="demoService2" check="false" interface="com.alibaba.dubbo.demo.DemoService2"
                     loadbalance="roundrobin"/>

</beans>
~~~

##  服务打包
可以通过 **maven-shade-plugin** 来构建一个包含所有依赖的 jar 包（FatJar）。执行命令 `mvn clean package`。

~~~ xml
<build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-shade-plugin</artifactId>
                <version>3.1.0</version>
                <configuration>
                    <createDependencyReducedPom>false</createDependencyReducedPom>
                </configuration>
                <executions>
                    <execution>
                        <phase>package</phase>
                        <goals>
                            <goal>shade</goal>
                        </goals>
                        <configuration>
                            <filters>
                                <filter>
                                    <artifact>*:*</artifact>
                                    <excludes>
                                        <exclude>META-INF/*.SF</exclude>
                                        <exclude>META-INF/*.DSA</exclude>
                                        <exclude>META-INF/*.RSA</exclude>
                                    </excludes>
                                </filter>
                            </filters>
                            <transformers>
                                <transformer implementation="org.apache.maven.plugins.shade.resource.ManifestResourceTransformer">
                                    <mainClass>com.alibaba.dubbo.demo.provider.Provider</mainClass>
                                </transformer>
                                <transformer implementation="org.apache.maven.plugins.shade.resource.AppendingTransformer">
                                    <resource>META-INF/spring.schemas</resource>
                                </transformer>
                                <transformer implementation="org.apache.maven.plugins.shade.resource.AppendingTransformer">
                                    <resource>META-INF/spring.handlers</resource>
                                </transformer>
                            </transformers>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
~~~

参考链接：[maven-shade-plugin 入门指南](https://www.jianshu.com/p/7a0e20b30401) 。

##  部署应用
参考 《TSF 操作手册》中 [应用部署](https://cloud.tencent.com/document/product/649/13686) 。
