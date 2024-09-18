from django.db import models

from user.models import User


# 文章 (Post) 模型
class Post(models.Model):
    title = models.CharField(max_length=255)  # 文章標題
    content = models.TextField()  # 文章內容
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 關聯到自定義 User 模型
    created_at = models.DateTimeField(auto_now_add=True)  # 發文時間
    updated_at = models.DateTimeField(auto_now=True)  # 更新時間

    def __str__(self) -> str:
        return self.title


# 評論 (Comment) 模型
class Comment(models.Model):
    content = models.TextField()  # 評論內容
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)  # 所屬文章
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 評論者 (關聯到自定義 User 模型)
    created_at = models.DateTimeField(auto_now_add=True)  # 評論時間

    def __str__(self) -> str:
        return f'Comment by {self.author.username} on {self.post.title}'
