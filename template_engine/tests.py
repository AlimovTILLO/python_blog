import unittest

from template_engine.template import Template

GREETINGS_FOR_NAMES_TEMPLATE = 'Greetings for names: {names}'
HELLO_NAME_TEMPLATE = '<span>Hello <b>{name}</b></span>'


class TemplateTests(unittest.TestCase):
    def test_simple(self):
        context = {
            'name': 'John Doe'
        }
        template = Template(HELLO_NAME_TEMPLATE, context)

        actual = template.render()
        expected = '<span>Hello <b>John Doe</b></span>'

        self.assertEqual(actual, expected)

    def test_with_list_of_objects(self):
        name1_context = {
            'name': 'Name 1'
        }
        template_name1 = Template(HELLO_NAME_TEMPLATE, name1_context)
        rendered_name1_template = template_name1.render()

        name2_context = {
            'name': 'Name 2'
        }
        template_name2 = Template(HELLO_NAME_TEMPLATE, name2_context)
        rendered_name2_template = template_name2.render()

        super_template_context = {
            'names': [rendered_name1_template, rendered_name2_template]
        }
        super_template = Template(GREETINGS_FOR_NAMES_TEMPLATE, super_template_context)

        actual = super_template.render()

        expected = 'Greetings for names: <span>Hello <b>Name 1</b></span><span>Hello <b>Name 2</b></span>'

        self.assertEqual(actual, expected)
