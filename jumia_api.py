from datetime import datetime
from Orders.ORDERS_GET import request_orders, request_comments, request_items, request_document, request_failure_reason
from Payments.PAYMENTS_GET import request_statements
from Date import Date


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
                   created_after: Date = None, created_before: Date = None, updated_after: Date = None,
                   updated_before: Date = None, limit: int = None, offset: int = None, version: str = '1.0'):
        """
        returns all orders with filtering if selected
        """
        parameters = {'Action': 'GetOrders',
                      'Timestamp': datetime.now().isoformat(),
                      'UserID': self.user_id,
                      'Status': status,
                      'Format': self.__OUTPUT_FORMAT,
                      'SortDirection': sort_direction,
                      'SortBy': sort_by,
                      'CreatedAfter': created_after,
                      'CreatedBefore': created_before,
                      'UpdatedAfter': updated_after,
                      'UpdatedBefore': updated_before,
                      'Limit': limit,
                      'Offset': offset,
                      'Version': version}

        orders = request_orders(self.api_key, parameters)
        return orders

    def receivables_from_orders(self):
        """
        basically all cash in pending, ready to ship and pending orders
        """
        pending = self.get_orders(status='pending') + \
            self.get_orders(status='ready_to_ship') + \
            self.get_orders(status='shipped')
        revenue = 0.0
        for order in pending:
            revenue += float(order.price)
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

    def get_document(self, order_item_id: int, document_type: str, version: str = '1.0'):
        if document_type not in self.DOCUMENT_TYPES:
            raise Exception("invalid document type, run .DOCUMENT_TYPES")
        parameters = {'Action': 'GetDocument',
                      'Timestamp': datetime.now().isoformat(),
                      'UserID': self.user_id,
                      'Format': self.__OUTPUT_FORMAT,
                      'DocumentType': document_type,
                      'OrderItemIds': [order_item_id],
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

    def get_payment_statements(self, created_after: Date = None, version: str = '1.0'):
        parameters = {'Action': 'GetPayoutStatus',
                      'Timestamp': datetime.now().isoformat(),
                      'UserID': self.user_id,
                      'Format': self.__OUTPUT_FORMAT,
                      'Version': version,
                      'CreatedAfter': created_after
                      }
        statements = request_statements(self.api_key, parameters)
        return statements

    def get_formatted_date(self, day: str, month: str, year: str):
        return Date(day, month, year)
