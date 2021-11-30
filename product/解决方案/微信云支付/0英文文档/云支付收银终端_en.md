## Overview of WeChat Cloud Pay POS Terminal
Tencent Cloud provides Cloud Pay POS Terminal that can be connected to various POS software on Windows without any change to the software, allowing merchants to access WeChat Pay and other third-party payment platforms quickly. [Cloud Pay POS Terminal Download Link](https://mc.qcloudimg.com/static/archive/6bc5c37b40edb6f566e573fb64e43b7a/archive.zip). The following describes the relevant operations.
### 1. A variety of payment modes
- Plug-In mode: Used with the merchant's existing POS software to capture the payment amount based on screen recognition. Support seamless connection to the merchant's POS software without any development.
- Full mode: Provide commodity management and other basic features of POS software and can be used as an independent POS software.
### 2. User login
- Store managers and store clerks can log in to the terminal by scanning QR code with WeChat.
- Login by ID and password for store clerks is under development.
### 3. Receiving money in Plug-In mode
- You can customize the option to scan the customer's payment code or press a shortcut key to trigger the payment window.
- Touch screen is supported.
- Capturing the order serial number on the POS software is supported.
- Input of remarks is supported.
### 4. Seamless connection to POS software is supported in Plug-In mode.
- You can customize the option of simulating cashier to click **Receive Money** on the POS software when the payment window pops up.
- You can customize the option of simulating cashier to click **Done** on the POS software when money is received.
### 5. Receive money in Full mode
- Creation, query, import and export of commodities are supported
- Full-featured payment, simple payment, and total-amount payment are available.
### 6. Printing receipts
- Both printing with driver and serial and parallel printing without driver are supported.
- You can customize receipt width, number of copies of printed receipts, top and bottom margins, font size (for printer with driver), interval between receipts printed, and other parameters.
### 7. Merchant reconciliation
- You can check the details of the orders and refunds on the POS plug-in and export them to an Excel file.
- You can print summary and calculate the total amount received automatically.
### 8. Refund
- Partial refund is supported.
- An unauthorized clerk has no permission for refund. Store manager must authorize such clerk by scanning QR code before the clerk can perform the refund operation.
### 9. Keyboard shortcuts
- Display or hide Cloud Pay POS Terminal: **Ctrl**+**E**.
- Navigation bar (Full mode) - Login: **L** or **F1**; Payment: **C** or **F2**; Commodity Management: **G** or **F3**; Order Query: **P** or **F4**; Refund Operation: **R** or **F5**; Basic configurations: **D** or **F6**; Printer Configurations: **Y** or **F7**; Shortcut Key Configurations: **S** or **F8**.
- Navigation bar (Plug-In mode) - Login: **L** or **F1**; Order Query: **P** or **F2**; Refund Operation: **R** or **F3**; Basic Configurations: **D** or **F4**; Printer Configurations: **Y** or **F5**; Shortcut key Configurations: **S** or **F6**.
- Order Query - Display order summary: **H**; Print order summary (in Order Summary window): **H**; Cancel: **Esc**.
- Order Query - select an order and copy the order ID: **Ctrl**+**C**; Display refund pop-up: **R**; Edit order remarks: **E**; Print order: **P**.
- Payment - Open or close payment window: **~** (this can be customized). It can also be closed by pressing Esc.
- Configurations - Positioning the payment amount: **Ctrl**+**Shift**+**P** (this can be customized); right-click to exit the positioning of payment amount.
- Others - Switching between window controls: Tab or arrow keys; Confirm: **Enter**.
### 10. Security
- Sensitive information protection: Merchant's sensitive information such as client key is encrypted to prevent the sensitive information from being leaked or tampered with when the POS computer is infected with virus.
- The reconciliation between local statement and statement on Cloud Pay service side is made in near-real-time. In case of an abnormal transaction (for example, a difference in order amount between local and cloud), the POS terminal stops payment and refund automatically to prevent further losses of merchant. The merchant can request service provider to contact Cloud Pay for solution. The POS terminal can be resumed after being reconfigured and restarted. 
## Requirements for the running environment of Cloud Pay POS terminal
- Cloud Pay only runs in a Windows environment, including:
√ Windows XP SP3
√ Windows7, Windwos7 SP1
√ Windows10
## Configure information of service provider, sub-merchants and stores on Cloud Pay
### 1. Configure service provider
- Be sure to activate service provider administrator permissions. For more information, please see: https://cloud.tencent.com/document/product/569/9796.
### 2. Configure sub-merchants
- Please see https://cloud.tencent.com/document/product/569/9795. Be sure to save the authentication key and signature private key, as shown below:
![](https://mc.qcloudimg.com/static/img/a562c95676b1d70027acf79d17549f1d/image.png)   
- If you have lost the authentication key and signature private key, go to "Sub-Merchant Details" to reset the keys (Resetting the keys will result in the payment failure of the sub-merchant who is using Cloud Pay). After clicking **Reset Key**, save the authentication key and signature private key (After resetting, the client's authentication key and the signature private key need to be reconfigured), as shown below:   
![](https://mc.qcloudimg.com/static/img/e8c8c8b7f1eac3ae5964d07c1444a39f/1.png)   
### 3. Configure store
- Add and activate store clerks, and add POS devices, with the device type set as "Pay by Card". For more information, please see: https://cloud.tencent.com/document/product/569/9797.
## Service provider configures POS terminal
### 1. Check the Cloud Pay sub-merchant account.
![](https://mc.qcloudimg.com/static/img/9befe70b634d7f70646e0f674171b385/1.png)   
### 2. Install Microsoft .NET Framework 4
- Microsoft .NET Framework 4 is required before you can run the POS terminal. Microsoft official download link is:
 https://www.microsoft.com/zh-cn/download/details.aspx?id=17718
 ### 3. Service provider logs in to the POS terminal as administrator
- Adjust the window size: When you use the terminal for the first time, the software window size may not match the size of the PC screen. Resize the window to match the PC screen. The adjusted size will be saved and no adjustment is needed later.
- Enter the Cloud Pay sub-merchant account and click to generate a login QR code. When the QR code pops up, scan the code to log in with the service provider administrator's WeChat (permissions need to be activated by scanning QR code with service provider administrator's WeChat).
- Enter the Cloud Pay sub-merchant account and click to generate a login QR code. When the QR code pops up, scan the code to log in with the service provider administrator's WeChat (permissions need to be activated by scanning QR code with service provider administrator's WeChat).
- To allow a merchant's POS terminal that resides in an LAN to access the Internet via a proxy, click **Configure Proxy** to set the address of the HTTP proxy built by the merchant as well as the user name and password.
![](https://mc.qcloudimg.com/static/img/0ea123e87547a454494e9939dea2650a/1.png)   
### 4. Service provider configures POS terminal
- Software configurations for service provider include basic configurations, printer configurations and shortcut key configurations. Basic configurations are different between plug-in mode and full mode. Basic configurations in the plug-in mode include store, device ID, settings related to capturing amount upon payment, authentication key, signature private key and welcoming words. The configurations in the full mode do not include settings related to capturing amount upon payment. Printer configurations are same in plug-in and full modes. Shortcut key configurations in the plug-in mode include shortcut keys for displaying/hiding main window, triggering/hiding payment window, capturing amount position as well as keyboard messages triggered before payment window is called up and those triggered after completion of payment. Shortcut key configurations in full mode only involves the shortcut keys for displaying/hiding main window. 
#### 4.1 Basic configurations
![](https://mc.qcloudimg.com/static/img/8af791df24826c36a4e9b8f0580850aa/1.png)  
- Configuration field description:
√ Store ID and Device ID: The store ID and device ID added when you configured the store. Do not configure the same store ID and device ID for different POS devices. Otherwise, it will result in duplicate order IDs and thus cause losses of merchant. The reconciliation program in the POS terminal can identify this exception and stop the running of POS software.
√ Select Mode: This includes plug-in mode and full mode. The plug-in mode is used with other POS software, and full mode is a complete POS software with commodity management features.
√ Auto Capture of Amount and Manually Input Amount: In the plug-in mode, only one of the two options can be selected. The option "Auto Capture of Amount" is used with other POS software to capture the amount at the selected position when the payment pop-up appears; the option "Manually Input Amount" is to scan the customer's payment code and input amount manually in the payment pop-up window, instead of capturing the amount on POS software. When the amount is input manually, press **Enter** to complete the payment. In the full mode, both of the radio buttons are not displayed.
√ Capture Amount after opening payment window with shortcut key **~**: In the plug-in mode, press the shortcut key **~** to open the payment window. If this option is selected, the amount is captured automatically when the payment pop-up window opens. You can use this option to test whether the captured amount is correct. It is not recommenced to select it in the actual use of the software. You can open the payment window manually to input amount and scan the payment code to complete the payment.
√ Capture Serial Number: Select this option to capture serial number by using the "Position Serial Number" below. The captured content is saved to the remarks in the bill.
√ Call up Payment Window by Scanning Code: You can configure whether the bar code scanner calls up the payment window. If this option is selected, the payment window is called up; if not, the content scanned by the bar code scanner is not captured.
√ Preprocess Captured Image: Generally, the amount image is recognized directly. If the POS device runs well, the option is not required. But if the image cannot be recognized well without preprocessing, you can choose this option to enhance the recognition effect.
√ Zoom in on Captured File: If the numbers in the amount captured from the screen is very small, you can select this option to zoom in on the captured amount for a better recognition effect.
√ Support Touch Screen: Touch screen is provided for POS devices without a keyboard. After this option is selected, the shortcut icon for calling up the payment window is added to the desktop and the **Confirm** and **Cancel** buttons are added to the payment window. After the text box of total amount is selected, a virtual keyboard will pop up for modifying and inputting amount.
√ Display Duration in Payment Window After Payment: In the plug-in mode, the display duration of payment result in the window after payment is made on POS terminal. If it is set to 0, the result disappears within 0.1s. It is recommended to set it to 2s at the early stage to make it easier to check the payment result, and set it to 0 later when you need to improve the efficiency. In the full mode, this option is not displayed in the drop-down menu.
√ Time for Confirming Payment Amount Manually: In the plug-in mode, if **Auto Capture of Amount** is selected, auto payment feature is enabled. Time for confirming payment amount manually refers to the time the cashier has to wait before the auto payment after the payment pop-up appears, amount is captured and payment code is input. If it is set to 0, the payment is made within 0.1s. There is a possibility that the captured amount is incorrect due to the incorrect positioning of captured window. Therefore, it is recommended to select **Manual Confirmation** at the early stage to confirm the correctness of amount and modify the incorrect amount manually or exit payment by pressing **Esc**. After the terminal has been operated normally for some time and the captured amount is always correct, configure it to 0 to improve the payment efficiency. If **Manual Confirmation** is selected, auto payment is unavailable. The cashier needs to press **Enter** to trigger the payment after confirming the amount manually. If the option of **Manually Input Amount** is selected, the "Time for confirming payment amount" is unavailable. In the full mode, Time for confirming payment amount manually is not displayed in the drop-down menu. 
√ Authentication Key and Signature Private Key: Cloud Pay sub-merchant's authentication key and signature private key, which are obtained when the sub-merchant is added. 
√ Receipt Printer Information: If the receipts need to be printed out, you need to configure the printer information, including the number of copies of printed receipts, interval between printed receipts, and select printer with a specification of 58mm or 88mm.
√ Welcoming Words: The words added at the bottom of a printed receipt.
√ Position Amount: In the plug-in mode, if you want to capture the amount, you need to position the amount to be captured with this option.
√ Position Serial Number: Serial numbers need to be captured some times when you use POS software in the plug-in mode. You can position the serial number with this option. 
√ Save Configuration: After all the above options are configured, click **Save Configuration** to save them.
√ Re-log in: When the configurations have been saved, the terminal is unavailable to service provider. It is necessary to click **Re-log in** and make the store clerk scan the QR code before the service provider can use it.
√ Reconfigure: If the configuration information is changed or the configuration is incorrect, click **Reconfigure** for a reconfiguration.
√ Software Update: The current version comes with the software update feature. If you are notified of a software update by the service provider after a new version has been released, you can click **Software Update**.
- The following error message indicates the authentication key entered is incorrect. In this case, enter a correct key. If the key is lost, reset it and then enter the correct key.
![](https://mc.qcloudimg.com/static/img/dcd5e7c7a7002330683a7c7aed55fb87/1.png)   
- The following error message indicates the signature private key entered is incorrect. In this case, enter the correct private key. If the private key is lost, reset it and then enter the correct private key.
![](https://mc.qcloudimg.com/static/img/8ae55e8a912c42911466e7294a704d4f/1.png)   
#### 4.2 Printer configurations
- Printer configurations include whether to enable receipt printer, copies of receipt, time interval between receipts, receipt paper width, font size, top/bottom margin and printing with/without driver.
![](https://mc.qcloudimg.com/static/img/3a0519e26e794b532fc70c76945f4ab1/2.png)   
- Configuration field descriptions
√ Enable Receipt Printing: Whether to print receipts after payment and refund.
√ Copies of Receipt: Number of copies of receipt after the payment is made successfully. One copy of refund receipt is printed by default.
√ Interval Between Receipts: Time interval between two printed receipts. This is suitable for the scenario where multiple receipts are printed for a bill. A larger interval can make it easier for cashier to tear up the receipt.
√ Receipt Paper Width: The actual width of printed receipt when printing with driver. The selected width should be consistent with that of the actual receipt paper. If the printing format is incorrect because of a special printer type, you can customize the width by entering an integer in the text box.
√ Top Margin: Top margin on the receipt printed out, which can be customized.
√ Bottom Margin: Bottom margin on the receipt printed out, which can be customized.
√ Printing with Driver: Suitable for a receipt printer with driver. When this is selected, you only need to select the receipt printer name to print the receipt.
√ Receipt Printer Name: When the receipt printer is enabled, select the printer name configured on the server.
![](https://mc.qcloudimg.com/static/img/e6b871c36e702b610265b12f67522da4/3.png)   
√ Printing Without Driver: Suitable for the all-in-on POS machine. The receipt printer is required to support Esc/Pos instruction set and the port type of receipt printer can be parallel, serial or USB. USB port is only used for testing and a receipt printer with a USB port often has a driver.
√ Port Type: The port type of receipt printer. Generally, a driverless receipt printer comes with parallel ports. You can select the type based on actual situation.
√ Select Port: Parallel port starts with LPT, and serial port with COM. You can select a port based on the receipt printer port. All the ports can be found via Device Manager. For serial port, it is required to configure the baud rate, data bits, parity, stop bits and flow control, all of which can be obtained from the self-test printing page of the receipt printer.
√ Test Printer: Test whether the printer works properly when all the parameters have been configured.
√ Save Configuration: Save the parameters to the local device to eliminate the need of reconfiguration.
#### 4.3 Shortcut key configuration
- Shortcut key configurations include global shortcut key configurations and the keyboard message configurations used with payment window in the plug-in mode. You need to select whether to enable this option first, then obtain the key values to be set by pressing single keys and key combinations in the text box, and then click **Save** to register or save these key values.
![](https://mc.qcloudimg.com/static/img/6b9bf3a58b6436c2a33f4a1613e9651d/4.png)   
- Configuration field descriptions
√ Show/Hide Main Window: Set the shortcut keys for displaying and hiding the main window. Default is **Ctrl**+**E**.
√ Trigger/Hide Payment Window: Set the shortcut keys for displaying and hiding the payment window. Default is **~**. It only takes effect in plug-in mode.
√ Capture Amount Position: Set the shortcut keys for capturing amount position. Default is **Ctrl**+**Shift**+**P**. It only takes effect in plug-in mode.
√ Keyboard message triggered before payment window is called up by scanning code: Used with other POS software. When the QR code is scanned, the set key values are input before the payment window is called up based on the payment code type. It only takes effect in the plug-in mode.
√ Keyboard message triggered after payment: The keyboard message sent to the system when payment is completed via the payment window. The set key values are input based on payment types. It only takes effect in the plug-in mode.
### 5. Position the payment amount to be captured
- In the plug-in mode, if the **Auto Capture of Amount** radio button is selected, you need to position the payment amount. After enabling the POS software, locate the total payment amount, click **Position Payment Amount** on the POS terminal to enclose the payment amount area as shown below. The ￥ symbol and other content can be included, which will be automatically filtered out by the the terminal later. After the positioning, click **Save Configuration** on the POS terminal to save all the configurations so that you need not to select the amount position next time. This option is not displayed in the Full mode.
![](https://mc.qcloudimg.com/static/img/8e647e84bef5f19842537786daefecd0/1.png)  
### 6. Reconfigure merchant information
- If service provider needs to reconfigure the merchant information, click **Reconfigure**.
![](https://mc.qcloudimg.com/static/img/03e97a26cd4add509a19c26263b0ab1d/1.png)  
## Merchant receives money in the plug-in mode
### 1. Store manager or clerk logs in to the POS terminal as administrator by scanning the QR code
- Service provider needs to select **Service Provider Logs in as Store Manager or Clerk** to enter the payment screen.
![](https://mc.qcloudimg.com/static/img/0f0d74b5825ba5b3ab39a8740f75df30/image.png)   
### 2. Store manager or clerk configures POS terminal as administrator
- If service provider or merchant's administrator scans the QR code and the merchant has multiple stores, select a store; otherwise, you can only configure the device ID and select mode.
- You can select **Auto Capture of Amount** and **Manually Input Amount** in the same way for service provider.
- You can configure the printer and shortcut keys in the same way for service provider.
![](https://mc.qcloudimg.com/static/img/a014b7f98eaf50597560b5c1676c9475/5.png)   
- Click **Save Configuration** to enter the order query page, and then click the **Close** button at the upper right corner to make the POS terminal run at the backend. Now, you can start to receive money.   
![](https://mc.qcloudimg.com/static/img/3b9c6f3c56ca90a1d6cefa5ab0a84431/5.2.png)   
### 3. Receive money 
- When the POS terminal runs at the backend, merchant starts to receive money with the POS software by scanning the payment code on the customer's mobile phone. A payment window will pop up. If **Auto Capture of Amount** is selected, the amount at the amount position will be captured. After confirming the correctness of the captured amount, cashier presses **Enter** to confirm the payment. Cashier can also wait till the time for manually confirming payment amount runs out for an auto payment, or press the **Esc** or **~** key to exit payment. If **Cancel Amount Capture** is selected, cashier needs to manually input the amount, and then press **Enter**.
- The merchant can also press the **~** key to trigger the payment window (whether to capture the amount depends on the configuration), then enter or scan the payment code (when scanning the payment code, place the cursor within the payment code box). After entering the payment code manually, press **Enter** to initiate the payment. After the payment code is obtained via the bar code scanner, the payment is initiated automatically after a delay, which depends on the "Time for confirming payment manually" in the software configuration. The payment cannot be canceled once being initiated, unless it is canceled by the consumer, in which case a payment failure is returned. For an incorrect payment, go to **Refund**. 
![](https://mc.qcloudimg.com/static/img/6e4a7202d60cacb7c53d8d2a053ab46a/image.png)  
- After the payment is completed, the merchant selects the order and presses **E** to edit the order remarks. If **Capture Serial Number** is selected in the configuration, the captured serial number is displayed in the order remarks. It is left blank by default.
![](https://mc.qcloudimg.com/static/img/4afc0962901bf53aff7c60cb76c10dac/5.3.png)     
- The reconciliation between local statement and statement on Cloud Pay service side is made within the POS terminal in near-real-time. In case of an abnormal transaction (for example, a difference in order amount between local and cloud), the POS terminal stops payment and refund automatically to prevent further losses of merchant, as shown below. 
![](https://mc.qcloudimg.com/static/img/e445e9c2df5fb4571740e6f4221f3d9d/1.png)     
### 4. Refund
- On the order query page, select the order, press **R** to initiate a refund. In the refund window, the refund amount can be modified and partial refund is supported.
![](https://mc.qcloudimg.com/static/img/3164c87cff678db7be5b056436952561/11.png)   
- After you click **Confirm Refund**, **Back** and **View Refund** will be displayed. If you click **Back**, you will exit the refund window; if you click **View Refund**, you will go back to the refund operation page to view the refund status.
![](https://mc.qcloudimg.com/static/img/f93a4584c12b1b023d19208079dc4d24/12.png)   
- In the refund operation page, enter the order ID to initiate a refund (you can scan the order's bar code in the payment success message on the customer's mobile phone).
![](https://mc.qcloudimg.com/static/img/f09905c5e1130bd1f42e6629abd48866/3.png)    
- You can configure whether the store clerks have the refund permission. If a clerk without the refund permission needs to initiate a refund, a QR code will pop up and the authorization by store manager by scanning the QR code is needed. For a clerk with the refund permission, the refund process is same as that for the store manager.
![](https://mc.qcloudimg.com/static/img/6b48ac4d6746c96a31dcc5683e80b55c/4.png)   
- After the refund is completed successfully, the entries displayed in the order query and refund operation will be refreshed so that you can verify whether the refund is successful. If the refund is successful and **Enable Receipt Printer** is selected, the refund receipt is printed out automatically. 
![](https://mc.qcloudimg.com/static/img/7bf666d920a1e688527ba61abdba24e7/6.png)   
- If the receipt printer is not enabled when the refund is made, and the refund receipt is required to be printed out later, the receipt printer needs to be enabled. To enable the receipt printer, select the refund receipt to be printed out on the refund operation page, and then press **P**.
![](https://mc.qcloudimg.com/static/img/0bfbf3cee73460b3fd1e6da61c83ee29/7.png)   
### 5. Statistical summary
- View summary: Click **Print Summary** or press shortcut key **H**. The **Summary Preview** page will pop up. By default, The summary data for the first time is the summary for the current shift. The start time is the login time, the end time is the current time, and the summary is the summary of money received and refunded by the current loged-in clerk during this time period. The statistical summary can be modified manually and the options that can be modified include summary type, clerk name and summary period. After the modification, click **Re-summary** to update the data.
![](https://mc.qcloudimg.com/static/img/12f0ca01f7d6f3d5ff114797c79e2751/8.png)
- Print Summary: Click **Print** or press **H** to print the summary from the receipt printer. After printing is completed, click **Cancel** or press **Esc** to close the summary page.
![](https://mc.qcloudimg.com/static/img/731314f711520dbbe8c20ad0dd466e3d/9.png)   
- Next-shift Login: The clerk of next shift needs to click **Re-log in** to go to the login page and log in to the terminal by scanning QR code.
![](https://mc.qcloudimg.com/static/img/671f24796a78156543818c1b7ed048fd/image.png)   
## Merchant receives money in the full mode
### 1. Store manager or clerk logs in to the POS terminal by scanning the QR code.
- See "Log in to POS terminal in plug-in mode".
### 2. Store manager or clerk configures POS terminal
- See "Configure POS terminal in plug-in mode".
### 3. Commodity management
- Commodity management is supported in the full mode, including commodity query, new commodity import and other features.
![](https://mc.qcloudimg.com/static/img/782db9a5dc106273c61f91210ca77cd3/1.png)   
- Commodity Query: You can query commodities based on commodity ID, bar code, category and name by selecting the query category and entering the content you want to query in the text box. If nothing is entered in the text box, all commodities will be queried by default. If the commodity entries are listed in more than one page, you can scroll through pages by clicking **Previous Page**, **Next Page** and **Go to**.
![](https://mc.qcloudimg.com/static/img/3c3b108e0028762df2a037dd58d99baf/2.png)   
- New Commodity: Click **New Commodity**. The **New Commodity Information** dialog box will pop up. Fill in the required information and click **OK** to save the commodity.
![](https://mc.qcloudimg.com/static/img/0e0c4713c97f7a3e4159f8398baadc0d/3.png)   
- Modify Commodity Information: If any information of a saved commodity is incorrect, select the commodity entry and press **E** to edit this commodity.
![](https://mc.qcloudimg.com/static/img/f9c03b54f6fa6ee3af7cd090bf07cccd/4.png)   
- Delete Commodity: To delete a commodity, select the commodity to be deleted and press **E** key. A dialog box for confirming deletion will pop up. Click **OK** to delete the commodity. If you select **Cancel**, the commodity will not be deleted.
![](https://mc.qcloudimg.com/static/img/75febed32c1fd65e29b5933e65b6a667/5.png)   
- Import Commodities: The software allows importing commodities to an Excel file. Create an Excel file of commodities in a format shown below. Fill in the column headers first, and input the information of commodities in the rows under the headers.
![](https://mc.qcloudimg.com/static/img/05dce2054569db5f3b89d492f68b2c59/image.png)   
- Save the Excel file when it has been created. Return to the software, and click **Import Commodities**. A dialog box for selecting file will pop up. Select the file to be imported to start the automatic import.
![](https://mc.qcloudimg.com/static/img/04346b0084963919da0b6fb92a535032/1.png)   
- Export Commodity Inventory: The software allows exporting the commodity inventory information in an Excel file. Click **Export Inventory** to export the commodity inventory.
![](https://mc.qcloudimg.com/static/img/359e77709ae150fa63dbc2cbca56ad2a/10.png)   
### 4. Payment
- Three payment types are available in the full mode: full-featured payment, simple payment and total-amount payment. You can select and configure these modes in the software configuration.
![](https://mc.qcloudimg.com/static/img/29d487d319f6c6cafba235a06c1b1bad/1.png)   
- Full-featured payment: Select the commodity conditions, including commodity ID and bar code, enter the contents in the text box, and then press **Enter** or click **OK** to generate the commodity item purchased. If the purchase quantity of the same commodity is more than one, you can enter the commodity repeatedly or change the commodity quantity by pressing **+** and **-**. When the commodity bar code is selected, input the bar code via the bar code scanner, with the cursor placed within the text box.
![](https://mc.qcloudimg.com/static/img/4e65c8c6514c6d52d68f4c67d563731c/2.png)  
- When all the commodities purchased by the consumer are entered, you can receive the money by inputting the payment code in the payment code box and click **Receive Money**. The payment code can be input via bar code scanner. Place the focus in the payment code box, and then scan the payment code.
![](https://mc.qcloudimg.com/static/img/cff5178e1047c68ff0e7ef7ce3b8022e/3.png)   
- The POS software supports payment in cash. After the purchased commodity is entered, click **Receive Money in Cash**. The **Receive Money in Cash** dialog box will pop up. Enter the received amount and then click **OK**. To view the change amount, enter the amount and then press **Tab**.
![](https://mc.qcloudimg.com/static/img/9bb304708bf5acaec90a1892960eb312/5.png)     
- Simple payment: only supports receiving money for a single commodity. Select the commodity from the drop-down menu and then receive the money. In this mode, the **Receive Money**, **Receive Money in Cash** and payment code text box are same as those in the full-featured payment mode.
![](https://mc.qcloudimg.com/static/img/8865a5d59c39fec02f2fac5f9780e50c/6.png)      
- Total-amount payment: In this mode, you only need to enter a total amount and receive the money. Other features are same as those in the full-featured payment mode.
![](https://mc.qcloudimg.com/static/img/f177d6f95aa09bee3ac8c5b8cec1a9f3/7.png)   
### 5. Refund
- See "Refund in the plug-in mode".
## Install and Upgrade Software
- Start the POS plug-in, and then click the **Software Upgrade** button in **Software Configuration** to complete the upgrade.
![](https://mc.qcloudimg.com/static/img/aa6d3c3bd71725c65b9265c2df44002b/1.png)   
## Use Cloud Pay POS Terminal in a Proxy Network
- To ensure the network security, most of company employees work with their PCs in an LAN environment. To give the PCs in the LAN the access to the public network, a company will deploy a proxy server between the LAN and the public network (the proxy server itself can access the public network) so that the PCs in the LAN and the Cloud Pay POS Terminal can access the public network via this proxy server. For more information, please see [Build an HTTP Proxy](https://cloud.tencent.com/document/product/569/12641).

