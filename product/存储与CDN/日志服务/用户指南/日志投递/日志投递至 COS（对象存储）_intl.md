CLS supports shipping logs to COS to store log data persistently. You can deliver logs at a certain time interval or based on certain file size to buckets of COS V4 or later.

## Permission Requirements

Configuring log shipper means you grant CLS the write permission for the bucket you specify. If you configure log shipper as a collaborator, make sure that you have grant CLS the write permission for the bucket under your main account. Otherwise, the shipping fails.

## Configuration Instructions

On the logset details page, select a log topic and click **Configure** to create shipping configurations on the log topic configuration page. A log topic can have multiple shipping configurations.

### Enabling/Disabling Shipping Tasks

You can enable or disable shipping tasks in the management list of shipping configuration.

### Basic Configuration

- Shipping task name: It can contain numbers, letters, underscores, and dashes.
- COS bucket: Select the bucket to which logs are shipped. CLS only supports shipping to the bucket in the area where the logset is located.
- Directory prefix (optional): CLS allows you to define directory prefixes. Logs are delivered to `COS-BUCKET/{prefix}/{logset}/{topic}/{Y}/{m}/{d}/{time}_{random}_{index}.gz`, a partition of the COS bucket. A new directory will be created under this bucket each day. The time in the path refers to the actual log time in the log file. random_index is a random number.
- Shipping interval: The shipping interval can be specified from 1 minute to 1 hour. If you set the shipping interval to 5 minutes, a file of your log data will be created every five minutes, and stored in the COS bucket. Log data will be shipped to your bucket in half an hour.
- File size: Specifies the maximum size of uncompressed shipped files within the shipping interval, which refers to the maximum size of the log file that can be shipped at the interval. A file greater than this size will be split into multiple log files. The maximum size supported can be set from 100 MB to 10 GB.

![](https://mc.qcloudimg.com/static/img/8d1f42f4657568290c95d79c4d6b2469/image.png)

### Advanced Configuration

Log shipper also allows you to determine whether to ship logs based on log content, which is an advanced configuration. You can specify a key, perform regular extraction of the key's value, and set a value to match with the extracted value. A log can be shipped only when the log data matches your configuration. Unmatched logs are not shipped. As shown in the figure below, if the "action" field is set to "write", the log is shipped. You can set a maximum of 5 rules to determine whether to ship or not.

![](https://mc.qcloudimg.com/static/img/98cf7e06c8883c55d7b61c7e81612083/image.png)

### Query of Shipping Tasks

You can query the shipping status and details of tasks within the last three days in the shipping task query menu.

