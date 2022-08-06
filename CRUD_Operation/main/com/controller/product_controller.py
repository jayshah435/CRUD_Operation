from flask import *
import os
from main import app
from main.com.vo.category_vo import CategoryVO
from main.com.vo.subcategory_vo import SubCategoryVO
from main.com.dao.category_dao import CategoryDAO
from main.com.dao.subcategory_dao import SubCategoryDAO
from main.com.dao.product_dao import ProductDAO
from main.com.vo.product_vo import ProductVO
from werkzeug.utils import secure_filename

PRODUCT_FOLDER = 'main/static/'
app.config['PRODUCT_FOLDER'] = PRODUCT_FOLDER
file_upload = app.config['PRODUCT_FOLDER']


@app.route('/admin/load_product')
def admin_load_product():
    try:
        category_dao = CategoryDAO()
        category_vo_list = category_dao.view_category()

        return render_template("admin/addProduct.html", category_vo_list=
        category_vo_list)
    except Exception as e:
        return e


@app.route('/admin/select_subcategory', methods=['GET'])
def admin_select_subcategory():
    try:

        subcategory = request.args.get('product')
        print(subcategory)

        subcategory_vo = SubCategoryVO()
        subcategory_dao = SubCategoryDAO()

        subcategory_vo.subcategory_category_id = subcategory
        subcategory_obj = subcategory_dao.view_category_subcategory(
            subcategory_vo)
        print('\n', subcategory_obj)
        subcategory_list = [i.as_dict() for i in subcategory_obj]
        print('\n', subcategory_list)

        return jsonify(subcategory_list)
    except Exception as e:
        return e


@app.route('/admin/insert_product', methods=['POST'])
def admin_insert_product():
    try:
        product_name = request.form.get('productName')
        product_description = request.form.get('productDescription')
        product_price = request.form.get('productPrice')
        product_quantity = request.form.get('productQuantity')
        product_category_id = request.form.get('product_category_id')
        product_subcategory_id = request.form.get('product_subcategory_id')
        product_image = request.files.get('productImage')

        product_image_name = secure_filename(product_image.filename)
        product_image_path = os.path.join(file_upload)
        product_image.save(
            os.path.join(product_image_path, product_image_name))

        product_vo = ProductVO()
        product_dao = ProductDAO()

        product_vo.product_image_name = product_image_name
        product_vo.product_image_path = product_image_path.replace("main",
                                                                   "..")
        product_vo.product_name = product_name
        product_vo.product_description = product_description
        product_vo.product_price = product_price
        product_vo.product_quantity = product_quantity
        product_vo.product_category_id = product_category_id
        product_vo.product_subcategory_id = product_subcategory_id

        product_dao.insert_product(product_vo)

        return render_template("admin/home.html")
    except Exception as e:
        return e


@app.route('/admin/view_product')
def admin_view_product():
    try:
        product_dao = ProductDAO()
        product_vo_list = product_dao.view_product()

        print("product_vo_list>", product_vo_list)

        return render_template("admin/viewProduct.html",
                               product_vo_list=product_vo_list)
    except:
        return render_template("admin/home.html")


@app.route('/admin/delete_product')
def admin_delete_product():
    try:
        r = request.args.get('pid')
        product_path = request.args.get('path').replace("..", "main")
        product_vo = ProductVO()
        product_dao = ProductDAO()

        product_vo.product_id = r
        product_dao.delete_product(product_vo)

        os.remove(product_path)


        return redirect(url_for('admin_view_product'))


    except Exception as e:

        return e

@app.route('/admin/edit_product')
def admin_edit_product():
    try:
        r = request.args.get('prid')

        product_vo = ProductVO()
        product_dao = ProductDAO()
        category_dao = CategoryDAO()

        category_vo_list = category_dao.view_category()

        product_vo.product_id = r


        product_vo_list = product_dao.edit_product(product_vo)

        print(">>>>>>>>>>>>>", product_vo_list[0])


        return render_template("admin/editProduct.html",
                           product_vo_list=product_vo_list[0],
                               category_vo_list = category_vo_list)

    except Exception as e:
        return e

@app.route('/admin/select_product', methods=['GET'])
def admin_select_product():
    try:

        subcategory = request.args.get('prd')
        print(subcategory)

        subcategory_vo = SubCategoryVO()
        subcategory_dao = SubCategoryDAO()

        subcategory_vo.subcategory_category_id = subcategory
        subcategory_obj = subcategory_dao.view_category_subcategory(
            subcategory_vo)
        print('\n', subcategory_obj)
        subcategory_list = [i.as_dict() for i in subcategory_obj]
        print('\n', subcategory_list)

        return jsonify(subcategory_list)
    except Exception as e:
        return e


@app.route('/admin/update_product', methods=['POST'])
def admin_update_product():
    try:
        product_name = request.form.get('productName')
        product_description = request.form.get('productDescription')
        product_price = request.form.get('productPrice')
        product_quantity = request.form.get('productQuantity')
        product_category_id = request.form.get('product_category_id')
        product_subcategory_id = request.form.get('product_subcategory_id')
        product_id = request.form.get('productId')


        product_vo = ProductVO()
        product_dao = ProductDAO()


        product_vo.product_name = product_name
        product_vo.product_description = product_description
        product_vo.product_price = product_price
        product_vo.product_quantity = product_quantity
        product_vo.product_category_id = product_category_id
        product_vo.product_subcategory_id = product_subcategory_id
        product_vo.product_id = product_id

        product_dao.update_product(product_vo)

        return redirect(url_for('admin_view_product'))


    except Exception as e:

        return e