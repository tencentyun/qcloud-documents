1) Log in to the Tencent Cloud console, and select **SCF**.

2) Click the **Create Function** button under the `Guangzhou` region to enter the page for creating a new function.

3) Enter `hello-world` as the function name and leave all other configuration options unchanged.

4) Click **Next** to enter the page for editing function codes, and then select default **Online Edit** and the `Hello World` template in **Template**. At this time, the default values in the template will be entered for the execution method and the code:

 - Execution method is `index.main_handler`. SCF console stores this code in an `index.py` file automatically, and compresses and uploads the file to the SCF platform to create a SCF.
 - The following code snippets are displayed in the function code:

```
print('Start Hello World function')
def main_handler(event, context):
    print("value1 = " + event['key1'])
    print("value2 = " + event['key2'])
    return event['key1']  #return the value of key "key1"
```
This sample code acquires the following form of data from the parameter `event`:
```
{
  "key1": "test value 1",
  "key2": "test value 2"
}
```

5) Click **Next** to enter the trigger method page. You don't need to configure any trigger for this sample code, so click **Complete**.

6) At this point, the console generates a code package automatically and uploads it to the SCF platform to create a SCF. Click the `hello-world` function you just create in the SCF list page to enter the SCF details page.


