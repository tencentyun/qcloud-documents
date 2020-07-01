
使用协处理，需要将jar包提供给我们，我们安装后提供hdfs地址，您可以再通过shell或者api方式（代码中有示例）安装。强烈建议开发好协处理器jar包后，经过充分测试再安装，避免安装后影响Hbase服务的正常使用。

## 协处理器开发步骤
1.编写proto文件（示例：RowCount.proto）；因为hbase使用google的protoc-2.5.0版本，所以最好使用相同版本编译proto文件，生成Java文件（示例：RowCountService.java）；
2.编写服务端EndPoint代码（示例：RowCountEndPoint.java）；
3.编写客户端调用Client代码（示例：RowCountClient.java）；
4.编译jar包

endpoint协处理器示例：
### proto文件
```
option java_package = "com.tencent.yun.endpoint.proto";
option java_outer_classname = "RowCountService";
option java_generic_services = true;
option java_generate_equals_and_hash = true;
option optimize_for = SPEED;

message RowCountRequest{
	required string family = 1;
    required string column = 2;
}
 
message RowCountResponse {
	required int64 rowCount = 1 [default = 0];
}

service RowCount {
	rpc getRowCount(RowCountRequest)
	returns (RowCountResponse);
}
```
### 服务端RowCountEndPoint类
```
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import org.apache.hadoop.hbase.Cell;
import org.apache.hadoop.hbase.Coprocessor;
import org.apache.hadoop.hbase.CoprocessorEnvironment;
import org.apache.hadoop.hbase.client.Scan;
import org.apache.hadoop.hbase.coprocessor.CoprocessorException;
import org.apache.hadoop.hbase.coprocessor.CoprocessorService;
import org.apache.hadoop.hbase.coprocessor.RegionCoprocessorEnvironment;
import org.apache.hadoop.hbase.protobuf.ResponseConverter;
import org.apache.hadoop.hbase.regionserver.InternalScanner;
import org.apache.hadoop.hbase.util.Bytes;

import com.google.protobuf.RpcCallback;
import com.google.protobuf.RpcController;
import com.google.protobuf.Service;
import com.tencent.yun.endpoint.proto.RowCountService;
import com.tencent.yun.endpoint.proto.RowCountService.RowCountRequest;
import com.tencent.yun.endpoint.proto.RowCountService.RowCountResponse;

public class RowCountEndPoint extends RowCountService.RowCount implements Coprocessor, CoprocessorService {

	private RegionCoprocessorEnvironment env;

	public Service getService() {
		return this;
	}

	public void start(CoprocessorEnvironment env) throws IOException {
		if (env instanceof RegionCoprocessorEnvironment) {
			this.env = (RegionCoprocessorEnvironment) env;
		} else {
			throw new CoprocessorException("Must be loaded on a table region!");
		}
	}

	public void stop(CoprocessorEnvironment arg0) throws IOException {
		// do nothing

	}

	@Override
	public void getRowCount(RpcController controller, RowCountRequest request, RpcCallback<RowCountResponse> done) {
		Scan scan = new Scan();
		scan.addFamily(Bytes.toBytes(request.getFamily()));
		scan.addColumn(Bytes.toBytes(request.getFamily()), Bytes.toBytes(request.getColumn()));
		// scan.setMaxVersions(1);
		InternalScanner scanner = null;
		RowCountResponse response = null;

		long count = 0L;
		try {
			List<Cell> results = new ArrayList<Cell>();
			boolean hasMore = false;
			scanner = env.getRegion().getScanner(scan);

			do {
				hasMore = scanner.next(results);
				for (Cell cell : results) {
					count++;
					// count = count + Bytes.toLong(CellUtil.cloneValue(cell));
				}
				results.clear();
			} while (hasMore);

			response = RowCountResponse.newBuilder().setRowCount(count).build();

		} catch (IOException e) {
			ResponseConverter.setControllerException(controller, e);
		} finally {
			if (scanner != null) {
				try {
					scanner.close();
				} catch (IOException ignored) {
				}
			}
		}
		done.run(response);
	}

}

```
### 客户端RowCountClient类

```

import java.io.IOException;
import java.util.Map;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.hbase.Coprocessor;
import org.apache.hadoop.hbase.HBaseConfiguration;
import org.apache.hadoop.hbase.HColumnDescriptor;
import org.apache.hadoop.hbase.HTableDescriptor;
import org.apache.hadoop.hbase.TableName;
import org.apache.hadoop.hbase.client.Admin;
import org.apache.hadoop.hbase.client.Connection;
import org.apache.hadoop.hbase.client.ConnectionFactory;
import org.apache.hadoop.hbase.client.Table;
import org.apache.hadoop.hbase.client.coprocessor.Batch;
import org.apache.hadoop.hbase.ipc.BlockingRpcCallback;
import org.apache.hadoop.hbase.ipc.ServerRpcController;

import com.google.protobuf.ServiceException;
import com.tencent.yun.endpoint.proto.RowCountService.RowCount;
import com.tencent.yun.endpoint.proto.RowCountService.RowCountRequest;
import com.tencent.yun.endpoint.proto.RowCountService.RowCountResponse;
import com.tencent.yun.observer.RegionObserver;

public class RowCountClient {

	public static void testRowCountEndpoint(String tableName, String family, String col) throws IOException {
		System.out.println("begin test.....");
		long t1 = System.currentTimeMillis();
		Configuration config = HBaseConfiguration.create();
		//填写hbase zk地址
		config.set("hbase.zookeeper.quorum", "100.67.159.134:2181,100.67.159.141:2181,100.67.159.196:2181");

		// 填寫family名和列名
		final RowCountRequest req = RowCountRequest.newBuilder().setFamily(family).setColumn(col).build();
		RowCountResponse resp = null;
		Connection con = null;
		Table table = null;
		try {
			con = ConnectionFactory.createConnection(config);
			table = con.getTable(TableName.valueOf(tableName));
			Map<byte[], Long> results = table.coprocessorService(RowCount.class, null, null,
					new Batch.Call<RowCount, Long>() {

						public Long call(RowCount instance) throws IOException {
							ServerRpcController controller = new ServerRpcController();
							BlockingRpcCallback<RowCountResponse> rpccall = new BlockingRpcCallback<RowCountResponse>();
							instance.getRowCount(controller, req, rpccall);
							RowCountResponse resp = rpccall.get();
							//
							return resp.hasRowCount() ? resp.getRowCount() : 0L;
						}

					});
			long count = 0L;
			for (Long sum : results.values()) {
				System.out.println("region row Sum = " + sum);
				count += sum;
			}
			System.out.println("total count = " + count);
			long t2 = System.currentTimeMillis();
			System.out.println("use time = " + (t2-t1));
		} catch (IOException e) {
			e.printStackTrace();
		} catch (ServiceException e) {
			e.printStackTrace();
		} catch (Throwable e) {
			e.printStackTrace();
		} finally{
			table.close();
			con.close();
		}
	}

	public static void delCorprocessor(String tableName) throws IOException {
		System.out.println("begin delCorprocessor.....");
		Connection con = null;
		Admin admin = null;
		try {
			Configuration config = HBaseConfiguration.create();
			//填写hbase zk地址
			config.set("hbase.zookeeper.quorum", "100.67.159.134:2181,100.67.159.141:2181,100.67.159.196:2181");

			TableName TABLE = TableName.valueOf(tableName);

			con = ConnectionFactory.createConnection(config);
			admin = con.getAdmin();

			HTableDescriptor tableDesc = admin.getTableDescriptor(TABLE);

			tableDesc.removeCoprocessor(RowCountEndPoint.class.getCanonicalName());
			tableDesc.removeCoprocessor(RegionObserver.class.getCanonicalName());

			admin.modifyTable(TABLE, tableDesc);
		} catch (IOException e) {
			e.printStackTrace();
		}finally{
			admin.close();
			con.close();
		}
		System.out.println("end delCorprocessor.....ok");
	}

	/**
	 * 支持hbase0.96以上版本
	 * @throws IOException 
	 */
	public static void setupToExistTable(String tableName) throws IOException {
		System.out.println("begin setupToExistTable.....");
		Connection con = null;
		Admin admin = null;
		try {
			Configuration config = HBaseConfiguration.create();
			//填写hbase zk地址
			config.set("hbase.zookeeper.quorum", "100.67.159.134:2181,100.67.159.141:2181,100.67.159.196:2181");

			TableName TABLE = TableName.valueOf(tableName);
			con = ConnectionFactory.createConnection(config);
			admin = con.getAdmin();

			HTableDescriptor tableDesc = admin.getTableDescriptor(TABLE);

			//填写我们提供的jar包的hdfs地址
			Path jarPath = new Path("hdfs://100.67.159.132:8020/coprocessor/1/thbase-1.0-SNAPSHOT.jar");

			tableDesc.addCoprocessor(RowCountEndPoint.class.getCanonicalName(), jarPath, Coprocessor.PRIORITY_USER,
					null);
			tableDesc.addCoprocessor(RegionObserver.class.getCanonicalName(), jarPath, Coprocessor.PRIORITY_USER, null);

			admin.modifyTable(TABLE, tableDesc);
		} catch (IOException e) {
			e.printStackTrace();
		}finally{
			admin.close();
			con.close();
		}
		System.out.println("end setupToExistTable.....ok");

	}

	public static void createAndSetup(String tableName) throws IOException {
		System.out.println("begin safesetup.....");
		Connection con = null;
		Admin admin = null;
		try {
			Configuration config = HBaseConfiguration.create();
			//填写hbase zk地址
			config.set("hbase.zookeeper.quorum", "100.67.159.134:2181,100.67.159.141:2181,100.67.159.196:2181");

			TableName TABLE = TableName.valueOf(tableName);

			con = ConnectionFactory.createConnection(config);
			admin = con.getAdmin();

			HTableDescriptor tableDesc = new HTableDescriptor(TABLE);
			HColumnDescriptor columnFamily1 = new HColumnDescriptor("f1");
			columnFamily1.setMaxVersions(3);
			tableDesc.addFamily(columnFamily1);

			//填写我们提供的jar包的hdfs地址
			Path jarPath = new Path("hdfs://100.67.159.132:8020/coprocessor/1/thbase-1.0-SNAPSHOT.jar");

			tableDesc.addCoprocessor(RowCountEndPoint.class.getCanonicalName(), jarPath, Coprocessor.PRIORITY_USER,
					null);
			tableDesc.addCoprocessor(RegionObserver.class.getCanonicalName(), jarPath, Coprocessor.PRIORITY_USER, null);

			admin.createTable(tableDesc);
			System.out.println("end safesetup.....ok");
		} catch (IOException e) {
			e.printStackTrace();
		}finally{
			admin.close();
			con.close();
		}

	}

	public static void main(String[] args) throws IOException {
		if (args == null || args.length < 2) {
			System.out.println("please input args....");
			return;
		}
		String op = args[0];
		String tableName = args[1];
		String family = args[2];
		String col = args[3];

		if (op.equals("setup")) {
			setupToExistTable(tableName);
		} else if (op.equals("safesetup")) {
			createAndSetup(tableName);
		} else if (op.equals("run")) {
			testRowCountEndpoint(tableName, family, col);
		} else if (op.equals("unset")) {
			delCorprocessor(tableName);
		}

	}

}
```
