> This feature is under internal trial. Please click [here](https://cloud.tencent.com/act/apply/PlacementSet) to apply for a trial use.

## Creating Placement Group

#### Creating placement group in the console
1. Log in to the [CVM Placement Group Console](https://console.cloud.tencent.com/cvm/ps). 
2. Select Placement Group in the navigation pane, and click **New**.
3. Specify a name for the placement group and select a layer.
4. Click **OK** to complete the creation.

## Starting up Instance in Placement Group
#### Starting up instance in placement group in the console
1. Go to the [CVM Purchase Page](https://buy.cloud.tencent.com/?tab=custom&step=1).
2. Complete the wizard as instructed and the following should be noted:
 - Select the availability zone, instance type and network type for your desired instance in **Region and Model**.
 - Select an image on the **Select Image** page.
 - Select desired configuration and parameters on the **Select Storage and Bandwidth** page.
 - Configure security group, login method and other information on the **Configure Security Group and CVM** page. Click **Advanced Configuration** at the bottom, check **Add Instance to Spread Placement Group**, and select an existing placement group. If no existing placement group meets your requirement, you can [create a placement group](https://console.cloud.tencent.com/cvm/ps?regionId=1) in the console.
 - On the **Confirm Configuration** page, enter the total number of instances to be added to the placement group, which must be less than the number limit set for the placement group.

## Modifying Instance's Placement Group
You can only change the name of a placement group.
#### Modifying instance's placement group in the console
1. Log in to the [CVM Placement Group Console](https://console.cloud.tencent.com/cvm/ps). 
2. Move the mouse over the name of a placement group, and click **Modify Name**.
3. Enter a new name.
4. Click **OK** to complete the modification.

## Deleting Placement Group
You can delete a placement group if you need to replace it or you no longer need it. You must terminate all instances running in your placement group before deleting it.

#### Terminating instances and deleting placement group in the console
1. Log in to the [CVM Placement Group Console](https://console.cloud.tencent.com/cvm/ps).
2. Select and terminate all instances in a placement group.
3. Select the placement group, and delete it. You can delete a single placement group or multiple placement groups in batches.
4. Select **OK** in the confirmation prompt.

