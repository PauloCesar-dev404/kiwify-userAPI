
# Obter Detalhes de uma Aula Específica de um Curso na Kiwify


```python
from kiwify_userAPI import Kiwify

# Inicializa a API do Kiwify
kiwify = Kiwify()

# ID do curso
course_id = 'course-id'

# Obtém os detalhes do curso
course_details = kiwify.get_details_course(course_id=course_id)

# IDs da aula e do módulo
lesson_id = ''  # ID da aula
module_id = ''  # ID do módulo

# Obtém os detalhes do módulo
m_details = course_details.module_details(module_id=module_id)
lessons_module = m_details.get_lessons()
lessons_count = m_details.count_lessons()
module_is_free = m_details.is_free()
thum_module = m_details.thumbnail()
date_upload = m_details.created_at()
is_active = m_details.is_active()
details_lesson = m_details.get_lesson_details(lesson_id=lesson_id)

# Imprime os detalhes da aula e do módulo
print("ID do curso:", course_details.id)
print("Módulos:", course_details.get_modules)
print("Quantidade de módulos:", course_details.count_modules)
print("Configurações do curso:", course_details.course_configs)
print("Certificado:", course_details.certificate)
print("Certificado habilitado:", course_details.certificate_enabled)
print("Aula atual:", course_details.current_lesson)
print("Nome do curso:", course_details.name)
print("Progresso completado:", course_details.completed_progress)
print("Informações da loja:", course_details.get_store_info)

print("Aulas do módulo:", lessons_module)
print("Quantidade de aulas no módulo:", lessons_count)
print("O módulo é gratuito?", module_is_free)
print("Thumbnail do módulo:", thum_module)
print("Data de upload do módulo:", date_upload)
print("O módulo está ativo?", is_active)

print("Título da aula:", details_lesson.title)
print("Thumbnail da aula:", details_lesson.thumbnail)
print("Tipo da aula:", details_lesson.type)
print("Conteúdo da aula:", details_lesson.content)
print("Aula completada:", details_lesson.completed)
print("Duração da aula em dias:", details_lesson.duration_days)
print("A aula expirou?", details_lesson.expired)
print("Arquivos da aula:", details_lesson.files)
print("Duração limitada da aula:", details_lesson.limit_duration)
print("A aula está bloqueada:", details_lesson.locked)
print("Ordem da aula:", details_lesson.order)
print("A aula é pública?", details_lesson.is_public)
### objeto video
video_object = details_lesson.video

if video_object:
    print("ID do vídeo:", video_object.get_id())
    print("Data de upload do host:", video_object.get_host_upload_date())
    print("Nome do vídeo:", video_object.get_name())
    print("Status do vídeo:", video_object.get_status())
    print("Thumbnail do vídeo:", video_object.get_thumbnail())
    print("Data de criação do vídeo:", video_object.get_created_at())
    print("Data de exclusão do vídeo:", video_object.get_deleted_at())
    print("Data de upload do host:", video_object.get_host_upload_date())
    print("Metadados de codificação do vídeo:", video_object.get_encoding_metadata())
    print("Link de stream do vídeo:", video_object.get_stream_link())
    print("Data de atualização do vídeo:", video_object.get_updated_at())
    print("Versão do Vimeo do vídeo:", video_object.get_vimeo_version())
```
