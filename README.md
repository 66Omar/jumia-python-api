# jumia-python-api
Python code to make using Jumia's sellercenter API easier (not complete)

seller = Seller(Api key, userId)

*  seller.get_orders()
* seller.receivables_from_orders()
* seller.get_order(ID)
* seller.get_order_comments(ID)
* get_order_items(ID)

to pass a date to any of above methods, you will need date class, you can create one using seller.get_formatted_date()
