from mongoengine import *


class MongoTest(Document):
    test_id = IntField(max_length=16)
    name = StringField()
    age = IntField(max_length=3)
    task = StringField()


connect('mongo_test')


def save_data():
    t1 = MongoTest(test_id=1, name="张小凡", age=18, task="诛仙")
    t2 = MongoTest(test_id=2, name="陆雪琪", age=17, task="天琊")
    t3 = MongoTest(test_id=3, name="碧瑶", age=16, task="合欢铃")
    t_obj = [t1, t2, t3]
    [item.save() for item in t_obj]


def update_date():
    # 错误语法
    # MongoTest.update({"test_id": 1, "name": "张小凡"}, {"$set": dict(test_id=11, name="张小凡", age=20, task="诛仙")}, True)
    # MongoTest.objects(test_id=1, name="张小凡").update({"$set": dict(test_id=11, name="张小凡", age=20, task="诛仙")}, True)

    # pymongo语法更新，不存在则创建
    # DeprecationWarning: update is deprecated. Use replace_one, update_one or update_many instead.
    # MongoTest._get_collection().update({"test_id": 1, "name": "张小凡"},
    #                                    {"$set": dict(test_id=11, name="张小凡", age=20, task="诛仙")}, True)
    # MongoTest._get_collection().update({"test_id": 17, "name": "小白"},
    #                                    {"$set": dict(test_id=17, name="小白", age=999, task="九尾")}, True)
    # res = MongoTest._get_collection().update_one({"test_id": 17, "name": "小白"},
    #                                              {"$set": dict(test_id=5, name="小白", age=999, task="九尾")}, True)
    # print(res)
    # 通过对象更新
    # t1 = MongoTest.objects.filter(test_id=11, name="张小凡").first()
    # t1.task = "大竹峰"
    # t1.save()

    # 只更新，找不到不创建
    # MongoTest.objects(test_id=5, name="小白").update(name="小六", age=666, task="六尾")
    # 存在更新返回1
    res = MongoTest.objects(test_id=5, name="小白").update_one(name="小六", age=666, task="六尾")
    print(res)
    # 不存在不创建返回0
    res = MongoTest.objects(test_id=7, name="小七").update_one(age=777, task="这是啥")
    print(res)


if __name__ == '__main__':
    # save_data()
    update_date()
    pass
