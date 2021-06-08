from django.db import models


# Create your models here.
# 新增的四张表的模型类


class User(models.Model):
    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Admin(models.Model):
    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    dbpassword = models.CharField(max_length=256)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tbcell(models.Model):
    city = models.CharField(db_column='CITY', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sector_id = models.CharField(db_column='SECTOR_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    sector_name = models.CharField(db_column='SECTOR_NAME', max_length=255)  # Field name made lowercase.
    enodebid = models.IntegerField(db_column='ENODEBID')  # Field name made lowercase.
    enodeb_name = models.CharField(db_column='ENODEB_NAME', max_length=255)  # Field name made lowercase.
    earfcn = models.IntegerField(db_column='EARFCN')  # Field name made lowercase.
    pci = models.IntegerField(db_column='PCI')  # Field name made lowercase.
    pss = models.IntegerField(db_column='PSS', blank=True, null=True)  # Field name made lowercase.
    sss = models.IntegerField(db_column='SSS', blank=True, null=True)  # Field name made lowercase.
    tac = models.IntegerField(db_column='TAC', blank=True, null=True)  # Field name made lowercase.
    vendor = models.CharField(db_column='VENDOR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    longitude = models.FloatField(db_column='LONGITUDE')  # Field name made lowercase.
    latitude = models.FloatField(db_column='LATITUDE')  # Field name made lowercase.
    style = models.CharField(db_column='STYLE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    azimuth = models.FloatField(db_column='AZIMUTH')  # Field name made lowercase.
    height = models.FloatField(db_column='HEIGHT', blank=True, null=True)  # Field name made lowercase.
    electtilt = models.FloatField(db_column='ELECTTILT', blank=True, null=True)  # Field name made lowercase.
    mechtilt = models.FloatField(db_column='MECHTILT', blank=True, null=True)  # Field name made lowercase.
    totletilt = models.FloatField(db_column='TOTLETILT')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tbcell'


class Tbkpi(models.Model):
    # 注意数据库里是sector_name和date联合主键，而model由于django限制只有一个
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    enodeb_name = models.CharField(db_column='ENODEB_NAME', max_length=255)  # Field name made lowercase.
    # enodeb_name = models.ForeignKey('Tbcell', on_delete=models.CASCADE, to_field=Tbcell.enodeb_name,
    #                                 db_column='ENODEB_NAME')
    # enodeb_name = models.ForeignKey(Tbcell, on_delete=models.CASCADE,
    #                                 db_column='ENODEB_NAME')  # Field name made lowercase.
    sector = models.CharField(db_column='SECTOR', max_length=255)  # Field name made lowercase.
    sector_name = models.CharField(db_column='SECTOR_NAME', primary_key=True,
                                   max_length=255)  # Field name made lowercase.
    rpc_establish = models.IntegerField(db_column='RPC_ESTABLISH', blank=True, null=True)  # Field name made lowercase.
    rpc_request = models.IntegerField(db_column='RPC_REQUEST', blank=True, null=True)  # Field name made lowercase.
    rpc_succrate = models.FloatField(db_column='RPC_SUCCRATE', blank=True, null=True)  # Field name made lowercase.
    erab_succ = models.IntegerField(db_column='ERAB_SUCC', blank=True, null=True)  # Field name made lowercase.
    erab_att = models.IntegerField(db_column='ERAB_ATT', blank=True, null=True)  # Field name made lowercase.
    erab_succrate = models.FloatField(db_column='ERAB_SUCCRATE', blank=True, null=True)  # Field name made lowercase.
    enodeb_erab_ex = models.IntegerField(db_column='ENODEB_ERAB_EX', blank=True,
                                         null=True)  # Field name made lowercase.
    sector_switch_erab_ex = models.IntegerField(db_column='SECTOR_SWITCH_ERAB_EX', blank=True,
                                                null=True)  # Field name made lowercase.
    erab_lossrate = models.FloatField(db_column='ERAB_LOSSRATE', blank=True, null=True)  # Field name made lowercase.
    ay = models.FloatField(db_column='AY', blank=True, null=True)  # Field name made lowercase.
    enodeb_reset_ue_release = models.IntegerField(db_column='ENODEB_RESET_UE_RELEASE', blank=True,
                                                  null=True)  # Field name made lowercase.
    ue_ex_release = models.IntegerField(db_column='UE_EX_RELEASE', blank=True, null=True)  # Field name made lowercase.
    ue_succ = models.IntegerField(db_column='UE_SUCC', blank=True, null=True)  # Field name made lowercase.
    lossrate = models.FloatField(db_column='LOSSRATE', blank=True, null=True)  # Field name made lowercase.
    enodeb_in_diff_succ = models.IntegerField(db_column='ENODEB_IN_DIFF_SUCC', blank=True,
                                              null=True)  # Field name made lowercase.
    enodeb_in_diff_att = models.IntegerField(db_column='ENODEB_IN_DIFF_ATT', blank=True,
                                             null=True)  # Field name made lowercase.
    enodeb_in_same_succ = models.IntegerField(db_column='ENODEB_IN_SAME_SUCC', blank=True,
                                              null=True)  # Field name made lowercase.
    enodeb_in_same_att = models.IntegerField(db_column='ENODEB_IN_SAME_ATT', blank=True,
                                             null=True)  # Field name made lowercase.
    enodeb_out_diff_succ = models.IntegerField(db_column='ENODEB_OUT_DIFF_SUCC', blank=True,
                                               null=True)  # Field name made lowercase.
    enodeb_out_diff_att = models.IntegerField(db_column='ENODEB_OUT_DIFF_ATT', blank=True,
                                              null=True)  # Field name made lowercase.
    enodeb_out_same_succ = models.IntegerField(db_column='ENODEB_OUT_SAME_SUCC', blank=True,
                                               null=True)  # Field name made lowercase.
    enodeb_out_same_att = models.IntegerField(db_column='ENODEB_OUT_SAME_ATT', blank=True,
                                              null=True)  # Field name made lowercase.
    enodeb_in_succrate = models.FloatField(db_column='ENODEB_IN_SUCCRATE', blank=True,
                                           null=True)  # Field name made lowercase.
    enodeb_out_succrate = models.FloatField(db_column='ENODEB_OUT_SUCCRATE', blank=True,
                                            null=True)  # Field name made lowercase.
    enodeb_same_succrate = models.FloatField(db_column='ENODEB_SAME_SUCCRATE', blank=True,
                                             null=True)  # Field name made lowercase.
    enodeb_diff_succrate = models.FloatField(db_column='ENODEB_DIFF_SUCCRATE', blank=True,
                                             null=True)  # Field name made lowercase.
    enodeb_switch_succrate = models.FloatField(db_column='ENODEB_SWITCH_SUCCRATE', blank=True,
                                               null=True)  # Field name made lowercase.
    pdcp_up = models.BigIntegerField(db_column='PDCP_UP', blank=True, null=True)  # Field name made lowercase.
    pdcp_down = models.BigIntegerField(db_column='PDCP_DOWN', blank=True, null=True)  # Field name made lowercase.
    rpc_rebuild = models.IntegerField(db_column='RPC_REBUILD', blank=True, null=True)  # Field name made lowercase.
    rpc_rebuildrate = models.FloatField(db_column='RPC_REBUILDRATE', blank=True,
                                        null=True)  # Field name made lowercase.
    rebuild_enodeb_out_same_succ = models.IntegerField(db_column='REBUILD_ENODEB_OUT_SAME_SUCC', blank=True,
                                                       null=True)  # Field name made lowercase.
    rebuild_enodeb_out_diff_succ = models.IntegerField(db_column='REBUILD_ENODEB_OUT_DIFF_SUCC', blank=True,
                                                       null=True)  # Field name made lowercase.
    rebuild_enodeb_in_same_succ = models.IntegerField(db_column='REBUILD_ENODEB_IN_SAME_SUCC', blank=True,
                                                      null=True)  # Field name made lowercase.
    rebuild_enodeb_in_diff_succ = models.IntegerField(db_column='REBUILD_ENODEB_IN_DIFF_SUCC', blank=True,
                                                      null=True)  # Field name made lowercase.
    enb_in_succ = models.IntegerField(db_column='ENB_IN_SUCC', blank=True, null=True)  # Field name made lowercase.
    eno_in_request = models.IntegerField(db_column='ENO_IN_REQUEST', blank=True,
                                         null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tbkpi'


class Tbprb(models.Model):
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    enodeb_name = models.CharField(db_column='ENODEB_NAME', max_length=255)  # Field name made lowercase.
    # enodeb_name = models.ForeignKey(Tbcell, on_delete=models.CASCADE,
    #                                 db_column='ENODEB_NAME')  # Field name made lowercase.
    sector_description = models.CharField(db_column='SECTOR_DESCRIPTION', max_length=255)  # Field name made lowercase.
    sector_name = models.CharField(db_column='SECTOR_NAME', primary_key=True,
                                   max_length=255)  # Field name made lowercase.
    avr_noise_prb0 = models.IntegerField(db_column='AVR_NOISE_PRB0')  # Field name made lowercase.
    avr_noise_prb1 = models.IntegerField(db_column='AVR_NOISE_PRB1')  # Field name made lowercase.
    avr_noise_prb2 = models.IntegerField(db_column='AVR_NOISE_PRB2')  # Field name made lowercase.
    avr_noise_prb3 = models.IntegerField(db_column='AVR_NOISE_PRB3')  # Field name made lowercase.
    avr_noise_prb4 = models.IntegerField(db_column='AVR_NOISE_PRB4')  # Field name made lowercase.
    avr_noise_prb5 = models.IntegerField(db_column='AVR_NOISE_PRB5')  # Field name made lowercase.
    avr_noise_prb6 = models.IntegerField(db_column='AVR_NOISE_PRB6')  # Field name made lowercase.
    avr_noise_prb7 = models.IntegerField(db_column='AVR_NOISE_PRB7')  # Field name made lowercase.
    avr_noise_prb8 = models.IntegerField(db_column='AVR_NOISE_PRB8')  # Field name made lowercase.
    avr_noise_prb9 = models.IntegerField(db_column='AVR_NOISE_PRB9')  # Field name made lowercase.
    avr_noise_prb10 = models.IntegerField(db_column='AVR_NOISE_PRB10')  # Field name made lowercase.
    avr_noise_prb11 = models.IntegerField(db_column='AVR_NOISE_PRB11')  # Field name made lowercase.
    avr_noise_prb12 = models.IntegerField(db_column='AVR_NOISE_PRB12')  # Field name made lowercase.
    avr_noise_prb13 = models.IntegerField(db_column='AVR_NOISE_PRB13')  # Field name made lowercase.
    avr_noise_prb14 = models.IntegerField(db_column='AVR_NOISE_PRB14')  # Field name made lowercase.
    avr_noise_prb15 = models.IntegerField(db_column='AVR_NOISE_PRB15')  # Field name made lowercase.
    avr_noise_prb16 = models.IntegerField(db_column='AVR_NOISE_PRB16')  # Field name made lowercase.
    avr_noise_prb17 = models.IntegerField(db_column='AVR_NOISE_PRB17')  # Field name made lowercase.
    avr_noise_prb18 = models.IntegerField(db_column='AVR_NOISE_PRB18')  # Field name made lowercase.
    avr_noise_prb19 = models.IntegerField(db_column='AVR_NOISE_PRB19')  # Field name made lowercase.
    avr_noise_prb20 = models.IntegerField(db_column='AVR_NOISE_PRB20')  # Field name made lowercase.
    avr_noise_prb21 = models.IntegerField(db_column='AVR_NOISE_PRB21')  # Field name made lowercase.
    avr_noise_prb22 = models.IntegerField(db_column='AVR_NOISE_PRB22')  # Field name made lowercase.
    avr_noise_prb23 = models.IntegerField(db_column='AVR_NOISE_PRB23')  # Field name made lowercase.
    avr_noise_prb24 = models.IntegerField(db_column='AVR_NOISE_PRB24')  # Field name made lowercase.
    avr_noise_prb25 = models.IntegerField(db_column='AVR_NOISE_PRB25')  # Field name made lowercase.
    avr_noise_prb26 = models.IntegerField(db_column='AVR_NOISE_PRB26')  # Field name made lowercase.
    avr_noise_prb27 = models.IntegerField(db_column='AVR_NOISE_PRB27')  # Field name made lowercase.
    avr_noise_prb28 = models.IntegerField(db_column='AVR_NOISE_PRB28')  # Field name made lowercase.
    avr_noise_prb29 = models.IntegerField(db_column='AVR_NOISE_PRB29')  # Field name made lowercase.
    avr_noise_prb30 = models.IntegerField(db_column='AVR_NOISE_PRB30')  # Field name made lowercase.
    avr_noise_prb31 = models.IntegerField(db_column='AVR_NOISE_PRB31')  # Field name made lowercase.
    avr_noise_prb32 = models.IntegerField(db_column='AVR_NOISE_PRB32')  # Field name made lowercase.
    avr_noise_prb33 = models.IntegerField(db_column='AVR_NOISE_PRB33')  # Field name made lowercase.
    avr_noise_prb34 = models.IntegerField(db_column='AVR_NOISE_PRB34')  # Field name made lowercase.
    avr_noise_prb35 = models.IntegerField(db_column='AVR_NOISE_PRB35')  # Field name made lowercase.
    avr_noise_prb36 = models.IntegerField(db_column='AVR_NOISE_PRB36')  # Field name made lowercase.
    avr_noise_prb37 = models.IntegerField(db_column='AVR_NOISE_PRB37')  # Field name made lowercase.
    avr_noise_prb38 = models.IntegerField(db_column='AVR_NOISE_PRB38')  # Field name made lowercase.
    avr_noise_prb39 = models.IntegerField(db_column='AVR_NOISE_PRB39')  # Field name made lowercase.
    avr_noise_prb40 = models.IntegerField(db_column='AVR_NOISE_PRB40')  # Field name made lowercase.
    avr_noise_prb41 = models.IntegerField(db_column='AVR_NOISE_PRB41')  # Field name made lowercase.
    avr_noise_prb42 = models.IntegerField(db_column='AVR_NOISE_PRB42')  # Field name made lowercase.
    avr_noise_prb43 = models.IntegerField(db_column='AVR_NOISE_PRB43')  # Field name made lowercase.
    avr_noise_prb44 = models.IntegerField(db_column='AVR_NOISE_PRB44')  # Field name made lowercase.
    avr_noise_prb45 = models.IntegerField(db_column='AVR_NOISE_PRB45')  # Field name made lowercase.
    avr_noise_prb46 = models.IntegerField(db_column='AVR_NOISE_PRB46')  # Field name made lowercase.
    avr_noise_prb47 = models.IntegerField(db_column='AVR_NOISE_PRB47')  # Field name made lowercase.
    avr_noise_prb48 = models.IntegerField(db_column='AVR_NOISE_PRB48')  # Field name made lowercase.
    avr_noise_prb49 = models.IntegerField(db_column='AVR_NOISE_PRB49')  # Field name made lowercase.
    avr_noise_prb50 = models.IntegerField(db_column='AVR_NOISE_PRB50')  # Field name made lowercase.
    avr_noise_prb51 = models.IntegerField(db_column='AVR_NOISE_PRB51')  # Field name made lowercase.
    avr_noise_prb52 = models.IntegerField(db_column='AVR_NOISE_PRB52')  # Field name made lowercase.
    avr_noise_prb53 = models.IntegerField(db_column='AVR_NOISE_PRB53')  # Field name made lowercase.
    avr_noise_prb54 = models.IntegerField(db_column='AVR_NOISE_PRB54')  # Field name made lowercase.
    avr_noise_prb55 = models.IntegerField(db_column='AVR_NOISE_PRB55')  # Field name made lowercase.
    avr_noise_prb56 = models.IntegerField(db_column='AVR_NOISE_PRB56')  # Field name made lowercase.
    avr_noise_prb57 = models.IntegerField(db_column='AVR_NOISE_PRB57')  # Field name made lowercase.
    avr_noise_prb58 = models.IntegerField(db_column='AVR_NOISE_PRB58')  # Field name made lowercase.
    avr_noise_prb59 = models.IntegerField(db_column='AVR_NOISE_PRB59')  # Field name made lowercase.
    avr_noise_prb60 = models.IntegerField(db_column='AVR_NOISE_PRB60')  # Field name made lowercase.
    avr_noise_prb61 = models.IntegerField(db_column='AVR_NOISE_PRB61')  # Field name made lowercase.
    avr_noise_prb62 = models.IntegerField(db_column='AVR_NOISE_PRB62')  # Field name made lowercase.
    avr_noise_prb63 = models.IntegerField(db_column='AVR_NOISE_PRB63')  # Field name made lowercase.
    avr_noise_prb64 = models.IntegerField(db_column='AVR_NOISE_PRB64')  # Field name made lowercase.
    avr_noise_prb65 = models.IntegerField(db_column='AVR_NOISE_PRB65')  # Field name made lowercase.
    avr_noise_prb66 = models.IntegerField(db_column='AVR_NOISE_PRB66')  # Field name made lowercase.
    avr_noise_prb67 = models.IntegerField(db_column='AVR_NOISE_PRB67')  # Field name made lowercase.
    avr_noise_prb68 = models.IntegerField(db_column='AVR_NOISE_PRB68')  # Field name made lowercase.
    avr_noise_prb69 = models.IntegerField(db_column='AVR_NOISE_PRB69')  # Field name made lowercase.
    avr_noise_prb70 = models.IntegerField(db_column='AVR_NOISE_PRB70')  # Field name made lowercase.
    avr_noise_prb71 = models.IntegerField(db_column='AVR_NOISE_PRB71')  # Field name made lowercase.
    avr_noise_prb72 = models.IntegerField(db_column='AVR_NOISE_PRB72')  # Field name made lowercase.
    avr_noise_prb73 = models.IntegerField(db_column='AVR_NOISE_PRB73')  # Field name made lowercase.
    avr_noise_prb74 = models.IntegerField(db_column='AVR_NOISE_PRB74')  # Field name made lowercase.
    avr_noise_prb75 = models.IntegerField(db_column='AVR_NOISE_PRB75')  # Field name made lowercase.
    avr_noise_prb76 = models.IntegerField(db_column='AVR_NOISE_PRB76')  # Field name made lowercase.
    avr_noise_prb77 = models.IntegerField(db_column='AVR_NOISE_PRB77')  # Field name made lowercase.
    avr_noise_prb78 = models.IntegerField(db_column='AVR_NOISE_PRB78')  # Field name made lowercase.
    avr_noise_prb79 = models.IntegerField(db_column='AVR_NOISE_PRB79')  # Field name made lowercase.
    avr_noise_prb80 = models.IntegerField(db_column='AVR_NOISE_PRB80')  # Field name made lowercase.
    avr_noise_prb81 = models.IntegerField(db_column='AVR_NOISE_PRB81')  # Field name made lowercase.
    avr_noise_prb82 = models.IntegerField(db_column='AVR_NOISE_PRB82')  # Field name made lowercase.
    avr_noise_prb83 = models.IntegerField(db_column='AVR_NOISE_PRB83')  # Field name made lowercase.
    avr_noise_prb84 = models.IntegerField(db_column='AVR_NOISE_PRB84')  # Field name made lowercase.
    avr_noise_prb85 = models.IntegerField(db_column='AVR_NOISE_PRB85')  # Field name made lowercase.
    avr_noise_prb86 = models.IntegerField(db_column='AVR_NOISE_PRB86')  # Field name made lowercase.
    avr_noise_prb87 = models.IntegerField(db_column='AVR_NOISE_PRB87')  # Field name made lowercase.
    avr_noise_prb88 = models.IntegerField(db_column='AVR_NOISE_PRB88')  # Field name made lowercase.
    avr_noise_prb89 = models.IntegerField(db_column='AVR_NOISE_PRB89')  # Field name made lowercase.
    avr_noise_prb90 = models.IntegerField(db_column='AVR_NOISE_PRB90')  # Field name made lowercase.
    avr_noise_prb91 = models.IntegerField(db_column='AVR_NOISE_PRB91')  # Field name made lowercase.
    avr_noise_prb92 = models.IntegerField(db_column='AVR_NOISE_PRB92')  # Field name made lowercase.
    avr_noise_prb93 = models.IntegerField(db_column='AVR_NOISE_PRB93')  # Field name made lowercase.
    avr_noise_prb94 = models.IntegerField(db_column='AVR_NOISE_PRB94')  # Field name made lowercase.
    avr_noise_prb95 = models.IntegerField(db_column='AVR_NOISE_PRB95')  # Field name made lowercase.
    avr_noise_prb96 = models.IntegerField(db_column='AVR_NOISE_PRB96')  # Field name made lowercase.
    avr_noise_prb97 = models.IntegerField(db_column='AVR_NOISE_PRB97')  # Field name made lowercase.
    avr_noise_prb98 = models.IntegerField(db_column='AVR_NOISE_PRB98')  # Field name made lowercase.
    avr_noise_prb99 = models.IntegerField(db_column='AVR_NOISE_PRB99')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tbprb'


class Tbmrodata(models.Model):
    timestamp = models.CharField(db_column='TimeStamp', max_length=30, primary_key=True)  # Field name made lowercase.
    servingsector = models.CharField(db_column='ServingSector', max_length=30)  # Field name made lowercase.
    interferingsector = models.CharField(db_column='InterferingSector', max_length=30)  # Field name made lowercase.
    ltescrsrp = models.FloatField(db_column='LteScRSRP', blank=True, null=True)  # Field name made lowercase.
    ltencrsrp = models.FloatField(db_column='LteNcRSRP', blank=True, null=True)  # Field name made lowercase.
    ltencearfcn = models.IntegerField(db_column='LteNcEarfcn', blank=True, null=True)  # Field name made lowercase.
    ltencpci = models.PositiveSmallIntegerField(db_column='LteNcPci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tbmrodata'
        unique_together = (('timestamp', 'servingsector', 'interferingsector'),)


class TbC2Inew(models.Model):
    nc_sector_id = models.CharField(db_column='NC_SECTOR_ID', max_length=50)  # Field name made lowercase.
    sc_sector_id = models.CharField(db_column='SC_SECTOR_ID', max_length=50)  # Field name made lowercase.
    rsrp_avg = models.FloatField(db_column='RSRP_AVG', blank=True, null=True)  # Field name made lowercase.
    rsrp_std = models.FloatField(db_column='RSRP_STD', blank=True, null=True)  # Field name made lowercase.
    probility_9 = models.FloatField(db_column='PROBILITY_9', blank=True, null=True)  # Field name made lowercase.
    probility_6 = models.FloatField(db_column='PROBILITY_6', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tbC2Inew'


class tbC2I3(models.Model):
    a_sector = models.CharField(db_column='A_SECTOR', max_length=50)  # Field name made lowercase.
    b_sector = models.CharField(db_column='B_SECTOR', max_length=50)  # Field name made lowercase.
    c_sector = models.CharField(db_column='C_SECTOR', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tbC2I3'


class Tbprbnew(models.Model):
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    enodeb_name = models.CharField(db_column='ENODEB_NAME', max_length=255)  # Field name made lowercase.
    sector_description = models.CharField(db_column='SECTOR_DESCRIPTION', max_length=255)  # Field name made lowercase.
    sector_name = models.CharField(db_column='SECTOR_NAME', primary_key=True,
                                   max_length=255)  # Field name made lowercase.
    avr_noise_prb0 = models.IntegerField(db_column='AVR_NOISE_PRB0')  # Field name made lowercase.
    avr_noise_prb1 = models.IntegerField(db_column='AVR_NOISE_PRB1')  # Field name made lowercase.
    avr_noise_prb2 = models.IntegerField(db_column='AVR_NOISE_PRB2')  # Field name made lowercase.
    avr_noise_prb3 = models.IntegerField(db_column='AVR_NOISE_PRB3')  # Field name made lowercase.
    avr_noise_prb4 = models.IntegerField(db_column='AVR_NOISE_PRB4')  # Field name made lowercase.
    avr_noise_prb5 = models.IntegerField(db_column='AVR_NOISE_PRB5')  # Field name made lowercase.
    avr_noise_prb6 = models.IntegerField(db_column='AVR_NOISE_PRB6')  # Field name made lowercase.
    avr_noise_prb7 = models.IntegerField(db_column='AVR_NOISE_PRB7')  # Field name made lowercase.
    avr_noise_prb8 = models.IntegerField(db_column='AVR_NOISE_PRB8')  # Field name made lowercase.
    avr_noise_prb9 = models.IntegerField(db_column='AVR_NOISE_PRB9')  # Field name made lowercase.
    avr_noise_prb10 = models.IntegerField(db_column='AVR_NOISE_PRB10')  # Field name made lowercase.
    avr_noise_prb11 = models.IntegerField(db_column='AVR_NOISE_PRB11')  # Field name made lowercase.
    avr_noise_prb12 = models.IntegerField(db_column='AVR_NOISE_PRB12')  # Field name made lowercase.
    avr_noise_prb13 = models.IntegerField(db_column='AVR_NOISE_PRB13')  # Field name made lowercase.
    avr_noise_prb14 = models.IntegerField(db_column='AVR_NOISE_PRB14')  # Field name made lowercase.
    avr_noise_prb15 = models.IntegerField(db_column='AVR_NOISE_PRB15')  # Field name made lowercase.
    avr_noise_prb16 = models.IntegerField(db_column='AVR_NOISE_PRB16')  # Field name made lowercase.
    avr_noise_prb17 = models.IntegerField(db_column='AVR_NOISE_PRB17')  # Field name made lowercase.
    avr_noise_prb18 = models.IntegerField(db_column='AVR_NOISE_PRB18')  # Field name made lowercase.
    avr_noise_prb19 = models.IntegerField(db_column='AVR_NOISE_PRB19')  # Field name made lowercase.
    avr_noise_prb20 = models.IntegerField(db_column='AVR_NOISE_PRB20')  # Field name made lowercase.
    avr_noise_prb21 = models.IntegerField(db_column='AVR_NOISE_PRB21')  # Field name made lowercase.
    avr_noise_prb22 = models.IntegerField(db_column='AVR_NOISE_PRB22')  # Field name made lowercase.
    avr_noise_prb23 = models.IntegerField(db_column='AVR_NOISE_PRB23')  # Field name made lowercase.
    avr_noise_prb24 = models.IntegerField(db_column='AVR_NOISE_PRB24')  # Field name made lowercase.
    avr_noise_prb25 = models.IntegerField(db_column='AVR_NOISE_PRB25')  # Field name made lowercase.
    avr_noise_prb26 = models.IntegerField(db_column='AVR_NOISE_PRB26')  # Field name made lowercase.
    avr_noise_prb27 = models.IntegerField(db_column='AVR_NOISE_PRB27')  # Field name made lowercase.
    avr_noise_prb28 = models.IntegerField(db_column='AVR_NOISE_PRB28')  # Field name made lowercase.
    avr_noise_prb29 = models.IntegerField(db_column='AVR_NOISE_PRB29')  # Field name made lowercase.
    avr_noise_prb30 = models.IntegerField(db_column='AVR_NOISE_PRB30')  # Field name made lowercase.
    avr_noise_prb31 = models.IntegerField(db_column='AVR_NOISE_PRB31')  # Field name made lowercase.
    avr_noise_prb32 = models.IntegerField(db_column='AVR_NOISE_PRB32')  # Field name made lowercase.
    avr_noise_prb33 = models.IntegerField(db_column='AVR_NOISE_PRB33')  # Field name made lowercase.
    avr_noise_prb34 = models.IntegerField(db_column='AVR_NOISE_PRB34')  # Field name made lowercase.
    avr_noise_prb35 = models.IntegerField(db_column='AVR_NOISE_PRB35')  # Field name made lowercase.
    avr_noise_prb36 = models.IntegerField(db_column='AVR_NOISE_PRB36')  # Field name made lowercase.
    avr_noise_prb37 = models.IntegerField(db_column='AVR_NOISE_PRB37')  # Field name made lowercase.
    avr_noise_prb38 = models.IntegerField(db_column='AVR_NOISE_PRB38')  # Field name made lowercase.
    avr_noise_prb39 = models.IntegerField(db_column='AVR_NOISE_PRB39')  # Field name made lowercase.
    avr_noise_prb40 = models.IntegerField(db_column='AVR_NOISE_PRB40')  # Field name made lowercase.
    avr_noise_prb41 = models.IntegerField(db_column='AVR_NOISE_PRB41')  # Field name made lowercase.
    avr_noise_prb42 = models.IntegerField(db_column='AVR_NOISE_PRB42')  # Field name made lowercase.
    avr_noise_prb43 = models.IntegerField(db_column='AVR_NOISE_PRB43')  # Field name made lowercase.
    avr_noise_prb44 = models.IntegerField(db_column='AVR_NOISE_PRB44')  # Field name made lowercase.
    avr_noise_prb45 = models.IntegerField(db_column='AVR_NOISE_PRB45')  # Field name made lowercase.
    avr_noise_prb46 = models.IntegerField(db_column='AVR_NOISE_PRB46')  # Field name made lowercase.
    avr_noise_prb47 = models.IntegerField(db_column='AVR_NOISE_PRB47')  # Field name made lowercase.
    avr_noise_prb48 = models.IntegerField(db_column='AVR_NOISE_PRB48')  # Field name made lowercase.
    avr_noise_prb49 = models.IntegerField(db_column='AVR_NOISE_PRB49')  # Field name made lowercase.
    avr_noise_prb50 = models.IntegerField(db_column='AVR_NOISE_PRB50')  # Field name made lowercase.
    avr_noise_prb51 = models.IntegerField(db_column='AVR_NOISE_PRB51')  # Field name made lowercase.
    avr_noise_prb52 = models.IntegerField(db_column='AVR_NOISE_PRB52')  # Field name made lowercase.
    avr_noise_prb53 = models.IntegerField(db_column='AVR_NOISE_PRB53')  # Field name made lowercase.
    avr_noise_prb54 = models.IntegerField(db_column='AVR_NOISE_PRB54')  # Field name made lowercase.
    avr_noise_prb55 = models.IntegerField(db_column='AVR_NOISE_PRB55')  # Field name made lowercase.
    avr_noise_prb56 = models.IntegerField(db_column='AVR_NOISE_PRB56')  # Field name made lowercase.
    avr_noise_prb57 = models.IntegerField(db_column='AVR_NOISE_PRB57')  # Field name made lowercase.
    avr_noise_prb58 = models.IntegerField(db_column='AVR_NOISE_PRB58')  # Field name made lowercase.
    avr_noise_prb59 = models.IntegerField(db_column='AVR_NOISE_PRB59')  # Field name made lowercase.
    avr_noise_prb60 = models.IntegerField(db_column='AVR_NOISE_PRB60')  # Field name made lowercase.
    avr_noise_prb61 = models.IntegerField(db_column='AVR_NOISE_PRB61')  # Field name made lowercase.
    avr_noise_prb62 = models.IntegerField(db_column='AVR_NOISE_PRB62')  # Field name made lowercase.
    avr_noise_prb63 = models.IntegerField(db_column='AVR_NOISE_PRB63')  # Field name made lowercase.
    avr_noise_prb64 = models.IntegerField(db_column='AVR_NOISE_PRB64')  # Field name made lowercase.
    avr_noise_prb65 = models.IntegerField(db_column='AVR_NOISE_PRB65')  # Field name made lowercase.
    avr_noise_prb66 = models.IntegerField(db_column='AVR_NOISE_PRB66')  # Field name made lowercase.
    avr_noise_prb67 = models.IntegerField(db_column='AVR_NOISE_PRB67')  # Field name made lowercase.
    avr_noise_prb68 = models.IntegerField(db_column='AVR_NOISE_PRB68')  # Field name made lowercase.
    avr_noise_prb69 = models.IntegerField(db_column='AVR_NOISE_PRB69')  # Field name made lowercase.
    avr_noise_prb70 = models.IntegerField(db_column='AVR_NOISE_PRB70')  # Field name made lowercase.
    avr_noise_prb71 = models.IntegerField(db_column='AVR_NOISE_PRB71')  # Field name made lowercase.
    avr_noise_prb72 = models.IntegerField(db_column='AVR_NOISE_PRB72')  # Field name made lowercase.
    avr_noise_prb73 = models.IntegerField(db_column='AVR_NOISE_PRB73')  # Field name made lowercase.
    avr_noise_prb74 = models.IntegerField(db_column='AVR_NOISE_PRB74')  # Field name made lowercase.
    avr_noise_prb75 = models.IntegerField(db_column='AVR_NOISE_PRB75')  # Field name made lowercase.
    avr_noise_prb76 = models.IntegerField(db_column='AVR_NOISE_PRB76')  # Field name made lowercase.
    avr_noise_prb77 = models.IntegerField(db_column='AVR_NOISE_PRB77')  # Field name made lowercase.
    avr_noise_prb78 = models.IntegerField(db_column='AVR_NOISE_PRB78')  # Field name made lowercase.
    avr_noise_prb79 = models.IntegerField(db_column='AVR_NOISE_PRB79')  # Field name made lowercase.
    avr_noise_prb80 = models.IntegerField(db_column='AVR_NOISE_PRB80')  # Field name made lowercase.
    avr_noise_prb81 = models.IntegerField(db_column='AVR_NOISE_PRB81')  # Field name made lowercase.
    avr_noise_prb82 = models.IntegerField(db_column='AVR_NOISE_PRB82')  # Field name made lowercase.
    avr_noise_prb83 = models.IntegerField(db_column='AVR_NOISE_PRB83')  # Field name made lowercase.
    avr_noise_prb84 = models.IntegerField(db_column='AVR_NOISE_PRB84')  # Field name made lowercase.
    avr_noise_prb85 = models.IntegerField(db_column='AVR_NOISE_PRB85')  # Field name made lowercase.
    avr_noise_prb86 = models.IntegerField(db_column='AVR_NOISE_PRB86')  # Field name made lowercase.
    avr_noise_prb87 = models.IntegerField(db_column='AVR_NOISE_PRB87')  # Field name made lowercase.
    avr_noise_prb88 = models.IntegerField(db_column='AVR_NOISE_PRB88')  # Field name made lowercase.
    avr_noise_prb89 = models.IntegerField(db_column='AVR_NOISE_PRB89')  # Field name made lowercase.
    avr_noise_prb90 = models.IntegerField(db_column='AVR_NOISE_PRB90')  # Field name made lowercase.
    avr_noise_prb91 = models.IntegerField(db_column='AVR_NOISE_PRB91')  # Field name made lowercase.
    avr_noise_prb92 = models.IntegerField(db_column='AVR_NOISE_PRB92')  # Field name made lowercase.
    avr_noise_prb93 = models.IntegerField(db_column='AVR_NOISE_PRB93')  # Field name made lowercase.
    avr_noise_prb94 = models.IntegerField(db_column='AVR_NOISE_PRB94')  # Field name made lowercase.
    avr_noise_prb95 = models.IntegerField(db_column='AVR_NOISE_PRB95')  # Field name made lowercase.
    avr_noise_prb96 = models.IntegerField(db_column='AVR_NOISE_PRB96')  # Field name made lowercase.
    avr_noise_prb97 = models.IntegerField(db_column='AVR_NOISE_PRB97')  # Field name made lowercase.
    avr_noise_prb98 = models.IntegerField(db_column='AVR_NOISE_PRB98')  # Field name made lowercase.
    avr_noise_prb99 = models.IntegerField(db_column='AVR_NOISE_PRB99')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tbprbnew'


class Tbc2I(models.Model):
    city = models.CharField(db_column='CITY', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scell = models.CharField(db_column='SCELL', primary_key=True, max_length=255)  # Field name made lowercase.
    ncell = models.CharField(db_column='NCELL', max_length=255)  # Field name made lowercase.
    prc2i9 = models.FloatField(db_column='PrC2I9', blank=True, null=True)  # Field name made lowercase.
    c2i_mean = models.FloatField(db_column='C2I_Mean', blank=True, null=True)  # Field name made lowercase.
    std = models.FloatField(db_column='Std', blank=True, null=True)  # Field name made lowercase.
    samplecount = models.FloatField(db_column='SampleCount', blank=True, null=True)  # Field name made lowercase.
    weightedc2i = models.FloatField(db_column='WeightedC2I', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tbc2i'
        unique_together = (('scell', 'ncell'),)