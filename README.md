# fs 是一个使用python编写的终端文本编辑程序，灵感来源于Unix的ed编辑器

该应用共有5种状态分别是 V,H,N,I,O

Tips：命令参数应用空格隔开，示例：show 5 10 查看5到10行的文件内容

# 各个状态的释义

V:虚拟缓冲区文件打开方式,该状态是在 fs 未附加参数是进入的状态。该模式会在工作目录下暂时生产一个名为"Buffer_Files-fs.txt"的缓冲区文件。

H:有对应读写文件，该状态是在fs附加参数或是使用了 load 激活的。

N:无文件状态，该状态在使用了 unload 命令后激活的

I:连续插入状态，该状态在使用 i 命令后激活的，进入后可连续插入内容，在输入-end后退出 I 状态

O:覆写状态，该状态在使用 o 命令后激活的，进入后可连续覆写多行，在输入-end后退出 O 状态

# 提示符释义

一般情况下提示符样式大体如下

```bash
[Buffer_Files-fs.txt]@V-[1]~>
      |               |   \
打开的文件名      文件状态  行号
```

# 附加参数

fs 附加参数: fs [file(可选)]	file用于指定fs打开文件,不指定则会创建一个名为"Buffer_Files-fs.txt"的缓冲区文件(暂时的)。

程序内命令的附加参数:

fs 共有11个命令	line，show，i，o，w，wq，q，load，unload，del，help/?

line [lines]		line用于查看行号，附加参数后用于改变行号

show [start stop]	show用于查看文件内容，不附加参数内容查看全部的文件内容，附加一个参数默认从附加参数提供的行号打印到文件末，附加2个参数则打印区间文件内容

i [line]			i用于插入行并写入内容，不附加参数则以当前光标所在行添加行，附加参数则在指定行插入

o [line]			和i用法相似只不过是覆写，不会添加新行，会在原来行上重写，进入O状态

w				将缓冲区的文本写入当前编辑文件，进入H状态

wq				将缓冲区的文本写入当前编辑文件并退出，进入H状态

q				不将缓冲区的文件写入当前编辑文件，而是直接退出

load [file]			加载一个文件到缓冲区，进入H状态

unload			将当前编辑文件弹出并清空缓冲区，进入N状态

del [start stop]	删除区间行或是删除指定行，附加一个参数是删除参数指定行，附加两个参数是删除从参数1到参数2区间(不包括参数2所在行)的所有行

help/? [command]	帮助命令，不指定参数时列出使用命令，指定参数为编辑器内的命令可查看简单的命令介

af 				查看当前正在编辑文件的基本信息

about 查看本软件的基本信息