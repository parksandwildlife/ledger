from __future__ import unicode_literals

from django.db import models
from ledger.payments.bpoint import settings as bpoint_settings
from django.utils.encoding import python_2_unicode_compatible
from oscar.apps.order.models import Order

class BpointTransaction(models.Model):
    ACTION_TYPES = (
        ('payment','payment'),
        ('refund','refund'),
        ('reversal','reversal'),
        ('preauth', 'preauth'),
        ('capture','capture')
    )
    CARD_TYPES = (
        ('AX','American Express'),
        ('DC','Diners Club'),
        ('JC','JCB Card'),
        ('MC','MasterCard'),
        ('VC','Visa')
    )
    SUB_TYPES = (
        ('single','single'),
        ('recurring','recurring')
    )
    TRANSACTION_TYPES = (
        ('callcentre','callcentre'),
        ('cardpresent','cardpresent'),
        ('ecommerce','ecommerce'),
        ('internet', 'internet'),
        ('ivr','ivr'),
        ('mailorder','mailorder'),
        ('telephoneorder','telephoneorder')
    )
    created = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=20, choices=ACTION_TYPES)
    amount = models.DecimalField(decimal_places=2,max_digits=12)
    amount_original = models.DecimalField(decimal_places=2,max_digits=12)
    amount_surcharge = models.DecimalField(default=0,decimal_places=2,max_digits=12)
    cardtype = models.CharField(max_length=2, choices=CARD_TYPES, blank=True, null=True)
    crn1 = models.CharField(max_length=50, help_text='Reference for the order that the transaction was made for')
    response_code = models.CharField(max_length=50)
    response_txt = models.CharField(max_length=128)
    receipt_number = models.CharField(max_length=50)
    processed = models.DateTimeField()
    settlement_date = models.DateField(blank=True, null=True)
    type = models.CharField(max_length=50, choices=TRANSACTION_TYPES)
    # store the txn number from Bpoint
    txn_number = models.CharField(unique=True, max_length=128, help_text='Transaction number used by BPOINT to identify a transaction')
    original_txn = models.ForeignKey('self', to_field='txn_number', blank=True, null=True, help_text='Transaction number stored \
                                           if current transaction depends on a previous transaction \
                                           in the case where the action is a refund, reversal or capture')
    
    class Meta:
        ordering = ('-created',)
    
    def __unicode__(self):
        return self.txn_number
    
    @property
    def approved(self):
        return self.response_code == "0"
    
    @property
    def order(self):
        return Order.objects.get(number=self.crn1[:-1])
    
    
    
