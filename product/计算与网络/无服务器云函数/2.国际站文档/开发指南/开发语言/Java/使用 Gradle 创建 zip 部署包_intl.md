Create a zip Deployment Package using Gradle
===

This section describes how to create a Java SCF deployment package using the Gradle tool. The created zip package conforming to the following rules can be identified and called by the SCF execution environment.

* The compiled package, class files and resource files are located under the root directory of the zip package.
* The jar package required for dependency is located under the /lib directory.

## Environment Preparation
Make sure Java and Gradle have been installed. Install JDK8. You can use OpenJDK (Linux) or download and install the JDK appropriate for your system via www.java.com.

### Gradle installation

For the specific installation method, please see [https://gradle.org/install/](https://gradle.org/install/). Here we describe the manual installation process:
1. Download [Binary Package](https://services.gradle.org/distributions/gradle-4.1-bin.zip) or [Complete Package with Documentation and Source Code](https://services.gradle.org/distributions/gradle-4.1-all.zip) of Gradle.
2. Decompress the package to your desired directory, for example `C:\Gradle` (Windows) or `/opt/gradle/gradle-4.1` (Linux).
3. Add the path of the bin directory under the decompression directory to the system PATH environment variable. For Linux, add it using `export PATH=$PATH:/opt/gradle/gradle-4.1/bin`. For Windows, `right-click **Computer**, and select **Attribute** -> **Advanced System Settings** -> **Advanced** -> **Environment Variables**` to enter the environment variable settings page, and then select the `Path` variable and add `;C:\Gradle\bin;` at the end of the variable value.
4. Run `gradle -v` in the command line. If the following content shows, it indicates that Gradle has been installed successfully. For any questions, please see [Gradle User Manual](https://gradle.org/docs/).
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

Create `build.gradle` file under the root directory of project folder and enter the following:
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
#### Process package dependency with Maven Central library

If you need to reference external package of Maven Central, you can add dependency as needed. The content of the `build.gradle` file is written as follows:
```
apply plugin: 'java'

repositories {
    mavenCentral()
}

dependencies {
    compile (
        'com.tencentcloudapi:scf-java-events:0.0.1'
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

With mavenCentral specified in repositories as the dependent library source, Gradle will pull dependency from Maven Central in the compilation process, namely `com.qcloud:qcloud-scf-java-events:1.0.0` package specified in dependencies.

#### Process package dependency using local Jar package library

If you have downloaded the Jar package locally, you can use the local library to process package dependency. In this case, create `jars` directory under the root directory of project folder, and place the downloaded dependency Jar package under this directory. Write the `build.gradle` file as follows:
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
Specify *.jar file under the jars directory as the searching directory via dependencies, and dependency will perform auto search in the compilation process.

## Compiling and Packaging

Run the command `gradle build` under the root directory of the project folder. The compiling output should be similar to the following:

```
Starting a Gradle Daemon (subsequent builds will be faster)

BUILD SUCCESSFUL in 5s
3 actionable tasks: 3 executed
```

If compiling fails, adjust the code according to the output compiling error message.
The compiled zip package is located under the `/build/distributions` directory of the project folder and is named as `scf_example.zip` with the project folder name.

## Function Use

For the generated zip package after compiling and packaging, you can choose the upload method based on the package size when creating or modifying the function. If the package is less than 10 MB, you can use page upload, otherwise you can upload the package to COS Bucket and then update it into the function via COS upload.

