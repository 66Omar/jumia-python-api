from dataclasses import dataclass


@dataclass
class OrderItem:
    item_id: object = None
    shop_id: object = None
    order_id: object = None
    name: object = None
    sku: object = None
    variation: object = None
    shop_sku: object = None
    shipping_type: object = None
    shipping_method: object = None
    item_price: object = None
    paid_price: object = None
    currency: object = None
    wallet_credits: object = None
    tax_amount: object = None
    cod_collectable_amount: object = None
    shipping_amount: object = None
    shipping_service_cost: object = None
    voucher_amount: object = None
    voucher_code: object = None
    status: object = None
    is_processable: object = None
    shipment_provider: object = None
    is_digital: object = None
    digital_delivery_info: object = None
    tracking_code: object = None
    tracking_code_pre: object = None
    reason: object = None
    reason_detail: object = None
    purchase_order_id: object = None
    purchase_order_number: object = None
    package_id: object = None
    promised_shipping_time: object = None
    extra_attributes: object = None
    shipping_provider_type: object = None
    created_at: object = None
    updated_at: object = None
    return_status: object = None
