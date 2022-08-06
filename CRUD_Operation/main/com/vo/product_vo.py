from main import db
from main.com.vo.category_vo import CategoryVO
from main.com.vo.subcategory_vo import SubCategoryVO

class ProductVO(db.Model):

    __tablename__ = 'product_table'
    product_id = db.Column('product_id', db.Integer,
                               primary_key=True, autoincrement=True)
    product_name= db.Column('product_name', db.String(255),
                                nullable=False)
    product_description= db.Column('product_description', db.Text)
    product_price = db.Column('product_price', db.Integer)
    product_quantity = db.Column('product_quantity', db.Integer)
    product_category_id= db.Column('product_category_id',db.Integer,
                                       db.ForeignKey(CategoryVO.category_id,onupdate='CASCADE',ondelete='CASCADE'),
                                       nullable=False)
    product_subcategory_id = db.Column('product_subcategory_id',db.Integer,
                                       db.ForeignKey(
                                           SubCategoryVO.subcategory_id,
                                           onupdate='CASCADE',ondelete='CASCADE'),
                                       nullable=False)
    product_image_name = db.Column('product_image_name', db.String(255),
                                nullable=False)
    product_image_path = db.Column('product_image_path', db.String(255),
                                nullable=False)

    def as_dict(self):
        return {
            'product_id': self.product_id,
            'product_name': self.product_name,
            'product_description': self.product_description,
            'product_category_id': self.product_category_id,
            'product_subcategory_id': self.product_subcategory_id,
            'product_image_name': self.product_image_name,
            'product_image_path': self.product_image_path,

        }

db.create_all()