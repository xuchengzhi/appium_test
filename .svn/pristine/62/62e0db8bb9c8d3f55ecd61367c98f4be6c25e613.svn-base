#-*-coding:utf-8-*-
import os,sys
# import pyqrcode
from PIL import Image
import imageio
from MyQR import myqr

	
def create_gif(image_list, gif_name):
    '''
    	方法：生成gif图片
    '''
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
    imageio.mimsave(gif_name, frames, 'GIF', duration = 0.1)
 
    return

def analyseImage(path):  
    ''''' 
    Pre-process pass over the image to determine the mode (full or additive). 
    Necessary as assessing single frames isn't reliable. Need to know the mode  
    before processing all frames. 
    '''  
    im = Image.open(path)  
    results = {  
        'size': im.size,  
        'mode': 'full',  
    }  
    try:  
        while True:  
            if im.tile:  
                tile = im.tile[0]  
                update_region = tile[1]  
                update_region_dimensions = update_region[2:]  
                if update_region_dimensions != im.size:  
                    results['mode'] = 'partial'  
                    break  
            im.seek(im.tell() + 1)  
    except EOFError:  
        pass  
    return results  
  
  
def processImage(path):  
	'''
	方法：分解gif图片
	'''
	photo_file=path.split(".")[-2]
	photo_files=[]
	if os.path.exists(photo_file):
		print "ok"
	else :
		os.mkdir(photo_file)
	mode = analyseImage(path)['mode']  
	im = Image.open(path)  
	i = 0
	p = im.getpalette()
	last_frame = im.convert('RGBA')
	photo_list=[]
	try:
		while True:
			print "saving %s (%s) frame %d, %s %s" % (path, mode, i, im.size, im.tile)
			if not im.getpalette():
				im.putpalette(p) 
			new_frame = Image.new('RGBA', im.size)
			if mode == 'partial':
				new_frame.paste(last_frame)
			new_frame.paste(im, (0,0), im.convert('RGBA'))
			name=("./"+photo_file+'/%s-%d.png' % (''.join(os.path.basename(path).split('.')[:-1]), i))
			photo_list.append(name)
			photo_files.append(photo_file)
			new_frame.save(photo_file+'/%s-%d.png' % (''.join(os.path.basename(path).split('.')[:-1]), i), 'PNG')
			i += 1
			last_frame = new_frame
			im.seek(im.tell() + 1)
	except EOFError:
		pass
	return {"photo_list":photo_list,"photo_file":photo_files}
def hebing(image_list,photo_file):
	'''
		方法：合成图片
	'''
	file_name=[]
	for i in range(len(image_list)):
		base_img = Image.open(ur'./3.png')
		target = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
		box = (5, 243, 338, 598)
		region = Image.open(ur'./{}'.format(image_list[i]))
		region = region.rotate(0)
		region = region.convert("RGBA")
		region = region.resize((box[2] - box[0], box[3] - box[1]))
		target.paste(region,box)
		target.paste(base_img,(0,0),base_img)
		target.save('./{}/{}.png'.format(photo_file[0],i))
		file_name.append('{}/{}.png'.format(photo_file[0],i))
	return file_name

def main():
	'''
		方法：调用合成图片gif方法
	'''
	get_gif("http://a.app.qq.com/o/simple.jsp?pkgname=com.font&fromcase=40003","./tmp.gif")
	res=processImage('002.gif')
	photo_list=res.get("photo_list")
	image_list=res.get("photo_file")
	gif_name = "ceshi.gif"#raw_input("请输入gif图片名称：\n")
	create_gif(hebing(photo_list,image_list), gif_name)
def get_gif(words,gif,):
	'''
		方法：生成二维码
	'''
	words=words
	version, level, qr_name = myqr.run(
    words,
    version = 10,
    level = 'H',
    picture = gif,
    colorized = True,
    contrast = 1.0,
    brightness = 1.0,
    save_name = "002.gif",
    save_dir = os.getcwd()
    )
if __name__ == "__main__":
    main()


