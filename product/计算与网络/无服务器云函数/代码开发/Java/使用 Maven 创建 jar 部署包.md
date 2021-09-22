
本节内容提供了通过使用 Maven 工具来创建 Java 类型云函数部署 jar 包的方式。

## 环境准备
确保您已经安装 Java 和 Maven。Java 请安装 JDK8，您可以使用 OpenJDK（Linux）或通过 `www.java.com` 下载安装合适您系统的 JDK。

### Maven 安装

具体安装方法可见 `https://maven.apache.org/install.html`，以下说明手工安装过程：
1. 下载 Maven 的 [zip 包](http://mirror.bit.edu.cn/apache/maven/maven-3/3.5.4/binaries/apache-maven-3.5.4-bin.zip) 或 [tar.gz 包](http://mirror.bit.edu.cn/apache/maven/maven-3/3.5.4/binaries/apache-maven-3.5.4-bin.tar.gz) 。
2. 解压包到自己所期望的目录。例如，Windows 下的 `C:\Maven` 目录或 Linux 下的 `/opt/mvn/apache-maven-3.5.0` 目录。
3. 将解压目录下 bin 目录的路径添加到系统 PATH 环境变量中，请对应操作系统执行以下步骤：
 - Linux：通过 `export PATH=$PATH:/opt/mvn/apache-maven-3.5.0/bin` 完成添加。
 - Windows：通过 `计算机>右键>属性>高级系统设置>高级>环境变量` 进入到环境变量设置页面，选择 `Path` 变量编辑，在变量值最后添加 `;C:\Maven\bin;`。
4. 在命令行下执行以下命令，查看 Maven 是否正确安装。
```
mvn -v
```
输出结果如下，则证明 Maven 已正确安装。如有问题，请查询 Maven 的 [官方文档](https://maven.apache.org/install.html)。
```
Apache Maven 3.5.0 (ff8f5e7444045639af65f6095c62210b5713f426; 2017-04-04T03:39:06+08:00)
Maven home: C:\Program Files\Java\apache-maven-3.5.0\bin\..
Java version: 1.8.0_144, vendor: Oracle Corporation
Java home: C:\Program Files\Java\jdk1.8.0_144\jre
Default locale: zh_CN, platform encoding: GBK
OS name: "windows 7", version: "6.1", arch: "amd64", family: "windows"
```

## 代码准备

### 准备代码文件
1. 在选定的位置创建项目文件夹，例如 `scf_example` 。
2. 在项目文件夹根目录，依次创建目录 `src/main/java/` 作为包的存放目录。
3. 在创建好的目录下再创建 `example` 包目录，并在包目录内创建 `Hello.java` 文件。最终形成如下目录结构：
```
scf_example/src/main/java/example/Hello.java
```
4. 在 `Hello.java` 文件内输入如下代码内容：
```java
package example;
public class Hello {
    public String mainHandler(String name, Context context) {
        System.out.println("Hello world!");
        return String.format("Hello %s.", name);
    }
}
```

### 准备编译文件
在项目文件夹根目录下创建 `pom.xml` 文件并输入如下内容：
```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  <modelVersion>4.0.0</modelVersion>

  <groupId>examples</groupId>
  <artifactId>java-example</artifactId>
  <packaging>jar</packaging>
  <version>1.0-SNAPSHOT</version>
  <name>java-example</name>

  <build>
    <plugins>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-shade-plugin</artifactId>
        <version>2.3</version>
        <configuration>
          <createDependencyReducedPom>false</createDependencyReducedPom>
        </configuration>
        <executions>
          <execution>
            <phase>package</phase>
            <goals>
              <goal>shade</goal>
            </goals>
          </execution>
        </executions>
      </plugin>
    </plugins>
  </build>
</project>
```

#### 使用 Maven Central 库处理包依赖
如果需要引用 Maven Central 的外部包，可以根据需要添加依赖，`pom.xml` 文件内容如下，添加依赖请关注 `<dependencies>` 部分。
```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  <modelVersion>4.0.0</modelVersion>

  <groupId>examples</groupId>
  <artifactId>java-example</artifactId>
  <packaging>jar</packaging>
  <version>1.0-SNAPSHOT</version>
  <name>java-example</name>
  
  <dependencies>
    <dependency>
      <groupId>com.tencentcloudapi</groupId>
      <artifactId>scf-java-events</artifactId>
      <version>0.0.2</version>
    </dependency>
  </dependencies>

  <build>
    <plugins>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-shade-plugin</artifactId>
        <version>2.3</version>
        <configuration>
          <createDependencyReducedPom>false</createDependencyReducedPom>
        </configuration>
        <executions>
          <execution>
            <phase>package</phase>
            <goals>
              <goal>shade</goal>
            </goals>
          </execution>
        </executions>
      </plugin>
    </plugins>
  </build>
</project>
```

## 编译打包
在项目文件夹根目录下执行命令 `mvn package`，应有编译输出类似如下：
```
[INFO] Scanning for projects...
[INFO]
[INFO] ------------------------------------------------------------------------
[INFO] Building java-example 1.0-SNAPSHOT
[INFO] ------------------------------------------------------------------------
[INFO]
...
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 1.785 s
[INFO] Finished at: 2017-08-25T10:53:54+08:00
[INFO] Final Memory: 17M/214M
[INFO] ------------------------------------------------------------------------
```
如果显示编译失败，请根据输出的编译错误信息调整代码。
编译后的 jar 包位于项目文件夹内的 `target` 目录内，并根据 pom.xml 内的 artifactId、version 字段命名为 `java-example-1.0-SNAPSHOT.jar`。

## 函数使用
编译打包后生成的 jar 包，可在创建或修改函数时，根据包大小，选择使用页面上传（小于10M），或将包上传 COS Bucket 后再通过 COS 上传的方式更新到函数内。

