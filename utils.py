import json


def load_all_posts():
    """Возвращает все посты и расставляет в них ссылки по тегам"""
    with open('data/posts.json', encoding='utf-8') as file:
        all_posts_list = json.load(file)
    for post in all_posts_list:
        if '#' in post['content']:
            content = post['content']
            word_list = content.split(' ')
            for index, word in enumerate(word_list):
                if '#' in word:
                    word_list[index] = f"<a href='/feed/tag/{word[1:]}'>{word}</a>"
            post['content'] = ' '.join(word_list)
    return all_posts_list


def get_comments_by_post_id(post_id=None):
    """Возвращает комментарии определенного поста"""
    with open('data/comments.json', encoding='utf-8') as file:
        all_comments = json.load(file)
    if post_id is None:
        return all_comments
    elif post_id in [posts_id['pk'] for posts_id in load_all_posts()]:
        comments_by_post_id = [comment for comment in all_comments if comment['post_id'] == post_id]
        return comments_by_post_id
    else:
        raise ValueError


def get_posts_by_user(user_name: str):
    """Возвращает посты определенного пользователя"""
    all_posts = load_all_posts()
    all_comments = get_comments_by_post_id()
    for post in all_posts:
        if post['poster_name'] == user_name.lower():
            user_posts = [post for post in all_posts if post['poster_name'] == user_name.lower()]
            return user_posts
    for comment in all_comments:
        if comment['commenter_name'] == user_name.lower():
            return []
    raise ValueError


def search_for_posts(query: str):
    """Возвращает список постов по ключевому слову"""
    all_posts = load_all_posts()
    search_posts = [post for post in all_posts if query.lower() in post['content'].lower()]
    return search_posts


def get_post_by_pk(pk: int):
    """Возвращает один пост по его идентификатору"""
    all_posts = load_all_posts()
    for post in all_posts:
        if post['pk'] == pk:
            return post
    raise ValueError


def load_all_bookmarks():
    with open('data/bookmarks.json', encoding='utf-8') as file:
        all_bookmark_list = json.load(file)
    return all_bookmark_list


def bookmark_add_post(post_id):
    post = get_post_by_pk(post_id)
    all_bookmarks = load_all_bookmarks()
    all_bookmarks.append(post)
    with open('data/bookmarks.json', 'w', encoding='utf-8') as file:
        json.dump(all_bookmarks, file, ensure_ascii=False, indent=4)


def remove_bookmark_post(post_id):
    all_bookmarks = load_all_bookmarks()
    for bookmark in all_bookmarks:
        if bookmark['pk'] == post_id:
            all_bookmarks.remove(bookmark)
            break
    with open('data/bookmarks.json', 'w', encoding='utf-8') as file:
        json.dump(all_bookmarks, file, ensure_ascii=False, indent=4)
