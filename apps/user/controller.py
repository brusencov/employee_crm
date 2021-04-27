from flask import render_template, request, redirect, session, abort
import random
import string

from config import app
from apps.user.model import *


class UserController:

    def __init__(self):
        @app.route('/register', methods=['GET', 'POST'])
        def register_view():
            def GET():
                return render_template('register.html')

            def POST():
                user = User(role=UserRole.ADMIN, **request.form)
                db.session.add(user)
                db.session.commit()
                return redirect('/')

            if request.method == 'GET':
                return GET()
            elif request.method == 'POST':
                return POST()

        @app.route('/logout', methods=['GET'])
        def logout_user():
            if 'email' in session:
                session.pop('email')
            return redirect('/')

        @app.route('/login', methods=['GET', 'POST'])
        def login():
            def GET():
                return render_template('login.html')

            def POST():
                email = request.form.get('email')
                password = request.form.get('password')
                user = User.query.filter_by(email=email).first()
                if user.password == password:
                    session['id'] = user.id
                    session['email'] = user.email
                    session['role'] = user.role
                else:
                    return redirect('/login')

            if request.method == 'GET':
                return GET()
            elif request.method == 'POST':
                return POST()

        @app.route('/employee', methods=['GET', 'POST'])
        def employee():
            def GET():
                return render_template('employee.html', employees=User.query.filter_by(role=UserRole.EMPLOYEE).all())

            def POST():
                user = User(**request.form)
                db.session.add(user)
                db.session.commit()
                return redirect('/employee')

            if request.method == 'GET':
                return GET()
            elif request.method == 'POST':
                return POST()

        @app.route('/employee/<int:id>', methods=['GET'])
        def get_employee(id: int):
            return render_template('employee_detail.html', employee=User.query.filter_by(role=UserRole.EMPLOYEE, id=id).first())
