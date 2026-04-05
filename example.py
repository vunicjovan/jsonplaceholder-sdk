from src.client import PhotoClient
from src.client import PostClient

if __name__ == "__main__":
    post_client = PostClient()
    posts = post_client.list()

    for post in posts:
        print(post)

    photo_client = PhotoClient()
    photos = photo_client.list()

    print(photos[1])
