from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Rank.
class Rank(models.Model):
	TYPE_CHOICES = [
		('Beginner', 'Beginner'),
		('Intermediate', 'Intermediate'),
		('Advanced', 'Advanced'),
		('Expert', 'Expert'),
	]

	SCORE_CHOICES = [
		('A', 'A'),
		('B', 'B'),
		('C', 'C'),
		('D', 'D'),
		('F', 'F'),
		('E', 'E'),
	]

	rank_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
	level = models.IntegerField(default=0)
	description = models.TextField(blank=True, null=True)
	score = models.CharField(max_length=1, choices=SCORE_CHOICES, default=SCORE_CHOICES[-1][0])
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'{self.score} - {self.level} {self.rank_type}'

# Custom User Manager.
class CustomUserManager(BaseUserManager):
	def create_user(self, email, password=None, **extra_fields):
		if not email:
			raise ValueError(_('The Email field must be set.'))
		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password=None, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError(_('Superuser must have is_staff=True.'))
		if extra_fields.get('is_superuser') is not True:
			raise ValueError(_('Superuser must have is_superuser=True.'))

		return self.create_user(email, password, **extra_fields)

# Custom User.
class CustomUser(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(unique=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	rank = models.ForeignKey(to=Rank, on_delete=models.CASCADE, blank=True, null=True)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	date_joined = models.DateTimeField(default=timezone.now)

	objects = CustomUserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name', 'last_name']

	def __str__(self):
		return f'{self.first_name} - {self.rank}'

	class Meta:
		verbose_name = 'User'
		verbose_name_plural = 'Users'