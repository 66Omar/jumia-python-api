from dataclasses import dataclass


@dataclass
class Order:
    order_id: object = None
    customer_firstname: object = None
    customer_lastname: object = None
    order_number: object = None
    payment_method: object = None
    remarks: object = None
    delivery_info: object = None
    price: object = None
    voucher_code: object = None
    created_at: object = None
    updated_at: object = None
    address_updated_at: object = None
    address_billing: object = None
    address_shipping: object = None
    items_count: object = None
    promised_shipping_time: object = None
    extra_attributes: object = None
    statuses: object = None
    returning_user: bool = False
    number_of_orders_inclusive: int = None
    previous_order_numbers: list = None
