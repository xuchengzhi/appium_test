#-*-coding:utf-8-*-
import os
import sys
import re


reload(sys)
sys.setdefaultencoding("utf-8")

'''
    扫描文件夹dir中所有.java文件并按照包名输出
'''
def GetFileList(dir, fileList):
    newDir = dir
    if os.path.isfile(dir):  # 如果是文件
        fileList.append(dir)
    elif os.path.isdir(dir):
        for s in os.listdir(dir):  # 如果是文件夹
            newDir = os.path.join(dir, s)
            GetFileList(newDir, fileList)
    return fileList

'''
    格式化参数列表，并去除参数名
    对于复杂类型包含包名
'''
def varReform(varFunc, classImportMatch):
    # 去除参数列表中的多于的空白字符
    varTmp = removeVarSpaceChar(varFunc)

    # 去除 ) 及之后的内容
    varRemoveRightRedundant = removeVarRightRedundant(varTmp)

    # 去除形参声明中的参数名、参数类型声明中的 final、及=等
    varTmpReform = removeVarName(varRemoveRightRedundant)

    # 对于复杂类型添加包名
    varTmpReformPackage = varClassIncludePackage(varTmpReform, classImportMatch)

    return varTmpReformPackage

'''
    去除函数名中对于的' '
'''
def apiFuncNameReform(apiFuncName):
    apiName = ''
    i = 0
    while(i < len(apiFuncName)):
        chTmp = apiFuncName[i];
        if chTmp == ' ':
            i += 1
            continue;
        else:
            i += 1
            apiName += chTmp;
    return apiName

'''
    去除参数列表中的多于的空白字符
'''
def removeVarSpaceChar(varFunc):
    varTmp = ""
    i = 0
    while (i < len(varFunc)):
        chTmp = varFunc[i]
        if chTmp == '\n' or chTmp == '\t' or chTmp == '\r':
            # 循环变量自增
            i += 1
            continue;
        else:
            spaceFlag = 0;  # 标志变量：是否为连续的空格
            # 将多个空格或制表符化简为1个
            # 有可能存在空格后面有制表符的情况
            while ((chTmp == ' ' or chTmp == '\n' or chTmp == '\t' or chTmp == '\r') and i < len(varFunc)):
                spaceFlag = 1
                i += 1
                # 更新chTmp 并且保证不超过数组下标
                if (i < len(varFunc)):
                    chTmp = varFunc[i]
            if spaceFlag == 1:
                varTmp += ' '
            varTmp += chTmp
        # 循环变量自增
        i += 1
    return varTmp

'''
    去除 最右的 ） 右边多余的内容
    输入：
    Bundle bundle) throws AuthenticatorException
    final Account account, @Size(min = 1) final String newName, AccountManagerCallback<Account> callback, Handler handler)
    Account account)
    )
    根据观察只要去除最右 ） 及之后的内容即可
'''
def removeVarRightRedundant(varTmp):
    varRemoveRightRedundant = ''

    iTmp = len(varTmp)-1
    while(iTmp >= 0):
        if(varTmp[iTmp] == ')'):
            break;
        iTmp -= 1

    varRemoveRightRedundant = varTmp[0:iTmp]    # 截取字符串


    return varRemoveRightRedundant

'''
    去除参数列表中形参名称

    同时去除参数类型中声明的类似：
    @ServiceName @NonNull String
    中与@紧临的部分，只保留 String

    <去除形参名称>
        现在的参数列表的格式有较多种：
        A.B 、
        String[] 、
        List<Node>、
        A::B、
        AdapterView<?> parent、
        HashMap<Class, HashMap<String, Method>>、
        @AnimatorRes int id、
        单纯使用形参之间的','分隔已经不能实现分隔参数声明
        由于参数列表中存在 <> [] ? 等字符 而对于一般的参数类型如：String 则遇到空格及可
        判断这次形参声明结束，之后的一个单词为形参名（不保存），而遇到 <> [] 符号时由于他们成对
        出现设置两个标志变量标志 < 与 > ； [ 与 ] 均声明结束
        flag1 : < >
        flag2 : [ ]
        当 flag1 < 0 时形参类型未声明结束， flag1 = 0 时结束， flag1 < 0 时有错误
        当 flag1 = 0 时，如果遇到  ',' 或者 到了varTmp 的末尾则刚刚扫描的字符串为参数名
        final A tmp, 或 final A tmp 则 tmp 为参数名
        遇到空格新开一个单词，遇到',' 判断flag1 和 flag2 如果都为0则刚才的单词为参数名，不写入数组
        对于每个形参的声明检查之前 flag1 = flag2 = 0

        flag3 : 标志现在声明的是参数类型 还是参数名
        flag3 = 0 参数类型
        flag3 = 1 参数名


        同时存在参数类型声明中有()的情况，去除()及之间的内容后，在进行通种方法的去除参数名即可

'''
def removeVarName(varTmp):

    # 去除当前参数列表中的成对的()及其中间的内容
    bracketFlag = 0
    i = 0
    varTmpB = ''
    while(i < len(varTmp)):
        if(varTmp[i] == '('):
            bracketFlag = 1
        if(bracketFlag == 0):
            varTmpB = varTmpB + varTmp[i]
        if(varTmp[i] == ')'):
            bracketFlag = 0
        i += 1
    varTmp = varTmpB

    # print(varTmp)

    i = 0
    # 将 varTmp 开头的 ' ' 去掉，将参数列表格式化
    if (i < len(varTmp) and varTmp[i] == ' '):
        i += 1
    varTmpReform = ''
    tmpWord = ''  # 存储参数列表中的每一个单词
    while (i < len(varTmp)):
        flag1 = 0  # < >
        flag2 = 0  # [ ]
        flag3 = 0  # 参数类型 or 参数名
        # flag4 = 0  # 用于标记每个参数声明中空格的填充
        tmpWord = ''
        # 形参声明遍历
        while (i < len(varTmp)):
            # 重新开始一个新的单词
            while (i < len(varTmp) and varTmp[i] != ' '):
                tmpWord += varTmp[i]
                # < > [ ] 成对性检测
                if varTmp[i] == '<':
                    flag1 += 1
                if varTmp[i] == '>':
                    flag1 -= 1
                if varTmp[i] == '[':
                    flag2 += 1
                if varTmp[i] == ']':
                    flag2 -= 1
                i += 1
            # 如果满足以下条件则为参数名，不加入到形参列表中
            if (flag1 == 0 and flag2 == 0 and (varTmp[i - 1] == ',' or i == len(varTmp))):
                # 后面还有参数声明，不加空格
                if (varTmp[i - 1] == ','):
                    varTmpReform += ','
                break;
            else:  # 参数类型
                # # 填充参数类型声明时的空格 --> 不需要参数声明之间的空格
                # if (flag4 == 1):
                #     varTmpReform += ' '
                if(len(tmpWord) != 0 and tmpWord[0]!='@' and tmpWord != 'final'):
                    varTmpReform += tmpWord
                    # flag4 = 1
            tmpWord = ''
            i += 1
        i += 1
    return varTmpReform

'''
    对于参数列表+返回值中的复杂参数声明类型添加其包名
    <不处理的情况>
    对于已经包含包名的参数类型声明不处理
    对于基本参数类型声明也不处理
'''
def varClassIncludePackage(varTmpReform, classImportMatch):
    # 如果是返回值为空则返回 void
    if(varTmpReform == 'void'):
        return varTmpReform

    varClassIP = ''
    i = 0
    while(i<len(varTmpReform)):
        tmpWord = ''  # 存储参数列表中的每一个单词
        # 取下一个单词，如果包含.仍算作一个单词
        while(i<len(varTmpReform)):
            if(varTmpReform[i].isalpha() or varTmpReform[i] == '.'):
                tmpWord += varTmpReform[i]
            else:
                break;
            i += 1
        # print(tmpWord)
        # 如果这个单词在 classImportMatch 中则替换
        if(tmpWord in classImportMatch.keys()):
            varClassIP += classImportMatch[tmpWord]
        else:
            varClassIP += tmpWord
        # 对于其他字符直接添加进来
        while(i<len(varTmpReform) and (varTmpReform[i].isalpha() == False)):
            varClassIP += varTmpReform[i]
            i += 1
    return varClassIP

'''
    Android 系统 API 的相对路径格式化：
    将android-23\android\accessibilityservice\AccessibilityService.java
       格式化为：
           android.accessibilityservice.AccessibilityService
    将格式化之后的数据存储在 tmp 中
'''
def apiRouteReform(package):
    tmp = ''  # 存储此次遍历的类名
    flag = 0  # 标志是否开始存储
    for str in package:
        # print(str,end='')
        if (flag == 0) and (str == '\\'):
            flag = 1
            # print(flag,end='')
            continue
        # flag == 1 : 开始
        if flag == 1:
            if str == '\\':
                tmp = tmp + '.'
            elif str == '.':
                break
            else:
                tmp = tmp + str
    return tmp

'''
    classRoute 与 classInThisPackage 是针对每一个类本身的路径的提取与同一个包内部
    类所在包的情况，这样时间与空间复杂度较高，运行时间长，为此了解决 0-记录.txt 中的
    Question 2 和 3 在遍历完所有.java 文件之后即构建 android-23 所有类与对应包名之间的
    对应关系
'''

'''
    <得到类所在包名的路径>
    输入：android-23\android\accessibilityservice\AccessibilityService.java （Java 类的相对路径）
    转化成：../android-23\android\accessibilityservice
    方便之后遍历文件夹，得到与当前类在同一个包中的所有类的名称

    tmpClassRoute 存储类所在包名的路径 如：../android-23\android\accessibilityservice
    classRouteReform 存储类所在包名的格式化 如：android.accessibilityservice
'''
def classRoute(package):
    tmp = ''    # 存储类所在的包名的路径
    flag = 0    # 用于标记是否在split得到的串之间加 斜杠
    tmpClassRoute = ''
    tmp = package.split('\\')   # 根据 斜杠 符号分隔最后一个元组为 .java 的名称 去除之后及为要得到的路径
    i = 0
    while(i < (len(tmp)-1)):
        if(flag == 0):
            flag = 1
        else:
            tmpClassRoute += '\\'
        tmpClassRoute += tmp[i]
        i += 1
    return tmpClassRoute

'''
    package 的格式：../android-23\android\accessibilityservice 及 classRoute的返回值
    得到与本.java 同一个包中所有类的格式化
    返回一个列表
'''
def classInThisPackage(package):
    classList = GetFileList(package,[])     # 得到这个文件夹下所有的类（）
    classReformList = []
    for tmpPackage in classList:
        tmp = apiRouteReform(tmpPackage)
        classReformList.append(tmp)
    # print(classReformList)
    return classReformList

'''
    构造当前 package 中 所有 类：包名 对应关系
'''
def classInThisPackageMatch(package):

    # 得到当前包中所有类的格式化的形式的列表
    tmpClassInThisPackage = classInThisPackage(classRoute(package))

    tmpClassInThisPackageMatch = {'key':'package'}
    flag = 0;       # 标记是否开始存储数据
    for classPackage in tmpClassInThisPackage:
        tmpClassSet = classPackage.split('.')  # 将包名根据 '.' 分隔
        tmpClassName = tmpClassSet[len(tmpClassSet) - 1]  # 最后一个字符串为类名
        # 如果没有赋值过则先清空 map
        if (flag == 0):
            flag = 1
            tmpClassInThisPackageMatch.clear()
        tmpClassInThisPackageMatch[tmpClassName] = classPackage

    # 这个包里面没有类则返回空
    if (flag == 0):
        tmpClassInThisPackageMatch.clear()

    # for tmpItem in tmpClassInThisPackageMatch:
    #     print(tmpClassInThisPackageMatch[tmpItem])

    return tmpClassInThisPackageMatch

'''
    package 所指向类的内部类、接口
    如：Callbacks 为 android.accessibilityservice.AccessibilityService 的内部接口
    则返回：android.accessibilityservice.AccessibilityServic.Callbacks
    即：
    Callbacks --> android.accessibilityservice.AccessibilityServic.Callbacks

    最后返回所有内部类（接口）的包名.类名列表

'''
def classOrInterfaceInThisPackage(package):

    # print(package)

    ListclassOrInterfaceInThisPackage = []  # 该类所有内部类、接口的列表(包含了它自身)

    # 编译正则表达式筛选出内部类（接口）
    # patternInnerClassInterface = re.compile(
    #     r'^[\s]*(public|private|protected)[\s]*(static|final|abstract)*[\s]*(class|interface)[\s]*([\w|\$|\.|_]*)[\s]*[\w|_|\$| |,|\s|\.|\[|\]|\<|\>|\:|\?|@]*\{',
    #     re.M)
    # 类的名字中包括<T>的符号 如： private abstract class Future2Task<T>
    patternInnerClassInterface = re.compile(
        r'^[\s]*(public|private|protected)[\s]*(static|final|abstract)*[\s]*(class|interface)[\s]*([\w|\$|\.|_|\<|\>]*)[\s]*[\w|_|\$| |,|\s|\.|\[|\]|\<|\>|\:|\?|@]*\{',
        re.M)
    IDXfile = open(package, 'r', encoding='utf-8')  # gbk 格式的文件 IDXfile.read() 会报错，以 utf-8 格式打开就行
    fileread = IDXfile.read()
    IDXfile.close()
    InnerClassInterface = re.findall(patternInnerClassInterface, fileread)

    '''
        InnerClassInterface 每个元素的第四个元组为类名或者接口名
        ('public', 'abstract', 'class', 'AccessibilityService')
        ('public', '', 'interface', 'Callbacks')
        ('public', 'static', 'class', 'IAccessibilityServiceClientWrapper')
    '''

    # 将路径文件../android-23\android\accessibilityservice\AccessibilityService.java
    # 转换成 ：android.accessibilityservice.AccessibilityService
    tmpPackageClass = apiRouteReform(package)
    # print(tmpPackageClass)

    # 这个 package 所指文件的类名，在添加的时候不加进去
    thisClassName = tmpPackageClass.split('.')
    thisClassName = thisClassName[len(thisClassName)-1]
    # print(thisClassName)

    # 检查有多少.java文件中，一个类（接口）的声明都没有找到的情况
    # 尽管没有找到类（接口）的声明没有找到，但是之后的遍历已经包含这个类（接口）声明本身 --> classInThisPackageMatch 方法
    # 一共 955 个
    # if(len(InnerClassInterface)==0):
    #     print("Find Nothing!")

    # 将内部类（接口）添加进去
    # 格式：android.accessibilityservice.AccessibilityServic.Callbacks
    for tmpICIF in InnerClassInterface:
        if tmpICIF[3] != thisClassName:

            # 去掉内部类（接口）名称中的<>其中的内容<>之中往往是<T>等泛型，在内部类包引用中没有用处，直接去掉也方便后面map的构造
            tmpFlag = 0
            tmpInnerCI = ''
            tmpI = 0
            while(tmpI < len(tmpICIF[3])):
                if(tmpICIF[3][tmpI] == '<'):
                    tmpFlag = 1
                if(tmpFlag == 0):
                    tmpInnerCI += tmpICIF[3][tmpI]
                if(tmpICIF[3][tmpI] == '>'):
                    tmpFlag = 0
                tmpI += 1

            ListclassOrInterfaceInThisPackage.append(tmpPackageClass+'.'+tmpInnerCI)
            # print(tmpPackageClass+'.'+tmpInnerCI)

    # 遍历所有内部类的结果：一共5193个
    # for tmp in ListclassOrInterfaceInThisPackage:
    #     print(tmp)
    #     # 检查是否重复添加了 .java 类名本身，发现输出结果中没有
    #     tmp112 = tmp.split('.')
    #     if(tmp112[len(tmp112)-1] == tmp112[len(tmp112)-2]):
    #         print('asdfasdfasdf')

    # print('\n')

    return ListclassOrInterfaceInThisPackage


'''
    输入：import 集合 形如：[('import ', 'android.os.Parcelable', ';'), ('import ', 'android.os.Parcel', ';')]
    输出：map 对象 map 对应关系
    <1>
    List --> java.util.List
    SomeArgs --> com.android.internal.os.SomeArgs
    类：包名 对应关系
    <2>
    package 为当前类所在包中所有类的 map 对应关系 tmpClassThisPackageMathch
    最后返回的 map 为 import 与 tmpClassThisPackageMathch 的合并
    先求 tmpClassThisPackageMathch 后 求 import 是为了更新同名类（不同包，但同名，以import 为准）的引用
    <3>
    package 所指向类的内部类、接口
    如：Callbacks 为 android.accessibilityservice.AccessibilityService 的内部接口
    则返回：android.accessibilityservice.AccessibilityServic.Callbacks
    即：
    Callbacks --> android.accessibilityservice.AccessibilityServic.Callbacks
'''
def classMatchPackage(classImport, package):

    # 构造当前 类 所在 package 中的左右类的 类：包名 对应关系
    tmpClassThisPackageMathch = classInThisPackageMatch(package)

    # package 所指向类的内部类、接口的 类（接口）：包名 对应关系
    tmpClassOrInterfaceInThisPackage = classOrInterfaceInThisPackage(package)

    # 遍历 classImport 集合
    for tmpclassImport in classImport:
        tmpPackage = tmpclassImport[1]
        tmpClassSet = tmpPackage.split('.')             # 将包名根据 '.' 分隔
        tmpClassName = tmpClassSet[len(tmpClassSet)-1]  # 最后一个字符串为类名
        tmpClassThisPackageMathch[tmpClassName] = tmpPackage

    # 遍历 tmpClassOrInterfaceInThisPackage 集合
    for tmpPackage in tmpClassOrInterfaceInThisPackage:
        tmpClassSet = tmpPackage.split('.')             # 将包名根据 '.' 分隔
        tmpClassName = tmpClassSet[len(tmpClassSet)-1]  # 最后一个字符串为类名
        tmpClassThisPackageMathch[tmpClassName] = tmpPackage

    # for item in tmpClassThisPackageMathch:
    #     print(item, ':',tmpClassThisPackageMathch[item])
    #
    # print('\n\n')

    return tmpClassThisPackageMathch

'''
    根据返回值和函数名的字符串返回返回值和函数名
    输入：
    1.一般格式：void text
    2.构造函数：AClass
    3.复杂类型：@NonNull String getMediaId 、 native int getFlags 等
'''
def findReturnValueAndFuncName(apiFunc):
    returnValue = ''    # 返回值
    funcName = ''       # 函数名

    apiCount = 0        # 计数器，第一个非空为函数名，第二个非空为返回值

    apiTmp = apiFunc.split(" ");

    iTmp = len(apiTmp)-1    # 循环变量
    # 防止数组越界 、 确保不多找到东西
    while(iTmp >= 0 and apiCount < 2):
        if(apiTmp[iTmp] != ''):
            # python 中没有 switch 语句
            # 第一个非空为函数名
            if(apiCount == 0):
                funcName = apiTmp[iTmp]
            # 第二个非空为返回值
            if(apiCount == 1):
                returnValue = apiTmp[iTmp]
                break;  # 找到之后退出
            apiCount += 1   # 该计数器的自增应该在连续的 if 语句之后，这样才连续的 if 语句才能起到 swithch 的效果
        iTmp -= 1

    # 辅助输出：分隔之后元组个数
    # print(len(apiTmp))
    # print(apiTmp)

    # print(funcName + ": " + returnValue)

    return returnValue, funcName

'''
    遍历 package 指向的.java 类中所有的方法
    1).java 类自己的方法
    2).java 类的内部类（接口）的方法
'''
def ergodicClassFunc(package):
    '''
    :param package:存储每个系统API的Java的相对路径
    :return:0:.java类的方法正常遍历；1：.java类的方法没有正常提取
    '''
    '''
        编译正则表达式
    '''
    # pattern = re.compile(r'');
    # 1
    # pattern = re.compile(r'^[ \t]*(public |protected |private )((static |final )*)(.*)\((.*)*$',re.M);    # 需要打开多行模式才能匹配函数开头
    # 2
    # pattern = re.compile(r'^[ \t]*(public |protected |private )((static |final )*)(.*)(.*)*$',re.M);        # 没有括号的话会把常量也提取出来
    # 3
    # pattern = re.compile(r'^[ \t]*(public |protected |private )((static |final )*)(.*)\((.*)*$',re.M);
    # 4 正确匹配返回值 ：
    # 排除private Transport mTransport = new Transport(); 的情况
    # public String getPublicId() { return null; }
    # pattern = re.compile(r'^[ \t]*(public |protected |private )((static |final )*)([a-zA-Z0-9|_|\$| ]*)\((.*)*$',re.M);
    # 5
    # pattern = re.compile(
    #     r'^[ \t]*(public |protected |private )((static |final |abstract )*)([\w|_|\$| ]*)\(([\w|_|\$| |,|\r|\n|\t|.|\[|\]|\<|\>|\:|\?|@]*)(.*)$',
    #     re.M);
    # 6
    # pattern = re.compile(
    #     r'^[ \t]*(public |protected |private )((static |final |abstract )*)([\w|_|\$| |,|\r|\n|\t|.|\[|\]|\<|\>|\:|\?|@]*)\(([\w|_|\$| |,|\r|\n|\t|.|\[|\]|\<|\>|\:|\?|@]*)(.*)$',
    #     re.M);
    # 7
    pattern = re.compile(
        r'^[ \t]*(public |protected |private )((static |final |abstract )*)([\w|_|\$| |,|\r|\n|\t|.|\[|\]|\<|\>|\:|\?|@]*)\(([\w|_|\$| |,|\r|\n|\t|.|\[|\]|\<|\>|\:|\?|@|\(|\)|=]*)(.*)$',
        re.M);

    # 正则表达式匹配 import 语句
    patternImport = re.compile(
        r'^(import )([a-zA-Z0-9|_|\$| |,|.|\:|\?|@]*)(;)$',
        re.M);

    '''
        数据处理
    '''
    flag = 0        # 标志变量：0:.java类的方法正常遍历；1：.java类的方法没有正常提取

    # package 存储每个系统API的Java的相对路径
    # tmpClassPackage 存储格式化之后的文件路径
    tmpClassPackage = apiRouteReform(package)

    # 遍历该.java文件提取所有方法
    # print(package)
    IDXfile = open(package, 'r', encoding='utf-8')  # gbk 格式的文件 IDXfile.read() 会报错，以 utf-8 格式打开就行
    fileread = IDXfile.read()
    IDXfile.close()
    methods = re.findall(pattern, fileread)  # 匹配 类声明的方法
    classImport = re.findall(patternImport, fileread)  # 匹配 import 语句
    # 构造 类：包名 的对应关系 ： 包含 1. import 语句引用的；2.与该类同一个 package 的
    # 3.内部类（接口）- public / private / protected 三种类型的都记录下来
    classMatch = classMatchPackage(classImport, package)  # 构造 map



    # print(methods)

    # 输出所有未能遍历的.java类 ，更换正则表达式遍历
    if len(methods) == 0:
        # print(tmp)    # tmp 中存储的是 . 连接的类名
        flag = 1
    else:
        for eFunc in methods:
            # eFunc 为每个函数的完整的说明
            apiFunc = eFunc[3];  # 第四个分组为函数名格式 ： void release  或者为类名如：AccessibilityServiceInfo 又或者由三部分组成，这个时候需要细致区分
            varFunc = eFunc[4];  # 第五个分组为参数声明分组：其中包含与参数声明无关的 \r,\n,\t 字符，需要先将这几种字符去掉，并且包含 声明括号中右括号）之后到 { 之前内容如：String name)\n        throws SAXNotRecognizedException, SAXNotSupportedException
            # 函数参数格式化
            varFunc = varReform(varFunc, classMatch)
            # 如果不是类名则为方法名，用split 分隔
            if ' ' in apiFunc:
                # 得到该方法的返回值和函数名
                apiFuncReturn, apiFuncName = findReturnValueAndFuncName(apiFunc);
                # 对返回值的类型进行 类：包名 的对应
                apiFuncReturn = varClassIncludePackage(apiFuncReturn, classMatch)
                # 去除函数名中多于的空格
                apiFuncName = apiFuncNameReform(apiFuncName)
                apiFunc = tmpClassPackage + '.' + apiFuncName + '(' + varFunc + '):' + apiFuncReturn;
            # 对于构造函数
            else:
                # 去除函数名中多于的空格
                apiFunc = apiFuncNameReform(apiFunc)
                apiFunc = tmpClassPackage + '.' + apiFunc + '(' + varFunc + ')';

            # 去除 API 中的 \n 等空白字符
            apiFunc = removeVarSpaceChar(apiFunc)

            # 输出API

            print(apiFunc)
    return flag

'''
    主函数
'''
# 重定向输出位置
output = sys.stdout
outputfile = open('test.txt', 'w')
sys.stdout = outputfile

list = GetFileList('../android-23', [])  # 获取所有.java类的路径

count = 0;  # 统计能匹配的.java文件个数
for package in list:
    # package 存储每个系统API的Java的相对路径
    # ergodicClassFunc 提取.java类的所有方法
    # 返回：1：未成功提取；0：成功提取；
    count += ergodicClassFunc(package)

# print(count);

# 关闭输出重定向
outputfile.close()
sys.stdout = output