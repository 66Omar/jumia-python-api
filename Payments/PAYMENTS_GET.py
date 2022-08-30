from get_data import get_data
from Errors import isSuccessful
from Payments.Models.Statement import Statement


def request_statements(api_key, parameters):
    data_dict = get_data(api_key, parameters)

    isSuccessful(data_dict)

    try:
        statements = data_dict.get("SuccessResponse").get("Body").get("PayoutStatus").get('Statement')
    except AttributeError:
        statements = None

    if isinstance(statements, dict):
        statements = [statements]

    all_statements = []
    if statements is not None:
        for statement in statements:
            all_statements.append(Statement(statement['StatementNumber'], statement['CreatedAt'],
                                            statement['UpdatedAt'], statement['OpeningBalance'],
                                            statement['ItemRevenue'], statement['ShipmentFee'],
                                            statement['ShipmentFeeCredit'], statement['OtherRevenueTotal'],
                                            statement['FeesTotal'], statement['Subtotal1'], statement['Refunds'],
                                            statement['FeesOnRefundsTotal'], statement['Subtotal2'],
                                            statement['ClosingBalance'],statement['GuaranteeDeposit'],
                                            statement['Payout'], statement['Paid']))
    return all_statements
