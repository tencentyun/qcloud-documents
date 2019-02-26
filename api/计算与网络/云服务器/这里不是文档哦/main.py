import toml
import pymysql
import functools
import itertools
import jinja2
import re
import os
loader = jinja2.FileSystemLoader('.')
class RelEnvironment(jinja2.Environment):
    """Override join_path() to enable relative template paths."""
    def join_path(self, template, parent):
        return os.path.join(os.path.dirname(parent), template)

env = RelEnvironment(loader=loader)
url={'instance_buy_limit':'https://cloud.tencent.com/document/product/213/2664'}

def gen(**args):
    import glob
    end_strings='.template'
    for filename in list(glob.glob(f'**/*{end_strings}',recursive=True)):
        print(f"处理{filename}...")
        template = env.get_template(filename)
        result = template.render(**args)
        new_filename=filename[:-len(end_strings)]
        open(new_filename,"w").write(result)


print ('context 构建完成。')    
gen(**locals())
