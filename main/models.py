from django.db import models
from django.utils.translation import gettext_lazy as _


class Album(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    cover = models.ImageField(_("Cover"), upload_to='albums/%Y/%m', blank=True, null=True)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)

    class Meta:
        verbose_name = _("Album")
        verbose_name_plural = _("Albums")

    def __str__(self):
        return self.name


class Singer(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    birthdate = models.DateField(_("Birth date"), blank=True, null=True)
    country = models.CharField(_("Country"), max_length=100, blank=True, null=True)
    albums = models.ManyToManyField(Album, verbose_name=_("Albums"), blank=True)

    class Meta:
        verbose_name = _("Singer")
        verbose_name_plural = _("Singers")

    def __str__(self):
        return self.name


class Song(models.Model):

    genre_choices = (
        ('pop', _('Pop')),
        ('rock', _('Rock')),
        ('classic', _('Classic')),
    )

    name = models.CharField(_("Name"), max_length=100)
    genre = models.CharField(_("Genre"), choices=genre_choices, max_length=100)
    duration = models.DurationField(_("Duration"))
    file = models.FileField(_("File"), upload_to='songs/%Y/%m', blank=True, null=True)
    singer = models.ForeignKey(
        Singer,
        verbose_name=_("Singer"),
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    album = models.ForeignKey(
        Album,
        verbose_name=_("Album"),
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _("Song")
        verbose_name_plural = _("Songs")

    def __str__(self):
        return f"{self.name} - {self.singer}"