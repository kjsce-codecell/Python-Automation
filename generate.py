from jinja2 import Environment, FileSystemLoader
import csv


def _render_template(name, seats):
    file_loader = FileSystemLoader('templates')
    env = Environment(
        loader=file_loader,
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
    )
    template = env.get_template('remind.html')
    return template.render(name=name, seats=seats)
