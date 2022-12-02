from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from .validators import CustomUnicodeUsernameValidator

class User(AbstractUser):
    """
    Default custom user model for Hire-Them.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    class Department(models.TextChoices):
        CSE = "CSE", "COMPUTER SCIENCE"
        IT = "IT", "INFORMATION TECHNOLOGY"
        EE = "EE", "ELECTRIC ENGINEERING"
        CE = "CE", "CIVIL ENGINEERING"
        TE = "TE", "TEXTILE ENGINEERING"
        ME = "ME", "MECHANICAL ENGINEERING"
        OT = "OT", "OTHER"

    username_validator =  CustomUnicodeUsernameValidator()
    
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 30 characters or fewer. Letters, digits, no spaces and ./_ character only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    
    name = models.CharField(_("Name of User"), max_length=255)
    
    first_name = None  # type: ignore
    
    last_name = None  # type: ignore
    
    email = models.EmailField(max_length=100, unique=True)
    
    roll_number = models.CharField(
        max_length=10,
        unique=True,
        null=True,
        blank=True)
    
    profile_picture = models.ImageField(
        upload_to="photos/profiles/",
        max_length=255,
        null=True,
        blank=True
    )

    bio = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    
    department = models.CharField(
        max_length=5,
        choices=Department.choices,
        default=Department.CSE,
        blank=True,
        null=True,
    )

    address = models.CharField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name="Your State and Country",
        help_text=(_("Enter your address in format - your state, your country"))
    )
    
    # resume = models.FileField(
    #     upload_to="resumes/pdf/",
    #     blank=True,
    #     null=True,
    #     validators=[validate_file_extension],
    #     help_text=_(
    #         "Requires a ` pdf ` format of your resume."
    #     )
    # )
    
    github = models.CharField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name="Github link",
        help_text=_(
            """

             - Requires a unique link of your github profile.<br>
             - Add link without 'https://'.

            """
        ),
        )

    REQUIRED_FIELDS = [
        "email",
        "name",
    ]

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})