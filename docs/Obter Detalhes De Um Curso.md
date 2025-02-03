# Obter Detalhes de um Curso

Para obter detalhes de um curso específico, siga o exemplo abaixo:

```python
from kiwify_userAPI import Kiwify

# Inicializa a API do Kiwify
kiwify = Kiwify()

# ID do curso
course_id = 'course-id'

# Obtém os detalhes do curso
course_details = kiwify.get_details_course(course_id=course_id)

# Imprime os detalhes do curso
print("ID do curso:", course_details.id)
print("Módulos:", course_details.get_modules)
print("Quantidade de módulos:", course_details.count_modules)
print("Configurações do curso:", course_details.course_configs)
print("Certificado:", course_details.certificate)
print("Certificado habilitado:", course_details.certificate_enabled)
print("Aula atual:", course_details.current_lesson)
print("Nome:", course_details.name)
print("Progresso completado:", course_details.completed_progress)
print("Informações da loja:", course_details.get_store_info)

```
