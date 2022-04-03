from django import template

from instagramUser.models import Profile, Following


register = template.Library()

@register.inclusion_tag('who_is_follow.html')
def show_follow(**df):
    profile = Profile.objects.all()
    print(df)
    # k=0
    # while k!=4:
    #     follow_status = Following.objects.filter(following=prof, follower=request.user).exists()

    return {'profile':profile}
