from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
import uuid
from  django.contrib.auth.models import User 


class Ticket(models.Model):

    class Category(models.TextChoices):
        SILVER = "SR", _("Silver")
        GOLD = "GD", _("Gold")
        PLATINUM = "PM", _("Platinum")

    uuid = models.UUIDField(
        blank=False,
        null=False,
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )
    user = models.ForeignKey(
        User,
        blank=False,
        null=False,
        on_delete=models.PROTECT,
    )
    event = models.ForeignKey("Event", on_delete=models.PROTECT)
    category = models.CharField(
        max_length=2,
        blank=False,
        null=False,
        editable=False,
        choices=Category,
        default=Category.SILVER,
    )


    def __str__(self):
        return f"{self.user} - {self.event}"
