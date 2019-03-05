This document introduces how to upload MTA Android Crash V2 symbol table and contains two parts: Java Symbol Table and Native (C/C++) Symbol Table, which is used for obfuscated stack information after the system is restored.

### Java Symbol Table
1. Eclipse
Symbol table is generally named "mapping.txt" and located in the proguard directory. If the symbol table is compiled using the ant script, it resides in the specified directory.
2. Android Studio
Enable obfuscated code in the build.gradle file. A mapping file is generated when minifyEnabled is set to true, and its path is `build/outputs/mapping/release/mapping.txt` under the project directory.
![](http://developer.qq.com/wiki/mta/imgs/20170524182818_63386.png)
![](http://developer.qq.com/wiki/mta/imgs/20170524182930_41284.png)
3. Upload Java symbol table
Open the upload page of symbol table in the foreground, enter App version number, then select **Java** for file type, click **Select File** to select the mapping.txt file, and click **Upload**.
![](http://developer.qq.com/wiki/mta/imgs/20170524183030_67938.png)

### Native Symbol Table

Native symbol table is used to restore Crash stack to retrieve so file. Because of the compiler, the published so file does not contain any symbol, only intermediate files generated during compiling contains symbol table. So, it is recommended to back up the debug so file every time you build so file.
1. Eclipse
Build the so file with Eclipse. The debug so file is located in the directory `/obj/local/xxxeabi/`. "xxxeabi" is the architecture information, as shown below:
![](http://developer.qq.com/wiki/mta/imgs/20170524183109_57363.png)
The Objs directory under the architecture should be removed before we can package the local directory.
2. Android Studio
The so file compiled with Android Studio has two versions: Debug and Release. The directories to these two versions are `/<Module>/build/intermediates/cmake/debug/obj/xxxeabi/` and `/<Module>/build/intermediates/cmake/release/obj/xxxeabi/`. We need to package the entire obj directory into a zip file.
![](http://developer.qq.com/wiki/mta/imgs/20170524183147_55166.png)
Path varies with different Android studio versions, which can be determined by following the method below. Take Linux/Mac OS system as an example:
(1) Open terminal command line, then go to the current project directory by executing cd command, and enter `find ./ -name your-lib-name.so` to locate the directory generated during the compiling of so file.
![](http://developer.qq.com/wiki/mta/imgs/20170524183225_69933.png)
(2) Enter `file your-full-so-path`. If [not stripped] is outputted, the so file contains symbol table information. If [stripped] is outputted, all symbol table information is deleted from the so file.
![](http://developer.qq.com/wiki/mta/imgs/20170524183233_30230.png)
3. Upload Native Symbol Table
Open the upload page of symbol table in the foreground, enter App version number, then select **native** for file type, click **Select File** to select the packaged zip file, and click **Upload**.
