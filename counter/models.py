from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
import uuid


class Production(models.Model):
    """生産形式のモデル"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
    title = models.CharField(max_length=100, blank=False, verbose_name="生産形式")
    work_date = models.DateField(blank=False, verbose_name="作業日")
    planned_quantity = models.IntegerField(blank=False, validators=[MinValueValidator(1)], verbose_name="計画数") # 1以上であることを保証
    cycle_time = models.IntegerField(blank=False, validators=[MinValueValidator(1)], verbose_name="サイクルタイム(s)") # 1以上であることを保証する
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日")
    edited_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="編集者")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "生産形式"
        verbose_name_plural = "生産形式"
        ordering = ["work_date"] # デフォルトで作業日順にソート