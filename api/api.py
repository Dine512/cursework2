from flask import Blueprint, jsonify
from utils import load_all_posts, get_post_by_pk
import logging

api = Blueprint('api', __name__)
logging.basicConfig(filename='api.log', level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')


@api.route('/posts')
def api_all_posts():
    all_posts = load_all_posts()
    logging.info('/api/posts')
    return jsonify(all_posts)


@api.route('/post/<int:post_id>')
def posts_by_id(post_id):
    post = get_post_by_pk(post_id)
    logging.info(f'/api/posts/{post_id}')
    return jsonify(post)
