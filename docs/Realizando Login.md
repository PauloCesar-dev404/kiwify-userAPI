# Realizando Login

Para acessar a plataforma kiwify utilizamos a classe `KiwifyAuth`.

### 1. **Login Convencional (Com Email e Senha)**

O login convencional exige que o usuário forneça seu e-mail e senha.

```python
from kiwify_userAPI import KiwifyAuth
auth = KiwifyAuth()
is_login = auth.login(email='',password=r'')
if is_login:
    print('foi!')
else:
    print("Erro!")
```

#### Parâmetros:
- `email`: E-mail do usuário registrado na plataforma.
- `password`: Senha associada ao e-mail do usuário.

---