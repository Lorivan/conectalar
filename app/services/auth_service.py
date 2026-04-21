import bcrypt


def verificar_senha(senha_plana: str, hash_senha: str) -> bool:
    if not senha_plana or not hash_senha:
        return False

    return bcrypt.checkpw(
        senha_plana.encode('utf-8'),
        hash_senha.encode('utf-8')
    )


def gerar_hash_senha(senha_plana: str) -> str:
    hash_senha = bcrypt.hashpw(
        senha_plana.encode('utf-8'),
        bcrypt.gensalt()
    )
    return hash_senha.decode('utf-8')
