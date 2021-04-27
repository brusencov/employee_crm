from config import app

"""
@TODO
1) Создать связь один ко многим в моделе Attendance
2) Создать запросы в apps.attendance.controller для создания, удаления и редактирования Attendance
3) Создать html формы для User, Attendance
"""


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
