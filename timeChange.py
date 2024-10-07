import datetime
import re
import os

def _timeChange(lines, second):
    '''
    时间轴改变
    '''
    def _timeSecondsAdd(matched):
        '''
                  时间str转obj                 sub中找到原时间                                            改变的时间
        '''                                  
        return (datetime.datetime.strptime(matched.group('time'), "%H:%M:%S.%f") + datetime.timedelta(seconds=second)).strftime("%H:%M:%S.%f")[:-4:]
    return re.sub(r"(?P<time>\d{1}:\d{2}:\d{2}.\d{2})", _timeSecondsAdd, lines)

def _aloneFileChange(oldPath, newPath, second):
    '''
    单个文件操作
    '''
    with open(oldPath, encoding='utf_8_sig') as file1:
        lines = file1.read()
        newText1 = _timeChange(lines, second)
        with open(newPath,  'w', encoding='utf_8_sig') as newFile1:
            newFile1.write(newText1)
            newFile1.close()
        file1.close()

def allFileChange(path, second):
    '''
    批量读取文件
    '''
    if os.listdir(path+"new\\"):
        for file in os.listdir(path+"old\\"):
            os.remove(path+"new\\"+file)
    for file in os.listdir(path+"old\\"):
        _aloneFileChange(path+"old\\"+file, path+"new\\"+file, second)
        print(file+"の时间轴add"+ str(second) +"  OK")