from django.db import models

class Location(models.Model):
    LOCATION = [
        ("baku",  "Baku"),
        ("ganja",  "Ganja"),
        ("sumgait",  "Sumgait"),
        ("agsu",  "Agsu"),
        ("shamakhi",  "Shamakhi"),
        ("salyan",  "Salyan"),
        ("shirvan",  "Shirvan"),
        ("khachmaz",  "Khachmaz"),
        ("shaki",  "Shaki"),
        ("nakhchivan",  "Nakhchivan"),
        ("lankaran",  "Lankaran"),
        ("masalli",  "Masalli")

    ]

    location = models.CharField(max_length=20, choices=LOCATION,  default="agsu", null=True, blank=True)

    def __str__(self):
        return self.location