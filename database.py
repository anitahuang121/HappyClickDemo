'''
connect to mongo db in atlas
'''

from flask_pymongo import pymongo
from pymongo import message


def connection():
    PASSWORD = '123'
    DATABASE = 'Cluster0'
    CONNECTION_STRING = f"mongodb://danny:{PASSWORD}@cluster0-shard-00-00.wow4z.mongodb.net:27017,cluster0-shard-00-01.wow4z.mongodb.net:27017,cluster0-shard-00-02.wow4z.mongodb.net:27017/{DATABASE}?ssl=true&replicaSet=atlas-q4etkp-shard-0&authSource=admin&retryWrites=true&w=majority"
    client = pymongo.MongoClient(CONNECTION_STRING)
    db = client

    return db


def get_divisions():
    divisions = {
        "竹科": ['台積總部及晶圓十二A廠', '研發中心及晶圓十二B廠', '晶圓二廠', '晶圓三廠', '晶圓五廠', '晶圓六廠', '晶圓八廠', '先進封測一廠'],
        "中科": ['晶圓十五A廠', '晶圓十五B廠', '先進封測五廠'],
        "南科": ['晶圓十四A廠', '晶圓十四B廠', '晶圓十八廠', '先進封測二廠'],
        "中國": ['台積電(南京)有限公司及晶圓十六廠', '台積電(中國)有限公司及晶圓十廠'],
        "美國": ['WaferTech L.L.C. 及晶圓十一廠'],
        "新加坡": ['SSMC (TSMC-NXP JV)'],
        "龍潭封測廠": ['先進封測三廠']
    }
    return divisions


meds = [70523, 75088, 97493, 89384, 41195]


def get_factories():
    factory_code = {
        '台積總部及晶圓十二A廠': "F12A",
        '研發中心及晶圓十二B廠': "F12B",
        '晶圓二廠': "F2",
        '晶圓三廠': "F3",
        '晶圓五廠': "F5",
        '晶圓六廠': "F6",
        '晶圓八廠': "F8",
        '晶圓十五A廠': "F15A",
        '晶圓十五B廠': "F15B",
        '晶圓十四A廠': "F14A",
        '晶圓十四B廠': "F14B",
        '晶圓十八廠': "F18",
        '台積電(南京)有限公司及晶圓十六廠': "F16",
        '台積電(中國)有限公司及晶圓十廠': "F10",
        'WaferTech L.L.C. 及晶圓十一廠': "F11",
        'SSMC (TSMC-NXP JV)': "SSMC",
        '先進封測一廠': "AP1",
        '先進封測二廠': "AP2",
        '先進封測三廠': "AP3",
        '先進封測五廠': "AP5"
    }

    return factory_code
