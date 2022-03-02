本文介绍如何使用 Java 连接和操作图数据库 KonisGraph。以 [Gremlin-console tutorials](https://tinkerpop.apache.org/docs/3.5.1/tutorials/getting-started/#_the_first_five_minutes) 中的人和软件的关系图为示例。
![enter image description here](https://main.qcloudimg.com/raw/51a52aabf2b24289aa61f713a8cd1eb4.png)
如图所示，整个图包含2类点 person 和 software，2类边 knows 和 created，和几类属性 id、name、age、lang、weight。

## 环境准备
1. 安装 JDK 8.0，并配置 Java 环境。
2. 安装 maven，参考 [Installing Apaceh Maven](https://maven.apache.org/install.html)。
3. 获取图数据库的连接参数。在 [控制台](https://console.cloud.tencent.com/konisgraph) 实例详情页中可以查看实例的 VIP 和 PORT，即内网地址和 Gremlin 端口。

## 示例代码
1. 创建 graph_demo 目录。
2. 创建 pom.xml 文件，并写入如下内容：
```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.tencent.konisgraph</groupId>
    <artifactId>tutorial</artifactId>
    <version>0.1</version>

    <name>Getting started with TinkerGraph</name>

    <packaging>jar</packaging>
    <properties>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <maven.compiler.source>8</maven.compiler.source>
        <maven.compiler.target>8</maven.compiler.target>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.apache.tinkerpop</groupId>
            <artifactId>gremlin-core</artifactId>
            <version>3.5.1</version>
        </dependency>
        <dependency>
            <groupId>org.apache.tinkerpop</groupId>
            <artifactId>gremlin-driver</artifactId>
            <version>3.5.1</version>
        </dependency>
        <dependency>
            <groupId>org.slf4j</groupId>
            <artifactId>slf4j-log4j12</artifactId>
            <version>1.7.25</version>
        </dependency>
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <version>4.12</version>
            <scope>test</scope>
        </dependency>
    </dependencies>
    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <configuration>
                    <source>8</source>
                    <target>8</target>
                </configuration>
                <version>3.1</version>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-assembly-plugin</artifactId>
                <configuration>
                    <archive>
                        <manifest>
                            <mainClass>com.tencent.konisgraph.App</mainClass>
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
    </build>
</project>
```
3. 创建目录并新建文件。
```sh
mkdir -p src/main/java/com/tencent/konisgraph/
touch src/main/java/com/tencent/konisgraph/App.java
```
4. 编写测试程序。
```java
package com.tencent.konisgraph;

import java.util.concurrent.ExecutionException;

import org.apache.tinkerpop.gremlin.driver.Client;
import org.apache.tinkerpop.gremlin.driver.Cluster;
import org.apache.tinkerpop.gremlin.driver.MessageSerializer;
import org.apache.tinkerpop.gremlin.driver.remote.DriverRemoteConnection;
import org.apache.tinkerpop.gremlin.driver.ser.GryoMessageSerializerV3d0;
import org.apache.tinkerpop.gremlin.process.traversal.dsl.graph.GraphTraversalSource;

import static org.apache.tinkerpop.gremlin.process.traversal.dsl.graph.__.*;
import static org.apache.tinkerpop.gremlin.process.traversal.AnonymousTraversalSource.traversal;

public class App {

    public static void main(String[] args) {
        // 设置正确的 serializer
        MessageSerializer serializer = new GryoMessageSerializerV3d0();
        Cluster cluster = Cluster.build().
            addContactPoint("KONISGRAPH_VIP").port(KONISGRAPH_PORT).
            credentials("your username", "your password").
            serializer(serializer).
            create();
        Client client = cluster.connect();
       
        // 添加属性、点、边等元数据。submit 方法需要捕获异常处理
        try {
            client.submit("s.addP('id', 'T_LONG', '0')").all().get();
            client.submit("s.addP('name', 'T_STRING', '')").all().get();
            client.submit("s.addP('age', 'T_INT', '0')").all().get();
            client.submit("s.addP('lang', 'T_STRING', '')").all().get();
            client.submit("s.addP('weight', 'T_DOUBLE', '0.0')").all().get();
            client.submit("s.addV('person', 'id', ['name', 'age'])").all().get();
            client.submit("s.addV('software', 'id', ['name', 'lang'])").all().get();
            client.submit("s.addE('knows', 'person', 'person', ['weight'])").all().get();
            client.submit("s.addE('created', 'person', 'software', ['weight'])").all().get();
        } catch (InterruptedException | ExecutionException e) {
            e.printStackTrace();
        }

        // 创建一个 GraphTraversalSource 实例用于查询数据
        GraphTraversalSource g = traversal().withRemote(DriverRemoteConnection.using(cluster));

        // property 必须分开写才能成功
        g.addV("person").property("id", 1).property("name", "marko").property("age", 29).iterate();

        g.addV("person").property("id", 2).property("name", "vadas").property("age", 27).
            addV("person").property("id", 4).property("name", "josh").property("age", 32).
            addV("person").property("id", 6).property("name", "peter").property("age", 35).iterate();
        
        g.addV("software").property("id", 3).property("name", "lop").property("lang", "java").
            addV("software").property("id", 5).property("name", "ripple").property("lang", "java").iterate();

        g.V(1).addE("knows").to(V(2)).iterate();
        g.V(1).addE("knows").to(V(4)).iterate();
        g.V(1).addE("created").to(V(3)).property("weight", 0.4).iterate();
        g.V(6).addE("created").to(V(3)).property("weight", 0.2).iterate();
        g.V(4).addE("created").to(V(3)).property("weight", 0.4).iterate();
        g.V(4).addE("created").to(V(5)).property("weight", 1.0).iterate();

        System.out.println("marko: " + g.V().hasLabel("person").has("name", "marko").valueMap("name", "age").toList());

        System.out.println("who marko knows: " + g.V().hasLabel("person").has("name", "marko").out("knows").valueMap("name", "age").toList());

        System.out.println("who creates software lop: " + g.V().hasLabel("software").has("name", "lop").in("created").valueMap("name").toList());
        
        cluster.close();
    }
}
```

## 编译运行
```sh
mvn package
java -jar target/tutorial-0.1-jar-with-dependencies.jar
```
