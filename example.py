from src.client import PhotoClient
from src.client import PostClient

if __name__ == "__main__":
    post_client = PostClient()
    posts = post_client.list()

    for post in posts:
        print(post)

    photo_client = PhotoClient()
    second_photo = photo_client.fetch(id=1)

    print(second_photo)

    deleted_photo = photo_client.delete(id=1)
    print(deleted_photo)
