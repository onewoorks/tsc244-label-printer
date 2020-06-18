import ctypes
import json

LEBAR = "35"
TINGGI = "25"
GAP = "2"

def medivest_asset(asset_data):
    mydll.sendcommandW("SIZE 35 mm,25 mm")
    mydll.sendcommandW('GAP 4 mm,0 mm')
    mydll.sendcommandW('DIRECTION 1')
    mydll.sendcommandW('DENSITY 15')
    mydll.sendcommandW('CLS')

    mydll.sendcommandW('TEXT 140,28,"0",0,8,8,2,"MEDIVEST"')
    mydll.sendcommandW('BAR 24,56,232,1')
    mydll.sendcommandW('QRCODE 24,72,H,4,M,0,M2,"'+asset_data['qr_code']+'"')
    mydll.sendcommandW('TEXT 132,72,"0",0,6,6,0,"Asset No :"')
    mydll.sendcommandW('TEXT 132,88,"0",0,6,6,0,"'+asset_data['asset_no']+'"')
    mydll.sendcommandW('TEXT 132,112,"0",0,6,6,0,"Model :"')
    mydll.sendcommandW('TEXT 132,128,"0",0,4,4,0,"'+asset_data['model']+'"')
    mydll.sendcommandW('PRINT 1')

def medivest_activity(activity_data, asset_no):
    mydll.sendcommandW("SIZE 35 mm,25 mm")
    mydll.sendcommandW('GAP 4 mm,0 mm')
    mydll.sendcommandW('DIRECTION 1')
    mydll.sendcommandW('DENSITY 15')
    mydll.sendcommandW('CLS')

    mydll.sendcommandW('TEXT 140,28,"0",0,8,8,2,"MEDIVEST"')
    mydll.sendcommandW('BAR 24,56,232,1')
    mydll.sendcommandW('QRCODE 24,72,H,4,M,0,M2,"'+activity_data['qr_code'].replace('_',':')+'"')
    mydll.sendcommandW('TEXT 132,72,"0",0,6,6,0,"Activity Name"')
    mydll.sendcommandW('TEXT 132,88,"0",0,6,6,0,"'+activity_data['name']+'"')
    mydll.sendcommandW('TEXT 132,112,"0",0,6,6,0,"Asset No :"')
    mydll.sendcommandW('TEXT 132,128,"0",0,6,6,0,"'+asset_no+'"')
    mydll.sendcommandW('PRINT 1')

mydll = ctypes.windll.LoadLibrary('D:\\ExternalCode\\Onewoorks\\BarcodePrinter\\tsc_sample\\TSCLIB.dll')
mydll.openportW("TSC TTP-244 Plus")

medivest_payload = json.loads('{"id":144,"payloads":{"qr_code":"AA0100000144","activity":[{"name":"Power Supply (PSU) - Cleaning","qr_code":"AA0100000144_01000001"},{"name":"Fan & Filter Check&Clean","qr_code":"AA0100000144_01000002"},{"name":"Battery Check","qr_code":"AA0100000144_01000003"}],"asset_no":"SBN150100"},"asset_info":{"model":"Fresenius 4008s Ng - Fresenius Medical Care Ag & Co","state":"Negeri Sembilan","asset_no":"SBN150100","hospital":"Tuanku Jaafar","serial_no":"3SXAH002","company_name":"Medivest","location_name":"Ruang Rawatan I"}}')

asset = {
    "asset_no" : medivest_payload['payloads']['asset_no'],
    "model" : medivest_payload['asset_info']['model'],
    "qr_code": medivest_payload['payloads']['qr_code']
}
medivest_asset(asset)

activities = medivest_payload['payloads']['activity']
for activity in activities:
    medivest_activity(activity, medivest_payload['payloads']['asset_no'])

mydll.closeport()
print ("Finished Printing")