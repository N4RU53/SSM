import psutil
import urwid
import socket


def ref(_loop,_data):
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory()
    swp = psutil.swap_memory()
    disk = psutil.disk_usage('/')
    
    host = socket.gethostname()
    
    txt.set_text(f'\n  [{host}]'+ 
                 '\n   - CPU    : ' + f'{cpu}'+ 
                 '\n   - Memory : ' + f'{mem.percent}'+ 
                 '\n   - Swap   : ' + f'{swp.percent}'+ 
                 '\n   - Disk   : ' + f'{disk.percent}')
    txt.set_align_mode(mode='left')
    
    loop.set_alarm_in(1,ref) 


txt = urwid.Text('\nSimple System Monitor\n\nPowered by Naru', align='center')

fill = urwid.Filler(txt, 'top')
frame = (urwid.Frame(body=fill))
loop = urwid.MainLoop(frame)
loop.set_alarm_in(4,ref) 
loop.run()