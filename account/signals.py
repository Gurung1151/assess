from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import teacherProfile,Teacher

# @receiver(post_save,sender=teacherProfile)
# def profileUpdated(sender,instance,created,**kwargs):
#     print('Profile Saved!')
#     print('Instance:',instance)
#     print('created:',created)


def createProfile(sender,instance,created,**kwargs):
   print('signal triggered')
   if created:
       user=instance
       profile = teacherProfile.objects.create(
           user=user,
           username = user.user.username,
           email = user.user.email,
       )

    # print('Profile Saved!')
    # print('Instance:',instance)
    # print('created:',created)

def updateProfile(sender,instance,created,**kwargs):
    profile = instance
    user = profile.user.user
    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()



def deleteProfile(sender,instance,**kwargs):
    user = instance.user
    user.delete()
    print('deleting user...')

post_save.connect(createProfile,sender=Teacher)
post_save.connect(updateProfile,sender=teacherProfile)
post_delete.connect(deleteProfile,sender=teacherProfile)