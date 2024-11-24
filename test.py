import cmd

class MyConsole(cmd.Cmd):
    intro = '欢迎使用我的命令行控制台。输入 help 或 ? 来查看命令.'
    prompt = '(myconsole) '

    # 定义可用的命令
    commands = ['start', 'stop', 'status', 'exit']

    def do_start(self, arg):
        '启动系统'
        print("系统已启动")

    def do_stop(self, arg):
        '停止系统'
        print("系统已停止")

    def do_status(self, arg):
        '显示系统状态'
        print("系统状态良好")

    def do_exit(self, arg):
        '退出命令行'
        print("再见!")
        return True

    def complete_start(self, text, line, begidx, endidx):
        '补全 start 命令的参数'
        return [cmd for cmd in self.commands if cmd.startswith(text)]

    def complete_stop(self, text, line, begidx, endidx):
        '补全 stop 命令的参数'
        return [cmd for cmd in self.commands if cmd.startswith(text)]

    def complete_status(self, text, line, begidx, endidx):
        '补全 status 命令的参数'
        return [cmd for cmd in self.commands if cmd.startswith(text)]

    def complete_exit(self, text, line, begidx, endidx):
        '补全 exit 命令的参数'
        return [cmd for cmd in self.commands if cmd.startswith(text)]

# 启动命令行接口
if __name__ == '__main__':
    MyConsole().cmdloop()
