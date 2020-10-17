from flask_app import create_app
from werkzeug.security import generate_password_hash

from models.db import db
from models.user import User

app = create_app()
app.app_context().push()

# User
n_users = 30
for i in range(n_users):
  id_ = i + 1
  name = 'test' + str(id_)
  email = 'test' + str(id_) + '@test'
  password = generate_password_hash('testtest')

  user = User(name=name, email=email, password=password)
  db.session.add(user)
db.session.commit()

if __name__ == '__main__':
  app.run()
