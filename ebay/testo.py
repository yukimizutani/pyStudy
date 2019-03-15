from ebaysdk.trading import Connection as Trading
from ebaysdk.exception import ConnectionError

try:
    # 各種情報を設定
    api = Trading(config_file=None,appid="YukiMizu-test-PRD-4a6d8dc4f-c04e8105", devid="0a50fcfa-837a-4a9a-82dc-a4ca6fc336ea", certid="PRD-a6d8dc4f38cb-3996-4fa9-aed5-51e5")
    # 注文データ取得
    api.execute('GetOrders', {
        "OrderStatus": "Completed",  # 支払い済みの注文のみに絞り込み
        "OrderRole": "Seller",  # セラーの注文のみに絞り込み
        "NumberOfDays": 1,  # 本日から1日遡って注文情報を取得
        "IncludeFinalValueFee": True  # 手数料データも一緒に取得
    })

    # 取得した注文データから各種データを取得
    for order in api.response.reply.OrderArray.Order:
        # ShippedTime属性がある場合は発送済みなのでスルー
        if hasattr(order, "ShippedTime") is True:
            continue

        for txn in order.TransactionArray.Transaction:
            data = {
                "order_id": order.OrderID,  # 注文ID
                "order_item_id": txn.Item.ItemID,  # 商品ID
                "created_time": order.CreatedTime,  # 注文日時
                "product_name": txn.Item.Title,  # 商品名
                "sku": txn.Item.SKU,  # SKU
                "quantity_purchased": txn.QuantityPurchased,  # 数量
                "price": txn.TransactionPrice,  # 単価
                "fee": txn.FinalValueFee.value,  # 手数料
                "shipping_cost": txn.ActualShippingCost.value,  # 送料
                "ship_name": order.ShippingAddress.Name,
                "ship_address1": order.ShippingAddress.Street1,
                "ship_address2": order.ShippingAddress.Street2,
                "ship_city": order.ShippingAddress.CityName,
                "ship_state": order.ShippingAddress.StateOrProvince,
                "ship_postal_code": order.ShippingAddress.PostalCode,
                "ship_country": order.ShippingAddress.Country,
                "ship_phone": order.ShippingAddress.Phone
            }

            print(data)

except ConnectionError as e:
    print(e)