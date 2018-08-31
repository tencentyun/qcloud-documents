我们在 Gaiastack 环境上，编译了 xgboost 0.7 版本，以 jar 包的形式提供给用户使用，下面为具体流程：

1. 下载 [xgboost4j-0.7.jar](https://tio.cloud.tencent.com/gitbook/doc/manual/attachments/xgboost4j-0.7.jar) 和 [xgboost4j-spark-0.7.jar](https://tio.cloud.tencent.com/gitbook/doc/manual/attachments/xgboost4j-spark-0.7.jar)

2. 将 jar 包安装到本地 Maven 库中。
```
    mvn install:install-file -Dfile=./xgboost4j-0.7.jar -DgroupId=ml.dmlc -DartifactId=xgboost4j -Dversion=0.7 -Dpackaging=jar
    
    mvn install:install-file -Dfile=./xgboost4j-spark-0.7.jar -DgroupId=ml.dmlc -DartifactId=xgboost4j-spark -Dversion=0.7 -Dpackaging=jar
```

3. 在自己 Spark 作业的 pom 中引入 xgboost4j 和 xgboost4j-spark 的 Maven 依赖。

        <?xml version="1.0" encoding="UTF-8"?>
    	<project xmlns="http://maven.apache.org/POM/4.0.0"
    	         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    	         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    	    <modelVersion>4.0.0</modelVersion>
    	    <groupId>com.tencent.gaia</groupId>
    	    <artifactId>xgb</artifactId>
    	    <version>1.0-SNAPSHOT</version>
    	
    	    <properties>
    	        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    	        <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
    	    </properties>
    	
    	    <dependencies>
    	        <dependency>
    	            <groupId>ml.dmlc</groupId>
    	            <artifactId>xgboost4j</artifactId>
    	            <version>0.7</version>
    	        </dependency>
    	        <dependency>
    	            <groupId>ml.dmlc</groupId>
    	            <artifactId>xgboost4j-spark</artifactId>
    	            <version>0.7</version>
    	        </dependency>
    	        <dependency>
    	            <groupId>org.apache.spark</groupId>
    	            <artifactId>spark-core_2.11</artifactId>
    	            <version>2.2.0</version>
    	            <scope>provided</scope>
    	        </dependency>
    	        <dependency>
    	            <groupId>org.apache.spark</groupId>
    	            <artifactId>spark-mllib_2.11</artifactId>
    	            <version>2.2.0</version>
    	            <scope>provided</scope>
    	        </dependency>
    	        <dependency>
    	            <groupId>org.apache.spark</groupId>
    	            <artifactId>spark-sql_2.11</artifactId>
    	            <version>2.2.0</version>
    	            <scope>provided</scope>
    	        </dependency>
    	        <dependency>
    	            <groupId>org.apache.commons</groupId>
    	            <artifactId>commons-lang3</artifactId>
    	            <version>3.4</version>
    	        </dependency>
    	    </dependencies>
    	
    	    <build>
    	        <plugins>
    	            <plugin>
    	                <groupId>net.alchim31.maven</groupId>
    	                <artifactId>scala-maven-plugin</artifactId>
    	                <version>3.2.0</version>
    	                <executions>
    	                    <execution>
    	                        <id>scala-compile-first</id>
    	                        <phase>process-resources</phase>
    	                        <goals>
    	                            <goal>compile</goal>
    	                        </goals>
    	                    </execution>
    	                </executions>
    	                <configuration>
    	                    <scalaVersion>2.11.8</scalaVersion>
    	                    <recompileMode>incremental</recompileMode>
    	                    <useZincServer>true</useZincServer>
    	                    <args>
    	                        <arg>-unchecked</arg>
    	                        <arg>-deprecation</arg>
    	                        <arg>-feature</arg>
    	                    </args>
    	                </configuration>
    	            </plugin>
    	            <plugin>
    	                <artifactId>maven-assembly-plugin</artifactId>
    	                <configuration>
    	                    <archive>
    	                        <manifest>
    	                            <mainClass>fully.qualified.MainClass</mainClass>
    	                        </manifest>
    	                    </archive>
    	                    <descriptorRefs>
    	                        <descriptorRef>jar-with-dependencies</descriptorRef>
    	                    </descriptorRefs>
    	                </configuration>
    	            </plugin>
    	        </plugins>
    	        <resources>
    	            <resource>
    	                <directory>src/main/resources</directory>
    	            </resource>
    	        </resources>
    	    </build>
    	</project>

4. 在自己 Spark 作业中使用 xgboost4j 和 xgboost4j-spark 的 API，具体参考 xgboost 官方 github 中的 example，简单样例如下：
```
    package xgb.gaia
    
    import ml.dmlc.xgboost4j.scala.Booster
    import ml.dmlc.xgboost4j.scala.spark.XGBoost
    import org.apache.spark.SparkConf
    import org.apache.spark.sql.SparkSession
    
    object SparkWithDataFrame {
      def main(args: Array[String]): Unit = {        
        // create SparkSession
        val sparkConf = new SparkConf().setAppName("XGBoost-spark-example")
          .set("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
        sparkConf.registerKryoClasses(Array(classOf[Booster]))
        val sparkSession = SparkSession.builder().config(sparkConf).getOrCreate()
    
        // create training and testing dataframes
        val numRound = args(0).toInt
        val inputTrainPath = args(2)
        val inputTestPath = args(3)
        val predictResultPath = args(4)
    
        // build dataset
        val trainDF = sparkSession.sqlContext.read.format("libsvm").load(inputTrainPath)
        val testDF = sparkSession.sqlContext.read.format("libsvm").load(inputTestPath)
    
        // start training
        val paramMap = List(
          "eta" -> 0.1f,
          "max_depth" -> 2,
          "objective" -> "binary:logistic").toMap
        val xgboostModel = XGBoost.trainWithDataFrame(
          trainDF, paramMap, numRound, nWorkers = args(1).toInt, useExternalMemory = true)
    
        // xgboost-spark appends the column containing prediction results
        val output = xgboostModel.transform(testDF)
        output.show()
        output.rdd.saveAsTextFile(predictResultPath)
      }
    }
```

5. 将自己的 Spark 作业进行打包。

      `mvn clean compile assembly:single`
			
6. 将自己的 Spark 作业打好的包，上传到 [TI-ONE 控制台](https://tio.cloud.tencent.com/) 中进行运行。 
可参考 [示例任务](https://tio.cloud.tencent.com/ml/platform.html?projectId=28&flowId=310)。
测试数据：[agaricus.txt.train](https://tio.cloud.tencent.com/gitbook/doc/manual/attachments/agaricus.txt.train)、[agaricus.txt.test](https://tio.cloud.tencent.com/gitbook/doc/manual/attachments/agaricus.txt.test)
