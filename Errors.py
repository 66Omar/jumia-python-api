def isSuccessful(data: dict):
    if data.get("SuccessResponse") is not None:
        return True
    else:
        try:
            if data.get('ErrorResponse').get("Head").get("ErrorCode") == '7':
                raise Exception("Signature mismatch, check arguments given!")

            if data.get('ErrorResponse').get("Head").get("ErrorCode") == '4':
                raise Exception("invalid timestamp format")

            if data.get('ErrorResponse').get("Head").get("ErrorCode") == '62':
                raise Exception("No seller was found by e-mail")

            elif data.get('ErrorResponse').get("Head").get("ErrorCode") == '14':
                raise Exception("Invalid offset")

            elif data.get('ErrorResponse').get("Head").get("ErrorCode") == '16':
                raise Exception("Invalid order id")

            elif data.get('ErrorResponse').get("Head").get("ErrorCode") == '17':
                raise Exception("Invalid date format, please use .date('dd/mm/yyyy') function")

            elif data.get('ErrorResponse').get("Head").get("ErrorCode") == '19':
                raise Exception("Invalid limit")

            elif data.get('ErrorResponse').get("Head").get("ErrorCode") == '20':
                raise Exception("Invalid order item ID")

            elif data.get('ErrorResponse').get("Head").get("ErrorCode") == '21':
                raise Exception("OMS Api Error Occurred")

            elif data.get('ErrorResponse').get("Head").get("ErrorCode") == '32':
                raise Exception("Invalid Document Type")

            elif data.get('ErrorResponse').get("Head").get("ErrorCode") == '34':
                raise Exception("Order Item must be packed. set ready_to_ship before this")

            elif data.get('ErrorResponse').get("Head").get("ErrorCode") == '35':
                raise Exception("Document wasn't found")

            elif data.get('ErrorResponse').get("Head").get("ErrorCode") == '36':
                raise Exception("Invalid status, see .STATUS_OPTIONS")

            elif data.get('ErrorResponse').get("Head").get("ErrorCode") == '74':
                raise Exception("Invalid sort_direction, see .SORT_DIRECTION_OPTIONS")

            elif data.get('ErrorResponse').get("Head").get("ErrorCode") == '75':
                raise Exception("Invalid sort_filter, see .SORT_BY_OPTIONS")

        except AttributeError:
            raise Exception("Api call unsuccessful, check api_key, userID and arguments")



