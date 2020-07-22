SCF provides Java8 runtime environment for Java runtime environment.

Because the Java language needs to be compiled before it can be run in JVM, its use method in SCF is different with such scripting languages as Python and Node.js. Here are the restrictions:

* Code upload is not supported: For the Java language, only developed, compiled and packaged zip/jar packages can be uploaded. SCF environment does not provide Java compiling capability.
* Online editing is not supported: Online code editing is not supported as code cannot be uploaded. For Java runtime function, you can only see the methods of "uploading again via page" or "COS code submitting" on the code page.

## Code Form

The code form of SCF developed with Java is generally as follows:
```java
package example;

public class Hello {
    public String mainHandler(String name) {
        System.out.println("Hello world!");
        return String.format("Hello %s.", name);
    }
}
```

## Execution Method

Since Java involves the concept of package, its execution method is different from other languages and requires package information. The corresponding execution method in the code example is `example.Hello::mainHandle`, where `example` is identified as Java package, `Hello` is identified as class, and `mainHandle` is identified as class method.

## Deployment Package Upload

You can create a zip or jar package via two methods: [Create zip Deployment Package Using Gradle](https://cloud.tencent.com/document/product/583/12216) and [Create jar Deployment Package Using Maven](https://cloud.tencent.com/document/product/583/12217). After the package is created, you can directly upload it (less than 10 MB) via the console, or upload the deployment package to COS bucket and specify the Bucket and Object of the deployment package on SCF console to complete the deployment package submission.

## Input Parameters and Returned Values

In the code example, the input parameters used by mainHandler contains two classes (String and Context), while returned values are String classes. The first input class identifies the input event, and the second one identifies the runtime information of the function. Event input and function return support Java base classes and POJO classes. The function runtime is of class `com.qcloud.scf.runtime.Context` and its associated library file can be downloaded [here](https://search.maven.org/artifact/com.tencentcloudapi/scf-java-events/0.0.1/jar).

* Supported event input parameters and return parameter classes
	* Java base classes, including eight basic classes (byte, int, short, long, float, double, char, and boolen), wrapper classes and String class.
	* POJO (Plain Old Java Object) classes. You should use variable POJOs and public getters and setters to implement corresponding classes in your code.

* Context input parameter
	* To use Context, you need to use the import package `com.qcloud.scf.runtime.Context;` in the code and bring it into the jar package for packaging.
	* If you do not use this object, you can ignore it in the function input parameter, which can be written as `public String mainHandler(String name)`.


## Log

You can use the following statement in the program to complete the log output:

```java
System.out.println("Hello world!");
```

The output can be found in the `log` of the function log.





