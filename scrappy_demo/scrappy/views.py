from io import BytesIO
from threading import Thread

import pandas as pd
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import render_to_response

from scrappy.db import db
from scrappy.models import ScrappyData
from scrappy.utils.uniontask import task

t = Thread(target=task)
t.start()

def index(request):
    return render(request, 'index.html', {})

def todata(request):
    options = {}
    url = request.GET.get('url')
    options.update({'url':url})
    result = db.query_data(url)
    options.update({'result': result})
    return render_to_response('data.html', options)


def search(request):
    options = {}
    render_to_url = 'data.html'
    url = request.POST.get('url')
    if not url:
        return JsonResponse({'error': '请输入网址！'}, safe=False)
    request.session['url'] = url

    sdata = ScrappyData.objects.filter(url=url).count()
    if sdata == 0:
        data = {'url': url, 'url_level': 1,'flag': 0}
        dbdata = ScrappyData()
        dbdata.from_dict(data)
        dbdata.save()

    # 跳转data页面
    return render_to_response( render_to_url, {})


def refresh(request):
    url = request.POST.get('url')
    if not url:
        url = request.session.get('url')
    result = db.query_data(url)
    return JsonResponse({'result':result}, safe=False)


def export(request):
    url = request.GET.get('url')
    type = request.GET.get('type')
    if not url:
        return JsonResponse({'error': '请输入网址！'}, safe=False)

    # 创建数据流
    output = BytesIO()
    # 创建excel work book
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    workbook = writer.book
    # cell 样式
    cell_format = workbook.add_format({'bold': 1, 'align': 'center', 'valign': 'vcenter'})

    worksheet = workbook.add_worksheet('有效链接')

    col = 0
    # 定义列名
    columns = ['id', 'url', 'url_level', 'parent_id', 'title', 'keywords', 'description', 'flag']
    # 写入第一行列名
    for item in columns:
        worksheet.write(0, col, item, cell_format)  # 第一个参数0为row值
        col += 1
    # 获取数据
    spider_result_list = db.query_data(url)
    # 写入数据
    row = 1
    index = 0
    while index < len(spider_result_list):
        for co in columns:
            worksheet.write(row, columns.index(co), spider_result_list[index][co])
        row += 1
        index += 1

    # 设置excel中A-H列的宽
    az = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    las = az[len(columns) - 1:len(columns)]
    worksheet.set_column('A:%s' % (las), 20)

    writer.close()
    output.seek(0)

    response = HttpResponse()
    execl_name = 'spiderdata'
    response['Content-Disposition'] = 'attachment;filename={0}.xlsx'.format(execl_name)
    response['Content-Type'] = 'application/vnd.ms-excel'
    response.write(output.getvalue())
    return response
