import requests
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver
from django.conf import settings
from .models import paydata
import logging

logger = logging.getLogger(__name__)

@receiver(valid_ipn_received)
def paypal_payment_received(sender, **kwargs):
    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        # Verify IPN data
        if verify_ipn(ipn_obj):
            # Extract relevant data
            transaction_id = ipn_obj.txn_id
            amount = ipn_obj.mc_gross
            payer_email = ipn_obj.payer_email
            
            # Store payment information in the database
            payment_data = paydata(
                paypurchase_price=amount,
                
            )
            payment_data.save()
            logger.info(f"Payment received: {transaction_id}, Amount: {amount}, Payer: {payer_email}")
        else:
            logger.warning("IPN verification failed.")
    else:
        logger.warning(f"Payment not completed: {ipn_obj.payment_status}")

def verify_ipn(ipn_obj):
    data = {
        'cmd': '_notify-validate',
        'txn_id': ipn_obj.txn_id,
        'payment_status': ipn_obj.payment_status,
        'mc_gross': ipn_obj.mc_gross,
        'payer_email': ipn_obj.payer_email,
        # Add other necessary fields
    }
    response = requests.post('https://www.sandbox.paypal .com/cgi-bin/webscr', data=data)
    return response.text == 'VERIFIED'