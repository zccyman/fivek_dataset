import os
import sys
from urllib.request import urlretrieve

from torch.utils.data import dataset

img_lst=[]
with open('filesAdobe.txt', 'r') as f:
    for line in f.readlines():
        img_lst.append(line.rstrip("\n"))#去掉换行符

with open('filesAdobeMIT.txt', 'r') as f:
    for line in f.readlines():
        img_lst.append(line.rstrip("\n"))#去掉换行符

#urlretrieve 函数的回调函数，显示下载进度
def cbk(a,b,c):
    '''回调函数
    @a:已经下载的数据包数量
    @b:数据块的大小
    @c:远程文件的大小
    '''
    per=100.0*a*b/c
    if per>100:
        per=100
    #在终端更新进度
    sys.stdout.write("progress: %.2f%%   \r" % (per))
    sys.stdout.flush()

expert = "a"
#根据文件的url下载图片
for i in img_lst:
    URL = f'https://data.csail.mit.edu/graphics/fivek/img/dng/' + i + '.dng'
    print('Downloading input ' + i +':')
    urlretrieve(URL, f'/home/developer/zhangcc/myopendatasets/color_enhancement/fivek/input/' + i + '.dng', cbk)

    URL = f'https://data.csail.mit.edu/graphics/fivek/img/tiff16_{expert}/' + i + '.tif'
    print('Downloading output ' + i +':')
    urlretrieve(URL, f'/home/developer/zhangcc/myopendatasets/color_enhancement/fivek/output/' + i + '.tif', cbk)
