#-*-coding:utf-8-*-
import zbar
from PIL import Image
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def scan(file):
	'''
	方法：识别二维码
	
	使用方法：调用scan 传入文件路径名称'001.jpg'

	author ：xuchengzhi
	'''
	scanner = zbar.ImageScanner()
	scanner.parse_config('enable')
	img = Image.open(file).convert('L')
	w, h = img.size
	zimg = zbar.Image(w, h, 'Y800', img.tobytes())
	scanner.scan(zimg)
	for s in zimg:
		return(s.data)
	del(img)
print scan("E:\\code\\py\\baidu.jpg")