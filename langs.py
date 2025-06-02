speech_zh = [
    "欢迎! 键入 help 或 ? 来列出全部的命令.\n", 
	"配置文件已存在,是否覆盖(Y/N):",
	"是否保存该文件? (Yes/No)-[默认:Yes]",
	"这是一个新的文件，请输入文件名:",
	"文件名: ",
	"状态: ",
	"行数: ",
	"当前行: ",
	"文件编码: ",
	"fs已退出!",
	"不受支持的语言!",
	"作者: ",
	"联系方式: "
]
speech_en = [
    "Welcome! Type help or ? to list all the commands.\n",
    "The configuration file already exists, whether it is overridden (Y/N):",
    "Do you want to save the file? (Yes/No)-[Default: Yes]",
    "This is a new file, please enter the file name:",
    "FileName: ",
    "State: ",
    "Number of Lines: ",
    "Current Row: ",
    "File Encoding: ",
    "FS has exited!",
    "Unsupported Languages!",
    "Author: ",
    "Contact :"
]
Error_Code_zh = [
    "", "文件错误", "超出索引", "参数无效", 
	"非法的文件名", "编码错误", 
	"请检测你的配置文件,或是当前的设置,当前配置编码:", "参数过多", "未知的命令"
]
Error_Code_en = [
    "", "File Error", "Out Of Index", "The parameter is invalid",
	"Illegal File Name", "Encoding Errors",
	"Please check your profile, or the current settings, the current configuration code:",
	"Too Many Parameters", "Unknown Command"
]
HelpfulTips = {
    "load": ["加载文件到缓冲区","Load the file into the buffer"],
	"show": ["展示文件内容", "Present the contents of the file"],
	"i": ["插入指定行(未指定则以光标所在行为准)输入 -end 可结束插入", 
			"Insert the specified line (if not specified, the cursor will be accurate) and enter -end to end the insertion"],
	"o": ["覆写指定行(未指定则以光标所在行为准)输入 -end 可结束覆写", 
			"Overwrite the specified line (if not specified, the cursor is accurate), enter -end to end the override"],
	"del": ["删除多行或指定删除单行", 
			"Delete multiple rows or specify to delete a single line"],
	"line": ["查看行或是更改行", "View rows or change rows"],
	"unload": ["将当前文件弹出", "Ejects the current file"],
	"config": ["配置临时设置或是生成配置文件", 
				"Configure temporary settings or generate configuration files"],
	"w": ["将缓冲区的文本写入文件", 
			"Write the text of the buffer to a file"],
	"af": ["关于正在编辑文件的信息", 
			"Information about the file being edited"],
	"about": ["显示关于信息", 
				"Displays information about"],
	"wq": ["将缓冲区的文本写入文件并退出fs", 
			"Write the text of the buffer to the file and exit FS"],
	"q": ["退出 fs", "Exit FS"]
}
ValidLanguageCode = ['zh-CN', "en-US"]
Version = "1.5.1"