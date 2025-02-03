import json
import os
import pickle
import traceback
import requests
import cloudscraper
from .exeptions import LoginException

DEBUG = False


def _get_default_headers() -> dict:
    """Retorna os cabeçalhos padrão para as requisições."""
    return {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, como Gecko) "
                      "Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Referer": "https://dashboard.kiwify.com.br",
        "Origin": "https://dashboard.kiwify.com.br",
        "DNT": "1",
        "Connection": "keep-alive",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
    }


class KiwifyAuth:
    def __init__(self):
        """
        Inicializa a autenticação e configura o diretório de cookies.
        """
        self.__cookie_dict = {}
        current_directory = os.path.dirname(__file__)
        cache = '.cache'
        cache_dir = os.path.join(current_directory, cache)
        os.makedirs(cache_dir, exist_ok=True)
        self.__user_dir = os.path.join(cache_dir)
        file_name1 = '.kiwify_userAPI'
        file_name2 = '.refresh'
        self.__file_path = os.path.join(self.__user_dir, file_name1)
        self._refresh_path = os.path.join(self.__user_dir, file_name2)

    def verif_login(self) -> bool:
        """
        Verifica se o login foi realizado com sucesso usando cookies salvos.

        Returns:
            bool: True se o login for bem-sucedido, False caso contrário.
        """
        try:
            headers = self._load_headers()
            if not headers:
                return False

            url = 'https://api.kiwify.com.br/v1/viewer/schools/courses?page=1&archived=false'
            response = requests.get(url=url, headers=headers)
            response.raise_for_status()
            data = response.json()
            return not data.get('error', data)

        except requests.RequestException:
            return False
        except json.JSONDecodeError:
            raise LoginException('Erro ao decodificar a resposta do servidor.')

    def login(self, email: str, password: str) ->bool:
        """
        Realiza o login no Kiwify e retorna a sessão autenticada.

        Args:
            email (str): Email do usuário.
            password (str): Senha do usuário.
        """
        session = cloudscraper.create_scraper()
        # Obtém o token CSRF
        response = session.get("https://dashboard.kiwify.com.br/login")
        data = {
            'email': email,
            'password': password,
            'returnSecureToken': True
        }
        session.cookies.update(response.cookies)
        session.headers.update(_get_default_headers())
        # Tenta realizar o login
        response = session.post("https://admin-api.kiwify.com.br/v1/handleAuth/login", data=data)
        if response.status_code != 200:
            errors = response.json()
            error_msg = errors.get("error", response.text)
            raise LoginException(f"Não foi possível efetuar o login: {error_msg}")

        refresh_token = response.json().get('refreshToken')
        if not refresh_token:
            raise LoginException("Erro ao obter refreshToken.")

        # Obtém o ID Token
        id_token_response = session.post(
            'https://admin-api.kiwify.com.br/v1/handleAuth/getIdToken',
            data={'grant_type': 'refresh_token', 'refresh_token': refresh_token}
        )
        id_token_response.raise_for_status()
        access_token = id_token_response.json().get("access_token")
        refresh_token_cache = id_token_response.json()
        with open(self._refresh_path, 'wb') as f:
            pickle.dump(refresh_token_cache, f)
        if not access_token:
            raise LoginException("Erro ao obter access_token.")
        # Obtém os dados do usuário
        user_data_response = session.post(
            'https://admin-api.kiwify.com.br/v1/handleAuth/getUserData',
            data={'idToken': access_token}
        )
        if user_data_response.status_code == 200:
            # Atualiza os cabeçalhos com o token de autorização
            session.headers.update({"Authorization": f"Bearer {access_token}"})
            # Salva cookies e headers
            self._save_headers(session.headers)
            return  True
        else:
            if DEBUG:
                print(f"Fail-login: {user_data_response.text}")
            return False
    def _save_headers(self, headers):
        """
        Salva os headers HTTP em um arquivo usando pickle.

        Args:
            headers (dict): Dicionário contendo os headers a serem salvos.
        """
        try:
            if not isinstance(headers, dict):
                raise ValueError("Headers devem ser um dicionário.")
            with open(self.__file_path, 'wb') as f:
                pickle.dump(headers, f)
        except Exception as e:
            raise LoginException(f"Erro ao salvar headers: {e}")

    def _load_headers(self) -> dict:
        """
        Carrega os headers HTTP salvos e retorna-os como um dicionário.

        Returns:
            dict: Um dicionário contendo os headers ou um dicionário vazio se o arquivo não existir.
        """
        try:
            if os.path.exists(self.__file_path) and os.path.getsize(self.__file_path) > 0:
                with open(self.__file_path, 'rb') as f:
                    headers = pickle.load(f)
                if isinstance(headers, dict):
                    return headers
                else:
                    raise LoginException("Formato inválido nos headers salvos.")
            else:
                return {}
        except (EOFError, pickle.UnpicklingError):
            return {}
        except Exception as e:
            if DEBUG:
                e = traceback.format_exc()
            raise LoginException(f"Erro ao carregar headers: {e}")

    def remove_cache(self):
        """Remove os cache salvos."""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'wb') as f:
                f.write(b'')
        if os.path.exists(self._refresh_path):
            with open(self.__file_path, 'wb') as f:
                f.write(b'')

    def _load_refresh_token(self) -> dict:
        """
        Carrega o refresh token salvo e retorna-o como um dicionário.

        Returns:
            dict: Um dicionário contendo o refresh token ou um dicionário vazio se o arquivo não existir.
        """
        try:
            with open(self._refresh_path, 'rb') as f:
                data: dict = pickle.load(f)
                return data
        except Exception as e:
            raise Exception(f"Erro ao carregar tokens: {e}")

    def _update_session(self):
        """Atualiza a sessão autenticada usando o refresh token salvo."""
        session = cloudscraper.create_scraper()

        # Obtém o token CSRF
        response = session.get("https://dashboard.kiwify.com.br/login")
        response.raise_for_status()
        session.cookies.update(response.cookies)
        session.headers.update(_get_default_headers())
        # Tenta realizar o login
        refresh_token = self._load_refresh_token().get('refresh_token')
        # Obtém o ID Token
        id_token_response = session.post(
            'https://admin-api.kiwify.com.br/v1/handleAuth/getIdToken',
            data={'grant_type': 'refresh_token', 'refresh_token': refresh_token}
        )
        id_token_response.raise_for_status()
        access_token = id_token_response.json().get("access_token")
        refresh_token_cache = id_token_response.json()
        with open(self._refresh_path, 'wb') as f:
            pickle.dump(refresh_token_cache, f)
        if not access_token:
            raise LoginException("Erro ao obter access_token.")
        # Obtém os dados do usuário
        user_data_response = session.post(
            'https://admin-api.kiwify.com.br/v1/handleAuth/getUserData',
            data={'idToken': access_token}
        )
        user_data_response.raise_for_status()
        # Atualiza os cabeçalhos com o token de autorização
        session.headers.update({"Authorization": f"Bearer {access_token}"})
        # Salva cookies e headers
        self._save_headers(session.headers)
