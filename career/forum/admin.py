from django.contrib import admin
from .models import Forum_table,Transaction,Donation,Mentor,Primemember,Feedback,transcatid,Demo

class forum_tab(admin.ModelAdmin):
    list_display = ['question','email','answer','answer_set']

class Donor(admin.ModelAdmin):
    list_display = ['Name','Email','Date','Amount','Mobileno']

class mentor(admin.ModelAdmin):
    list_display = ['Name','Email','Mobileno','Profession','Mentor_Img']

class Transcation_data(admin.ModelAdmin):
    list_display = ['made_by','made_on','amount','order_id']

class prime(admin.ModelAdmin):
    list_display = ['Name','Email','Mobileno','Plan']

class feedback(admin.ModelAdmin):
    list_display = ['Name','Query']

class imp(admin.ModelAdmin):
    list_display = ['order_id','transcation_id']

class demo(admin.ModelAdmin):
    list_display = ['Name','Email','Mobileno']

admin.site.register(Forum_table,forum_tab)
admin.site.register(Donation,Donor)
admin.site.register(Mentor,mentor)
admin.site.register(Transaction,Transcation_data)
admin.site.register(Primemember,prime)
admin.site.register(Feedback,feedback)
admin.site.register(transcatid,imp)
admin.site.register(Demo,demo)
