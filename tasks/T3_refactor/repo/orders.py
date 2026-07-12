def process(orders, region, currency, vip_users, banned_users, today):
    result = []
    total = 0
    for o in orders:
        if o["region"] == region:
            if o["currency"] == currency:
                if o["user_id"] not in banned_users:
                    if o["status"] == "paid":
                        if o["date"] <= today:
                            if o["user_id"] in vip_users:
                                discount = 0.20
                            else:
                                if o["amount"] > 1000:
                                    discount = 0.10
                                else:
                                    if o["amount"] > 500:
                                        discount = 0.05
                                    else:
                                        discount = 0.0
                            final = o["amount"] * (1 - discount)
                            total = total + final
                            result.append({
                                "id": o["id"],
                                "user_id": o["user_id"],
                                "amount": o["amount"],
                                "final": final,
                                "discount": discount,
                            })
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            else:
                pass
        else:
            pass
    return {"orders": result, "total": total}
