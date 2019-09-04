'''MIT License

Copyright (c) 2019 HLS_Groffer

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''

################################
#为什么给MIT License? 因为那堆许可证看得我头疼
#Unlicense 不存在的，我这么自负的人这辈子都不可能Unlicense的(狗头)(申公豹式自豪：灵珠，我偷得！敖丙！我徒弟！这个，我写的！给License，就任性！)
#官方协助提供伙伴：https://www.baidu.com （大误）
#邮箱：2017221177@stu.bisu.edu.cn
################################

#方法目录：
#findFiles()找错题本文件
#newFile()比较完善的新建错题本文件技巧
#printElement(number_of_problem,elements)题目输出
#checkinput(textanswer,textjiexi,ck)判题
#inputcheck(text)录入内容确认
#recordtext(ck)录入界面
#writeFile(ck,text,options,answer,jiexi)将录入的内容写入文件
#countProblem(ck):题目计数器
#readFile(ck)读取文件
#exercise(ck,lines):正序和逆序做题方法
#ranEx(ck, lines): 随机顺序做题方法
#main()欢迎界面

import random
import os
path = os.getcwd()

#如果你要把你的错题本存在某个地方，将上面的path改成某个绝对地址应该就行了。记得用两个单引号圈起来，例如'D:\'。我没试过，不行百度。
#用os读取目录下的*.ctb文件（拓展名错题本首字母）。扫描错题本文件，返回列表

#查找错题本文件，返回错题本列表
def findFiles():
    files=os.listdir(path)
    ctbfiles=[]
    for name in files:
        if name.split('.')[-1]=='ctb':
            ctbfiles.append(name)
        else:
            pass
    return ctbfiles

#建立错题本文件
def newFile():
    failToWrite=False
    os.system('title 错题本    请输入新错题本名称')
    name=input('输入名字建立新的错题本\n')
    if os.path.isfile(name+'.ctb'):
        count=1
        altname=name
        while os.path.isfile(altname+'.ctb')==True:
             count=count+1
             altname=name+'('+str(count)+')'
        try:
            file=open(altname+'.ctb','w')
        except:
            os.system('title 错题本        创建失败')
            print("可能存在写保护，未能成功创建 "+altname+'.ctb\n')
            failToWrite=True
        #检查
        if os.path.isfile(altname+'.ctb'):
            os.system('title 错题本        '+altname+'.ctb'+'    创建成功')
            print("存在重名文件，已更名为 "+altname+'.ctb'+" 并创建成功！\n")
        else:
            pass
    else:
        try:
            file=open(name+'.ctb','w')
        except:
            os.system('title 错题本        创建失败')
            print("可能存在写保护，未能成功创建 "+name+'.ctb\n')
            failToWrite=True
        #检查
        if os.path.isfile(name+'.ctb'):
            print("创建 "+name+'.ctb'+" 成功！\n")
            os.system('title 错题本        '+name+'.ctb'+'    创建成功')
        else:
            pass
    try:
        file.close()
    except:
        if failToWrite:
            pass
        else:
            print('file.close没成功，这个程序退出以后应该就能动它了…………')
    return 0

#打印题目和选项
def printElement(number_of_problem,elements):
    element=elements[1].split(';')
    print(str(number_of_problem)+'. '+elements[0])#打印题目
    for y in element:
        print(y)
    return 0

#检查答案,返回正误
def checkinput(textanswer,textjiexi,ck):
    os.system('title 错题本        '+ck+'    请输入答案    !new建新题    !quit退出'+ck)
    answerInput=str.upper(input("请输入答案，多选按顺序无间隔输入。!new建新题,!quit退出\n"))
    if str.lower(answerInput)=="!new":
        return recordtext(ck) 
    if str.lower(answerInput)=="!quit":
        return 0
    if str.upper(answerInput)==textanswer:
        print("恭喜回答正确\n"+textjiexi)
        os.system('color 2f')
        return "Right"
    else:
        print('答案错误。正确答案是：'+textanswer+'\n'+textjiexi)
        os.system('color cf')
        return "Wrong"
    
def inputcheck(text):
    #print (text.find('\t'))
    print("您的输入是“"+text+"”。")
    #查空格
    onlySpace=True
    for x in text.split(' '):
        if x !='':
            onlySpace=False
        else:
            pass
    #查空白
    if text=='':
        print("本次您没有输入任何内容！请重新输入！")
        return 'continue'
    else:
        pass
    if onlySpace==True:
        print('为何跟自己过不去，只打空格呢？？请重新输入！')
        return 'continue'
    else:
        pass
    #查Tab
    if text.find('\t')!=-1:          
        print('请不要在输入中包含Tab，它是ctb文件的分隔符。')
        return 'continue'
    
    try:#为选项检查是否有空选项（不是很必要，但是如果有这么干的做题的时候就会有一堆空行）
        splitTexts=text.split(';')
        nullsplit=False
        del splitTexts[-1]
        for x in splitTexts:
            if x=='':
                nullsplit=True
            else:
                pass
    except:
        pass
    if nullsplit==True:
        print('提示：每个英文分号前应当有内容！（可忽略） 如果在录入选项时空分号会导致莫名其面的空行')
    else:
        pass
    os.system('title 输入检查    是：y    否：回车')
    check=input("是否重输？是：y；否：回车")
    while True:
        if str.lower(check)=='y':
            return "continue"
        elif check=='':
            return "break"
        else:
            print('您的输入有误')
            check=input("是否重输？是：y；否：回车")
#录入错题
def recordtext(ck):
    waitingInput=True
    while waitingInput:
        while waitingInput:
            os.system('color')
            os.system('title 错题本        '+ck+'    输入内容    回车退出编辑')
            text=input("请输入题目，回车结束。直接回车退出编辑，返回欢迎界面\n")
            if text=='':
                waitingInput=False
                break
            else:
                pass
            result=inputcheck(text)
            if result=='continue':
                continue
            elif result=='break':
                break
            else:
                pass
        while waitingInput:
            os.system('title 错题本        '+ck+'    输入内容    回车继续')
            options=input("请输入选项，用英文分号;分割，回车键结束。\n")
            result=inputcheck(options)
            if result=='continue':
                continue
            elif result=='break':
                break
            else:
                pass
        while waitingInput:
            os.system('title 错题本        '+ck+'    输入内容    回车结束编辑')
            answer=str.upper(input("请输入正确答案，多选按字母顺序无间隔输入，不区分大小写。\n"))
            result=inputcheck(answer)
            if result=='continue':
                continue
            elif result=='break':
                break
            else:
                pass
        while waitingInput:
            os.system('title 错题本        '+ck+'    输入内容    回车结束编辑')
            jiexi=input("请输入解析。回车键结束。不支持解析间换行\n")#因为我才疏学浅，不会
            result=inputcheck(jiexi)
            if result=='continue':
                continue
            elif result=='break':
                break
            else:
                pass
        if waitingInput==False:
            return 0
        os.system('title 错题本        '+ck+'    Y/y    N/n')
        finalcheck=input("您输入的题目是\n"+text+'\n'+options+'\n'+answer+'\n'+jiexi+"\n是否正确录入并写入笔记本？Y/N\n")
        invalidinput=True
        while invalidinput:
            if str.upper(finalcheck)=='Y':
                writeFile(ck,text,options,answer,jiexi)
                print("已写入")
                #Check whether the files were written successfully if time permits
                #Unfortunately, time may permits, but my energy have already used up.
                invalidinput=False
            elif str.upper(finalcheck)=='N':
                os.system('title 错题本        '+ck+'确认重输？    确认：N/n')
                if str.upper(input('确定要重新输入吗？再次输入N放弃之前的输入。此操作不可恢复'))=='N':
                    recordtext(ck)
                    return 0
                else:
                    pass
            else:
                finalcheck=input("/n您输入的题目是\n"+text+'\n'+options+'\n'+answer+"\n是否正确？Y/N\n")
    return 0
#写入文件
def writeFile(ck,text,options,answer,jiexi):
    afile=open(ck,'a')
    afile.write(text+"\t"+options+'\t'+answer+'\t'+jiexi+'\n')

#题目计数器
def countProblem(ck):
    rfile=open(ck,"r")
    lines=rfile.readlines()
    rfile.close()
    return len(lines)

#读取
#结构：题目\t选项A;选项B,;选项C;选项D...\t正确选项正确选项\t解析\n
def readFile(ck):
    rfile=open(ck,"r")
    lines=rfile.readlines()
    rfile.close()
    if lines==[]:
        os.system('title 错题本        '+ck+'    是：Y/y  否：其他')
        print("空错题本！是否录入新题？Y")
        ifrecord=input()
        if str.upper(ifrecord)=="Y":
            recordtext(ck)
            return 0
        else:
            print("反正你输的不是‘Y’或者”y“，回主页面了……")
            return 0
    os.system('title 错题本        '+ck+'        Y：是 N：否 R：随机  new输入新题    quit退出错题本')
    shunxu=str.upper(input("是否从新向旧顺序出题？Y是，N否，R打破顺序 new建新题\n"))
    if str.lower(shunxu)=="new":
        return recordtext(ck) 
    if str.lower(shunxu)=="quit":
        return 0
    if shunxu=="Y":
        lines=lines[::-1]
        print('将按照时间顺序从新向旧出题！')
        exercise(ck,lines)
        return 0
    if shunxu=="N":
        print('将按照时间顺序从旧向新出题！')
        exercise(ck,lines)
        return 0
    if shunxu=="R":
        print('将不重不漏随机出题！')
        number_of_problem=1
        ranEx(ck,lines,number_of_problem)
        return 0
    else:
        print("您的输入有误!")
        readFile(ck)
        return 0
#顺序和逆序做题方法
def exercise(ck,lines):
    number_of_problem=1
    for x in lines:
        if x=='\n':
            continue
        else:
            #try:
                elements=x.split("\t")
                printElement(number_of_problem,elements)#这一句是打印题目和选项的
                number_of_problem=number_of_problem+1
                ifcorrect=checkinput(elements[2],elements[3],ck)
                if ifcorrect==0:
                    return 0
                else:
                    continue
            #except:
                print('试题读取出错，ctb文件存在异常'+ck)
                print('异常的行："'+x+'"')
    print('您已做完所有收藏的错题！\n')
    return 0
#不重不漏随机做题法
def ranEx(ck,lines,number_of_problem):
    if len(lines)!=1:
        y=random.randint(0,len(lines)-1)
    else:
        y=0
    x=lines[y]
    if x=='\n':
        del lines[y]
    else:
        try:
            elements=x.split("\t")
            printElement(number_of_problem,elements)#这一句是打印题目和选项的
            number_of_problem=number_of_problem+1
            ifcorrect=checkinput(elements[2],elements[3],ck)
            if ifcorrect==0:
                return 0
            else:
                pass
        except:
            print('试题读取出错，ctb文件存在异常'+ck)
            print('异常的行："'+x+'"')
    del lines[y]
    if len(lines)!=0:
       ranEx(ck,lines,number_of_problem)
    else:
        print('您已做完所有收藏的错题！\n')
    return 0
#欢迎界面
def main():
    print("欢迎使用错题本！")
    ctb=findFiles()
    if ctb==[]:
        print("没有找到错题本！")
        choosebook=input("请输入new新建错题本")
    else:
        count=1
        for x in ctb:
            print(str(count)+'. ',x+'  (共'+str(countProblem(ctb[count-1]))+'题)')
            count=count+1
        os.system('title 错题本        输入序号或名称打开错题本。    new新建错题本    help帮助页    quit退出')
        choosebook=input("输入序号打开错题本，输入“new”创建新错题本,输入help查看帮助\n")
        if str.lower(choosebook)=="new":
            try:
                newFile()
            except:
                print("文件名不要输奇怪的东西！（例如Tab,\,/,?,*,<,>,|等\n")
            return 0
        if str.lower(choosebook)=="help":
            helpPage()
            return 0
        if str.lower(choosebook)=="quit":
            return 1
        else:
           '''#调试
            ck=ctb[int(choosebook)-1]
            os.system('title 错题本        '+ck+'    quit退出')
            readFile(ck)
            return 0
            
            '''#正常工作的版本
           pass
           
    try:
            if str.lower(choosebook)=="new":
                try:
                    newFile()
                except:
                    print("文件名不要输奇怪的东西！（例如Tab,\,/,?,*,<,>,|等\n")
                return 0
            if str.lower(choosebook)=="help":
                helpPage()
                return 0
            if str.lower(choosebook)=="quit":
                return 1
            try:
                ck=ctb[int(choosebook)-1]
                os.system('title 错题本        '+ck+'    quit退出')
                readFile(ck)
                return 0
            except:
                try:
                    readFile(choosebook+".ctb")
                    return 0
                except:
                    print('打开错题本失败，请检查输入，或者文件可能已被移动。\n')
                    return 0    
    except:
            print('操作失败，未知错误\n')
            #正常工作的版本结束点
            
#main() complete
def helpPage():
    os.system('cls')
    os.system('title 错题本        帮助页 HELP    任意键返回')
    print('################################HLS 2019 All rights reserved.\n这是一个用来回顾错题用的小程序\n邮箱：2017221177@stu.bisu.edu.cn\n################################\n')
    print('软件说明：\n错题本小程序建立错题本文件(.ctb)来储存数据，除非不再需要，不要删掉冒出来的ctb文件。如果看着不舒服，你可以把错题本小程序本身和ctb文件一起放在你喜欢的地方，之后向桌面发送快捷方式。')
    print('一个错题本文件不必存太多错题，你可以创建多个错题本，方便切换。')
    print('\n打开错题本：\n可以通过错题本序号和名称的方法打开错题本\n只有名称不与关键词冲突时才能用名称打开\n关键词包括new,quit和help。\n如果名称和序号冲突，以序号为准。')
    print('\n错题本的使用：\n除了在新建错题本和录入新题的任何时候，你都可以用quit返回上一层。欢迎页面quit则退出')
    print('错题本文件(.ctb)数据格式为每一行是一道题，题干、选项、正确答案和解析的分隔是Tab，每个选项之间的分隔是英文分号。错题本小程序自带错题录入功能，不需要钻研数据是怎么记在错题本里了。')
    print('错题本不具备重命名和删除试题的功能，有需要请用记事本打开ctb文件修改。如果修改后不能正常识别，可以整行删除然后重新录入。\nctb文件本质就是文本文档。修改的时候注意不要修改其中的分隔符或Tab，否则将不能被程序正确识别。如果修改细节可以直接修改，大面积还是整行删掉重新录入吧，除非你有英伟达的刀工（误）')
    print('大部分判断的情况错题本都不区分大小写，但是最好按照你舒服的大小写和提示的方法操作。')
    print('在用命令行打开的情况下，命令行窗口标题将显示可以进行的操作，在做题判断正误时候也会有背景颜色显示\n录入错题的时候一定要耐心仔细检查是否录入正确。\n')
    os.system('pause')
    os.system('cls')
    return 0
#一切就绪！
run=0
while run!=1:
    os.system('color 0f')
    run=main()

#查找文件方法if os.path.isfile(name+'.ctb'):
#file=open("tk.ctb","r")
#lines = file.readlines()
#print(lines)

##out.write(x)
#out.close()
