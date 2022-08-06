from main import db
from main.com.vo.subcategory_vo import SubCategoryVO
from main.com.vo.category_vo import CategoryVO
from main.com.vo.product_vo import ProductVO

class ProductDAO:
    def insert_product(self, product_vo):
        db.session.add(product_vo)
        db.session.commit()

    def view_product(self):

        product_vo_list = db.session.query(ProductVO, CategoryVO, SubCategoryVO).join(CategoryVO, ProductVO.product_category_id == CategoryVO.category_id).join(SubCategoryVO,ProductVO.product_subcategory_id == SubCategoryVO.subcategory_id).all()
        print('product_vo_list>>', product_vo_list)
        return product_vo_list

    def delete_product(self, p):

        db.session.delete(ProductVO.query.get(p.product_id))
        db.session.commit()

    def edit_product(self,product_vo):
        product_vo_list = ProductVO.query.filter_by(
            product_id=product_vo.product_id).all()  #all-(
        # list-object)-show/without all-only object
        print(">>>>>>>>>>>>>>>>>>>>pp", product_vo_list[0])
        return product_vo_list

    def update_product(self, product_vo):
        db.session.merge(product_vo)
        db.session.commit()