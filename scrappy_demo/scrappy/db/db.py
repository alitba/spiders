from django.db.models import Q
import json
from threading import Lock
from scrappy.models import ScrappyData

# 根据给定的URL，获取所有子URL信息
def query_data(url):
    result = []
    level1_data = ScrappyData.objects.filter(url=url).all()
    if len(level1_data) > 0:
        result.append(level1_data[0].to_dict())
        # leveled_ids = get_sub_ids([level1_data[0].id])
        level2_data = ScrappyData.objects.filter(parent_id=level1_data[0].id).all()
        level2_ids = []
        for data_l2 in level2_data:
            r_dict = data_l2.to_dict()
            result.append(r_dict)
            level2_ids.append(data_l2.id)
        levele3_data = ScrappyData.objects.filter(parent_id__in=level2_ids).all()
        for data_l3 in level2_data:
            r_dict = data_l3.to_dict()
            result.append(r_dict)
    return result
