import collections
import os

from settings import TEMPLATES_DIR


class Template(object):
    def __init__(self, template_path, context):
        self.context = dict()

        with open(os.path.join(TEMPLATES_DIR, template_path), 'r') as template_file:
            self.template = template_file.read()

        for key, value in context.items():
            if isinstance(value, collections.Iterable):
                value = ''.join(value)
            self.context[key] = value

    def render(self):
        return self.template.format(**self.context)
