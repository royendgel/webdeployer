class Generator(object):
  def __init__(self, generate=None):
    pass

  def config_parser(self, global_first=False):
    if global_first:
      eval(open(self.global_path).read())

    eval(open('webdeployer-config.py'))


  def __template_parser(self, template, settings=None):
    with open('generators/nginx.tpl') as tpl:
      from jinja2 import Template
      jinja_template = Template(tpl.read())
      print  jinja_template.render(app_name="jsjsjsj")


  def generate_nginx(self, settings=None):
    template = 'generators/nginx.tpl'
    self.__template_parser(template)

  def generate_gunicorn(self, settings=None):
    template = 'generators/gunicorn.tpl'
    pass

  def generate_supervisord(self, settings=None):
    template = 'generators/supervisord.tpl'
    pass

  def generate_config(self, settings=None):
    template = 'project-config.tpl'
    pass

a = Generator()
a.generate_nginx()