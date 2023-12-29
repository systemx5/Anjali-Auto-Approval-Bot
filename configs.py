# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "21011056"))
    API_HASH = getenv("API_HASH", "696033b1a9c35f0dc027f8ecfbaa9645)
    BOT_TOKEN = getenv("BOT_TOKEN", "6856342807:AAFxautkt3EKiVqcRWpxhvFA7923LrUhEhU")
    FSUB = getenv("FSUB", "VJ_Botz")
    CHID = int(getenv("CHID", "-1001970031336"))
    SUDO = list(map(int, getenv("SUDO", "1841888978").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://Bikash:Bikash@bikash.yl2nhcy.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
