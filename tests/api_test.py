from main import app

keys = ["poster_name",
        "poster_avatar",
        "pic",
        "content",
        "views_count",
        "likes_count",
        "pk"]


def test_api_posts_correct_keys():
    response = app.test_client().get('/api/posts')
    posts_list = response.json
    for index, post in enumerate(posts_list):
        assert set(keys) == set(post.keys()), f'Ошибка в посте {index + 1}, не корректные ключи'


def test_api_posts_return_list():
    response = app.test_client().get('/api/posts')
    assert type(response.json) == list, 'Возвращается не список'


def test_api_posts_post_id_return_dict():
    response = app.test_client().get('/api/post/6')
    assert type(response.json) == dict, 'Возвращается не словарь'


def test_api_post_post_id_correct_keys():
    response = app.test_client().get('/api/post/6')
    post = response.json
    assert set(keys) == set(post.keys()), f'Ошибка в посте, не корректные ключи'

