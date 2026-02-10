from flask_smorest import Blueprint, abort
from flask import request, jsonify
from flask.views import MethodView

def create_posts_blueprint(mysql):
    posts_bp = Blueprint('Posts', __name__, description="posts api", url_prefix="/posts")

    # CRUD
    @posts_bp.route('/')
    class Posts(MethodView):
        def get(self):
            cursor = mysql.connection.cursor()
            sql = 'SELECT * FROM posts'
            cursor.execute(sql)
            posts = cursor.fetchall()
            cursor.close()

            # post_list = [{"id": p[0], "title":p[1], 'content':p[2]} for p in posts]
            

            return jsonify([{"id": p[0], "title":p[1], 'content':p[2]} for p in posts])
        
        def post(self):
            cursor = mysql.connection.cursor()
            data = request.get_json()
            # print(f'*******this is data : {data}*******')
            if not data['title'] or not data['content']:
                return ({"msg": "title, content is not found"}), 404
            sql = "INSERT INTO posts(title, content) VALUES(%s, %s)"
            val = (data['title'], data['content'])
            cursor.execute(sql, val)
            mysql.connection.commit()
            cursor.close()

            return jsonify({
                "msg": f"created user id: {data['title']}, content: {data['content']}"
            })
        
    @posts_bp.route("/<int:id>")
    class PostOne(MethodView):
        def get(self, id):
            cursor = mysql.connection.cursor()
            sql = f'SELECT * FROM posts WHERE id = {id}'
            cursor.execute(sql)
            post = cursor.fetchone()
            if not post:
                abort(404, "not found post")
            return jsonify({
                "id": post[0],
                "title": post[1],
                "content": post[2]
            })
            

        def put(self, id):
            cursor = mysql.connection.cursor()
            data = request.get_json()
            if not data['title'] or not data['content']:
                abort(404, "data not found")
            sql = "INSERT INTO posts(title, content) VALUES(%s, %s) WHERE id = %s"
            val = (data['title'], data['content'], id)
            cursor.execute(sql, val)
            mysql.connection.commit()
            cursor.close()
            return {"msg": "put post"}, 204

        def delete(self, id):
            cursor = mysql.connection.cursor()
            sql = f"DELETE FROM posts WHERE id = {id}"
            cursor.execute(sql)
            mysql.connection.commit()
            cursor.close()

            return{"msg": "delete post"}, 200
    
    return posts_bp