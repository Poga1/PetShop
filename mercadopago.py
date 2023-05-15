import mercadopago
# Agrega credenciales
sdk = mercadopago.SDK("TEST-1799800389514061-051422-37dc35518bd55f62a7cde16d6282ccfe-193220669")


preference_data = {
    "items": [
        {
            "title": "Mi producto",
            "quantity": 1,
            "unit_price": 75
        }
    ]
}

preference_response = sdk.preference().create(preference_data)
preference = preference_response["response"]