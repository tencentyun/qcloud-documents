
When using co-processing, you need to provide us with the jar package, and we provide the hdfs address after installation. You can then install via shell or APIs (there are samples in the code). It is strongly recommended to install the co-processor jar package through sufficient testing after fully developed, so as to avoid affecting the normal use of Hbase service after installation.

## Co-processor Development Steps
1. Write the proto file (sample: RowCount.proto); because hbse uses the Google version protoc-2.5.0, you'd better to use same version to compile the proto file and generate the jave file (sample: RowCountService.java);
2. Write the server-side EndPoint code (sample: RowCountEndPoint.java);
3. Write the client-side calling Client code (sample: RowCountClient.java);
4. Compile the jar package.

endpoint Co-processor Sample:
### proto File
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
### Server-side RowCountEndPoint Class
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
### Client-side RowCountClient Class

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
		//Fill in the hbase zk address
		config.set("hbase.zookeeper.quorum", "100.67.159.134:2181,100.67.159.141:2181,100.67.159.196:2181");

		// Fill in the family name and column name
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
			//Fill in the hbase zk address
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
	 * Support versions later than hbase0.96
	 * @throws IOException 
	 */
	public static void setupToExistTable(String tableName) throws IOException {
		System.out.println("begin setupToExistTable.....");
		Connection con = null;
		Admin admin = null;
		try {
			Configuration config = HBaseConfiguration.create();
			//Fill in the hbase zk address
			config.set("hbase.zookeeper.quorum", "100.67.159.134:2181,100.67.159.141:2181,100.67.159.196:2181");

			TableName TABLE = TableName.valueOf(tableName);
			con = ConnectionFactory.createConnection(config);
			admin = con.getAdmin();

			HTableDescriptor tableDesc = admin.getTableDescriptor(TABLE);

			//Fill in the hdfs address of the jar package we provided
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
			//Fill in the hbase zk address
			config.set("hbase.zookeeper.quorum", "100.67.159.134:2181,100.67.159.141:2181,100.67.159.196:2181");

			TableName TABLE = TableName.valueOf(tableName);

			con = ConnectionFactory.createConnection(config);
			admin = con.getAdmin();

			HTableDescriptor tableDesc = new HTableDescriptor(TABLE);
			HColumnDescriptor columnFamily1 = new HColumnDescriptor("f1");
			columnFamily1.setMaxVersions(3);
			tableDesc.addFamily(columnFamily1);

			//Fill in the hdfs address of the jar package we provided
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
