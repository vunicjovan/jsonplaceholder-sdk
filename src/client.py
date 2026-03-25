from typing import Any, Dict, List

import requests

from .constants import POSTS_BASE_URL


class APIClient:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url
        self.session = requests.Session()

    def get(self, url: str) -> Any:
        # TODO: Add support for query params
        response = self.session.get(url=url)
        response.raise_for_status()
        return response.json()

    def post(self): ...

    def put(self): ...

    def patch(self): ...

    def delete(self): ...


class PostClient(APIClient):
    def __init__(self) -> None:
        super().__init__(POSTS_BASE_URL)

    def get_posts(self) -> List[Dict]:
        return self.get(url=self.base_url)

    def get_post(self): ...

    def create_post(self): ...

    def replace_post(self): ...

    def update_post(self): ...

    def delete_post(self): ...


class CommentClient(APIClient): ...


class AlbumClient(APIClient): ...


class PhotoClient(APIClient): ...


class TodoClient(APIClient): ...


class UserClient(APIClient): ...
