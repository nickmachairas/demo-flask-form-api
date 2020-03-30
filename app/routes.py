from flask import render_template, redirect, url_for
from app import app, db
from app.forms import StudentForm, DepartmentForm
from app.models import Students, Departments


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    dept_form = DepartmentForm()
    if dept_form.validate_on_submit():
        dept = Departments(
            dept_name=dept_form.dept_name.data,
            building=dept_form.building.data,
            budget=dept_form.budget.data)
        db.session.add(dept)
        db.session.commit()
        return redirect(url_for('index'))

    departments = Departments.query.all()

    form = StudentForm()
    form.dept_name.choices = [
        (i, i) for i in [ii.dept_name for ii in departments]]
    if form.validate_on_submit():
        student = Students(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            dept_name=form.dept_name.data)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('index'))

    students = Students.query.all()

    return render_template(
        'index.html', title='Home', dept_form=dept_form, form=form,
        departments=departments, students=students)


@app.route('/delete_dept/<dept_id>')
def delete_dept(dept_id):
    dept = Departments.query.get(dept_id)
    db.session.delete(dept)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/delete_student/<stu_id>')
def delete_student(stu_id):
    student = Students.query.get(stu_id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('index'))
