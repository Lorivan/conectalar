import bcrypt
from werkzeug.security import check_password_hash, generate_password_hash


def verificar_senha(senha_plana: str, hash_senha: str) -> bool:
    if not senha_plana or not hash_senha:
        return False

    # 1) Tenta validar hash bcrypt legado (compatível com base atual)
    try:
        return bcrypt.checkpw(
            senha_plana.encode('utf-8'),
            hash_senha.encode('utf-8')
        )
    except ValueError:
        # 2) Fallback para hashes Werkzeug (pbkdf2/scrypt)
        return check_password_hash(hash_senha, senha_plana)


def gerar_hash_senha(senha_plana: str) -> str:
    if not senha_plana:
        raise ValueError('Senha inválida para geração de hash.')

    # Novo padrão de cadastro usando Werkzeug
    return generate_password_hash(senha_plana)