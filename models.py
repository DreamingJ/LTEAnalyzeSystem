# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class LoginAdmin(models.Model):
    name = models.CharField(unique=True, max_length=128)
    password = models.CharField(max_length=256)
    dbpassword = models.CharField(max_length=256)
    c_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'login_admin'


class LoginUser(models.Model):
    name = models.CharField(unique=True, max_length=128)
    password = models.CharField(max_length=256)
    c_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'login_user'


class LoginVariable(models.Model):
    variable_name = models.CharField(db_column='Variable_name', primary_key=True, max_length=128)  # Field name made lowercase.
    value = models.IntegerField(db_column='Value')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'login_variable'


class Tbc2Inew(models.Model):
    nc_sector_id = models.CharField(db_column='NC_SECTOR_ID', max_length=50)  # Field name made lowercase.
    sc_sector_id = models.CharField(db_column='SC_SECTOR_ID', max_length=50)  # Field name made lowercase.
    rsrp_avg = models.FloatField(db_column='RSRP_AVG')  # Field name made lowercase.
    rsrp_std = models.FloatField(db_column='RSRP_STD')  # Field name made lowercase.
    probility_9 = models.FloatField(db_column='PROBILITY_9')  # Field name made lowercase.
    probility_6 = models.FloatField(db_column='PROBILITY_6')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbC2Inew'


class Tbadjcell(models.Model):
    s_sector = models.OneToOneField('Tbcellcopy', models.DO_NOTHING, db_column='S_SECTOR_ID', primary_key=True)  # Field name made lowercase.
    n_sector_id = models.CharField(db_column='N_SECTOR_ID', max_length=50)  # Field name made lowercase.
    s_earfcn = models.IntegerField(db_column='S_EARFCN', blank=True, null=True)  # Field name made lowercase.
    n_earfcn = models.IntegerField(db_column='N_EARFCN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbadjcell'
        unique_together = (('s_sector', 'n_sector_id'),)


class Tbatuc2I(models.Model):
    sector_id = models.CharField(db_column='SECTOR_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    ncell_id = models.CharField(db_column='NCELL_ID', max_length=50)  # Field name made lowercase.
    ratio_all = models.FloatField(db_column='RATIO_ALL', blank=True, null=True)  # Field name made lowercase.
    rank = models.IntegerField(db_column='RANK', blank=True, null=True)  # Field name made lowercase.
    cosite = models.PositiveIntegerField(db_column='COSITE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbatuc2i'
        unique_together = (('sector_id', 'ncell_id'),)


class Tbatudata(models.Model):
    seq = models.BigIntegerField(primary_key=True)
    filename = models.CharField(db_column='FileName', max_length=255)  # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=100, blank=True, null=True)  # Field name made lowercase.
    longitude = models.FloatField(db_column='Longitude', blank=True, null=True)  # Field name made lowercase.
    latitude = models.FloatField(db_column='Latitude', blank=True, null=True)  # Field name made lowercase.
    cellid = models.CharField(db_column='CellID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tac = models.IntegerField(db_column='TAC', blank=True, null=True)  # Field name made lowercase.
    earfcn = models.IntegerField(db_column='EARFCN', blank=True, null=True)  # Field name made lowercase.
    pci = models.SmallIntegerField(db_column='PCI', blank=True, null=True)  # Field name made lowercase.
    rsrp = models.FloatField(db_column='RSRP', blank=True, null=True)  # Field name made lowercase.
    rs_sinr = models.FloatField(db_column='RS_SINR', blank=True, null=True)  # Field name made lowercase.
    ncell_id_1 = models.CharField(db_column='NCell_ID_1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ncell_earfcn_1 = models.IntegerField(db_column='NCell_EARFCN_1', blank=True, null=True)  # Field name made lowercase.
    ncell_pci_1 = models.SmallIntegerField(db_column='NCell_PCI_1', blank=True, null=True)  # Field name made lowercase.
    ncell_rsrp_1 = models.FloatField(db_column='NCell_RSRP_1', blank=True, null=True)  # Field name made lowercase.
    ncell_id_2 = models.CharField(db_column='NCell_ID_2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ncell_earfcn_2 = models.IntegerField(db_column='NCell_EARFCN_2', blank=True, null=True)  # Field name made lowercase.
    ncell_pci_2 = models.SmallIntegerField(db_column='NCell_PCI_2', blank=True, null=True)  # Field name made lowercase.
    ncell_rsrp_2 = models.FloatField(db_column='NCell_RSRP_2', blank=True, null=True)  # Field name made lowercase.
    ncell_id_3 = models.CharField(db_column='NCell_ID_3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ncell_earfcn_3 = models.IntegerField(db_column='NCell_EARFCN_3', blank=True, null=True)  # Field name made lowercase.
    ncell_pci_3 = models.SmallIntegerField(db_column='NCell_PCI_3', blank=True, null=True)  # Field name made lowercase.
    ncell_rsrp_3 = models.FloatField(db_column='NCell_RSRP_3', blank=True, null=True)  # Field name made lowercase.
    ncell_id_4 = models.CharField(db_column='NCell_ID_4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ncell_earfcn_4 = models.IntegerField(db_column='NCell_EARFCN_4', blank=True, null=True)  # Field name made lowercase.
    ncell_pci_4 = models.SmallIntegerField(db_column='NCell_PCI_4', blank=True, null=True)  # Field name made lowercase.
    ncell_rsrp_4 = models.FloatField(db_column='NCell_RSRP_4', blank=True, null=True)  # Field name made lowercase.
    ncell_id_5 = models.CharField(db_column='NCell_ID_5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ncell_earfcn_5 = models.IntegerField(db_column='NCell_EARFCN_5', blank=True, null=True)  # Field name made lowercase.
    ncell_pci_5 = models.SmallIntegerField(db_column='NCell_PCI_5', blank=True, null=True)  # Field name made lowercase.
    ncell_rsrp_5 = models.FloatField(db_column='NCell_RSRP_5', blank=True, null=True)  # Field name made lowercase.
    ncell_id_6 = models.CharField(db_column='NCell_ID_6', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ncell_earfcn_6 = models.IntegerField(db_column='NCell_EARFCN_6', blank=True, null=True)  # Field name made lowercase.
    ncell_pci_6 = models.SmallIntegerField(db_column='NCell_PCI_6', blank=True, null=True)  # Field name made lowercase.
    ncell_rsrp_6 = models.FloatField(db_column='NCell_RSRP_6', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbatudata'
        unique_together = (('seq', 'filename'),)


class Tbatuhandover(models.Model):
    ssector_id = models.CharField(db_column='SSECTOR_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    nsector_id = models.CharField(db_column='NSECTOR_ID', max_length=50)  # Field name made lowercase.
    hoatt = models.IntegerField(db_column='HOATT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbatuhandover'
        unique_together = (('ssector_id', 'nsector_id'),)


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
        managed = False
        db_table = 'tbc2i'
        unique_together = (('scell', 'ncell'),)


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
        managed = False
        db_table = 'tbcell'


class TbcellTraffic(models.Model):
    stadate = models.DateField(db_column='STADATE', primary_key=True)  # Field name made lowercase.
    statime = models.SmallIntegerField(db_column='STATIME')  # Field name made lowercase.
    sectorid = models.CharField(db_column='SECTORID', max_length=255)  # Field name made lowercase.
    celltraffic = models.FloatField(db_column='CellTraffic', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbcell_traffic'
        unique_together = (('stadate', 'statime', 'sectorid'),)


class Tbcellcopy(models.Model):
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
        managed = False
        db_table = 'tbcellcopy'


class Tbhandover(models.Model):
    city = models.CharField(db_column='CITY', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scell = models.CharField(db_column='SCELL', primary_key=True, max_length=50)  # Field name made lowercase.
    ncell = models.CharField(db_column='NCELL', max_length=50)  # Field name made lowercase.
    hoatt = models.PositiveIntegerField(db_column='HOATT', blank=True, null=True)  # Field name made lowercase.
    hosucc = models.PositiveIntegerField(db_column='HOSUCC', blank=True, null=True)  # Field name made lowercase.
    hosuccrate = models.FloatField(db_column='HOSUCCRATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbhandover'
        unique_together = (('scell', 'ncell'),)


class Tbkpi(models.Model):
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    enodeb_name = models.CharField(db_column='ENODEB_NAME', max_length=255)  # Field name made lowercase.
    sector = models.CharField(db_column='SECTOR', max_length=255)  # Field name made lowercase.
    sector_name = models.CharField(db_column='SECTOR_NAME', primary_key=True, max_length=255)  # Field name made lowercase.
    rpc_establish = models.IntegerField(db_column='RPC_ESTABLISH', blank=True, null=True)  # Field name made lowercase.
    rpc_request = models.IntegerField(db_column='RPC_REQUEST', blank=True, null=True)  # Field name made lowercase.
    rpc_succrate = models.FloatField(db_column='RPC_SUCCRATE', blank=True, null=True)  # Field name made lowercase.
    erab_succ = models.IntegerField(db_column='ERAB_SUCC', blank=True, null=True)  # Field name made lowercase.
    erab_att = models.IntegerField(db_column='ERAB_ATT', blank=True, null=True)  # Field name made lowercase.
    erab_succrate = models.FloatField(db_column='ERAB_SUCCRATE', blank=True, null=True)  # Field name made lowercase.
    enodeb_erab_ex = models.IntegerField(db_column='ENODEB_ERAB_EX', blank=True, null=True)  # Field name made lowercase.
    sector_switch_erab_ex = models.IntegerField(db_column='SECTOR_SWITCH_ERAB_EX', blank=True, null=True)  # Field name made lowercase.
    erab_lossrate = models.FloatField(db_column='ERAB_LOSSRATE', blank=True, null=True)  # Field name made lowercase.
    ay = models.FloatField(db_column='AY', blank=True, null=True)  # Field name made lowercase.
    enodeb_reset_ue_release = models.IntegerField(db_column='ENODEB_RESET_UE_RELEASE', blank=True, null=True)  # Field name made lowercase.
    ue_ex_release = models.IntegerField(db_column='UE_EX_RELEASE', blank=True, null=True)  # Field name made lowercase.
    ue_succ = models.IntegerField(db_column='UE_SUCC', blank=True, null=True)  # Field name made lowercase.
    lossrate = models.FloatField(db_column='LOSSRATE', blank=True, null=True)  # Field name made lowercase.
    enodeb_in_diff_succ = models.IntegerField(db_column='ENODEB_IN_DIFF_SUCC', blank=True, null=True)  # Field name made lowercase.
    enodeb_in_diff_att = models.IntegerField(db_column='ENODEB_IN_DIFF_ATT', blank=True, null=True)  # Field name made lowercase.
    enodeb_in_same_succ = models.IntegerField(db_column='ENODEB_IN_SAME_SUCC', blank=True, null=True)  # Field name made lowercase.
    enodeb_in_same_att = models.IntegerField(db_column='ENODEB_IN_SAME_ATT', blank=True, null=True)  # Field name made lowercase.
    enodeb_out_diff_succ = models.IntegerField(db_column='ENODEB_OUT_DIFF_SUCC', blank=True, null=True)  # Field name made lowercase.
    enodeb_out_diff_att = models.IntegerField(db_column='ENODEB_OUT_DIFF_ATT', blank=True, null=True)  # Field name made lowercase.
    enodeb_out_same_succ = models.IntegerField(db_column='ENODEB_OUT_SAME_SUCC', blank=True, null=True)  # Field name made lowercase.
    enodeb_out_same_att = models.IntegerField(db_column='ENODEB_OUT_SAME_ATT', blank=True, null=True)  # Field name made lowercase.
    enodeb_in_succrate = models.FloatField(db_column='ENODEB_IN_SUCCRATE', blank=True, null=True)  # Field name made lowercase.
    enodeb_out_succrate = models.FloatField(db_column='ENODEB_OUT_SUCCRATE', blank=True, null=True)  # Field name made lowercase.
    enodeb_same_succrate = models.FloatField(db_column='ENODEB_SAME_SUCCRATE', blank=True, null=True)  # Field name made lowercase.
    enodeb_diff_succrate = models.FloatField(db_column='ENODEB_DIFF_SUCCRATE', blank=True, null=True)  # Field name made lowercase.
    enodeb_switch_succrate = models.FloatField(db_column='ENODEB_SWITCH_SUCCRATE', blank=True, null=True)  # Field name made lowercase.
    pdcp_up = models.BigIntegerField(db_column='PDCP_UP', blank=True, null=True)  # Field name made lowercase.
    pdcp_down = models.BigIntegerField(db_column='PDCP_DOWN', blank=True, null=True)  # Field name made lowercase.
    rpc_rebuild = models.IntegerField(db_column='RPC_REBUILD', blank=True, null=True)  # Field name made lowercase.
    rpc_rebuildrate = models.FloatField(db_column='RPC_REBUILDRATE', blank=True, null=True)  # Field name made lowercase.
    rebuild_enodeb_out_same_succ = models.IntegerField(db_column='REBUILD_ENODEB_OUT_SAME_SUCC', blank=True, null=True)  # Field name made lowercase.
    rebuild_enodeb_out_diff_succ = models.IntegerField(db_column='REBUILD_ENODEB_OUT_DIFF_SUCC', blank=True, null=True)  # Field name made lowercase.
    rebuild_enodeb_in_same_succ = models.IntegerField(db_column='REBUILD_ENODEB_IN_SAME_SUCC', blank=True, null=True)  # Field name made lowercase.
    rebuild_enodeb_in_diff_succ = models.IntegerField(db_column='REBUILD_ENODEB_IN_DIFF_SUCC', blank=True, null=True)  # Field name made lowercase.
    enb_in_succ = models.IntegerField(db_column='ENB_IN_SUCC', blank=True, null=True)  # Field name made lowercase.
    eno_in_request = models.IntegerField(db_column='ENO_IN_REQUEST', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbkpi'
        unique_together = (('sector_name', 'date'),)


class Tbmrodata(models.Model):
    timestamp = models.CharField(db_column='TimeStamp', max_length=30)  # Field name made lowercase.
    servingsector = models.CharField(db_column='ServingSector', max_length=30)  # Field name made lowercase.
    interferingsector = models.CharField(db_column='InterferingSector', max_length=30)  # Field name made lowercase.
    ltescrsrp = models.FloatField(db_column='LteScRSRP', blank=True, null=True)  # Field name made lowercase.
    ltencrsrp = models.FloatField(db_column='LteNcRSRP', blank=True, null=True)  # Field name made lowercase.
    ltencearfcn = models.IntegerField(db_column='LteNcEarfcn', blank=True, null=True)  # Field name made lowercase.
    ltencpci = models.PositiveSmallIntegerField(db_column='LteNcPci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbmrodata'


class Tboptcell(models.Model):
    sector_id = models.CharField(db_column='SECTOR_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    earfcn = models.IntegerField(db_column='EARFCN', blank=True, null=True)  # Field name made lowercase.
    cell_type = models.CharField(db_column='CELL_TYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tboptcell'


class Tbpciassignment(models.Model):
    assign_id = models.PositiveSmallIntegerField(db_column='ASSIGN_ID', primary_key=True)  # Field name made lowercase.
    earfcn = models.IntegerField(db_column='EARFCN', blank=True, null=True)  # Field name made lowercase.
    sector_id = models.CharField(db_column='SECTOR_ID', max_length=32)  # Field name made lowercase.
    sector_name = models.CharField(db_column='SECTOR_NAME', max_length=32, blank=True, null=True)  # Field name made lowercase.
    enodeb_id = models.IntegerField(db_column='ENODEB_ID', blank=True, null=True)  # Field name made lowercase.
    pci = models.IntegerField(db_column='PCI', blank=True, null=True)  # Field name made lowercase.
    pss = models.IntegerField(db_column='PSS', blank=True, null=True)  # Field name made lowercase.
    sss = models.IntegerField(db_column='SSS', blank=True, null=True)  # Field name made lowercase.
    longitude = models.FloatField(db_column='LONGITUDE', blank=True, null=True)  # Field name made lowercase.
    latitude = models.FloatField(db_column='LATITUDE', blank=True, null=True)  # Field name made lowercase.
    style = models.CharField(db_column='STYLE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    opt_datetime = models.DateTimeField(db_column='OPT_DATETIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbpciassignment'
        unique_together = (('assign_id', 'sector_id'),)


class Tbprb(models.Model):
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    enodeb_name = models.CharField(db_column='ENODEB_NAME', max_length=255)  # Field name made lowercase.
    sector_description = models.CharField(db_column='SECTOR_DESCRIPTION', max_length=255)  # Field name made lowercase.
    sector_name = models.CharField(db_column='SECTOR_NAME', primary_key=True, max_length=255)  # Field name made lowercase.
    avr_noise_prb0 = models.IntegerField(db_column='AVR_NOISE_PRB0', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb1 = models.IntegerField(db_column='AVR_NOISE_PRB1', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb2 = models.IntegerField(db_column='AVR_NOISE_PRB2', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb3 = models.IntegerField(db_column='AVR_NOISE_PRB3', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb4 = models.IntegerField(db_column='AVR_NOISE_PRB4', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb5 = models.IntegerField(db_column='AVR_NOISE_PRB5', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb6 = models.IntegerField(db_column='AVR_NOISE_PRB6', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb7 = models.IntegerField(db_column='AVR_NOISE_PRB7', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb8 = models.IntegerField(db_column='AVR_NOISE_PRB8', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb9 = models.IntegerField(db_column='AVR_NOISE_PRB9', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb10 = models.IntegerField(db_column='AVR_NOISE_PRB10', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb11 = models.IntegerField(db_column='AVR_NOISE_PRB11', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb12 = models.IntegerField(db_column='AVR_NOISE_PRB12', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb13 = models.IntegerField(db_column='AVR_NOISE_PRB13', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb14 = models.IntegerField(db_column='AVR_NOISE_PRB14', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb15 = models.IntegerField(db_column='AVR_NOISE_PRB15', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb16 = models.IntegerField(db_column='AVR_NOISE_PRB16', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb17 = models.IntegerField(db_column='AVR_NOISE_PRB17', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb18 = models.IntegerField(db_column='AVR_NOISE_PRB18', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb19 = models.IntegerField(db_column='AVR_NOISE_PRB19', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb20 = models.IntegerField(db_column='AVR_NOISE_PRB20', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb21 = models.IntegerField(db_column='AVR_NOISE_PRB21', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb22 = models.IntegerField(db_column='AVR_NOISE_PRB22', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb23 = models.IntegerField(db_column='AVR_NOISE_PRB23', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb24 = models.IntegerField(db_column='AVR_NOISE_PRB24', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb25 = models.IntegerField(db_column='AVR_NOISE_PRB25', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb26 = models.IntegerField(db_column='AVR_NOISE_PRB26', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb27 = models.IntegerField(db_column='AVR_NOISE_PRB27', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb28 = models.IntegerField(db_column='AVR_NOISE_PRB28', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb29 = models.IntegerField(db_column='AVR_NOISE_PRB29', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb30 = models.IntegerField(db_column='AVR_NOISE_PRB30', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb31 = models.IntegerField(db_column='AVR_NOISE_PRB31', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb32 = models.IntegerField(db_column='AVR_NOISE_PRB32', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb33 = models.IntegerField(db_column='AVR_NOISE_PRB33', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb34 = models.IntegerField(db_column='AVR_NOISE_PRB34', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb35 = models.IntegerField(db_column='AVR_NOISE_PRB35', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb36 = models.IntegerField(db_column='AVR_NOISE_PRB36', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb37 = models.IntegerField(db_column='AVR_NOISE_PRB37', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb38 = models.IntegerField(db_column='AVR_NOISE_PRB38', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb39 = models.IntegerField(db_column='AVR_NOISE_PRB39', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb40 = models.IntegerField(db_column='AVR_NOISE_PRB40', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb41 = models.IntegerField(db_column='AVR_NOISE_PRB41', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb42 = models.IntegerField(db_column='AVR_NOISE_PRB42', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb43 = models.IntegerField(db_column='AVR_NOISE_PRB43', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb44 = models.IntegerField(db_column='AVR_NOISE_PRB44', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb45 = models.IntegerField(db_column='AVR_NOISE_PRB45', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb46 = models.IntegerField(db_column='AVR_NOISE_PRB46', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb47 = models.IntegerField(db_column='AVR_NOISE_PRB47', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb48 = models.IntegerField(db_column='AVR_NOISE_PRB48', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb49 = models.IntegerField(db_column='AVR_NOISE_PRB49', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb50 = models.IntegerField(db_column='AVR_NOISE_PRB50', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb51 = models.IntegerField(db_column='AVR_NOISE_PRB51', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb52 = models.IntegerField(db_column='AVR_NOISE_PRB52', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb53 = models.IntegerField(db_column='AVR_NOISE_PRB53', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb54 = models.IntegerField(db_column='AVR_NOISE_PRB54', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb55 = models.IntegerField(db_column='AVR_NOISE_PRB55', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb56 = models.IntegerField(db_column='AVR_NOISE_PRB56', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb57 = models.IntegerField(db_column='AVR_NOISE_PRB57', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb58 = models.IntegerField(db_column='AVR_NOISE_PRB58', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb59 = models.IntegerField(db_column='AVR_NOISE_PRB59', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb60 = models.IntegerField(db_column='AVR_NOISE_PRB60', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb61 = models.IntegerField(db_column='AVR_NOISE_PRB61', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb62 = models.IntegerField(db_column='AVR_NOISE_PRB62', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb63 = models.IntegerField(db_column='AVR_NOISE_PRB63', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb64 = models.IntegerField(db_column='AVR_NOISE_PRB64', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb65 = models.IntegerField(db_column='AVR_NOISE_PRB65', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb66 = models.IntegerField(db_column='AVR_NOISE_PRB66', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb67 = models.IntegerField(db_column='AVR_NOISE_PRB67', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb68 = models.IntegerField(db_column='AVR_NOISE_PRB68', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb69 = models.IntegerField(db_column='AVR_NOISE_PRB69', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb70 = models.IntegerField(db_column='AVR_NOISE_PRB70', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb71 = models.IntegerField(db_column='AVR_NOISE_PRB71', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb72 = models.IntegerField(db_column='AVR_NOISE_PRB72', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb73 = models.IntegerField(db_column='AVR_NOISE_PRB73', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb74 = models.IntegerField(db_column='AVR_NOISE_PRB74', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb75 = models.IntegerField(db_column='AVR_NOISE_PRB75', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb76 = models.IntegerField(db_column='AVR_NOISE_PRB76', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb77 = models.IntegerField(db_column='AVR_NOISE_PRB77', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb78 = models.IntegerField(db_column='AVR_NOISE_PRB78', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb79 = models.IntegerField(db_column='AVR_NOISE_PRB79', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb80 = models.IntegerField(db_column='AVR_NOISE_PRB80', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb81 = models.IntegerField(db_column='AVR_NOISE_PRB81', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb82 = models.IntegerField(db_column='AVR_NOISE_PRB82', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb83 = models.IntegerField(db_column='AVR_NOISE_PRB83', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb84 = models.IntegerField(db_column='AVR_NOISE_PRB84', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb85 = models.IntegerField(db_column='AVR_NOISE_PRB85', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb86 = models.IntegerField(db_column='AVR_NOISE_PRB86', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb87 = models.IntegerField(db_column='AVR_NOISE_PRB87', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb88 = models.IntegerField(db_column='AVR_NOISE_PRB88', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb89 = models.IntegerField(db_column='AVR_NOISE_PRB89', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb90 = models.IntegerField(db_column='AVR_NOISE_PRB90', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb91 = models.IntegerField(db_column='AVR_NOISE_PRB91', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb92 = models.IntegerField(db_column='AVR_NOISE_PRB92', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb93 = models.IntegerField(db_column='AVR_NOISE_PRB93', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb94 = models.IntegerField(db_column='AVR_NOISE_PRB94', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb95 = models.IntegerField(db_column='AVR_NOISE_PRB95', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb96 = models.IntegerField(db_column='AVR_NOISE_PRB96', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb97 = models.IntegerField(db_column='AVR_NOISE_PRB97', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb98 = models.IntegerField(db_column='AVR_NOISE_PRB98', blank=True, null=True)  # Field name made lowercase.
    avr_noise_prb99 = models.IntegerField(db_column='AVR_NOISE_PRB99', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbprb'
        unique_together = (('sector_name', 'date'),)


class Tbsecadjcell(models.Model):
    s_sector_id = models.CharField(db_column='S_SECTOR_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    n_sector_id = models.CharField(db_column='N_SECTOR_ID', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbsecadjcell'
        unique_together = (('s_sector_id', 'n_sector_id'),)
