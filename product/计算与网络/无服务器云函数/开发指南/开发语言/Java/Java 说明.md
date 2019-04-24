SCF 云函数在 Java 运行时环境中提供了 Java8 的运行环境。

Java 语言由于需要编译后才可以在 JVM 虚拟中运行，因此在 SCF 中的使用方式，和 Python、Node.js 这类脚本型语言不太一样，有如下限制：

* 不支持上传代码：使用 Java 语言，仅支持上传已经开发完成，编译打包后的 zip/jar 包。SCF 云函数环境不提供 Java 的编译能力。
* 不支持在线编辑：不能上传代码，所以不支持在线编辑代码。Java 运行时的函数，在代码页面仅能看到再次通过页面上传或 COS 提交代码的方法。

## 代码形态

Java 开发的 SCF 云函数的代码形态一般如下所示：
```java
package example;

public class Hello {
    public String mainHandler(String name) {
        System.out.println("Hello world!");
        return String.format("Hello %s.", name);
    }
}
```

## 执行方法

由于 Java 包含有包的概念，因此执行方法和其他语言有所不同，需要带有包信息。代码例子中对应的执行方法为 `example.Hello::mainHandler`，此处 `example` 标识为 Java package，`Hello` 标识为类，`mainHandler` 标识为类方法。

## 部署包上传

可以通过 [使用 Gradle 创建 zip 部署包](https://cloud.tencent.com/document/product/583/12216) 和 [使用 Maven 创建 jar 部署包](https://cloud.tencent.com/document/product/583/12217) 这两种方式来创建zip或jar包。创建完成后，可通过控制台页面直接上传包（小于 10 M），或通过把部署包上传至 COS Bucket 后，在 SCF 控制台上通过指定部署包的 Bucket 和 Object 信息，完成部署包提交。

## 入参和返回

代码例子中，mainHandler 所使用的入参包含了两个类型，String 和 Context，返回使用了 String 类型。其中入参的前一类型标识事件入参，后一类型标识函数运行时信息。事件入参和函数返回目前支持的类型包括 Java 基础类型和 POJO 类型；函数运行时目前为 `com.qcloud.scf.runtime.Context` 类型，其相关库文件可从 [此处](https://mc.qcloudimg.com/static/archive/12ec94d2852a4cfbdb066e0b99b39070/com.qcloud.scf.runtime.Context.1.0.jar.zip) 下载。

* 事件入参及返回参数类型支持
	* Java 基础类型，包括 byte，int，short，long，float，double，char，boolen 这八种基本类型和包装类，也包含 String 类型。
	* POJO 类型，Plain Old Java Object，您应使用可变 POJO 及公有 getter 和 setter，在代码中提供相应类型的实现。

* Context 入参
	* 使用 Context 需要在代码中使用 `com.qcloud.scf.runtime.Context;` 引入包，并在打包时带入 jar 包。
	* 如不使用此对象，可在函数入参中忽略，可写为`public String mainHandler(String name)`


## 日志

您可以在程序中使用如下语句来完成日志输出：

```java
System.out.println("Hello world!");
```

输出内容您可以在函数日志中的 `log` 位置查看。

## 测试

通过控制台界面的测试按钮，可以打开测试界面，实时触发云函数并查看运行结果。针对代码例子，由于入参是 `String name` 字符串类型，因此在使用调试界面进行触发运行时，需要输入的为字符串内容，例如 `"Tencent Cloud"`。

如果修改了示例代码，期望接收较复杂格式的 JSON 入参，可使用 [POJO 类型参数](https://cloud.tencent.com/document/product/583/12215)，在代码中定义对应的数据结构。SCF 平台在传递对应 JSON 参数到入口函数时，会转换为对象实例，可由代码直接使用。



