from django.contrib import admin
from .models import Projecten, Projectko, ProCommenten, ProCommentko, ProTagko, ProTagen

admin.site.register(Projecten)
admin.site.register(Projectko)
admin.site.register(ProCommenten)
admin.site.register(ProCommentko)
admin.site.register(ProTagko)
admin.site.register(ProTagen)
