from django.db import models

# Create your models here.

class School(models.Model):
    """
    School model to host information related to school
    """
    class Meta:
        db_table = 'school'
        verbose_name_plural='School'

    school_id = models.CharField(
        verbose_name='School ID',
        primary_key=True,
        auto_created=False,
        max_length=10,
    )
    name = models.CharField(
        verbose_name='School Name',
        max_length=255,
    )
    address = models.TextField(
        verbose_name='School Address',
        max_length=300,
    )
    phone_no = models.CharField(
        verbose_name='Phone Numbers',
        max_length=255,
        null=True,
    )
    pincode = models.CharField(
        verbose_name='PINCODE',
        max_length=6,
        null=True,
    )

    no_of_compliants = models.CharField(
        verbose_name='Number of compliants',
        max_length=6,
        null=True,
    )

    def __str__(self):
        return self.name

class TotalSeats(models.Model):
    """
    Model to store total number of seats
    """
    class Meta:
        db_table = 'total_number_of_seats'
        verbose_name_plural = 'Total Seats'

    school = models.ForeignKey(School)

    PRESCHOOL = 'PRESCHOOL'
    PREPRIMARY = 'PREPRIMARY'
    CLASSONE = 'CLASSONE'

    GRADE_LEVEL = (
        (PRESCHOOL, 'Pre-school'),
        (PREPRIMARY, 'Pre-primary'),
        (CLASSONE, 'Class-1'),
    )
    grade = models.CharField(
        verbose_name='Entering Classroom',
        max_length=100,
        choices=GRADE_LEVEL,
    )

    # OPENSEATS = 'OPENSEATS'
    # EWSDGSEATS = 'EWSDGSEATS'
    # FREEQUOTASEATS = 'FREEQUOTASEATS'
    #
    # TYPE_OF_CATEGORIES = (
    #     (OPENSEATS, 'Open/General seats'),
    #     (EWSDGSEATS, 'EWS/DG seats'),
    #     (FREEQUOTASEATS, 'Free Quota seats'),
    # )

    open_seats = models.CharField(
        verbose_name='Open/General seats',
        max_length=200,
    )
    # category = models.CharField(
    #     verbose_name='Student category',
    #     max_length=100,
    #     choices=TYPE_OF_CATEGORIES,
    # )

    ews_dg_seats = models.CharField(
        verbose_name='EWS/DG seats',
        max_length=200,
    )

    free_quota_seats = models.CharField(
        verbose_name='Free Quota seats',
        max_length=200,
    )

    def __str__(self):
        return 'Total Number of Seats'

class AdmissionGiven(models.Model):
    """
    Model to store total number of seats for which admission is given
    """
    class Meta:
        db_table = 'admission_given'
        verbose_name_plural = 'Admissions given'

    school = models.ForeignKey(School)

    PRESCHOOL = 'PRESCHOOL'
    PREPRIMARY = 'PREPRIMARY'
    CLASSONE = 'CLASSONE'

    GRADE_LEVEL = (
        (PRESCHOOL, 'Pre-school'),
        (PREPRIMARY, 'Pre-primary'),
        (CLASSONE, 'Class-1'),
    )
    grade = models.CharField(
        verbose_name='Entering Classroom',
        max_length=100,
        choices=GRADE_LEVEL,
    )

    # OPENSEATS = 'OPENSEATS'
    # EWSDGSEATS = 'EWSDGSEATS'
    # FREEQUOTASEATS = 'FREEQUOTASEATS'
    #
    # TYPE_OF_CATEGORIES = (
    #     (OPENSEATS, 'Open/General seats'),
    #     (EWSDGSEATS, 'EWS/DG seats'),
    #     (FREEQUOTASEATS, 'Free Quota seats'),
    # )

    open_seats = models.CharField(
        verbose_name='Open/General seats',
        max_length=200,
    )
    # category = models.CharField(
    #     verbose_name='Student category',
    #     max_length=100,
    #     choices=TYPE_OF_CATEGORIES,
    # )

    ews_dg_seats = models.CharField(
        verbose_name='EWS/DG seats',
        max_length=200,
    )

    free_quota_seats = models.CharField(
        verbose_name='Free Quota seats',
        max_length=200,
    )

    def __str__(self):
        return 'Admission given/enrollment'

class VacantSeats(models.Model):
    """
    Model to store total number of vacant seats
    """
    class Meta:
        db_table = 'vacant_seats'
        verbose_name_plural = 'Vacant seats'

    school = models.ForeignKey(School)

    PRESCHOOL = 'PRESCHOOL'
    PREPRIMARY = 'PREPRIMARY'
    CLASSONE = 'CLASSONE'

    GRADE_LEVEL = (
        (PRESCHOOL, 'Pre-school'),
        (PREPRIMARY, 'Pre-primary'),
        (CLASSONE, 'Class-1'),
    )
    grade = models.CharField(
        verbose_name='Entering Classroom',
        max_length=100,
        choices=GRADE_LEVEL,
    )

    # OPENSEATS = 'OPENSEATS'
    # EWSDGSEATS = 'EWSDGSEATS'
    # FREEQUOTASEATS = 'FREEQUOTASEATS'
    #
    # TYPE_OF_CATEGORIES = (
    #     (OPENSEATS, 'Open/General seats'),
    #     (EWSDGSEATS, 'EWS/DG seats'),
    #     (FREEQUOTASEATS, 'Free Quota seats'),
    # )

    open_seats = models.CharField(
        verbose_name='Open/General seats',
        max_length=200,
    )
    # category = models.CharField(
    #     verbose_name='Student category',
    #     max_length=100,
    #     choices=TYPE_OF_CATEGORIES,
    # )

    ews_dg_seats = models.CharField(
        verbose_name='EWS/DG seats',
        max_length=200,
    )

    free_quota_seats = models.CharField(
        verbose_name='Free Quota seats',
        max_length=200,
    )

    def __str__(self):
        return 'Total Number of Vacant Seats'

class ApplicationsReceived(models.Model):
    """
    Model to store total number of seats
    """
    class Meta:
        db_table = 'applications_received'
        verbose_name_plural = 'Applications received'

    school = models.ForeignKey(School)

    PRESCHOOL = 'PRESCHOOL'
    PREPRIMARY = 'PREPRIMARY'
    CLASSONE = 'CLASSONE'

    GRADE_LEVEL = (
        (PRESCHOOL, 'Pre-school'),
        (PREPRIMARY, 'Pre-primary'),
        (CLASSONE, 'Class-1'),
    )
    grade = models.CharField(
        verbose_name='Entering Classroom',
        max_length=100,
        choices=GRADE_LEVEL,
    )

    # OPENSEATS = 'OPENSEATS'
    # EWSDGSEATS = 'EWSDGSEATS'
    # FREEQUOTASEATS = 'FREEQUOTASEATS'
    #
    # TYPE_OF_CATEGORIES = (
    #     (OPENSEATS, 'Open/General seats'),
    #     (EWSDGSEATS, 'EWS/DG seats'),
    #     (FREEQUOTASEATS, 'Free Quota seats'),
    # )

    open_seats = models.CharField(
        verbose_name='Open/General seats',
        max_length=200,
    )
    # category = models.CharField(
    #     verbose_name='Student category',
    #     max_length=100,
    #     choices=TYPE_OF_CATEGORIES,
    # )

    ews_dg_seats = models.CharField(
        verbose_name='EWS/DG seats',
        max_length=200,
    )

    free_quota_seats = models.CharField(
        verbose_name='Free Quota seats',
        max_length=200,
    )

    def __str__(self):
        return 'Total Number of Applications received'

# class EWSSeatsInfo(models.Model):
#     """
#     Model to in house EWS seats information
#     """
#     class Meta:
#         db_table = 'ews-seats-info'
#
#     school = models.ForeignKey(School)
#
#     PRESCHOOL = 'PRESCHOOL'
#     PREPRIMARY = 'PREPRIMARY'
#     CLASSONE = 'CLASSONE'
#
#     GRADE_LEVEL = (
#         (PREPRIMARY, 'Pre-school'),
#         (PREPRIMARY, 'Pre-primary'),
#         (CLASSONE, 'Class-1'),
#     )
#     grade = models.CharField(
#         verbose_name='Entering Classroom',
#         max_length=100,
#         choices=GRADE_LEVEL,
#     )
#
#     OPENSEATS = 'OPENSEATS'
#     EWSDGSEATS = 'EWSDGSEATS'
#     FREEQUOTASEATS = 'FREEQUOTASEATS'
#
#     TYPE_OF_CATEGORIES = (
#         (OPENSEATS, 'Open/General seats'),
#         (EWSDGSEATS, 'EWS/DG seats'),
#         (FREEQUOTASEATS, 'Free Quota seats'),
#     )
#
#     category = models.CharField(
#         verbose_name='Student category',
#         max_length=100,
#         choices=TYPE_OF_CATEGORIES,
#     )
#
#     no_of_seats = models.IntegerField(verbose_name='Number of seats')
#
#
#     TOTALSEATS = 'TOTALSEATS'
#     ADMGIVEN  = 'ADMGIVEN'
#     VACANTSEATS = 'VACANTSEATS'
#     APPLICATIONSRECEIVED = 'APPLICATIONSRCVD'
#
#     SEAT_GROUP = (
#         (TOTALSEATS, 'Total number of seats'),
#         (ADMGIVEN, 'Admission given/Enrollment'),
#         (VACANTSEATS, 'Seats still vacant'),
#         (APPLICATIONSRECEIVED, 'Number of applications received'),
#     )
#
#     seat_group = models.CharField(
#         verbose_name='Seat groups',
#         max_length=100,
#         choices=SEAT_GROUP,
#     )
#





