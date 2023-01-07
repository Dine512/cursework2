from flask import render_template, Blueprint, request, redirect
from utils import load_all_posts, load_all_bookmarks, get_post_by_pk, get_comments_by_post_id, search_for_posts, \
    get_posts_by_user, bookmark_add_post, remove_bookmark_post

feed = Blueprint('feed', __name__, template_folder='templates', static_folder='static')


@feed.route('/')
def index():
    all_posts = load_all_posts()
    len_all_bookmarks = len(load_all_bookmarks())
    return render_template('index.html', all_posts=all_posts, len_all_bookmarks=len_all_bookmarks)


@feed.route('/post/<int:post_id>')
def post(post_id):
    try:
        post_by_id = get_post_by_pk(post_id)
        comments_by_post = get_comments_by_post_id(post_id)
        return render_template('post.html', post=post_by_id, comments=comments_by_post,
                               count_comments=len(comments_by_post))
    except ValueError:
        return "<h1>Пост не найден</h1>"


@feed.route('/search/')
def search_posts():
    search_name = request.args.get('s')
    posts = search_for_posts(search_name)
    count_posts = len(posts)
    return render_template('search.html', posts=posts, count_posts=count_posts)


@feed.route('/users/<username>')
def username_posts(username):
    try:
        posts = get_posts_by_user(username)
        user_name = username
        return render_template('user-feed.html', posts=posts, user_name=user_name)
    except ValueError:
        return "<h1>Данный пользователь не найден</h1>"


@feed.route('/tag/<tagname>')
def tag_posts(tagname):
    posts = search_for_posts(f'#{tagname}')
    return render_template('tag.html', posts=posts, tagname=tagname)


@feed.route('/bookmark/add/<int:post_id>')
def bookmark_add_post_id(post_id):
    bookmark_add_post(post_id)
    return redirect('/feed/', code=302)


@feed.route('/bookmark')
def bookmark():
    all_bookmarks = load_all_bookmarks()
    return render_template('bookmarks.html', bookmarks=all_bookmarks)


@feed.route('/bookmark/remove/<int:post_id>')
def bookmark_remove_post_id(post_id):
    remove_bookmark_post(post_id)
    return redirect('/feed/bookmark', code=302)


