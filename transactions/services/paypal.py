def process_payment(data):
    # Simulate PayPal processing
    return {
        "data": data,
        "status": "completed",
        "payment":{
            "message": "Payment initiated via PayPal",
            "status": "success",
             }
    }
