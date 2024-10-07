import os
import zhconv

def _hant_2_hans(hant_str: str):
    '''
    繁 -->> 简
    '''
    return zhconv.convert(hant_str, 'zh-hans')


def _aloneFileChange(oldPath, newPath):
    '''
    单个文件操作
    '''
    with open(oldPath, encoding='utf_8_sig') as file1:
        lines = file1.read()
        newText1 = _hant_2_hans(lines)
        with open(newPath,  'w', encoding='utf_8_sig') as newFile1:
            newFile1.write(newText1)
            newFile1.close()
        file1.close()

def allFileChange(path):
    '''
    批量读取文件
    '''
    if os.listdir(path+"new\\"):
        for file in os.listdir(path+"old\\"):
            os.remove(path+"new\\"+file)
    for file in os.listdir(path+"old\\"):
        _aloneFileChange(path+"old\\"+file, path+"new\\"+_hant_2_hans(file))
        print(file+" --> "+_hant_2_hans(file)+"  OK")
