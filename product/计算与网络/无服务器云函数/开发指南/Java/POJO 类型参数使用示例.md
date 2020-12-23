## 操作场景
通过使用 POJO 类型参数，您可以处理除简单事件入参外更复杂的数据结构。在本文档中，将使用一组示例说明在 SCF 中如何使用 POJO 参数，并能支持何种格式的入参。

## 前提条件
已登录 [SCF 控制台](https://console.cloud.tencent.com/scf/index?rid=1)。

## 操作步骤
### 事件入参和 POJO 
本文使用的事件入参如下所示：
```json
{
  "person": {"firstName":"bob","lastName":"zou"},
  "city": {"name":"shenzhen"}
}
```
在有如上入参的情况下，输出内容如下：
```json
{
  "greetings": "Hello bob zou.You are from shenzhen"
}
```
根据入参，构建了如下四个类：
* RequestClass：用于接受事件，作为接受事件的类
* PersonClass：用于处理事件 JSON 内 `person` 段
* CityClass：用于处理事件 JSON 内 `city` 段
* ResponseClass：用于组装响应内容

### 代码准备
根据入参已构建的四个类及入口函数，请按照以下步骤进行代码准备。

#### 项目目录准备
创建项目根目录，例如 `scf_example`。

#### 代码目录准备
1. 在项目根目录下创建文件夹 `src\main\java` 作为代码目录。
2. 根据准备使用的包名，在代码目录下创建包文件夹。
例如 `example`，形成 `scf_example\src\main\java\example` 的目录结构。

#### 代码准备
在 `example` 文件夹内创建 `Pojo.java`，`RequestClass.java`，`PersonClass.java`，`CityClass.java`，`ResponseClass.java` 文件，文件内容分别如下：

<dx-codeblock>
::: Pojo.java java
package example;

public class Pojo{  
    public ResponseClass handle(RequestClass request){
        String greetingString = String.format("Hello %s %s.You are from %s", request.person.firstName, request.person.lastName, request.city.name);
        return new ResponseClass(greetingString);
    }
}
:::
::: RequestClass.java java
package example;

public class RequestClass {
    PersonClass person;
    CityClass city;

    public PersonClass getPerson() {
        return person;
    }

    public void setPerson(PersonClass person) {
        this.person = person;
    }
    
    public CityClass getCity() {
        return city;
    }

    public void setCity(CityClass city) {
        this.city = city;
    }

    public RequestClass(PersonClass person, CityClass city) {
        this.person = person;
        this.city = city;
    }

    public RequestClass() {
    }
}
:::
::: PersonClass.java java
package example;

public class PersonClass {
    String firstName;
    String lastName;

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public PersonClass(String firstName, String lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }

    public PersonClass() {
    }
}
:::
::: CityClass.java java
package example;

public class CityClass {
    String name;
    
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public CityClass(String name) {
        this.name = name;
    }

    public CityClass() {
    }
}
:::
::: ResponseClass.java java
package example;

public class ResponseClass {
    String greetings;

    public String getGreetings() {
        return greetings;
    }

    public void setGreetings(String greetings) {
        this.greetings = greetings;
    }

    public ResponseClass(String greetings) {
        this.greetings = greetings;
    }

    public ResponseClass() {
    }
}
:::
</dx-codeblock>

### 代码编译
>?本示例使用 Maven 进行编译打包，您可以根据自身情况，选择使用打包方法。
>
1. 在项目根目录创建 pom.xml 函数，并输入如下内容：
```
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
2. 在命令行内执行命令 `mvn package` ，确保有编译成功字样，输出结果如下则说明成功打包。
```
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 1.800 s
[INFO] Finished at: 2017-08-25T15:42:41+08:00
[INFO] Final Memory: 18M/309M
[INFO] ------------------------------------------------------------------------
```
如果编译失败，请根据提示进行相应修改。
3. 编译后的生成包位于 `target\java-example-1.0-SNAPSHOT.jar`。

### SCF 云函数创建及测试
1. 创建云函数，详情请参见 [创建及更新函数](https://cloud.tencent.com/document/product/583/19806)。
2. 使用编译后的包作为提交包上传。
您可以自行选择使用 zip 上传，或先上传至 COS Bucket 后再通过选择 COS Bucket 上传来提交。
3. 设置云函数的执行方法为 `example.Pojo::handle`。
4. 通过测试按钮展开测试界面，在测试模版内输入我们一开始期望能处理的入参：
```json
{
  "person": {"firstName":"bob","lastName":"zou"},
  "city": {"name":"shenzhen"}
}
```
单击运行后，可查看返回内容为：
```
{
  "greetings": "Hello bob zou.You are from shenzhen"
}
```
您也可以自行修改测试入参内结构的 value 内容，运行后可以看到修改效果。

### 相关示例
您可前往如下地址，拉取示例代码并进行测试。
```
https://github.com/tencentyun/scf-demo-java
```
