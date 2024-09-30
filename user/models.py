from django.contrib.auth.models import AbstractUser
from django.db import models


# 自定義的 User 模型，繼承自 AbstractUser
class User(AbstractUser):
    email = models.EmailField(unique=True)  # 強制唯一的 email
    bio = models.TextField(null=True)  # 個人簡介欄位（可選）

    # XXX 以下設定主要避免發生權限衝突，讀者可以自行參考，不需要完全理解
    # 設置不同的 related_name 來避免與 Django 預設模型發生衝突
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # 自定義 related_name 避免衝突
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',  # 自定義 related_name 避免衝突
        blank=True,
    )
    avatar = models.ImageField(upload_to='avatars/', null=True)

    def __str__(self) -> str:
        return self.username
