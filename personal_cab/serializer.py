from rest_framework import serializers
from .models import Expenses

class ExpensesSerializer(serializers.Serializer):
    exp_title = serializers.CharField(max_length=100,)
    imp_of_srvc = serializers.CharField(max_length=100,)
    inc_fr_brs = serializers.CharField(max_length=100,)
    bsns_exp_acrd = serializers.CharField(max_length=100,)
    bsns_exp_pd = serializers.CharField(max_length=100,)
    prchs_of_mtrls = serializers.CharField(max_length=100,)
    pmnt_to_splrs = serializers.CharField(max_length=100,)
    wrtf_of_mtrls = serializers.CharField(max_length=100,)
    rnmrtn_for_prfmrs = serializers.CharField(max_length=100,)
    pmnt_of_rmnt = serializers.CharField(max_length=100,)
    prdctn_csts_acrd = serializers.CharField(max_length=100,)
    prdctn_csts_pd = serializers.CharField(max_length=100,)
    eqpmnt_prchs = serializers.CharField(max_length=100,)
    eqpmnt_pmnt = serializers.CharField(max_length=100,)
    dprctn_of_eqpmnt = serializers.CharField(max_length=100,)
    admn_expns_chrgd = serializers.CharField(max_length=100,)
    admn_expns_pd = serializers.CharField(max_length=100,)
    txs_chrgd = serializers.CharField(max_length=100,)
    txs_pd = serializers.CharField(max_length=100,)
    lns_rcvd = serializers.CharField(max_length=100,)
    lns_rpd = serializers.CharField(max_length=100,)
    intrsts_wrtoff = serializers.CharField(max_length=100,)
    wthdrwls_of_ownrs = serializers.CharField(max_length=100,)
    ownrs_invstmnts = serializers.CharField(max_length=100,)
    created_date = serializers.DateField()


    def create(self, validated_data):
        return Expenses.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.exp_title = validated_data.get('exp_title', instance.exp_title)
        instance.imp_of_srvc = validated_data.get('imp_of_srvc', instance.imp_of_srvc)
        instance.inc_fr_brs = validated_data.get('inc_fr_brs', instance.inc_fr_brs)
        instance.bsns_exp_acrd = validated_data.get('bsns_exp_acrd', instance.bsns_exp_acrd)
        instance.bsns_exp_pd = validated_data.get('bsns_exp_pd', instance.bsns_exp_pd)
        instance.prchs_of_mtrls = validated_data.get('prchs_of_mtrls', instance.prchs_of_mtrls)
        instance.pmnt_to_splrs = validated_data.get('pmnt_to_splrs', instance.pmnt_to_splrs)
        instance.wrtf_of_mtrls = validated_data.get('wrtf_of_mtrls', instance.wrtf_of_mtrls)
        instance.rnmrtn_for_prfmrs = validated_data.get('rnmrtn_for_prfmrs', instance.rnmrtn_for_prfmrs)
        instance.pmnt_of_rmnt = validated_data.get('pmnt_of_rmnt', instance.pmnt_of_rmnt)
        instance.prdctn_csts_acrd = validated_data.get('prdctn_csts_acrd', instance.prdctn_csts_acrd)
        instance.prdctn_csts_pd = validated_data.get('prdctn_csts_pd', instance.prdctn_csts_pd)
        instance.eqpmnt_prchs = validated_data.get('eqpmnt_prchs', instance.eqpmnt_prchs)
        instance.eqpmnt_pmnt = validated_data.get('eqpmnt_pmnt', instance.eqpmnt_pmnt)
        instance.dprctn_of_eqpmnt = validated_data.get('dprctn_of_eqpmnt', instance.dprctn_of_eqpmnt)
        instance.admn_expns_chrgd = validated_data.get('admn_expns_chrgd', instance.admn_expns_chrgd)
        instance.admn_expns_pd = validated_data.get('admn_expns_pd', instance.admn_expns_pd)
        instance.txs_chrgd = validated_data.get('txs_chrgd', instance.txs_chrgd)
        instance.txs_pd = validated_data.get('txs_pd', instance.txs_pd)
        instance.lns_rcvd = validated_data.get('lns_rcvd', instance.lns_rcvd)
        instance.lns_rpd = validated_data.get('lns_rpd', instance.lns_rpd)
        instance.intrsts_wrtoff = validated_data.get('intrsts_wrtoff', instance.intrsts_wrtoff)
        instance.wthdrwls_of_ownrs = validated_data.get('wthdrwls_of_ownrs', instance.wthdrwls_of_ownrs)
        instance.ownrs_invstmnts = validated_data.get('ownrs_invstmnts', instance.ownrs_invstmnts)
        instance.created_date = validated_data.get('created_date', instance.created_date)


        instance.save()
        return instance


class ODRSerializer(serializers.Serializer):
    ODR_title = serializers.CharField(max_length=100,)
    realization = serializers.CharField(max_length=100,)
    right_exp = serializers.CharField(max_length=100,)
    gross_profit = serializers.CharField(max_length=100,)
    opex = serializers.CharField(max_length=100,)
    com_exp = serializers.CharField(max_length=100,)
    prod_exp = serializers.CharField(max_length=100,)
    admin_exp = serializers.CharField(max_length=100,)