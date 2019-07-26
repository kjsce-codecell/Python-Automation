from jinja2 import Environment, FileSystemLoader
import csv


def _render_template(name, payment_status):
    # loading the templates folder
    file_loader = FileSystemLoader('templates')
    env = Environment(
        loader=file_loader,
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
    )
    # fetching the template from the FileSystemLoader
    template = env.get_template('message.txt')
    # rendering the template
    return template.render(name=name, payment_status=payment_status)


def preprocess(participants):
    # converting the list of lists to list of dict
    data = []
    for participant in participants:
        data.append({
            "name": participant[0],
            "dob": participant[1],
            "email": participant[2],
            "city": participant[3],
            "phone": participant[4],
            "payment": participant[5],
        })
    return data
