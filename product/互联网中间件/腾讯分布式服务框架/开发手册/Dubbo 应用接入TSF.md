## 1. 安装依赖

[下载依赖 >>](https://main.qcloudimg.com/raw/d075de11daa5d1427346e19880cd5492/dubbo-registry-consul-1.1.4-SNAPSHOT.zip)

```
mvn install:install-file -Dfile=dubbo-registry-consul-1.1.4-SNAPSHOT.jar -DpomFile=dubbo-
registry-consul-1.1.4-SNAPSHOT.pom
```



## 2. 注册中心配置

文件路径： `src/main/resources/META-INF/spring/dubbo-demo-provider.xml`
Dubbo 官网 demo：

```
<dubbo:registry address="multicast://224.5.6.7:1234"/>
```

TSF demo (**注册中心地址使用注册中心 IP 和端口替换**)：

```
<dubbo:registry address="consul://注册中心地址:端口"/>
```



## 3. 添加依赖

```XML
<dependency> 
	<groupId>com.tencent.tsf</groupId> 
	<artifactId>dubbo-registry-consul</artifactId> 
	<!-- 修改为对应的版本号 -->
	<version>1.1.4-SNAPSHOT</version> 
</dependency> 
```



## 4. 打包 FATJAR

您可以通过 **maven-shade-plugin** 来构建一个包含所有依赖的 jar 包（FatJar）。执行命令 `mvn clean package`。

>**注意：**您需要根据实际情况，修改以下 mainClass 标签内容。

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

参考文档：[maven-shade-plugin 入门指南](https://www.jianshu.com/p/7a0e20b30401) 。

##  部署应用
请参考 [应用基本操作](https://cloud.tencent.com/document/product/649/13686) 。
