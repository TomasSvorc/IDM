from app import app, db
from app.models import User
from werkzeug.security import generate_password_hash

def create_admin():
    with app.app_context():
        if not User.query.filter_by(username='admin').first():
            hashed_password = generate_password_hash('admin', method='pbkdf2:sha256')
            admin = User(username='admin', password=hashed_password, role='admin')
            db.session.add(admin)
            db.session.commit()
            print('Admin user created')

def create_database():
    with app.app_context():
        db.create_all()
        create_admin()

if __name__ == '__main__':
    create_database()
    app.run(host='0.0.0.0', port=5000)