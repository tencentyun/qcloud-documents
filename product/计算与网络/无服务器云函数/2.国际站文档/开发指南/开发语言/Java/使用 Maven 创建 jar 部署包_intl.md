Create jar Deployment Package Using Maven
===

This section describes how to create a jar deployment package using the Maven tool for Java SCF.

## Environment Preparation
Make sure Java and Maven have been installed. Install JDK8. You can use OpenJDK (Linux) or download and install the JDK appropriate for your system via www.java.com.

### Maven installation

For the specific installation method, please see [https://maven.apache.org/install.html](https://maven.apache.org/install.html). Here we describe the manual installation process:
1. Download [zip Package](http://mirror.bit.edu.cn/apache/maven/maven-3/3.5.2/binaries/apache-maven-3.5.2-bin.zip) or [tar.gz Package](http://mirror.bit.edu.cn/apache/maven/maven-3/3.5.2/binaries/apache-maven-3.5.2-bin.tar.gz) of Maven.
2. Decompress the package to your desired directory, for example, `C:\Maven` (Windows) or `/opt/mvn/apache-maven-3.5.0` (Linux).
3. Add the path of the bin directory under the decompression directory to the system PATH environment variable. For Linux, add it using `export PATH=$PATH:/opt/mvn/apache-maven-3.5.0/bin`. For Windows, `right-click **Computer**, and select **Attribute** -> **Advanced System Settings** -> **Advanced** -> **Environment Variables**` to enter the environment variable settings page, and then select the `Path` variable and add `;C:\Maven\bin;` at the end of the variable value.
4. Run `mvn -v` in the command line. If the following content shows, it indicates that Maven has been installed successfully. For any questions, please see [Installing Apache Maven](https://maven.apache.org/install.html).
	```
	Apache Maven 3.5.0 (ff8f5e7444045639af65f6095c62210b5713f426; 2017-04-04T03:39:06+08:00)
	Maven home: C:\Program Files\Java\apache-maven-3.5.0\bin\..
	Java version: 1.8.0_144, vendor: Oracle Corporation
	Java home: C:\Program Files\Java\jdk1.8.0_144\jre
	Default locale: zh_CN, platform encoding: GBK
	OS name: "windows 7", version: "6.1", arch: "amd64", family: "windows"
	```

## Code Preparation

### Prepare code file

Create a project folder in the selected location, for example `scf_example`. Under the root directory of project folder, create the directory `src/main/java/` for storing the package. Create the `example` package directory under the created directory, and create the `Hello.java` file under the package directory. The final directory structure is as follows:
`scf_example/src/main/java/example/Hello.java`

Enter the code content in the `Hello.java` file:

```java
package example;

public class Hello {
    public String mainHandler(String name, Context context) {
        System.out.println("Hello world!");
        return String.format("Hello %s.", name);
    }
}
```
### Prepare compilation file

Create `pom.xml` file under the root directory of project folder and enter the following:

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

#### Process package dependency with Maven Central library

If you need to reference external package of Maven Central, you can add dependency as needed. The content of the `pom.xml` file is written as follows:
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
      <version>0.0.1</version>
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

## Compiling and Packaging

Run the command `mvn package` under the root directory of the project folder. The compiling output should be similar to the following:
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
If compiling fails, adjust the code according to the output compiling error message.

The compiled jar package is located under the `target` directory of the project folder and is named as `java-example-1.0-SNAPSHOT.jar` based on the fields artifactId and version of pom.xml.

## Function Use

For the generated jar package after compiling and packaging, you can choose the upload method based on the package size when creating or modifying the function. If the package is less than 10 MB, you can use page upload, otherwise you can upload the package to COS Bucket and then update it into the function via COS upload.


