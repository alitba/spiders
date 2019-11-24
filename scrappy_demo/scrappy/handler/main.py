from scrappy import views
from scrappy_demo import settings

cmd_list = [('查询', 'query'), ('退出', 'exit')]

def main():
    print('\033[1;42m欢迎您登录Scrappy系统\033[0m')

    # 程序启动，打印功能列表
    for i, j in enumerate(cmd_list, 1):
        print(i, j[0])

    while True:
        input_num = 0
        try:
            input_num = int(input('请输入操作的序号：'))
        except:
            print('对不起，输入的序号有误。')
            continue

        if 1 == input_num:
            while True:
                url = input('>>请输入想要访问的网址，不填将默认使用 Baidu，q 结束查询：')
                if 'q' == url:
                    break
                elif '' == url:
                    url = settings.url
                kw = input('>>请输入想要查询的关键字：')
                result = getattr(views, cmd_list[input_num - 1][1])(url, kw)
                print('搜索结果：\n', result)
        elif 2 == input_num:
            print('\033[1;42m系统退出\033[0m')
            exit(0)


