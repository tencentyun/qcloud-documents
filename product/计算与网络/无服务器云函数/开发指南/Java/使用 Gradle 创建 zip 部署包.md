
本节内容提供了通过使用 Gradle 工具来创建 Java 类型云函数部署包的方式。创建好的 zip 包符合以下规则，即可以由云函数执行环境所识别和调用。

* 编译生成的包、类文件、资源文件位于 zip 包的根目录。
* 依赖所需的 jar 包，位于 /lib 目录内。

## 环境准备
确保您已经安装 Java 和 Gradle。Java 请安装 JDK8，您可以使用 OpenJDK（Linux）或通过 `www.java.com` 下载安装合适您系统的 JDK。

### Gradle 安装
具体安装方法可见 `https://gradle.org/install/`，以下说明手工安装过程：
1. 下载 Gradle 的 [二进制包](https://services.gradle.org/distributions/gradle-4.1-bin.zip) 或 [带文档和源码的完整包](https://services.gradle.org/distributions/gradle-4.1-all.zip)。
2. 解压包到自己所期望的目录。例如，Windows 下的 `C:\Gradle`  目录或 Linux 下的 `/opt/gradle/gradle-4.1` 目录。
3. 将解压目录下 bin 目录的路径添加到系统 PATH 环境变量中，请对应操作系统执行以下步骤：
 - Linux：通过 `export PATH=$PATH:/opt/gradle/gradle-4.1/bin` 完成添加。
 - Windows：通过 `计算机>右键>属性>高级系统设置>高级>环境变量` 进入到环境变量设置页面，选择 `Path` 变量编辑，在变量值最后添加`;C:\Gradle\bin;`。
4. 在命令行执行以下命令，查看 Gradle 是否正确安装。
```
gradle -v
```
输出结果如下，则证明 Gradle 已正确安装。如有问题，请查询 Gradle 的 [官方文档](https://gradle.org/docs/)。
```
	------------------------------------------------------------
	Gradle 4.1
	------------------------------------------------------------
	Build time:   2017-08-07 14:38:48 UTC
	Revision:     941559e020f6c357ebb08d5c67acdb858a3defc2
	Groovy:       2.4.11
	Ant:          Apache Ant(TM) version 1.9.6 compiled on June 29 2015
	JVM:          1.8.0_144 (Oracle Corporation 25.144-b01)
	OS:           Windows 7 6.1 amd64
```

## 代码准备

### 准备代码文件
1. 在选定的位置创建项目文件夹，例如 `scf_example`。
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
在项目文件夹根目录下创建 `build.gradle` 文件并输入如下内容：
```
apply plugin: 'java'

task buildZip(type: Zip) {
    from compileJava
    from processResources              
    into('lib') {
        from configurations.runtime
    }           
}

build.dependsOn buildZip
```

#### 使用 Maven Central 库处理包依赖
如果需要引用 Maven Central 的外部包，可根据需要添加依赖，`build.gradle` 文件内容如下：
```
apply plugin: 'java'

repositories {
    mavenCentral()
}

dependencies {
    compile (
        'com.tencentcloudapi:scf-java-events:0.0.2'
    )
}

task buildZip(type: Zip) {
    from compileJava
    from processResources              
    into('lib') {
        from configurations.runtime
    }           
}

build.dependsOn buildZip
```

通过 repositories 指明依赖库来源为 mavenCentral 后，在编译过程中，Gradle 会自行从 Maven Central 拉取依赖项，也就是 dependencies 中指明的 `com.tencentcloudapi:scf-java-events:0.0.2` 包。

#### 使用本地 Jar 包库处理包依赖
如果已经下载 Jar 包到本地，可以使用本地库处理包依赖。在这种情况下，请在项目文件夹根目录下创建 `jars` 目录，并将下载好的依赖 Jar 包放置到此目录下。`build.gradle` 文件内容如下：
```
apply plugin: 'java'

dependencies {
    compile fileTree(dir: 'jars', include: '*.jar')
}

task buildZip(type: Zip) {
    from compileJava
    from processResources              
    into('lib') {
        from configurations.runtime
    }
}

build.dependsOn buildZip
```
通过 dependencies 指明搜索目录为 jars 目录下的 `*.jar` 文件，依赖会在编译时自动进行搜索。

## 编译打包
在项目文件夹根目录下执行命令 `gradle build`，应有编译输出类似如下：
```
Starting a Gradle Daemon (subsequent builds will be faster)

BUILD SUCCESSFUL in 5s
3 actionable tasks: 3 executed
```
如果显示编译失败，请根据输出的编译错误信息调整代码。
编译后的 zip 包位于项目文件夹内的 `/build/distributions` 目录内，并以项目文件夹名命名为 `scf_example.zip`。

## 函数使用
编译打包后生成的 zip 包，可在创建或修改函数时，根据包大小，选择使用页面上传（小于10M），或将包上传 COS Bucket 后再通过 COS 上传的方式更新到函数内。
