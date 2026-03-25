from flask import Flask


def create_app():
    app = Flask(__name__)

    from app.routes.person_routes import person_bp
    from app.routes.course_routes import course_bp
    # from app.routes.booking_routes import booking_bp

    app.register_blueprint(person_bp)
    app.register_blueprint(course_bp)
    # app.register_blueprint(booking_bp)

    return app
