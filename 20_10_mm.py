import ctypes
import json

def stok_info():
    # mydll.sendcommandW('QRCODE 8,8,H,3,M,0,M2,"00023519"')
    mydll.sendcommandW('TEXT 80,0,"0",0,6,6,2,"RANTAI GAJAH LICIN KSG"')
    mydll.sendcommandW('TEXT 80,18,"0",0,6,6,2,"B:8.02, U:20.00"')
    mydll.sendcommandW('TEXT 80,36,"0",0,6,6,2,"916/FC"')
    mydll.sendcommandW('PRINT 1')

mydll = ctypes.windll.LoadLibrary('D:\\ExternalCode\\Onewoorks\\BarcodePrinter\\tsc_sample\\TSCLIB.dll')
mydll.openportW("TSC TTP-244 Plus")
mydll.sendcommandW("SIZE 20 mm,10 mm")
mydll.sendcommandW('GAP 4 mm,0 mm')
mydll.sendcommandW('DIRECTION 1')
mydll.sendcommandW('DENSITY 15')
mydll.sendcommandW('CLS')

stok_info()
stok_info()

mydll.closeport()
print ("Finished Printing")