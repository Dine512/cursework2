import pytest

from utils import load_all_posts, get_comments_by_post_id, get_posts_by_user, search_for_posts, get_post_by_pk


def test_load_all_posts_return_list():
    all_posts = load_all_posts()
    assert type(all_posts) == list


def test_get_comments_by_post_id_post_not_exist():
    with pytest.raises(ValueError):
        get_comments_by_post_id(9)


def test_get_comments_by_post_id_not_an_empty_list():
    comments_by_post = get_comments_by_post_id(4)
    assert comments_by_post


def test_get_posts_by_user_not_an_empty_list():
    posts_by_user = get_posts_by_user('larry')
    assert posts_by_user


def test_get_posts_by_user_not_posts_by_user():
    posts_by_user = get_posts_by_user('jlia')
    assert not posts_by_user


def test_get_posts_by_user_user_not_exist():
    with pytest.raises(ValueError):
        get_posts_by_user('antoha')


def test_search_for_posts_not_an_empty_list():
    search_posts = search_for_posts('утром')
    assert search_posts


def test_search_for_posts_no_matches():
    search_posts = search_for_posts('Нисан Скайлайн')
    assert not search_posts


def test_get_post_by_pk_return_correct_post():
    post = get_post_by_pk(5)
    assert post['pk'] == 5


def test_get_post_by_pk_not_exist_pk():
    with pytest.raises(ValueError):
        get_post_by_pk(2000)


