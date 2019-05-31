

### HBase has set switch_balance to true in the shell, but hmaster didn't perform loadbalance operation.
 The condition for hmaser to perform loadbalance is: when the minimum load of the entire cluster is less than the average load *0.8 and the maximum load is greater than the average load* 1.2, it works accordingly. Setting the parameter "balance" is only to enable the automatic balancing, and hmaster can only perform automatic balancing when this condition is satisfied.
 
### The HBase service can not be connected after the HBase access parameters have been set on user cvm.
After setting the HBase-related parameters, you need to set the parameter config.setBoolean("chbase.tencent.enable", true), and replace the community version of jars with jarhbase-client-1.1.3.jar, hbase-common-1.1.3.jar, hbase-server-1.1.3.jar, and hbase-protocol-1.1.3.jar provided by Tencent Cloud.

### How to access HBase services through hbase shell after the services are activated?
  Download the HBbase version hbase-1.1.3-bin.tar.gz provided by Tencent, and then modify the hbase-site.xml under conf to add the following configuration entry.
![](https://mccdn.qcloud.com/static/img/2ef77269830c9943218be54187db01cf/3.png)

### How to proceed if I want to run the YARN-based MR task?
Sample code

```


public class MR {

	 public static void main(String[] args) throws Exception{
	 // TODO Auto-generated method stub
		Job job =Job.getInstance();
		Configuration conf=job.getConfiguration();
		conf.set("hbase.zookeeper.quorum", "The ZK address provided by Tencent Cloud");
		conf.set("yarn.chbase.tencent.instanceid", "The instance ID provided by Tencent Cloud");
		job.setJobName("testjob");
		String tableName = "tablename";
		
		Scan scan = new Scan();
		scan.setStartRow(Bytes.toBytes("0800:00_00000000"));
		scan.setCaching(500);
		scan.setCacheBlocks(false);
	
		job.setJarByClass(MR.class);
		job.setReducerClass(Reduce.class);
		job.setOutputFormatClass(NullOutputFormat.class);
		job.setNumReduceTasks(5);
		//job.addFileToClassPath(JobHelper.addJarToDistributedCache(GenericObjectPoolConfig.class, conf));
	
		TableMapReduceUtil.initTableMapperJob(tableName, scan, Mapper.class, Text.class, Text.class, job);
		boolean b = job.waitForCompletion(true);
		if (!b) {
		throw new Exception("error with job!");
		}
	}
}
```
Use the hadoop version 2.6.4 and the following jars provided by Tencent Cloud 
hadoop-mapreduce-client-app-2.6.4.jar
hadoop-mapreduce-client-common-2.6.4.jar
hadoop-mapreduce-client-core-2.6.4.jar
hadoop-mapreduce-client-jobclient-2.6.4.jar


to replace the jars of community version.

### The class not found errors caused by guava if using spring-hbase
 Hbase uses guava12 by default, but spring-hbase uses guava18. You need to force the guava version to be 12.
 
### How to view the system monitoring information?
After logging in to Tencent Cloud, enter the console through management center.
Then you can see your own cluster and the system monitoring can be checked by clicking on **Details**. This function will be placed in the navigation column of the home site after release.

### How to use the co-processor native to HBase?
![](https://mccdn.qcloud.com/static/img/5d73d6385ac49533eea3c0f49ffd48b6/xichuliqi.png)


