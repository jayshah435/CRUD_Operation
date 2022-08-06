from flask import *
from main import app
from main.com.vo.category_vo import CategoryVO
from main.com.dao.category_dao import CategoryDAO


@app.route('/home')
def load_index():
    try:
        return render_template("admin/home.html")
    except:
        return render_template("admin/home.html")


@app.route('/admin/load_category')
def admin_load_category():
    try:
        return render_template('admin/addCategory.html')
    except:
        return render_template("admin/home.html")


@app.route('/admin/insert_category', methods=['POST'])
def admin_insert_category():
    try:
        category_vo = CategoryVO()
        category_dao = CategoryDAO()

        category_name = request.form.get("categoryName")
        category_description = request.form.get("categoryDescription")

        category_vo.category_name = category_name
        category_vo.category_description = category_description

        category_dao.insert_category(category_vo)

        return render_template("admin/home.html")
    except:
        return render_template("admin/home.html")


@app.route('/admin/view_category')
def admin_view_category():
    try:
        category_dao = CategoryDAO()
        category_vo_list = category_dao.view_category()

        return render_template("admin/viewCategory.html",
                               category_vo_list=category_vo_list)
    except:
        return render_template("admin/home.html")


@app.route('/admin/delete_category')
def admin_delete_category():
    try:

        category_vo = CategoryVO()
        category_dao = CategoryDAO()

        category_vo.category_id = request.args.get('userid')
        category_dao.delete_category(category_vo)

        return redirect(url_for('admin_view_category'))

    except:
        return render_template("admin/home.html")


@app.route('/admin/edit_category')
def admin_edit_category():
    try:

        category_vo = CategoryVO()
        category_id = request.args.get('userid')
        print("category_id>>>", category_id)
        category_vo.category_id = category_id
        print("category_vo.category_id>>>", category_vo.category_id)
        category_dao = CategoryDAO()
        category_vo_list = category_dao.edit_category(category_vo)
        print("category_vo_list>>>", category_vo_list)

        return render_template("admin/editCategory.html",
                               category_vo_list=category_vo_list[0])
    except:
        return render_template("admin/home.html")


@app.route('/admin/update_category', methods=['POST'])
def admin_update_category():
    try:
        category_vo = CategoryVO()
        category_dao = CategoryDAO()

        category_name = request.form.get("categoryName")
        category_description = request.form.get("categoryDescription")
        category_id = request.form.get("categoryId")

        category_vo.category_name = category_name
        category_vo.category_description = category_description
        category_vo.category_id = category_id

        category_dao.update_category(category_vo)

        return redirect(url_for('admin_view_category'))

    except:

        return render_template("admin/home.html")
