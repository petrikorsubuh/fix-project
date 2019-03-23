from django.contrib import admin
# from django.contrib.auth.models import User as user
from apps.account.models import Account
# from apps.authentication.models import 
# from apps.build.models import
from apps.caleg.models import Caleg
from apps.dapil.models import Dapil
from apps.kategori.models import KategoriCaleg
from apps.partai.models import Partai
from apps.suara.models import Suara
from apps.tps.models import Tps
# Register your models here.


# admin.site.register(user)
admin.site.register(Account)
admin.site.register(Caleg)
admin.site.register(Dapil)
admin.site.register(KategoriCaleg)
admin.site.register(Partai)
admin.site.register(Suara)
admin.site.register(Tps)

