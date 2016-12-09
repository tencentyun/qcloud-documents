#coding:utf-8
import sys
import json
sys.path.append('.')
import glob
f = glob.glob('*.py')
for i in f:
    if 'render' not in i:
        a=__import__(i[:-3])
        from jinja2 import Template
        from jinja2 import Environment, PackageLoader
        template = Template(open("templates.md").read().decode('utf-8'))
        a.output_json=json.dumps(a.output_json,indent=4)
        print template.render(globals()['a'].__dict__)
