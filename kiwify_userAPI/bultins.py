from .exeptions import TokenInvalid


class Video:
    """
    id
    name
    course_id
    encoded
    size
    duration
    external_id
    stream_link
    download_link
    thumbnail
    status
    url
    producer_id
    host_upload_date
    created_at
    updated_at
    deleted_at
    last_processed_at
    last_vimeo_processing_at
    vimeo_version
    encoding_started_at
    encoding_finished_at
    encoding_status
    encoding_workflow_name
    encoding_error_stacktrace
    encoding_metadata
    """

    def __init__(self, video: dict):
        """
        Inicializa o objeto Video.

        Args:
            video (dict): Um dicionário contendo dados do vídeo.
        """
        self.__video_data = video

    def get_id(self) -> str:
        """
        Obtém o ID do vídeo.

        Returns:
            str: O ID do vídeo.
        """
        return self.__video_data.get('id', '')

    def get_name(self) -> str:
        """
        Nome bruto do vídeo (o que foi feito upload).

        Returns:
            str: O nome bruto do vídeo.
        """
        return self.__video_data.get('name', '')

    def get_stream_link(self) -> str:
        """
        Obtém o link de streaming.

        Returns:
            str: O link de streaming.
        """
        link = self.__video_data.get('stream_link', '')
        if not link.startswith('https://'):
            if link:
                link = 'https://d3pjuhbfoxhm7c.cloudfront.net' + link
                return str(link)
            else:
                return ""
        else:
            return ""

    def get_thumbnail(self) -> str:
        """
        Obtém o link da thumbnail.

        Returns:
            str: O link da thumbnail.
        """
        link = self.__video_data.get('thumbnail', '')
        if not link.startswith('https://'):
            if link:
                link = 'https://d3pjuhbfoxhm7c.cloudfront.net' + link
                return link
            else:
                return ''
        else:
            return ''

    def get_status(self) -> str:
        """
        Obtém o status do vídeo.

        Returns:
            str: O status do vídeo.
        """
        return self.__video_data.get('status', '')

    def get_host_upload_date(self) -> str:
        """
        Data de upload.

        Returns:
            str: A data de upload do vídeo.
        """
        return self.__video_data.get('host_upload_date', '')

    def get_created_at(self) -> str:
        """
        Obtém a data de criação do vídeo.

        Returns:
            str: A data de criação do vídeo.
        """
        return self.__video_data.get('created_at', '')

    def get_updated_at(self) -> str:
        """
        Obtém a data de atualização do vídeo.

        Returns:
            str: A data de atualização do vídeo.
        """
        return self.__video_data.get('updated_at', '')

    def get_deleted_at(self) -> str:
        """
        Obtém a data de exclusão do vídeo.

        Returns:
            str: A data de exclusão do vídeo.
        """
        return self.__video_data.get('deleted_at', '')

    def get_vimeo_version(self) -> str:
        """
        Obtém a versão do Vimeo.

        Returns:
            str: A versão do Vimeo.
        """
        return self.__video_data.get('vimeo_version', '')

    def get_encoding_metadata(self) -> dict:
        """
        Obtém os metadados de codificação.

        Returns:
            dict: Os metadados de codificação.
        """
        return self.__video_data.get('encoding_metadata', {})


class Lesson:
    """
    id
    title
    content
    published
    delivery_type
    delivery_days
    duration_days
    limit_duration
    module_id
    order
    ref
    delivery_date
    locked
    expired
    completed
    type
    thumbnail
    thumbnail_slider_cover
    show_thumbnail_title
    files
    video
    """

    def __init__(self, lesson: dict):
        """
        Inicializa o objeto Lesson.

        Args:
            lesson (dict): Um dicionário contendo dados da aula.
        """
        self._lesson = lesson
    @property
    def is_public(self) -> bool:
        """
        Verifica se a aula é privada ou pública.

        Returns:
            bool: True se a aula for pública, False se for privada.
        """
        return self._lesson.get('published', False)

    @property
    def title(self) -> str:
        """
        Obtém o título da aula.

        Returns:
            str: O título da aula.
        """
        return self._lesson.get('title', '')

    @property
    def content(self) -> str:
        """
        Descrição da aula.

        Returns:
            str: A descrição da aula.
        """
        return self._lesson.get('content', "")

    @property
    def duration_days(self) -> int:
        """
        Obtém a duração em dias.

        Returns:
            int: A duração em dias.
        """
        return self._lesson.get('duration_days', 0)

    @property
    def limit_duration(self) -> bool:
        """
        Verifica se a duração é limitada.

        Returns:
            bool: True se a duração for limitada, False caso contrário.
        """
        return self._lesson.get('limit_duration', False)

    @property
    def order(self) -> int:
        """
        Obtém a ordem da aula.

        Returns:
            int: A ordem da aula.
        """
        return self._lesson.get('order', 0)

    @property
    def locked(self) -> bool:
        """
        Verifica se a aula está bloqueada.

        Returns:
            bool: True se a aula estiver bloqueada, False caso contrário.
        """
        return self._lesson.get('locked', False)

    @property
    def expired(self) -> bool:
        """
        Verifica se a aula expirou.

        Returns:
            bool: True se a aula tiver expirado, False caso contrário.
        """
        return self._lesson.get('expired', False)

    @property
    def completed(self) -> bool:
        """
        Verifica se a aula está concluída.

        Returns:
            bool: True se a aula estiver concluída, False caso contrário.
        """
        return self._lesson.get('completed', False)

    @property
    def type(self) -> str:
        """
        Obtém o tipo de aula.

        Returns:
            str: O tipo de aula.
        """
        return self._lesson.get('type', '')

    @property
    def thumbnail(self) -> str:
        """
        Obtém a URL da thumbnail.

        Returns:
            str: A URL da thumbnail.
        """
        return self._lesson.get('thumbnail', '')

    @property
    def files(self) -> list:
        """
        Obtém a lista de arquivos.

        Returns:
            list: A lista de arquivos.
        """
        return self._lesson.get('files', [])

    @property
    def video(self) -> Video:
        """
        Obtém a URL do vídeo.

        Returns:
            Video: O objeto Video.
        """
        v = self._lesson.get('video', {})
        vv = Video(video=v)
        return vv


class Module:

    def __init__(self, module: dict, course_id: str):
        """
        Inicializa o objeto Module.

        Args:
            module (dict): Um dicionário contendo dados do módulo.
        """
        self._modules = module
        self._course_id = course_id

    def get_lessons(self) -> list[dict]:
        """
        Obtém todas as aulas de um módulo.

        Returns:
            list[dict]: Uma lista contendo o ID da aula e seu título.
        """
        lessons = self._modules.get('lessons', [])
        ls = []
        for l in lessons:
            id_c = l.get("id")
            title = l.get("title")
            dt = {"title": title, "id": id_c}
            ls.append(dt)
        return ls

    def count_lessons(self) -> int:
        """
        Quantidade de aulas no módulo.

        Returns:
            int: O número de aulas no módulo.
        """
        l = self.get_lessons()
        return len(l)

    def is_free(self):
        """
        Verifica se a aula é gratuita.

        Returns:
            bool: True se a aula for gratuita, caso contrário False.
        """
        return self._modules.get('free')

    def is_active(self):
        """
        Verifica se a aula está ativa.

        Returns:
            bool: True se a aula estiver ativa, caso contrário False.
        """
        return self._modules.get("active")

    def thumbnail(self):
        """
        Obtém a thumbnail.

        Returns:
            A thumbnail do módulo.
        """
        return self._modules.get('thumbnail')

    def created_at(self):
        """
        Obtém a data de criação.

        Returns:
            A data de criação do módulo.
        """
        return self._modules.get('created_at')

    def get_lesson_details(self, lesson_id: str):
        """
        Obtém o objeto aula.

        Args:
            lesson_id (str): O ID da aula.

        Returns:
            Lesson: O objeto aula.
        """
        from .sections import get_lesson_details
        from .authenticate import KiwifyAuth
        auth = KiwifyAuth()
        l = self._modules.get('lessons', [])
        for aule in l:
            id_l = aule.get('id')
            if lesson_id == id_l:
                try:
                    details = get_lesson_details(lesson_id=lesson_id, course_id=self._course_id)
                    less = Lesson(lesson=details)
                    return less
                except TokenInvalid as e:
                    auth._update_session()
                    details = get_lesson_details(lesson_id=lesson_id, course_id=self._course_id)
                    less = Lesson(lesson=details)
                    return less
                except Exception as e:
                    raise Exception("Erro ao obter detalhes da aula!")


class Course:
    """Detalhes do curso."""

    def __init__(self, results: dict):
        """
        Inicializa o objeto Course.

        Args:
            results (dict): Um dicionário contendo dados do curso.
        """
        self.__results = results['course']
        self.__modules = self.__load_course()
        self.__data = results

    def __load_course(self) -> list[dict]:
        """
        Carrega os dados do curso.

        Returns:
            list[dict]: Uma lista de dicionários contendo dados dos módulos.
        """
        data = []
        modules = self.__results['modules']
        for k in modules:
            id_m = k.get("id", '')
            data.append({'id': id_m, 'brute': k})
        return data

    @property
    def id(self):
        """
        Obtém o ID do curso.

        Returns:
            O ID do curso.
        """
        return self.__results.get("id")

    @property
    def name(self):
        """
        Obtém o nome do curso.

        Returns:
            O nome do curso.
        """
        return self.__results.get("name")

    @property
    def current_lesson(self):
        """
        Obtém os dados da aula atual.

        Returns:
            Os dados da aula atual.
        """
        return self.__results.get("current_lesson_data")

    @property
    def get_store_info(self):
        """
        Obtém as informações da loja.

        Returns:
            As informações da loja.
        """
        return self.__results.get("store")

    @property
    def course_configs(self):
        """
        Obtém as configurações gerais do curso.

        Returns:
            As configurações gerais do curso.
        """
        return self.__results.get("config")

    @property
    def get_modules(self):
        """
        Extrai e retorna uma lista de módulos com informações organizadas em ordem.

        Returns:
            list[dict]: Uma lista de dicionários contendo 'order', 'name' e 'id' de cada módulo.
        """
        try:
            data = []
            modules = self.__results.get('modules', [])
            if not isinstance(modules, list):
                raise ValueError("O campo 'modules' deve ser uma lista.")

            for order, module in enumerate(modules, start=1):
                name = module.get('name', '')
                id_m = module.get("id", '')
                module_data = {"order": order, "name": name, "id": id_m}
                if module_data not in data:
                    data.append(module_data)

            return data

        except Exception as e:
            raise Exception(f"Erro ao obter os módulos: {e}")

    def module_details(self, module_id: str):
        """
        Obtém o objeto do módulo.

        Args:
            module_id (str): O ID do módulo.

        Returns:
            Module: O objeto do módulo.
        """
        for ids in self.__modules:
            if module_id == ids.get('id'):
                c = Module(module=ids.get('brute'), course_id=self.id)
                return c

    @property
    def count_modules(self) -> int:
        """
        Conta o número de módulos.

        Returns:
            int: O número de módulos.
        """
        return len(self.get_modules)

    @property
    def completed_progress(self):
        """
        Obtém a porcentagem de progresso concluído.

        Returns:
            str: A porcentagem de progresso concluído.
        """
        return str(f'{self.__results.get("completed_progress")}%')

    @property
    def certificate_enabled(self) -> bool:
        """
        Verifica se o certificado está habilitado.

        Returns:
            bool: True se o certificado estiver habilitado, caso contrário False.
        """
        return self.__data.get('certificate_enabled')

    @property
    def certificate(self):
        """
        Obtém os dados do certificado.

        Returns:
            Os dados do certificado.
        """
        return self.__data.get('certificate')
