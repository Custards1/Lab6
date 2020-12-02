from flask import Flask, render_template, request
from university import University

app = Flask(__name__)  # TODO: Check this. This is the flask app called in the main (at the bottom)
university = University("UCD")  # TODO: Check this. This is the university global object used by all flask methods.


# ----------------------------------------------------------------------------------------------------------------------
@app.route('/')
def home():
    """Renders the home path (Main Menu) for http://127.0.0.1:5000/"""
    return render_template('home.html')


# ----------------------------------------------------------------------------------------------------------------------
@app.route('/students_all')
def students_all():
    """
    Renders the path for http://127.0.0.1:5000/students_all
    List all the student objects once loaded using the university.
    """
    report_title = "All Students"
    #students = university.sample_student_list()  # TODO: Remove this Sample Statement
    students = university.load_all_students()  # TODO: uncomment after removing line above
    return render_template('students.html', report_title=report_title, students=students)


# ----------------------------------------------------------------------------------------------------------------------
@app.route('/students_search')
def students_search():
    """
    Renders the path for http://127.0.0.1:5000/students_search
    If the request has a name value such in  http://127.0.0.1:5000/students_search?name=john then loads the students
    with john in their names using the university.
    """
    if request.args.get('name'):
        report_title = "All Students"
        students = university.load_students_by_name(request.args.get('name'))
        return render_template('students.html', report_title=report_title, students=students)
    else:
        return render_template('student_search.html')


# ----------------------------------------------------------------------------------------------------------------------
@app.route('/courses_all')
def courses_all():
    """
    Renders the path for http://127.0.0.1:5000/courses_all
    List all the course objects once loaded using the university.
    """
    report_title = "List of All Courses"
    courses = university.load_all_courses()
    return render_template('courses.html', report_title=report_title, courses=courses)


# ----------------------------------------------------------------------------------------------------------------------
@app.route('/courses_search')
def courses_search():
    """
    Renders the path for http://127.0.0.1:5000/courses_search
    If the request has a subject value such in  http://127.0.0.1:5000/courses_search?subject=csc then loads the
    courses with csc in their subject using the university.
    """
    if request.args.get('subject'):
        report_title = "List of All Courses"
        courses = university.load_courses_by_subject(request.args.get('subject'))
        return render_template('courses.html', report_title=report_title, courses=courses)
    else:
        return render_template('course_search.html')


# ######################################################################################################################
# ######################################################################################################################
if __name__ == '__main__':
    app.run()
