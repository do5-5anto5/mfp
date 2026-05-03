# Excrever uma função que determina se uma senha é segura ou não.
# Definir uma senha degura como aquela que tenha 8 caracteres - x
#   que contem pelo menos uma letra maiúscula - x
#  e uma minúscula - x
#   e pelo menos 1 numero. - x
# Retornar True para segura e False para insegura

# def check_len(password: str) -> bool:
#     if len(password) >= 8:
#         return True
#     return False

# def check_upper(password: str) -> bool:
#     for  character in password:
#         if character.isupper():
#             return True
#     return False

# def check_lower(password: str) -> bool:
#     for  character in password:
#         if character.islower():
#             return True
#     return False

# def check_num(password: str) -> bool:
#     for character in password:
#         if character.isdigit():
#             return True
#     return False


# solução de com lambdas com iteraçoes - legal, mas menos pragmatica
# check_len= lambda password: len(password) >= 8
# check_upper = lambda password: any(char.isupper() for char in password)
# check_lower = lambda password: any(char.islower() for char in password)
# check_num = lambda password: any(char.isdigit for char in password)

# def check_password_security(password: str) -> bool:
#     if check_len(password) and check_lower(password) and check_upper(password) and check_num(password):
#         return True
#     else:
#         return False


def check_password_security(password: str) -> bool:
    check_len = (
        lambda password: not len(password) < 8
        and not password.isupper()
        and not password.islower()
        and not password.isdigit()
        and password.isalnum()
    )
    
    if check_len(password):
        return True
    else : return False


senha = '1jonathan'
print(check_password_security(senha))
