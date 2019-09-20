#import model, view
from flask import Flask, render_template, request, current_app
from app.computation.forms import InputForm
from app.computation.compute import compute
from app.computation import bp

# View
@bp.route('/index', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        result = compute(form.A.data, form.b.data, form.w.data, form.T.data)
    else: 
        result = None

    return render_template("view_bootstrap.html", form = form, result = result)

