from flask import Blueprint,jsonify
from services.cpf_validation import validar_cpf

validation_bp = Blueprint(
    "validation",
    __name__
)


@validation_bp.route("/api/v1/validators/cpf/<cpf>")
def cpf_validator(cpf):

    cpf = cpf.replace(".", "").replace("-", "")
    
    if not cpf.isdigit():
        return jsonify({
            "valido": False,
            "erro": "CPF contém caracteres inválidos."
            })
    
    return validar_cpf(cpf)   