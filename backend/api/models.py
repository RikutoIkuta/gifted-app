from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings


def upload_avatar_path(instance, filename):
    ext = filename.split('.')[-1]
    return '/'.join(['avatars', str(instance.userProfile.id)+str(instance.nickName)+str(".")+str(ext)])


def upload_post_path(instance, filename):
    ext = filename.split('.')[-1]
    return '/'.join(['posts', str(instance.userPost.id)+str(instance.title)+str(".")+str(ext)])


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Emailの登録は必須です。")
        # emailを正規化(大文字を全部小文字化)
        user = self.model(email=self.normalize_email(email))
        # passwordをハッシュ化
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        # 下記処理の詳細は「.memo」に記載
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return


class User(AbstractBaseUser, PermissionsMixin):
    # unique登録するemailがIDの役割をするため、重複するEmailは許可しない)
    email = models.EmailField("メールアドレス", max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email


class Tag(models.Model):
    tag_name = models.CharField(max_length=40)
    tag_image = models.ImageField(
        blank=True, null=True, upload_to=upload_post_path)


class Vote(models.Model):
    vote_flag = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    nickName = models.CharField(max_length=20)
    userProfile = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='userProfile',
        on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(blank=True, null=True,
                            upload_to=upload_avatar_path)

    def __str__(self):
        return self.nickName


class Post(models.Model):
    title = models.CharField(max_length=100)
    userPost = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='userPost',
        on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(blank=True, null=True, upload_to=upload_post_path)
    liked = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='liked', blank=True)

    def __str__(self):
        return self.title
