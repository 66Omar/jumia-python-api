from dataclasses import dataclass


@dataclass
class Statement:
    statement_number: object = None
    created_at: object = None
    updated_at: object = None
    opening_balance: object = None
    item_revenue: object = None
    shipment_fee: object = None
    shipment_fee_credit: object = None
    other_revenue_total: object = None
    fees_total: object = None
    sub_total: object = None
    refunds: object = None
    fees_on_refunds_total: object = None
    sub_total2: object = None
    closing_balance: object = None
    guarantee_deposit: object = None
    payout: object = None
    paid: object = None
