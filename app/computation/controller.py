#import model, view
from flask import Flask, render_template, request, current_app, url_for
from app.computation.forms import InputForm
from app.computation.compute import compute
from app.computation import bp

# View
@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        result = compute(form.A.data, form.b.data, form.w.data, form.T.data)
    else: 
        result = None

    return render_template("view_bootstrap.html", form = form, result = result)

