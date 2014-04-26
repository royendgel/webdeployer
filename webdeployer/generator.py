from pkg_resources import resource_string

class Generator(object):
  def __init__(self, generate=None):
    pass

  def config_parser(self, global_first=False):
    if global_first:
      eval(open(self.global_path).read())

    eval(open('webdeployer-config.py'))

  def __open_template(self, template_name):
    template_contents = resource_string('generators', template_name)
    return template_contents

  def __template_parser(self, template_name, settings=None):
    from jinja2 import Environment
    return Environment().from_string(self.__open_template(template_name)).render(settings=settings)

  def generate_nginx(self, settings=None):
    template = 'nginx.tpl'
    return self.__template_parser(template, settings)

  def generate_gunicorn(self, settings=None):
    template = 'gunicorn.tpl'
    pass

  def generate_supervisord(self, settings=None):
    template = 'supervisord.tpl'
    pass

  def generate_config(self, settings=None):
    template = 'project-config.tpl'
    pass