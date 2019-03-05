##  Connect Tencent Cloud Parameter Settings

1) When connecting the Tencent Cloud Hbase service, you must set the following parameter to true (please refer to the sample code for the complete code). The service then can be used normally:
config.setBoolean("chbase.tencent.enable", true);

2) If you want to use yarn, you also need to set the instance ID (which can be found in the management page, please refer to the sample code for the complete code), for example:
config.set("yarn.chbase.tencent.instanceid", "chb-lpvsvdlr");

Tips:
Other usage modes are consistent with the Hbase of community version except adding the above code; you can refer to the API document on https://hbase.apache.org/.
If you haven't set the above parameter, you can also connect to the Hbase of community version.

