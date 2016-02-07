from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from announcements.compat import AUTH_USER_MODEL

class Announcement(models.Model):
    """
    A single announcement.
    """
    DISMISSAL_NO = 1
    DISMISSAL_SESSION = 2
    DISMISSAL_PERMANENT = 3
    
    DISMISSAL_CHOICES = [
        (DISMISSAL_NO, _("No Dismissals Allowed")),
        (DISMISSAL_SESSION, _("Session Only Dismissal")),
        (DISMISSAL_PERMANENT, _("Permanent Dismissal Allowed"))
    ]
    
    title = models.CharField(_("title"), max_length=50)
    content = models.TextField(_("content"))
    creator = models.ForeignKey(AUTH_USER_MODEL, verbose_name=_("creator"))
    creation_date = models.DateTimeField(_("creation_date"), default=timezone.now)
    site_wide = models.BooleanField(_("site wide"), default=False)
    members_only = models.BooleanField(_("members only"), default=False)
    dismissal_type = models.IntegerField(choices=DISMISSAL_CHOICES, default=DISMISSAL_SESSION)
    publish_start = models.DateTimeField(_("publish_start"), default=timezone.now)
    publish_end = models.DateTimeField(_("publish_end"), blank=True, null=True)
    
    def get_absolute_url(self):
        return reverse("announcements_detail", args=[self.pk])
    
    def dismiss_url(self):
        if self.dismissal_type != Announcement.DISMISSAL_NO:
            return reverse("announcements_dismiss", args=[self.pk])
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        verbose_name = _("announcement")
        verbose_name_plural = _("announcements")


class Dismissal(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, related_name="announcement_dismissals")
    announcement = models.ForeignKey(Announcement, related_name="dismissals")
    dismissed_at = models.DateTimeField(default=timezone.now)
