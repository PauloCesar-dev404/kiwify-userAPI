import json
import requests
from .exeptions import KiwifyUserApiExceptions, UnhandledExceptions,TokenInvalid
from .sections import get_courses_plan
from .api import HEADERS_USER
from .authenticate import KiwifyAuth
from .bultins import Course

auth = KiwifyAuth()
verif_login = auth.verif_login()


class Kiwify:

    def __init__(self):
        """
        Inicializa o objeto Kiwify e atualiza a sessão se necessário.
        """
        self.__headers = HEADERS_USER
        if verif_login is None:
            auth._update_session()

    @staticmethod
    def my_subscribed_courses() -> list[dict]:
        """
        Obtém os cursos que o utilizador está inscrito.

        Returns:
            list: uma lista de diconarios contendo os cursos inscritos.
        """
        try:
            courses = get_courses_plan()
            return courses
        except TokenInvalid as e:
            auth._update_session()
            courses = get_courses_plan()
            return courses
        except KiwifyUserApiExceptions as e:
            err = str(e)
            if 'TOKEN_INVALID' in err:
                auth._update_session()
                courses = get_courses_plan()
                return courses
            else:
                raise UnhandledExceptions(e)

    def get_details_course(self, course_id) -> Course:
        """
        Obtém os detalhes de um curso específico.

        Args:
            course_id: O ID do curso.

        Returns:
            Course: Um objeto Course contendo os detalhes do curso.
        """
        try:
            response = requests.get(f'https://admin-api.kiwify.com.br/v1/viewer/courses/{course_id}',
                                    headers=self.__headers)
            if response.status_code == 200:
                results = json.loads(response.text)
                c = Course(results=results)
                return c
            else:
                r = json.loads(response.text)
                error = r.get("error", '')
                if 'TOKEN_INVALID' in error:
                    auth._update_session()
                else:
                    raise KiwifyUserApiExceptions(f"Erro ao acessar curso: {r}")
        except Exception as e:
            raise KiwifyUserApiExceptions(f"Erro ao obter curso: {e}")
