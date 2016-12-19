import web,os

root = os.path.dirname(__file__)
render = web.template.render(os.path.join(root, '..', 'templates/'))

urls=(
    '/hello', 'Index'
)


app=web.application(urls,globals())
class Index:
    def GET(self):
        form=web.input(name='Nobody')
        greeting='Hello{}'.format(form.name)
        return render.index(greeting = greeting)


if __name__=="__main__":
    app.run()