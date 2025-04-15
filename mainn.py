from jinja2 import Template

name ='Давид'

age=19

tm=Template("Мне {{a}} лет и имя мне {{n}} сын Араторна")
msg=tm.render(n=name,a=age)

print(msg)