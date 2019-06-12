## 操作场景
TSF 为其他应用提供服务注册中心，Dubbo 应用可通过依赖 jar 包的方式接入该项服务。本文档介绍 Dubbo 应用从接入TSF 到部署应用的 操作方法及相关注意事项。

## 操作步骤
#### 1. 安装依赖
```
mvn install:install-file -Dfile=dubbo-registry-consul-1.1.4-SNAPSHOT.jar -DpomFile=dubbo-
registry-consul-1.1.4-SNAPSHOT.pom
```

#### 2. 注册中心配置
文件路径：`src/main/resources/META-INF/spring/dubbo-demo-provider.xml`
Dubbo 官网 Demo：
```
<dubbo:registry address="multicast://224.5.6.7:1234"/>
```

TSF Demo (**注册中心地址使用注册中心IP和端口替换**)：
```
<dubbo:registry address="consul://注册中心地址:端口"/>
```



#### 3. 添加依赖
```XML
<dependency> 
	<groupId>com.tencent.tsf</groupId> 
	<artifactId>dubbo-registry-consul</artifactId> 
	<!-- 修改为对应的版本号 -->
	<version>1.1.4-SNAPSHOT</version> 
</dependency> 
```

#### 4. 打包 FATJAR
您可以通过**maven-shade-plugin**构建一个包含所有依赖的 jar 包（FatJar）。执行命令`mvn clean package`。

>!您需要根据实际情况，修改以下 mainClass 标签内容。

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
详情请参考 [maven-shade-plugin 入门指南](https://www.jianshu.com/p/7a0e20b30401) 。

#### 5. 部署应用
请参考 [应用基本操作](https://cloud.tencent.com/document/product/649/13686) 。



## 关于 Dubbo 兼容的说明
- TSF 提供服务注册中心，Dubbo 应用通过依赖 jar 包的方式使用。
- TSF 支持 Dubbo 应用的部署和日志采集、展示。
-  Dubbo 应用的其他能力（如 filter 机制等），可以继续使用。
- TSF 平台提供的服务限流、鉴权、路由功能目前只支持基于 Spring Cloud 和 Service Mesh 框架开发的应用。

