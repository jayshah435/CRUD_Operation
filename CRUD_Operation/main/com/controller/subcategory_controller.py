from flask import *
from main import app
from main.com.vo.category_vo import CategoryVO
from main.com.vo.subcategory_vo import SubCategoryVO
from main.com.dao.category_dao import CategoryDAO
from main.com.dao.subcategory_dao import SubCategoryDAO


@app.route('/admin/load_subcategory')
def admin_load_subcategy():
    try:
        category_dao = CategoryDAO()
        category_vo_list = category_dao.view_category()

        return render_template("admin/addSubcategory.html", category_vo_list = category_vo_list)
    except:
        return render_template("admin/home.html")

@app.route('/admin/insert_subcategory', methods=['POST'])
def admin_insert_subcategory():
    try:
        subcategory_vo = SubCategoryVO()
        subcategory_dao = SubCategoryDAO()

        subcategory_name = request.form.get("subcategoryName")
        subcategory_description = request.form.get("subcategoryDescription")
        subcategory_category_id = request.form.get("subcategoryCategoryId")
        subcategory_vo.subcategory_name = subcategory_name
        subcategory_vo.subcategory_description = subcategory_description
        subcategory_vo.subcategory_category_id = subcategory_category_id

        subcategory_dao.insert_subcategory(subcategory_vo)

        return render_template("admin/home.html")
    except:
        return render_template("admin/home.html")

@app.route('/admin/view_subcategory')
def admin_view_subcategory():
    try:
        subcategory_dao = SubCategoryDAO()
        subcategory_vo_list = subcategory_dao.view_subcategory()
        print("subcategory_vo_list>>>>", subcategory_vo_list)
        return render_template("admin/viewSubcategory.html",
                               subcategory_vo_list=subcategory_vo_list)
    except:
        return render_template("admin/home.html")

@app.route('/admin/delete_subcategory')
def admin_delete_subcategory():
    try:
        subcategory_dao = SubCategoryDAO()
        subcategory_vo = SubCategoryVO()

        r = request.args.get('userid')
        print("r>>>>>>>>>>>>>>", r)
        subcategory_vo.subcategory_id = r
        subcategory_dao.delete_subcategory(subcategory_vo)

        return redirect(url_for('admin_view_subcategory'))

    except:

        return render_template("admin/home.html")

@app.route('/admin/edit_subcategory')
def admin_edit_subcategory():
    try:
        subcategory_dao = SubCategoryDAO()
        subcategory_vo = SubCategoryVO()

        subcategory_id = request.args.get('userid')
        subcategory_vo.subcategory_id = subcategory_id
        subcategory_vo_list = subcategory_dao.edit_subcategory(subcategory_vo)
        print("subcategory_vo_list>>>", subcategory_vo_list)

        return render_template("admin/editSubcategory.html",
                           subcategory_vo_list= subcategory_vo_list[0])
    except:

        return render_template("admin/home.html")

@app.route('/admin/update_subcategory', methods=['POST'])
def admin_update_subcategory():
    try:
        subcategory_vo = SubCategoryVO()
        subcategory_dao = SubCategoryDAO()

        subcategory_name = request.form.get("subcategoryName")
        subcategory_description = request.form.get("subcategoryDescription")
        subcategory_id = request.form.get("subcategoryId")

        subcategory_vo.subcategory_name = subcategory_name
        subcategory_vo.subcategory_description = subcategory_description
        subcategory_vo.subcategory_id = subcategory_id

        subcategory_dao.update_subcategory(subcategory_vo)

        return redirect(url_for('admin_view_subcategory'))

    except:

        return render_template("admin/home.html")
