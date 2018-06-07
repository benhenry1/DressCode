from django.contrib import admin
from design.models import (
	Design,
	DesignComment,
	Status,
	StatusComment,
)

# Register your models here.
admin.site.register(Design)
admin.site.register(DesignComment)
admin.site.register(Status)
admin.site.register(StatusComment)