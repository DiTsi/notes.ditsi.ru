# Flask

main.py:

```Python
from flask import Flask, render_template, send_file, request
from forms import SearchForm


application = Flask(__name__)
# you must generate this key with os.urandom(<number>) command
application.config.update(dict(SECRET_KEY="<key>"))


@application.route("/", methods=['POST', 'GET'])
def root():
    form = SearchForm()
    status = ""

    if form.validate_on_submit():
        text = request.form.get("text")
        area_list = request.form.getlist("cities")

        if not form.subm.data:
            some_var = some_func()
            status = "some_var: {}".format(some_var)
        else:
            save_file(filename)
            return send_file("./file.txt", as_attachment=True)
    return render_template("root.html", form=form, title="Search", message=status)


if __name__ == "__main__":
    host = "0.0.0.0"
    port = "5000"
    application.run(host=host, port=port, debug=True)
```

forms.py:

```Python
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField


class SearchForm(FlaskForm):
    text = StringField('Text')
    cities = SelectMultipleField("list", choices=[
        ("1", "item_1"),
        ("2", "item_2")
    ])
    subm = SubmitField("submit")
    but = SubmitField("Button")
```

static/css/style.css:

```CSS
body {
    background-color: #eeeeee;
    color: #444444;
}

# select without scroll
select {
    height: 250px;
    width: 100%;
    padding:7px;
    display:inline-block;
    overflow:hidden;
}

tr .row_name {
    font-weight: bold;
    width: 160px;
}
tr .row_value {
    width: 250px;
}
td.row_value input {
    width: 100%;
}
```

templates/layout.html:

```HTML

<html lang="en">
<head>
    <meta charset="UTF-8">
    {% if title %}
    <title>Title -- {{ title }}</title>
    {% else %}
    <title>Title</title>
    {% endif %}
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <h1>{{ title }}</h1>
    {% block content %}{% endblock content %}
    <h5>{{ message }}</h5>
</body>
</html>
```

template/root.html:

```HTML
{% extends "layout.html" %}
{% block content %}
<form method="post" action="">
    {{ form.hidden_tag() }}
    <table>
        <tr>
            <td class="row_name">{{ form.text.label }}:</td>
            <td class="row_value">{{ form.text }}</td>
        </tr>
        <tr>
            <td class="row_name">{{ form.cities.label }}:</td>
            <td class="row_value">{{ form.cities }}</td>
        </tr>
    </table>
    {{ form.subm }}
    {{ form.calculate }}
</form>
{% endblock content %}
```

</body></html>