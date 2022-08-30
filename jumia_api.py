from datetime import datetime
from Orders.ORDERS_GET import request_orders, request_comments, request_items, request_document, request_failure_reason
from Payments.PAYMENTS_GET import request_statements


class Seller:
    STATUS_OPTIONS = ['pending', 'ready_to_ship', 'shipped', 'delivered', 'canceled', 'failed', 'returned']
    SORT_BY_OPTIONS = ['updated_at', 'created_at']
    SORT_DIRECTION_OPTIONS = ['DESC', 'ASC']
    DOCUMENT_TYPES = ['invoice', 'exportInvoice', 'shippingLabel', 'shippingParcel', 'carrierManifest', 'serialNumber']

    __OUTPUT_FORMAT = "JSON"

    def __init__(self, user_id, api_key):
        self.user_id = user_id
        self.api_key = api_key

    def get_orders(self, status: str = None, sort_direction: str = None,
                   sort_by: str = None,
                   created_after: str = None, created_before: str = None, updated_after: str = None,
                   updated_before: str = None, limit: int = None, offset: int = None, version: str = '1.0', check: bool = True):
        """
        returns all orders with filtering if selected
        """
        parameters = {'Action': 'GetOrders',
                      'Timestamp': datetime.now().isoformat(),
                      'UserID': self.user_id,
                      'Status': None,
                      'Format': self.__OUTPUT_FORMAT,
                      'SortDirection': sort_direction,
                      'SortBy': sort_by,
                      'CreatedAfter': created_after,
                      'CreatedBefore': created_before,
                      'UpdatedAfter': None,
                      'UpdatedBefore': updated_before,
                      'Limit': limit,
                      'Offset': offset,
                      'Version': version}
        if check:
            x = request_orders(self.api_key, parameters)
            numbers = {}
            for each in x:
                try:
                    if each.address_billing['Phone'] not in numbers.keys():
                        numbers[each.address_billing['Phone']] = [each.order_number]
                    else:
                        numbers[each.address_billing['Phone']].append(each.order_number)
                except:
                    pass
            print(len(x))


        parameters['UpdatedAfter'] = updated_after
        parameters['Status'] = status
        orders = request_orders(self.api_key, parameters)

        if check:
            for each in orders:
                if len(numbers[each.address_billing['Phone']]) > 1:
                    each.returning_user = True
                    each.number_of_orders_inclusive = len(numbers[each.address_billing['Phone']])
                    each.previous_order_numbers = numbers[each.address_billing['Phone']]

        return orders

    def receivables_from_orders(self, status=None):
        """
        basically all cash in pending, ready to ship and shipped orders
        """
        if status is not None:
            pending = self.get_orders(status=status, check=False)
        else:
            pending = self.get_orders(status='pending', check=False) + \
                self.get_orders(status='ready_to_ship', check=False) + \
                self.get_orders(status='shipped', check=False)

        revenue = 0.0
        for order in pending:
            for item in self.get_order_items(order.order_id):
                if item.status.lower() != 'canceled':
                    price = float(item.item_price)
                    revenue += price - (price * 0.171) # comission of 17.1% fashion
                    revenue -= 6 # item processing
        return revenue

    def latest_order(self):
        """
        Returns last order if any
        """
        return self.get_orders(sort_direction='DESC', limit=1)[0]

    def first_order(self):
        """
        Returns first order if any
        """
        return self.get_orders(sort_direction='ASC', limit=1)[0]

    def get_order(self, order_id: int, version: str = '1.0'):
        """
        returns one order using order id
        """
        parameters = {'Action': 'GetOrder',
                      'Timestamp': datetime.now().isoformat(),
                      'UserID': self.user_id,
                      'Format': self.__OUTPUT_FORMAT,
                      'OrderId': order_id,
                      'Version': version
                      }
        order = request_orders(self.api_key, parameters)
        return order[0]

    def get_order_comments(self, order_id: int, version: str = '1.0'):
        parameters = {'Action': 'GetOrderComments',
                      'Timestamp': datetime.now().isoformat(),
                      'UserID': self.user_id,
                      'Format': self.__OUTPUT_FORMAT,
                      'OrderId': order_id,
                      'Version': version
                      }
        comments = request_comments(self.api_key, parameters)
        return comments

    def get_order_items(self, order_id: int, version: str = '1.0'):
        parameters = {'Action': 'GetOrderItems',
                      'Timestamp': datetime.now().isoformat(),
                      'UserID': self.user_id,
                      'Format': self.__OUTPUT_FORMAT,
                      'OrderId': order_id,
                      'Version': version
                      }
        items = request_items(self.api_key, parameters)
        return items

    def get_document(self, order_item_id: list, document_type: str, version: str = '1.0'):
        if document_type not in self.DOCUMENT_TYPES:
            raise Exception("invalid document type, run .DOCUMENT_TYPES")
        parameters = {'Action': 'GetDocument',
                      'Timestamp': datetime.now().isoformat(),
                      'UserID': self.user_id,
                      'Format': self.__OUTPUT_FORMAT,
                      'DocumentType': document_type,
                      'OrderItemIds': order_item_id,
                      'Version': version
                      }
        document = request_document(self.api_key, parameters)
        return document

    def get_failure_reasons(self, version: str = '1.0'):
        parameters = {'Action': 'GetFailureReasons',
                      'Timestamp': datetime.now().isoformat(),
                      'UserID': self.user_id,
                      'Format': self.__OUTPUT_FORMAT,
                      'Version': version
                      }
        reasons = request_failure_reason(self.api_key, parameters)
        return reasons

    def get_payment_statements(self, created_after: str = None, version: str = '1.0'):
        parameters = {'Action': 'GetPayoutStatus',
                      'Timestamp': datetime.now().isoformat(),
                      'UserID': self.user_id,
                      'Format': self.__OUTPUT_FORMAT,
                      'Version': version,
                      'CreatedAfter': created_after
                      }
        statements = request_statements(self.api_key, parameters)
        return statements

