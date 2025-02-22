from django.db import models

# one-to-one relationship
# class College(models.Model):
  #  CollegeID = models.IntegerField(primary_key=True)
  #  name = models.CharField(max_length=50)
  #  strength = models.IntegerField()
  #  website = models.URLField()

# class Principal(models.Model):
  #  CollegeID = models.OneToOneField(
  #      College, 
  #      on_delete=models.CASCADE
  #  )
  #  Qualification = models.CharField(max_length=50)
  #  email = models.EmailField(max_length=50)

# one-to-many relationship

# class Subject(models.Model):
  #  Subjectcode = models.IntegerField(primary_key=True)
  #  name = models.CharField(max_length=30)
  #  credits = models.IntegerField()

# class Teacher(models.Model):
  #  TeacherID = models.IntegerField(primary_key=True)
  #  subjectcode = models.ForeignKey(
  #      Subject,
  #      on_delete=models.CASCADE
  #   )
  #  Qualification = models.CharField(max_length=50)
  #  email = models.EmailField(max_length=50)

# many-to-many relationship

# class Teacher(models.Model):
  #  TeacherID = models.IntegerField(primary_key=True)
  #  Qualification = models.CharField(max_length=50)
  #  email = models.EmailField(max_length=50)

# class Subject(models.Model):
  #  Subjectcode = models.IntegerField(primary_key=True)
  #   name= models.CharField(max_length=30)
  #  credits = models.IntegerField()
  #  teacher = models.ManyToManyField(Teacher)

class Menu(models.Model):
    name = models.CharField(max_length = 100)
    cuisine = models.CharField(max_length = 100)
    price = models.IntegerField()

    def __str__(self):
        return self.name + " : " + self.cuisine