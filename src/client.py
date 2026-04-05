from typing import Any
from typing import Dict
from typing import List

import requests

from .constants import ALBUMS_BASE_URL
from .constants import COMMENTS_BASE_URL
from .constants import PHOTOS_BASE_URL
from .constants import POSTS_BASE_URL
from .constants import TODOS_BASE_URL
from .constants import USERS_BASE_URL


class APIClient:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url
        self.session = requests.Session()

    def _get(self, url: str) -> Any:
        # TODO: Add support for query params
        response = self.session.get(url=url)
        response.raise_for_status()
        return response.json()

    def _post(self): ...

    def _put(self): ...

    def _patch(self): ...

    def _delete(self): ...

    def list(self) -> List[Dict]:
        return self._get(url=self.base_url)

    def fetch(self): ...

    def create(self): ...

    def update(self): ...

    def delete(self): ...


class PostClient(APIClient):
    def __init__(self) -> None:
        super().__init__(base_url=POSTS_BASE_URL)


class CommentClient(APIClient):
    def __init__(self) -> None:
        super().__init__(base_url=COMMENTS_BASE_URL)


class AlbumClient(APIClient):
    def __init__(self) -> None:
        super().__init__(base_url=ALBUMS_BASE_URL)


class PhotoClient(APIClient):
    def __init__(self) -> None:
        super().__init__(base_url=PHOTOS_BASE_URL)


class TodoClient(APIClient):
    def __init__(self) -> None:
        super().__init__(base_url=TODOS_BASE_URL)


class UserClient(APIClient):
    def __init__(self) -> None:
        super().__init__(base_url=USERS_BASE_URL)
