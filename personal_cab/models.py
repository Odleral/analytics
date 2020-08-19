from django.db import models

# Create your models here.


class Expenses(models.Model):
    exp_title = models.CharField(max_length=100, blank=True)
    imp_of_srvc = models.CharField(max_length=100, blank=True)
    inc_fr_brs = models.CharField(max_length=100, blank=True)
    bsns_exp_acrd = models.CharField(max_length=100, blank=True)
    bsns_exp_pd = models.CharField(max_length=100, blank=True)
    prchs_of_mtrls = models.CharField(max_length=100, blank=True)
    pmnt_to_splrs = models.CharField(max_length=100, blank=True)
    wrtf_of_mtrls = models.CharField(max_length=100, blank=True)
    rnmrtn_for_prfmrs = models.CharField(max_length=100, blank=True)
    pmnt_of_rmnt = models.CharField(max_length=100, blank=True)
    prdctn_csts_acrd = models.CharField(max_length=100, blank=True)
    prdctn_csts_pd = models.CharField(max_length=100, blank=True)
    eqpmnt_prchs = models.CharField(max_length=100, blank=True)
    eqpmnt_pmnt = models.CharField(max_length=100, blank=True)
    dprctn_of_eqpmnt = models.CharField(max_length=100, blank=True)
    admn_expns_chrgd = models.CharField(max_length=100, blank=True)
    admn_expns_pd = models.CharField(max_length=100, blank=True)
    txs_chrgd = models.CharField(max_length=100, blank=True)
    txs_pd = models.CharField(max_length=100, blank=True)
    lns_rcvd = models.CharField(max_length=100, blank=True)
    lns_rpd = models.CharField(max_length=100, blank=True)
    intrsts_wrtoff = models.CharField(max_length=100, blank=True)
    wthdrwls_of_ownrs = models.CharField(max_length=100, blank=True)
    ownrs_invstmnts = models.CharField(max_length=100, blank=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.exp_title)

class ODR(models.Model):
    ODR_title = models.CharField(max_length=100, blank=True)
    realization = models.CharField(max_length=100, blank=True)
    right_exp = models.CharField(max_length=100, blank=True)
    gross_profit = models.CharField(max_length=100, blank=True)
    opex = models.CharField(max_length=100, blank=True)
    com_exp = models.CharField(max_length=100, blank=True)
    prod_exp = models.CharField(max_length=100, blank=True)
    admin_exp = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return '{}'.format(self.ODR_title)


