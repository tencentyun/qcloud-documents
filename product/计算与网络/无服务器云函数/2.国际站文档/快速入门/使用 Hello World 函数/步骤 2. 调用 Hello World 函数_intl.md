Use the test template provided by the console to call the Hello World function you just create.

1) Click the Hello World function you just create in the list page to enter the function details page, and click **Test** on the right.

2) In the Test Function pop-up box, select `Hello World Test Code` from test templates, and the following data will appear in the window. You can modify the value of the JSON data (for example, change `test_1` to `my_own_data`), but cannot change the data structure.
```
{
  "key1": "test value 1",
  "key2": "test value 2"
}
```

3) Click **Run**, and the code starts running and the test result is displayed. Notes:
 - The running result (successful or failed) and the function execution result returned by `return` statement in the code will appear in the function return value.
 - The execution time of the function and memory will appear in the running information.
 - Logs generated during the function execution will appear in the log, including print statement in user codes and trace stack for function execution failure, and will be written in the log module.

4) You can run the code several times, and click the **Log** tab to check the log information of each run.

