### What is error mapping table?
The error mapping table is a mapping table of memory addresses, function names, file names, and line numbers. The symbol table elements are shown as follows:
< Start address > < end address > < function > [< file name: line number >]
### Where is the error mapping table configured?
As shown in the figure below, the error mapping table can be configured in **Quality Monitoring** -> **Error Exception Monitoring** -> **Error List** -> **Error Mapping Table Management**.
![](http://developer.qq.com/wiki/mta/imgs/20170122151435_80781.jpg)
### Why does the error mapping table have to be configured?
To quickly and accurately locate where in the codes the user App crash occurs, you can use the error mapping table to resolve and restore the stack of the App Crash. For example:
The errors reported by iOS is shown on the left of the figure below. It is a bunch of memory addresses and offsets, and developers cannot obtain valid information from it. The right figure shows the errors restored using the error mapping table, from which developers can easily view the reported stack information.
![](http://developer.qq.com/wiki/mta/imgs/20170122151528_57718.jpg)
