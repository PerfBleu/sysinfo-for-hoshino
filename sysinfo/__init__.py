__version__ = '0.1.0'
import os
from PIL import Image, ImageFont, ImageDraw
from hoshino import util, R
from hoshino import Service

sv = Service('sysinfo', visible= True, enable_on_default= True, bundle='sysinfo', help_='''
显示系统信息(screenfetch)
'''.strip())
def generate():
    logo_data = os.popen('screenfetch -L -N') 
    logo_text = logo_data.read()
    info_data = os.popen('screenfetch -n -N') 
    info_text = info_data.read()
    hi_mem_proc_data = os.popen(' ps aux | head -1;ps aux|sort -k4nr|head -15') 
    hi_mem_proc_text = hi_mem_proc_data.read()
    hi_mem_proc=''
    hmplist = hi_mem_proc_text.splitlines()
    for line in hmplist:
        hi_mem_proc = hi_mem_proc+line.replace(line[66:74],line[66:74]+'\n')+'\n'

    image = Image.open(os.path.join(os.path.dirname(__file__), "../bg.png")) # 读取图片
    #iwidth, iheight = image.size # 获取画布高宽
    font = ImageFont.truetype(os.path.join(os.path.dirname(__file__), "../IBMPlexMono-MediumItalic.ttf"),22) # 设置字体及字号
    draw = ImageDraw.Draw(image)

    #fwidth, fheight = draw.textsize('22', font) # 获取文字高宽
    flex = 750
    draw.text((flex+10,60), logo_text, '#f88066', font)
    draw.text((flex+490,130), info_text, '#f88066', font)
    draw.text((flex+230,560), hi_mem_proc, '#f88066', font)
    image.save(os.path.join(os.path.dirname(__file__), "../tmp.png")) # 保存图片
    return('generate success')

'''
@sv.on_prefix(('screenfetch'))
async def sysinfo(bot, ev):
    nfo = generate()
    if nfo == 'generate success':
        sv.logger.info(nfo)
    else:
        sv.logger.warning('图像创建失败')
    msg = f"[CQ:image,file=file:///{path}/hoshino/modules/sysinfo/tmp.png]"
    await bot.send(ev, msg, at_sender=True)
'''
@sv.on_fullmatch(('screenfetch'))
async def sysinfo(bot, ev):
    try:
        sv.logger.info(generate())
    except:
        sv.logger.warning('图片创建失败')
    tmppath = os.path.join(os.path.dirname(__file__), "../tmp.png")
    msg = f"[CQ:image,file=file:///{tmppath}]"
    await bot.send(ev, msg, at_sender=True)
