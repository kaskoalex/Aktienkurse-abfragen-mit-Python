from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader("Aktienkurse abfragen mit Python"),
    autoescape=select_autoescape()
)