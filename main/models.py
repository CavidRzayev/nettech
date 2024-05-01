from django.db import models
# import RPi.GPIO as GPIO
import time

# GPIO.setmode(GPIO.BCM)
sleepTimeShort = 0.2
sleepTimeLong = 0.1

class Rig(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    address = models.TextField(blank=True,null=True)
    create_date = models.DateTimeField(auto_now=True)
    ip = models.CharField(max_length=100,blank=True,null=True)
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return "{} - {}".format(self.name,self.ip)


class Box(models.Model):
    rig = models.ForeignKey(Rig,on_delete=models.CASCADE,related_name="box_rigs")
    name = models.CharField(max_length=100)
    gpio_id = models.IntegerField()
    size = models.CharField(max_length=100)
    status = models.BooleanField()
    reserved = models.BooleanField(blank=True,null=True)

    def __str__(self) -> str:
        return "{} - GPIO pin :{}".format(self.name,self.gpio_id)


class Package(models.Model):
    bar_code = models.CharField(max_length=200,blank=True,null=True)
    box = models.ForeignKey(Box,on_delete=models.CASCADE)
    user_id = models.IntegerField()
    package_id = models.IntegerField()
    status = models.BooleanField()
    date = models.DateTimeField(auto_now=True)
    user_bar_code = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self) -> str:
        return "Date : {} - User_id : {} - Packets_id : {}".format(self.date.date(),self.user_id,self.package_id)


    # def open_box(self):
    #     self.box.gpio_id
    #     GPIO.output(self.box.gpio_id, GPIO.LOW)
    #     time.sleep(sleepTimeShort)
    #     GPIO.output(self.box.gpio_id, GPIO.HIGH)
    #     time.sleep(sleepTimeLong)



