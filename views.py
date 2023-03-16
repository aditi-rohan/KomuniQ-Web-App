from flask import Blueprint, render_template, request, jsonify, redirect, url_for

#initialize blueprint
views = Blueprint(__name__, "views")


@views.route('/')
def home():
  return render_template("login.html")


database = {'username': 'password', 'StudentID': 'sPassword'}


# declara cual dashboard se le ensenara al usuario dependiendo de si es padre, maestro, admin, o no reconocido
@views.route('/form_login', methods=['POST', 'GET'])
def login():
  user = request.form('username')
  pwd = request.form('password')
  permission = request.form('permission')
  if (user not in database):
    return render_template('login.html', info='Usuario no es reconocido')
  else:
    if (database[user] != pwd):
      return render_template('login.html', info='Usuario no es reconocido')
    else:
      if (permission == ""):
        return render_template('login.html',
                               info='Usuario no es reconocido, escoja su rol')
      elif (permission == 'Acudiente'):
        return render_template('parent_dashboard.html')
      elif (permission == 'Educador/a'):
        return render_template('teacher_dashboard.html')
      elif (permission == 'Administrador/a'):
        return render_template('admin_dashboard.html')
  parent = "parent"
  teacher = "teacher"
  admins = "admin"
  userPermissions = input("Get user permissions")
  if (userPermissions == parent):
    return render_template("parent_dashboard.html")
  elif (userPermissions == teacher):
    return render_template("teacher_dashboard.html")
  elif (userPermissions == admins):
    return render_template("admin_dashboard.html")
  # si el usuario no es reconocido regresara a la pagina de entrada
  else:
    return go_to_home()


@views.route("/parent-dashboard/")
def parent_dashboard():
  args = request.args
  ID = args.get('StudentID')
  return render_template("index.html")


@views.route("/json")
def get_json():
  return jsonify({'name': 'tim', 'coolness': 10})


@views.route("/data")
def get_data():
  data = request.json
  return jsonify(data)


@views.route("/go-to-home")
def go_to_home():
  return redirect(url_for("views.get_json"))
