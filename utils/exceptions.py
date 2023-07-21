from flask_jwt_extended.exceptions import JWTExtendedException
from werkzeug.exceptions import UnprocessableEntity, Unauthorized


class ExcHandlers():
    def __init__(self, db):
        self.db = db

    def init_app(self, app):
        @app.errorhandler(ValueError)
        def value_error(e):
            self.db.rollback()
            return dict(error={"reason": str(e)}), 400

        @app.errorhandler(UnprocessableEntity)
        def unprocess(e):
            return dict(error={"reason": str(e)}), 400


        @app.errorhandler(Unauthorized)
        def unauthorized(e):
            return dict(error={"reason": str(e)}), 401

        @app.errorhandler(Exception)
        def general_error(e):
            self.db.rollback()
            return dict(error={"reason": str(e)}), 500
