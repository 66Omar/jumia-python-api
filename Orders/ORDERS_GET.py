from get_data import get_data
from Orders.Models.Order import Order
from Orders.Models.Comment import Comment
from Orders.Models.OrderItem import OrderItem
from Orders.Models.Document import Document
from Orders.Models.FailureReason import FailureReason
from Errors import isSuccessful


def request_orders(api_key, parameters):
    data_dict = get_data(api_key, parameters)

    isSuccessful(data_dict)

    try:
        orders = data_dict.get("SuccessResponse").get("Body").get("Orders").get('Order')
    except AttributeError:
        orders = None

    if isinstance(orders, dict):
        orders = [orders]

    total_orders = []
    if orders is not None:
        for each in orders:
            total_orders.append(Order(each['OrderId'], each['CustomerFirstName'], each['CustomerLastName'],
                                      each['OrderNumber'], each['PaymentMethod'], each['Remarks'], each['DeliveryInfo'],
                                      each['Price'], each['VoucherCode'], each['CreatedAt'], each['UpdatedAt'],
                                      each['AddressUpdatedAt'], each['AddressBilling'], each['AddressShipping'],
                                      each['ItemsCount'], each['PromisedShippingTime'], each['ExtraAttributes'],
                                      each['Statuses']))

    return total_orders


def request_comments(api_key, parameters):
    data_dict = get_data(api_key, parameters)

    isSuccessful(data_dict)

    try:
        comments = data_dict.get("SuccessResponse").get("Body").get("Comments").get('Comment')
    except AttributeError:
        comments = None

    if isinstance(comments, dict):
        comments = [comments]

    all_comments = []
    if comments is not None:
        for comment in comments:
            all_comments.append(Comment(comment['CommentId'], comment['Username'], comment['Content'], comment['Type'],
                                        comment['IsOpened'], comment['IsAnswered'], comment['CreatedAt'],
                                        comment['UpdatedAt'], comment['Comments']))
    return all_comments


def request_items(api_key, parameters):
    data_dict = get_data(api_key, parameters)

    isSuccessful(data_dict)

    try:
        items = data_dict.get("SuccessResponse").get("Body").get("OrderItems").get('OrderItem')
    except AttributeError:
        items = None

    if isinstance(items, dict):
        items = [items]

    all_items = []
    if items is not None:
        for item in items:
            all_items.append(OrderItem(item['OrderItemId'], item['ShopId'], item['OrderId'], item['Name'],
                                       item['Sku'], item['Variation'], item['ShopSku'], item['ShippingType'],
                                       item['ShipmentMethod'], item['ItemPrice'], item['PaidPrice'],
                                       item['Currency'], item['WalletCredits'], item['TaxAmount'],
                                       item['CodCollectableAmount'], item['ShippingAmount'],
                                       item['ShippingServiceCost'], item['VoucherAmount'], item['VoucherCode'],
                                       item['Status'], item['IsProcessable'], item['ShipmentProvider'],
                                       item['IsDigital'], item['DigitalDeliveryInfo'], item['TrackingCode'],
                                       item['TrackingCodePre'], item['Reason'], item['ReasonDetail'],
                                       item['PurchaseOrderId'], item['PurchaseOrderNumber'], item['PackageId'],
                                       item['PromisedShippingTime'], item['ExtraAttributes'],
                                       item['ShippingProviderType'], item['CreatedAt'], item['UpdatedAt'],
                                       item['ReturnStatus']))

    return all_items


def request_document(api_key, parameters):
    data_dict = get_data(api_key, parameters)
    isSuccessful(data_dict)

    try:
        document = data_dict.get("SuccessResponse").get("Body").get("Documents").get('Document')
    except AttributeError:
        document = None

    if document is not None:
        document = Document(document['DocumentType'], document['MimeType'], document['File'])

    return document


def request_failure_reason(api_key, parameters):
    data_dict = get_data(api_key, parameters)

    isSuccessful(data_dict)

    try:
        reasons = data_dict.get("SuccessResponse").get("Body").get("Reasons").get('Reason')
    except AttributeError:
        reasons = None

    if isinstance(reasons, dict):
        reasons = [reasons]

    all_reasons = []
    if reasons is not None:
        for reason in reasons:
            all_reasons.append(FailureReason(reason['Type'], reason['Name']))

    return all_reasons
