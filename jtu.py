# -*- coding: utf-8 -*-
import os, chardet, codecs, re
#文件类型扩展名  文件列表
FileType, FileList = [], []

def get_file_list(Dir):
	if len(Dir.strip(' ')) == 0:
		return 
	dirList = [os.path.join(Dir, f) for f in os.listdir(Dir)]
	fileList = [f for f in dirList if os.path.isfile(f) and os.path.splitext(f)[1].lower() in FileType]
	folderList = [f for f in dirList if os.path.isdir(f)]
	FileList.extend(fileList)
	# 递归字文件夹
	for subfolder in folderList:
		get_file_list(subfolder)

def convert_2_target_coding(coding='utf-8'):
    probar=0
    for filepath in FileList:
        if probar%100 == 0:
            print(probar)
        with open(filepath, 'rb') as f:
    	    data = f.read()
    	    codeType = chardet.detect(data)['encoding']
        if codeType not in (coding, 'ascii'):
            if codeType not in ('jis','Windows-1253','windows-1253','Windows-1252','SHIFT_JIS','CP932',None): 
                print(filepath+' '+codeType+'\n')
                #with codecs.open(filepath, 'r', codeType) as f:
                #    content = f.read()
            else:
                with codecs.open(filepath, 'r', 'cp932') as f:
                    content = f.read()            
                with codecs.open(filepath, 'w', coding) as f:
                    f.write(content)
        probar = probar+1

    		
if __name__ == '__main__':
	# 获取目录
	WorkDir = str(input('input target folder\n\t:'))
	# 文件类型扩展名
	FileType = re.split(r'\s+', str(input('file type(filename extension, such as .c .h)\n\t:')))
	os.chdir(WorkDir)
	get_file_list(WorkDir)
	print(len(FileList))
	convert_2_target_coding()