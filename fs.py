# -*- encoding:utf-8 -*-
''''
@Time : 2025/06/02 - 01:23:40 PM
@Author : 氢気氚 | qinch
@Version : 1.5.1
@Contact : BlueRectS@outlook.com
'''

import sys
import cmd
import os
import chardet
from colorama import init, Fore, Style
import json
import langs

init(autoreset=True)
env_dist = os.environ # environ是在os.py中定义的一个dict environ = {}

config_path = env_dist['HOMEDRIVE'] + env_dist['HOMEPATH'] + "\\Fs" 
print(config_path)
def Code_Detection(path, encoding, Error_Code):
    try:
        with open(path, 'rb') as f:
            result = chardet.detect(f.read())  # 读取一定量的数据进行编码检测
        if encoding == "auto":
            return result
        else:
            result["encoding"] = encoding
            return result
    except LookupError:
        print(Fore.RED + Error_Code[5])
        print(Fore.RED + Error_Code[6] +encoding)
    except IndexError:
        sys.exit()

def load_options(filename=f"{config_path}\\config.json"):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_options(options, filename=f"{config_path}\\config.json"):
    with open(filename, 'w') as f:
        json.dump(options, f, indent=4)

def ChangeTheLanguage(lang):
    
    if lang == "zh-CN":
        return langs.speech_zh, langs.Error_Code_zh
    elif lang == "en-US":
        return langs.speech_en, langs.Error_Code_en
print(os.getcwd())
class Consoles(cmd.Cmd):
    HelpfulTips = langs.HelpfulTips
    PersonalInformation = ["氢気氚 | qinch", "BlueRectS@outlook.com"]
    OpenEncodings = "auto"
    Language = "zh-CN"
    if os.path.exists(config_path) and os.path.exists(config_path+'\\config.json'):
        file_option = load_options()
        OpenEncodings = file_option['OpenEncodings']
        Language = file_option['Language']
    ValidLanguageCode = langs.ValidLanguageCode
    speech, Error_Code = ChangeTheLanguage(Language)
    intro = speech[0]
    Virtual_Text = []
    State = 'N'
    F = None
    path = ""
    line = 0
    temp = ""
    commands = ['load', 'show', 'i', 'o', 'del', 'unload', 'af', 
                'about', 'wq', 'q']
    try:
        result = Code_Detection(sys.argv[1], OpenEncodings, Error_Code)
        path = sys.argv[1]
        F = open(sys.argv[1], "r+", encoding=result["encoding"])
        State = 'H'
        prompt = f"[{F.name}]@{State}-[{line+1}]~>"
        Virtual_Text = F.readlines()
    except IndexError:
        State = 'V'
        path = "~Buffer_Files-fs.txt"
        if OpenEncodings == "auto":
                F = open("~Buffer_Files-fs.txt", "w+", encoding="utf-8")
                result = {'encoding':'utf-8'}
                result['encoding'] = 'utf-8'
                Virtual_Text = F.readlines()
                prompt = f"[{F.name}]@{State}-[{line+1}]~>"
        else:
            try:
                F = open("~Buffer_Files-fs.txt", "w+", encoding=OpenEncodings)
                result = {'encoding':OpenEncodings}
                result['encoding'] = OpenEncodings
                Virtual_Text = F.readlines()
                prompt = f"[{F.name}]@{State}-[{line+1}]~>"
            except LookupError:
                print(Fore.RED + Error_Code[5])
                print(Fore.RED + Error_Code[6] + OpenEncodings)
                os.remove("~Buffer_Files-fs.txt")
                sys.exit()
        
    def do_load(self, arg):
        '加载文件到缓冲区'
        self.F.close()
        if self.State == 'V':
            os.remove("~Buffer_Files-fs.txt")
        try:
            result = Code_Detection(arg, self.OpenEncodings, self.Error_Code)
            self.F = open(arg, "r+", encoding=result["encoding"])
            self.State = 'H'
            self.prompt = f"[{self.F.name}]@{self.State}-[{self.line+1}]~>"
            self.Virtual_Text = self.F.readlines()
            self.path = self.F.name
        except FileNotFoundError:
            print(Fore.RED+self.Error_Code[1])

    def do_show(self, arg=""):
        '展示文件内容'
        Error = 0
        if arg == "":
            print(f"===Show=== -> {1}:{len(self.Virtual_Text)} | {self.Error_Code[Error]}")
            k = 1
            for i in self.Virtual_Text:
                print(f"{k}|\t{i}", end="")
                k += 1
            print("\n", end="")
            print(f"===Show=== -> {1}:{len(self.Virtual_Text)} | {self.Error_Code[Error]}")
        else:
            try:
                parameter = arg.split( )
                if not len(parameter) > 2:
                    if len(parameter) == 1:
                        start = int(parameter[0]) - 1
                        k = 0
                        if start > len(self.Virtual_Text):
                            Error = 2
                        print(f"===Show=== -> {1}:{start+1} | {self.Error_Code[Error]}")
                        for i in self.Virtual_Text:
                            if k <= start:
                                print(f"{k+1}|\t{i}", end="")
                            k += 1
                        print("\n", end="")
                        print(f"\n===Show=== -> {1}:{start+1} | {self.Error_Code[Error]}")
                        Error = 0
                    elif len(parameter) == 2:
                        start = int(parameter[0]) - 1
                        stop = int(parameter[1]) - 1
                        k = 0
                        if start > len(self.Virtual_Text) or stop > len(self.Virtual_Text):
                            Error = 2
                        print(f"===Show=== -> {start+1}:{stop+1} | {self.Error_Code[Error]}")
                        for i in self.Virtual_Text:
                            if start <= k <= stop:# k >= start and k <= stop
                                print(f"{k+1}|\t{i}", end="")
                            k += 1
                        if stop == len(self.Virtual_Text):
                            print("\n", end="")
                        print(f"\n===Show=== -> {start+1}:{stop+1} | {self.Error_Code[Error]}")
                        Error = 0
                else:
                    print(Fore.RED + self.Error_Code[7])
            except ValueError:
                print(Fore.RED+self.Error_Code[3])
    def do_i(self, arg):
        '插入指定行(未指定则以光标所在行为准)输入 -end 可结束插入'
        o = self.State
        self.State = 'I'
        if self.line > len(self.Virtual_Text):
            for i in range(self.line - len(self.Virtual_Text)):
                self.Virtual_Text.append("\n")
        if arg == "":
            while True:
                temp = input(f"[{self.F.name}]@{self.State}-[{self.line+1}]~>")
                if temp == "-end":
                    self.State = o
                    break
                self.Virtual_Text.insert(self.line, temp + "\n")
                self.line += 1
        else:
            try:
                self.line = int(arg)
                while True:
                    temp = input(f"[{self.F.name}]@{self.State}-[{self.line+1}]~>")
                    if temp == "-end":
                        self.State = o
                        break
                    self.Virtual_Text.insert(self.line, temp + "\n")
                    self.line += 1
            except ValueError:
                print(Fore.RED+self.Error_Code[3])
    def do_o(self, arg):
        '覆写指定行(未指定则以光标所在行为准)输入 -end 可结束覆写'
        o = self.State
        self.State = 'W'
        if self.line > len(self.Virtual_Text):
            for i in range(self.line):
                self.Virtual_Text.append("\n")
        if arg == "":
            while True:
                try:
                    temp = input(f"[{self.F.name}]@{self.State}-[{self.line+1}]~>")
                    if temp == "-end":
                        self.State = o
                        break
                    else:
                        self.Virtual_Text[self.line] = temp+"\n"
                        self.line += 1
                except IndexError:
                    self.Virtual_Text.append(temp+"\n")
                    self.line += 1
            self.prompt = f"[{self.F.name}]@{self.State}-[{self.line+1}]~>"
        else:
            try:
                self.line = int(arg) - 1
                while True:
                        temp = input(f"[{self.F.name}]@{self.State}-[{self.line+1}]~>")
                        if temp == "-end":
                            self.State = o
                            break
                        else:
                            self.Virtual_Text[self.line] = temp+"\n"
                            self.line += 1
            except IndexError:
                self.Virtual_Text.append(temp+"\n")
            except ValueError:
                print(self.Error_Code[3])
    def do_del(self, arg):
        '删除多行或指定删除单行'
        parameter = arg.split( )
        try:
            if len(parameter) == 1:
                    temp = int(arg) - 1
                    del self.Virtual_Text[temp]
            elif len(parameter) == 2:
                    del self.Virtual_Text[int(parameter[0]) - 1: int(parameter[1]) - 1]
        except ValueError:
            print(Fore.RED+self.Error_Code[3])
        except IndexError:
            print(Fore.RED+self.Error_Code[2])
    def do_line(self, arg):
        '查看行或是更改行'
        if arg == "":
            print(self.line+1)
        else:
            try:
                self.line = int(arg) - 1
                self.prompt = f"[{self.F.name}]@{self.State}-[{self.line+1}]~>"
            except ValueError:
                print(Fore.RED+self.Error_Code[3])
    def do_unload(self, arg):
        '将当前文件弹出'
        self.F.close()
        self.path = "~Buffer_Files-fs.txt"
        self.line = 0
        self.State = 'N'
        self.Virtual_Text = []
        self.prompt = f"[{self.path}]@{self.State}-[{self.line+1}]~>"
    def do_config(self, arg):
        '配置临时设置或是生成配置文件'
        temp = ""
        partition = arg.split( )
        options = {
            "OpenEncodings": f"{self.OpenEncodings}",
            "Language": f"{self.Language}"
        }
        if arg == "new":
            if os.path.exists(config_path+'\\config.json'):
                temp = input(self.speech[1])
                if temp == "Y" or "y" or "":
                    f = open(config_path+'\\config.json', 'w')
                    f.close()
                    save_options(options)
                elif temp == "N" or "n":
                    pass
            else:
                if not os.path.exists(config_path):
                    os.mkdir(config_path)
                f = open(f"{config_path}\\config.json", 'w')
                f.close()
                save_options(options)
        elif arg == "res":
            save_options(options)
        elif arg == "write":
            save_options(options)
        elif partition[0] == "encoding":
            if len(partition) == 1:
                print(self.OpenEncodings)
            else:
                self.OpenEncodings = partition[1]
        elif partition[0] == "language":
            if len(partition) == 1:
                print(self.Language)
            else:
                if partition[1] in self.ValidLanguageCode:
                    self.Language = partition[1]
                    self.speech, self.Error_Code = ChangeTheLanguage(self.Language)
                else:
                    print(Fore.RED+self.speech[10])
    def do_w(self, arg):
        '将缓冲区的文本写入文件'
        self.F.close()
        self.F = open(self.path, "w+", encoding=self.result["encoding"])
        self.F.writelines(self.Virtual_Text)
        self.F.close()
        if self.State == 'V' or self.State == 'N':
            while True:
                    answer = input(self.speech[2])
                    if answer == "Yes" or "Y" or "y" or "":
                        try:
                            name = input(self.speech[3])
                            os.rename("~Buffer_Files-fs.txt", name)
                            self.State = 'H'
                            self.path = name
                            self.F = open(self.path, "r+", encoding="utf-8")
                            self.State = 'H'
                            self.prompt = f"[{self.F.name}]@{self.State}-[{self.line+1}]~>"
                            break
                        except FileNotFoundError:
                            print(Fore.RED+self.Error_Code[4])
                        except FileExistsError:
                            print(Fore.RED+self.Error_Code[4])
                    else:
                        break
        else:
            self.F = open(self.path, "r+", encoding=self.result["encoding"])
            self.State = 'H'
            self.prompt = f"[{self.F.name}]@{self.State}-[{self.line+1}]~>"
    def do_af(self, arg):
        '关于正在编辑文件的信息'
        print(self.speech[4] + self.F.name)
        print(self.speech[5] + self.State)
        print(self.speech[6] + str(len(self.Virtual_Text)+1))
        print(self.speech[7] + str(self.line+1))
        print(self.speech[8] + self.result['encoding'])
    def do_about(self, arg):
        '显示关于信息'
        print(langs.Version)
        print(self.speech[11] + self.PersonalInformation[0])
        print(self.speech[12] + self.PersonalInformation[1])
    def do_wq(self, arg):
        '将缓冲区的文本写入文件并退出fs'
        self.F.close()
        self.F = open(self.path, "w+", encoding=self.result["encoding"])
        self.F.writelines(self.Virtual_Text)
        self.F.close()
        
        if self.State == 'V' or self.State == 'N':
            while True:
                    answer = input(self.speech[2])
                    if answer == "Yes" or answer == "Y" or answer == "y" or answer == "":
                        try:
                            name = input(self.speech[3])
                            os.rename("~Buffer_Files-fs.txt", name)
                            self.State = 'H'
                            self.path = name
                            break
                        except FileNotFoundError:
                            print(self.Error_Code[4])
                        except FileExistsError:
                            print(self.Error_Code[4])
                    else:
                        os.remove("~Buffer_Files-fs.txt")
        print(self.speech[9])
        return True
    def do_q(self, arg):
        '退出 fs'
        self.F.close()
        if self.State == 'V':
            os.remove("~Buffer_Files-fs.txt")
        print(self.speech[9])
        return True
    def do_help(self, arg):
        if arg == '':
            for i in self.commands:
                print(f"{i}\t", end='')
            print("\n")
        else:
            temp = self.HelpfulTips[arg] 
            if self.Language == 'zh-CN':
                print(temp[0])
            elif self.Language == 'en-US':
                print(temp[1])  
    def default(self, line):
        print(Fore.RED+self.Error_Code[8])
    
conseols = Consoles(completekey="tab")
conseols.cmdloop()
