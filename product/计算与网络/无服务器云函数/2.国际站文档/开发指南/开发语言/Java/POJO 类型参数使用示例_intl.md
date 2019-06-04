With POJO parameters, in addition to simple event input parameters, you can process more complex data structures. In this section, a set of examples will be used to illustrate how to use POJO parameters in SCF and which input parameters formats are supported.

## Event Input Parameters and POJO 

Suppose our event input parameters are as follows:

```json
{
  "person": {"firstName":"bob","lastName":"zou"},
  "city": {"name":"shenzhen"}
}
```

For the above input parameters, the output is as follows:

```json
{
  "greetings": "Hello bob zou.You are from shenzhen"
}
```

Based on the input parameters, we have constructed the following four classes:
* RequestClass: Used to accept events as an event accepting class
* PersonClass: Used to process the `person` field in the event JSON
* CityClass: Used to process the `city` field in the event JSON
* ResponseClass: Used to organize response content

## Code Preparation

According to the four classes and entry functions designed for input parameters, follow the following steps to prepare.

### Project directory preparation

Create a project root directory, such as `scf_example`.

### Code directory preparation

Create the folder `src\main\java` under the project root directory as the code directory.

Based on the package name to be used, create a package folder in the code directory, such as `example`, to form the directory structure of `scf_example\src\main\java\example`.

### Code Preparation
Create files `Pojo.java`, `RequestClass.java`, `PersonClass.java`, `CityClass.java` and `ResponseClass.java` in the folder "example". The content of the files are as follows:

* Pojo.java

```
package example;

public class Pojo{  
    public ResponseClass handle(RequestClass request){
        String greetingString = String.format("Hello %s %s.You are from %s", request.person.firstName, request.person.lastName, request.city.name);
        return new ResponseClass(greetingString);
    }
}
```

* RequestClass.java

```
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

```

* PersonClass.java

```
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

```

* CityClass.java

```
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

```

* ResponseClass.java

```
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
```

## Code Compilation

In the example, we use Maven for compilation and packaging. You can choose the packaging method based on your needs.

Create the pom.xml function under the project root directory and enter the following content:

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

Execute the command `mvn package` in the command line, and make sure that it has been successfully compiled, as shown below:

```
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 1.800 s
[INFO] Finished at: 2017-08-25T15:42:41+08:00
[INFO] Final Memory: 18M/309M
[INFO] ------------------------------------------------------------------------
```

If the compilation fails, modify it according to the prompt.

The compiled package is located at `target\java-example-1.0-SNAPSHOT.jar`.

## Creating and Testing SCF

According to the guidelines, create a SCF and upload the compiled package as a submission package. You can choose to use zip upload, or upload it to COS Bucket and then select "COS Bucket upload" for submission.

The execution method of SCF is configured as `example.Pojo::handle`.

Click the **test** button to go to the test interface, and then enter the input parameters that we initially want to process in the test template:

```json
{
  "person": {"firstName":"bob","lastName":"zou"},
  "city": {"name":"shenzhen"}
}
```

Click **Run** and you can see the returned content:


```
{
  "greetings": "Hello bob zou.You are from shenzhen"
}
```

You can also modify the value in the structure of the test input parameter. After running the SCF, you can see the modification effect.

