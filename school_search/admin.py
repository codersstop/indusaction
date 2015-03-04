from django.contrib import admin
from .models import School, TotalSeats, AdmissionGiven, VacantSeats, ApplicationsReceived


# class EWSSeatsInfoInline(admin.TabularInline):
#     model = EWSSeatsInfo
#     extra = 12
#     # fieldsets = (
#     #     ('Student Category', {'fields':['category']}),
#     #     ('No. of seats', {'fields':['no_of_seats']}),
#     # )

class TotalSeatsInline(admin.TabularInline):
    model = TotalSeats
    max_num = 3

class AdmissionGivenInline(admin.TabularInline):
    model = AdmissionGiven
    max_num = 3

class VacantSeatsInline(admin.TabularInline):
    model = VacantSeats
    max_num = 3

class ApplicationReceivedInline(admin.TabularInline):
    model = ApplicationsReceived
    max_num = 3


class SchoolAdmin(admin.ModelAdmin):
    readonly_fields = ('school_id',)
    fieldsets = [
        (None, {'fields':[('school_id', 'name')]}),
        ('Address', {'fields':[('address', 'pincode')]}),
        ('Contact', {'fields': ['phone_no'], 'classes': ('wide', 'extrapretty'),}),
        ('Compliants', {'fields': ['no_of_compliants'], 'classes': ('wide', 'extrapretty')}),
    ]

    # inlines = [EWSSeatsInfoInline]
    inlines = [TotalSeatsInline,AdmissionGivenInline,VacantSeatsInline,ApplicationReceivedInline,]
    list_display = ('name', 'address', 'phone_no','pincode')
    search_fields = ['name']

admin.site.register(School, SchoolAdmin)

# Register your models here.
