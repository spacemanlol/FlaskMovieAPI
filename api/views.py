from flask import Blueprint, jsonify

# Blueprint init
main = Blueprint('main', __name__)

@main.route('/add_movie', methods=['POST'])
def add_move():
    # 201 - Created Successfully
    return 'Done', 201

# Display Movies
@main.route('/movies')
def movies():
    movies = []
    return jsonify({'movies': movies})