import json
import requests
from .api import HEADERS_USER
from .exeptions import TokenInvalid, KiwifyUserApiExceptions


def parser_course(data: dict):
    """Parseia os dados de um curso."""
    return {
        'course_name': data.get('name'),
        'course_id': data.get('id'),
        'course_img': data.get('course_img', False),
        'course_logo': data.get('logo_url'),
        'course_slug': data.get('slug'),
        'course_completed_progress': int(data.get('completed_progress', 0)),
        'course_archived': bool(data.get('archived', False)),
        'course_premium_members_area_enabled': bool(data.get('premium_members_area_enabled', False)),
        'course_version': data.get('version'),
    }


def get_courses_plan() -> list[dict]:
    """
    Obtém o plano de cursos da API da Kiwify.

    Returns:
        list: Lista de cursos disponíveis.

    Raises:
        KiwifyUserApiExceptions: Em caso de erro na requisição.
    """
    page = 1
    courses_list = []

    try:
        while True:
            url = f'https://admin-api.kiwify.com.br/v1/viewer/schools/courses?page={page}&archived=true'
            response = requests.get(url, headers=HEADERS_USER)

            if response.status_code == 200:
                results = response.json()
                courses = results.get('courses', [])
                if not courses:
                    break
                for course in courses:
                    course_info = course.get('course_info', {})
                    school_info = course.get('school_info', {})
                    if course_info:
                        courses_list.append(parser_course(course_info))
                    if school_info:
                        courses_list.append(parser_course(school_info))

                page += 1  # Avança para a próxima página
            else:
                error = response.json().get("error")
                if error:
                    if 'TOKEN_INVALID' in error or 'TOKEN_INVALID' in response.json():
                        raise TokenInvalid(
                            "Token inválido ou expirado."
                        )
                else:
                    raise UnboundLocalError(
                                            f"Uma falha na reposta da API ainda desconhecida, ao tentar obter cursos!"
                                            f"Detalhes: {error}"
                    )
    except Exception as e:
        raise KiwifyUserApiExceptions(
            f"Erro genérico {e},ao obter cursos!"
        )

    return courses_list


def get_lesson_details(lesson_id: str, course_id: str) -> dict:
    """
    Obtém os detalhes de uma aula específica.

    Args:
        lesson_id(str): O ‘ID’ da aula.
        course_id(str): O ‘ID’ do curso.

    Returns:
        dict: um dicionário contendo os detalhes da aula.
    """
    endpoint = f'https://admin-api.kiwify.com.br/v1/viewer/courses/{course_id}/lesson/{lesson_id}'
    try:
        response = requests.get(endpoint,
                                headers=HEADERS_USER)
        if response.status_code == 200:
            results = json.loads(response.text)
            return results.get('lesson', {})
        else:
            r = json.loads(response.text)
            error = r.get("error")
            if 'TOKEN_INVALID' in error or 'TOKEN_INVALID' in r:
                raise TokenInvalid(error)
            else:
                raise UserWarning(error)
    except Exception as e:
        raise KiwifyUserApiExceptions(
            f"Erro genérico {e},ao obter detalhes da aula!"
        )