

Refer to the following sample code, which includes the common operations on HBase, such as table creation, deletion, insertion, and data reading.
```
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.NavigableMap;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.hbase.Cell;
import org.apache.hadoop.hbase.CellUtil;
import org.apache.hadoop.hbase.HBaseConfiguration;
import org.apache.hadoop.hbase.HColumnDescriptor;
import org.apache.hadoop.hbase.HTableDescriptor;
import org.apache.hadoop.hbase.KeyValue;
import org.apache.hadoop.hbase.TableName;
import org.apache.hadoop.hbase.client.Admin;
import org.apache.hadoop.hbase.client.Connection;
import org.apache.hadoop.hbase.client.ConnectionFactory;
import org.apache.hadoop.hbase.client.Delete;
import org.apache.hadoop.hbase.client.Get;
import org.apache.hadoop.hbase.client.Put;
import org.apache.hadoop.hbase.client.Result;
import org.apache.hadoop.hbase.client.ResultScanner;
import org.apache.hadoop.hbase.client.Scan;
import org.apache.hadoop.hbase.client.Table;
import org.apache.hadoop.hbase.util.Bytes;

public class Connect {

	public static void createTable(String tableName, String[] familys) throws IOException {
		Admin admin = null;
		Connection con = null;
		try{
			Configuration config = HBaseConfiguration.create();
			// Fill in the address of zookeeper, and use comma to separate multiple addresses.
			config.set("hbase.zookeeper.quorum", "10.66.133.178:2181");
			// Set parameters for retry
			config.setInt("hbase.client.retries.number", 1);
			/*
			 * To connect the hbase service of Tencent Cloud, you must set this value to true; if not, it functions the same as the community version, and you can normally connect the self-built hbase service.
			 */
			config.setBoolean("chbase.tencent.enable", true);

			TableName TABLE = TableName.valueOf(tableName);
			con = ConnectionFactory.createConnection(config);
			admin = con.getAdmin();
			
			if (admin.tableExists(TABLE)) {
				System.out.println("table already exists!");
			} else {
				HTableDescriptor tableDesc = new HTableDescriptor(TABLE);
				for (int i = 0; i < familys.length; i++) {
					tableDesc.addFamily(new HColumnDescriptor(familys[i]));
				}
				admin.createTable(tableDesc);
				System.out.println("create table " + tableName + " ok.");
			}
		}catch(IOException e){
			e.printStackTrace();
		}finally{
			admin.close();
			con.close();
		}
	}

	public static void deleteTable(String tableName) throws IOException{
		Admin admin = null;
		Connection con = null;
		try{
			Configuration config = HBaseConfiguration.create();
			// Fill in the address of zookeeper, and use comma to separate multiple addresses.
			config.set("hbase.zookeeper.quorum", "10.66.133.178:2181");
			// Set parameters for retry
			config.setInt("hbase.client.retries.number", 1);
			/*
			 * To connect the hbase service of Tencent Cloud, you must set this value to true; if not, it functions the same as the community version, and you can normally connect the self-built hbase service.
			 */
			config.setBoolean("chbase.tencent.enable", true);

			TableName TABLE = TableName.valueOf(tableName);
			con = ConnectionFactory.createConnection(config);
			admin = con.getAdmin();

			if (!admin.tableExists(TABLE)) {
				System.out.println("table not exists!");
			} else {
				admin.disableTable(TABLE);
				admin.deleteTable(TABLE);
				System.out.println("delete table " + tableName + " ok.");
			}
		}catch(IOException e){
			e.printStackTrace();
		}finally{
			admin.close();
			con.close();
		}
	}

	public static void get(String tablename, String rowkey) throws IOException {
		Connection con = null;
		Table table = null;
		try{
			Configuration config = HBaseConfiguration.create();
			// Fill in the address of zookeeper, and use comma to separate multiple addresses.
			config.set("hbase.zookeeper.quorum", "10.66.133.178:2181");
			// Set parameters for retry
			config.setInt("hbase.client.retries.number", 1);
			/*
			 * To connect the hbase service of Tencent Cloud, you must set this value to true; if not, it functions the same as the community version, and you can normally connect the self-built hbase service.
			 */
			config.setBoolean("chbase.tencent.enable", true);

			con = ConnectionFactory.createConnection(config);
			table = con.getTable(TableName.valueOf(tablename));

			Get get = new Get(rowkey.getBytes());
			Result rs = table.get(get);
			for (Cell cell : rs.rawCells()) {
				System.out.print(new String(CellUtil.cloneRow(cell)) + " ");
				System.out.print(new String(CellUtil.cloneFamily(cell)) + ":");
				System.out.print(new String(CellUtil.cloneQualifier(cell)) + " ");
				System.out.print(cell.getTimestamp() + " ");
				System.out.println(new String(CellUtil.cloneValue(cell)));
			}
		}catch(IOException e){
			e.printStackTrace();
		}finally{
			table.close();
			con.close();
		}
	}

	public static void del(String tablename, String rowkey) throws IOException {
		Connection con = null;
		Table table = null;
		try{
			Configuration config = HBaseConfiguration.create();
			// Fill in the address of zookeeper, and use comma to separate multiple addresses.
			config.set("hbase.zookeeper.quorum", "10.66.133.178:2181");
			// Set parameters for retry
			config.setInt("hbase.client.retries.number", 1);
			/*
			 * To connect the hbase service of Tencent Cloud, you must set this value to true; if not, it functions the same as the community version, and you can normally connect the self-built hbase service.
			 */
			config.setBoolean("chbase.tencent.enable", true);

			con = ConnectionFactory.createConnection(config);
			table = con.getTable(TableName.valueOf(tablename));
			// Batch deletion
			List<Delete> list = new ArrayList<Delete>();
			Delete del = new Delete(rowkey.getBytes());
			list.add(del);
			table.delete(list);
			// Single deletion
			// Delete del = new Delete(Bytes.toBytes(rowkey));
			// table.delete(del);
			System.out.println("del recored " + rowkey + " ok.");
		}catch(IOException e){
			e.printStackTrace();
		}finally{
			table.close();
			con.close();
		}
	}

	public static void put(String tablename, String rowkey, String familyname, String colname, String value) throws IOException
			{
		Connection con = null;
		Table table = null;
		try{
			Configuration config = HBaseConfiguration.create();
			// Fill in the address of zookeeper, and use comma to separate multiple addresses.
			config.set("hbase.zookeeper.quorum", "10.66.133.178:2181");
			// Set parameters for retry
			config.setInt("hbase.client.retries.number", 1);
			/*
			 * To connect the hbase service of Tencent Cloud, you must set this value to true; if not, it functions the same as the community version, and you can normally connect the self-built hbase service.
			 */
			config.setBoolean("chbase.tencent.enable", true);

			con = ConnectionFactory.createConnection(config);
			table = con.getTable(TableName.valueOf(tablename));

			byte[] ROWKEY = Bytes.toBytes(rowkey);
			Put put = new Put(ROWKEY);

			Cell c1 = CellUtil.createCell(ROWKEY, Bytes.toBytes(familyname), Bytes.toBytes(colname),
					System.currentTimeMillis(), KeyValue.Type.Put.getCode(), Bytes.toBytes(value));
			put.add(c1);
			table.put(put);
			System.out.println("--------------------put ok------------------");
		}catch(IOException e){
			e.printStackTrace();
		}finally{
			table.close();
			con.close();
		}
	}

	public static void scan(String tablename, String rowkey, String family) throws IOException {
		Connection con = null;
		Table table = null;
		try{
			Configuration config = HBaseConfiguration.create();
			// Fill in the address of zookeeper, and use comma to separate multiple addresses.
			config.set("hbase.zookeeper.quorum", "10.66.133.178:2181");
			// Set parameters for retry
			config.setInt("hbase.client.retries.number", 1);
			/*
			 * To connect the hbase service of Tencent Cloud, you must set this value to true; if not, it functions the same as the community version, and you can normally connect the self-built hbase service.
			 */
			config.setBoolean("chbase.tencent.enable", true);
			Scan scan = new Scan();
			scan.setStartRow(Bytes.toBytes(rowkey));
			scan.setCaching(500);
			scan.setCacheBlocks(false);

			con = ConnectionFactory.createConnection(config);
			table = con.getTable(TableName.valueOf(tablename));

			ResultScanner ss = table.getScanner(scan);
			System.out.println("--------------------------------------");
			for (Result r : ss) {
				NavigableMap<byte[], byte[]> map = r.getFamilyMap(Bytes.toBytes(family));
				for (Map.Entry<byte[], byte[]> ent : map.entrySet()) {
					String key = new String(ent.getKey());
					String value = new String(ent.getValue());
					System.out.println(
							"find result is:" + new String(r.getRow()) + " and code is:" + key + " and value is:" + value);
				}
			}
			System.out.println("--------------------------------------");
		}catch(IOException e){
			e.printStackTrace();
		}finally{
			table.close();
			con.close();
		}
	}

	public static void main(String[] args) throws Exception {
		if (args == null || args.length < 1) {
			System.out.println("please input args....");
			return;
		}
		String op = args[0];

		if (op.equals("create")) {
			// The column name to be created.
			String[] familys = { "fam1", "fam2", "fam3" };
			createTable("test", familys);
		} else if (op.equals("put")) {
			put("test", "key1", "fam1", "col1", "value1");
		} else if (op.equals("get")) {
			get("test", "key1");
		} else if (op.equals("deltable")) {
			deleteTable("test");
		} else if (op.equals("scan")) {
			scan("test", "key1", "fam1");
		} else if (op.equals("del")) {
			del("test", "key1");
		}
	}

}
```
