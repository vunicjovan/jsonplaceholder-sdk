from src.client import PostClient

if __name__ == "__main__":
    post_client = PostClient()
    posts = post_client.get_posts()

    for post in posts:
        print(post)
