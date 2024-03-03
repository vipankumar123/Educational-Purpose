# pip install instaloader
#devganshivam

import instaloader

loader = instaloader.Instaloader()

profile = instaloader.Profile.from_username(loader.context, 'devganshivam')

posts = profile.get_posts()

for post in posts:
    print("Post ID", post.mediaid)
    print("Caption", post.caption)
    print("Likes", post.likes)
    print("Comment", post.comments)
    print("Location", post.location)
    print("")

