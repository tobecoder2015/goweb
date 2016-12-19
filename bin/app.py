import web,os

root = os.path.dirname(__file__)
render = web.template.render(os.path.join(root, '..', 'templates/'))

urls=(
    '/','Index'
)

"""
urls=('/','Index')
中Index 与类Index 为一一对应关系

render.index(greeting = greeting)

index  与templetes 文件名对应
参数与 模板文件中变量对应
"""
app=web.application(urls,globals())
class Index:
    def GET(self):
        greeting='Hello world'
        return render.index(greeting = greeting)


if __name__=="__main__":
    app.run()