from django.db import models

# Member
class Member(models.Model):
    user_id = models.CharField(max_length=45, primary_key=True)
    pwd = models.CharField(max_length=45, blank=True)
    name = models.CharField(max_length=45, blank=True)
    email = models.EmailField(max_length=45, null=True)
    phone = models.CharField(max_length=45, blank=True)
    birth = models.DateField(null=True)
    address = models.CharField(max_length=45, blank=True)

    class Agreement(models.IntegerChoices):
        yes = 1             # 동의
        no = 2              # 미동의

    created_at = models.DateField(null=True)
    updated_at = models.DateField(null=True)

    class Report(models.IntegerChoices):
        normal = 0          # 정상
        check = 1           # 확인중
        processing = 2      # 처리완료

    class Delete(models.IntegerChoices):
        normal = 0          # 정상
        deleted = 1         # 삭제됨

    agreement = models.IntegerField(choices=Agreement.choices, default=Agreement.yes)
    report = models.IntegerField(choices=Report.choices, default=Report.normal)
    delete = models.IntegerField(choices=Delete.choices, default=Delete.normal)

    # 내가 만든 테이블 사용
    class Meta:
        db_table = 'member'        # member 테이블 사용
        managed = False             # Django가 이 테이블을 관리하지 않음


# Post
class Post(models.Model):
    postNum = models.AutoField(primary_key=True)
    poster = models.ForeignKey(Member, on_delete=models.CASCADE,db_column='poster')  # ForeignKey로 관계 설정
    title = models.CharField(max_length=45, blank=True)
    contents = models.CharField(max_length=500, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    views = models.IntegerField(default=0)

    class Status(models.IntegerChoices):
        public = 0          # 공개
        nondisclosure = 1   # 비공개

    class Report(models.IntegerChoices):
        normal = 0          # 정상
        check = 1           # 확인중
        processing = 2      # 처리완료

    class Delete(models.IntegerChoices):
        normal = 0          # 정상
        deleted = 1         # 삭제됨

    status = models.IntegerField(choices=Status.choices, default=Status.public)
    report = models.IntegerField(choices=Report.choices, default=Report.normal)
    delete = models.IntegerField(choices=Delete.choices, default=Delete.normal)

    # 내가 만든 테이블 사용
    class Meta:
        db_table = 'post'  # post 테이블 사용
        managed = False     # Django가 이 테이블을 관리하지 않음


# Comment
class Comment(models.Model):
    commenNum = models.AutoField(primary_key=True)
    postNum = models.ForeignKey(Post, on_delete=models.CASCADE,db_column='postNum')  # ForeignKey로 관계 설정
    user_id = models.ForeignKey(Member, on_delete=models.CASCADE,db_column='user_id')  # ForeignKey로 관계 설정
    content = models.CharField(max_length=500, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Status(models.IntegerChoices):
        public = 0          # 공개
        nondisclosure = 1   # 비공개

    class Report(models.IntegerChoices):
        normal = 0          # 정상
        check = 1           # 확인중
        processing = 2      # 처리완료

    class Delete(models.IntegerChoices):
        normal = 0          # 정상
        deleted = 1         # 삭제됨

    status = models.IntegerField(choices=Status.choices, default=Status.public)
    report = models.IntegerField(choices=Report.choices, default=Report.normal)
    delete = models.IntegerField(choices=Delete.choices, default=Delete.normal)

    # 내가 만든 테이블 사용
    class Meta:
        db_table = 'comments'  # comments 테이블 사용
        managed = False        # Django가 이 테이블을 관리하지 않음


# PostLike
class PostLike(models.Model):
    like_id = models.AutoField(primary_key=True)
    postNum = models.ForeignKey(Post, on_delete=models.CASCADE,db_column='postNum')  # ForeignKey로 관계 설정
    user_id = models.ForeignKey(Member, on_delete=models.CASCADE,db_column='user_id')  # ForeignKey로 관계 설정
    created_at = models.DateField(auto_now_add=True)

    # 내가 만든 테이블 사용
    class Meta:
        db_table = 'post_like'  # post_like 테이블 사용
        managed = False         # Django가 이 테이블을 관리하지 않음


# CommentLike
class CommentLike(models.Model):
    like_id = models.AutoField(primary_key=True)
    commentNum = models.ForeignKey(Comment, on_delete=models.CASCADE,db_column='commentNum')  # ForeignKey로 관계 설정
    user_id = models.ForeignKey(Member, on_delete=models.CASCADE,db_column='user_id')  # ForeignKey로 관계 설정
    created_at = models.DateField(auto_now_add=True)

    # 내가 만든 테이블 사용
    class Meta:
        db_table = 'comment_like'  # comment_like 테이블 사용
        managed = False             # Django가 이 테이블을 관리하지 않음


# Attachment
class Attachment(models.Model):
    attachment_id = models.AutoField(primary_key=True)
    posNum = models.ForeignKey(Post, on_delete=models.CASCADE,db_column='postNum')  # ForeignKey로 관계 설정
    file_path = models.CharField(max_length=500, blank=True)
    file_name = models.CharField(max_length=500, blank=True)
    file_size = models.IntegerField()
    updated_at = models.DateField(auto_now=True)

    # 내가 만든 테이블 사용
    class Meta:
        db_table = 'attachments'  # attachments 테이블 사용
        managed = False           # Django가 이 테이블을 관리하지 않음
