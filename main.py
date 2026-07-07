from flask import Flask
from services.cpf_validation import validar_cpf
from routes.route_cpf import validation_bp

#---- Inicio App ------
app = Flask(__name__)


app.register_blueprint(validation_bp)




#------ Fim App
if __name__ == "__main__":
    app.run(debug=True)