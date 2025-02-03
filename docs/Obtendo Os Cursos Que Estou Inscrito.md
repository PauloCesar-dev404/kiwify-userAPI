# Obtendo os Cursos que Estou Inscrito

Este exemplo demonstra como obter os cursos que um usuário está inscrito na Kiwify.

> **Atenção**: Certifique-se sempre de estar autenticado antes de realizar qualquer operação.

Para obter os curso que o usuário está inscrito, siga o exemplo abaixo:

```python
from kiwify_userAPI import Kiwify

kiwify = Kiwify()

my_courses = kiwify.my_subscribed_courses() # lista
for course in my_courses:
    print(course)
```
