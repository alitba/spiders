from django.db import models

class ScrappyData(models.Model):
    # 自增字段
    id = models.AutoField(primary_key=True)
    # char类型最大4K(最大长度,默认值)
    url = models.CharField(max_length=800)
    url_level = models.IntegerField()
    parent_id = models.IntegerField(null=True)
    title = models.CharField(max_length=255, null=True, default='')
    # char类型最大4K(最大长度,默认值)
    keywords = models.CharField(max_length=200, null=True, default='')
    # char类型最大5K(最大长度,默认值)
    description = models.CharField(max_length=5000, null=True, default='')
    flag = models.IntegerField()
    # 时间(在保存对象自动设置当前时间,第一次创建时使用当前时间)
    update_timestamp = models.DateTimeField(auto_now=True)

    def to_dict(self):
        return {'id': self.id,
                'url': self.url,
                'url_level': self.url_level,
                'parent_id': self.parent_id,
                'title': self.title,
                'keywords': self.keywords,
                'description': self.description,
                'flag': self.flag}

    def from_dict(self, dic):
        self.url = dic['url']
        self.url_level = dic['url_level']
        self.parent_id = dic.get('parent_id')
        self.title = dic.get('title')
        self.keywords = dic.get('keywords')
        self.description = dic.get('description')
        self.flag = dic['flag']

    class Meta:
        app_label = "scrappy"


class Config(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=100)

    class Meta:
        app_label = "scrappy"
