# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Mysql's BinaryFields for Django 1.5

class TinyBlobField(models.Field):
    description = "Tinyblob"
    def db_type(self, connection):
        return 'tinyblob'

class BlobField(models.Field):
    description = "Blob"
    def db_type(self, connection):
        return 'blob'

class MediumBlobField(models.Field):
    description = "Mediumblob"
    def db_type(self, connection):
        return 'mediumblob'

class LongBlobField(models.Field):
    description = "Longblob"
    def db_type(self, connection):
        return 'longblob'

# Database models

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    passhint = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length = 6)
    birthday = models.DateField()
    gender = models.CharField(max_length=1)
    department = models.CharField(max_length=20, null=True)
    position = models.CharField(max_length=10, null=True)
    joindate = models.DateField()
    exitdate = models.DateField(null=True)
    activatedate = models.DateField(null=True)
    activateadmin = models.CharField(max_length = 6, null=True)
    contact1 = models.CharField(max_length=15)
    contact2 = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200, null=True)
    status = models.IntegerField()
    companynumber = models.IntegerField(null=True)
    email = models.CharField(max_length=20, null=True)
    introduce = models.CharField(max_length = 200, null=True)

    #0 - newbie
    #1 - working
    #2 - retired
    class Meta:
        permissions = (
            ("building_register", ""),
            ("building_search_building", ""),
            ("building_search_room", ""),
            ("resident_show", ""),
            ("resident_info", ""),
            ("resident_infofile", ""),
            ("lease_show", ""),
            ("lease_input", ""),
            ("lease_payment", ""),
            ("manage_activate", ""),
            ("manage_accountinfo", ""),
            ("manage_right", ""),
            ("manage_setting", ""),
        )

class ResidentInfo(models.Model):
    buildingName = models.IntegerField()
    manager = models.CharField(max_length=14)
    buildingRoomNumber = models.IntegerField()
    maintenanceFee = models.IntegerField()
    surtax = models.IntegerField()

    residentName = models.CharField(max_length=10)
    leaseNumber = models.IntegerField()
    leaseNumberTotal = models.IntegerField()
    leaseContractPeriod = models.IntegerField()
    #leaseContractPeriodUnit = models.CharField(max_length=4)
    inDate = models.DateField()
    outDate = models.DateField()

    leaseType = models.CharField(max_length=4)
    leaseDeposit = models.IntegerField()
    leasePayWay = models.CharField(max_length=4)
    leasePayDate = models.IntegerField()
    leaseMoney = models.IntegerField()

    checkType = models.IntegerField()
    checkE = models.IntegerField()
    checkG = models.IntegerField(null=True)
    checkW = models.IntegerField(null=True)
    checkHWG = models.IntegerField(null=True)
    checkHG = models.IntegerField(null=True)
    checkHWW = models.IntegerField(null=True)
    checkHW = models.IntegerField(null=True)
    readDate = models.DateField(null=True)
    readContent = models.CharField(max_length=200, null=True)

    agency = models.CharField(max_length=10)
    agencyName = models.CharField(max_length=50)

    checkIn = models.CharField(max_length=1)
    realInDate = models.DateField()
    checkOut = models.CharField(max_length=1)
    realOutDate = models.DateField(null=True)
    outReason = models.CharField(max_length=200, null=True)

    contractorName = models.CharField(max_length=10)
    contractorGender = models.CharField(max_length=1)
    contractorRegNumber = models.CharField(max_length=14)
    contractorContactNumber1 = models.CharField(max_length=13)
    contractorContactNumber2 = models.CharField(max_length=13, blank=True)
    contractorAddress = models.CharField(max_length=150)
    
    realResidentName = models.CharField(max_length=10)
    residentGender = models.CharField(max_length=1)
    residentRegNumber = models.CharField(max_length=14)
    relToContractor = models.CharField(max_length=10)
    residentPeopleNumber = models.IntegerField()
    residentAddress = models.CharField(max_length=150)
    residentContactNumber1 = models.CharField(max_length=13)
    residentContactNumber2 = models.CharField(max_length=13, blank=True)
    residentOfficeName = models.CharField(max_length=20, blank=True)
    residentOfficeLevel = models.CharField(max_length=10, blank=True)
    residentOfficeAddress = models.CharField(max_length=100, blank=True)
    residentOfficeContactNumber = models.CharField(max_length=13, blank=True)
    residentEmail = models.EmailField(max_length=40)
    haveCar = models.CharField(max_length=1)
    carNumber = models.CharField(max_length=15, blank=True)
    parkingFee = models.IntegerField(null=True, blank=True)

    sendMsg = models.CharField(max_length=1)
    itemCheckIn = models.CharField(max_length=1)
    itemCheckOut = models.CharField(max_length=1)
    checkoutWhy = models.CharField(max_length=200, null=True, blank=True)
    checkoutDate = models.DateField(null=True)

    memo = models.TextField(blank=True)

    #def __unicode__(self):
    #    return self.str

    #def __str__(self):
    #    return unicode(self).encode('utf-8')



class BuildingInfo(models.Model):
    number = models.IntegerField(unique=True)
    name = models.CharField(max_length=30)
    type = models.IntegerField()
    remote = models.IntegerField()
    address = models.CharField(max_length=300)
    floorFrom = models.IntegerField()
    floorTo = models.IntegerField()
    numRoom = models.IntegerField()
    numStore = models.IntegerField()
    numParking = models.IntegerField()
    manager = models.CharField(max_length=14)
    managerNumber = models.CharField(max_length=15)
    leaseNumber = models.CharField(max_length=15, null=True)
    guardNumber = models.CharField(max_length=15, null=True)
    facilityNumber = models.CharField(max_length=15, null=True)
    mainNumber = models.CharField(max_length=15, null=True)
    leaseFax = models.CharField(max_length=15, null=True)
    mainFax = models.CharField(max_length=15, null=True)
    bankName = models.CharField(max_length=14, null=True)
    bankAccount = models.CharField(max_length=30, null=True)
    bankAccountHolder = models.CharField(max_length=14, null=True)
    email = models.CharField(max_length=40, null=True)

class BuildingFloor(models.Model):
    building = models.ForeignKey('BuildingInfo')
    floor = models.IntegerField()
    roomNum = models.IntegerField()
    hasStore = models.CharField(max_length=1, blank=True, null=True)
    storeNum = models.IntegerField(blank=True, null=True)
    storeNames = models.CharField(max_length=300, blank=True, null=True)
    hasParking = models.CharField(max_length=1)
    parkingNum = models.IntegerField(blank=True, null=True)

class RoomInfo(models.Model):
    building = models.ForeignKey('BuildingInfo')
    floor = models.ForeignKey('BuildingFloor')
    roomnum = models.IntegerField()
    residentnum = models.IntegerField()
    isOccupied = models.BooleanField()
    nowResident = models.ForeignKey('ResidentInfo', blank=True, null=True)

class ExcelFiles(models.Model):
    type = models.CharField(max_length=11)
    building = models.ForeignKey('BuildingInfo')
    year = models.IntegerField()
    month = models.IntegerField()
    filename = models.CharField(max_length=150)
    uploadDate = models.DateField()

class EachMonthInfo(models.Model):
    building = models.ForeignKey('BuildingInfo')
    resident = models.ForeignKey('ResidentInfo', blank=True, null=True)
    room = models.ForeignKey('RoomInfo')
    year = models.IntegerField()
    month = models.IntegerField()
    isLiving = models.BooleanField(default=False)
    noticeNumber = models.IntegerField()
    leaseMoney = models.IntegerField(blank=True, null=True)
    maintenanceFee = models.IntegerField(blank=True, null=True)
    surtax = models.IntegerField(blank=True, null=True)
    parkingFee = models.IntegerField(blank=True, null=True)
    etcFee = models.IntegerField(blank=True, null=True)
    totalFee = models.IntegerField(blank=True, null=True)
    electricityFee = models.IntegerField(blank=True, null=True)
    waterFee = models.IntegerField(blank=True, null=True)
    gasFee = models.IntegerField(blank=True, null=True)
    changedFee = models.IntegerField(blank=True, null=True)
    inputCheck = models.BooleanField()
    inputDate = models.DateField(blank=True, null=True)
    noticeCheck = models.BooleanField()
    noticeDate = models.DateField(blank=True, null=True)

class EachMonthDetailInfo(models.Model):
    eachMonth = models.ForeignKey('EachMonthInfo')
    year = models.IntegerField()
    month = models.IntegerField()
    modifyNumber = models.IntegerField()
    leaseMoney = models.IntegerField(blank=True, null=True)
    maintenanceFee = models.IntegerField(blank=True, null=True)
    surtax = models.IntegerField(blank=True, null=True)
    parkingFee = models.IntegerField(blank=True, null=True)
    etcFee = models.IntegerField(blank=True, null=True)
    electricityFee = models.IntegerField(blank=True, null=True)
    waterFee = models.IntegerField(blank=True, null=True)
    gasFee = models.IntegerField(blank=True, null=True)
    amountNoPay = models.IntegerField(blank=True, null=True)
    delayFee = models.IntegerField(blank=True, null=True)
    totalFee = models.IntegerField(blank=True, null=True)
    changedFee = models.IntegerField(blank=True, null=True)
    msg = models.TextField()
    changeDate = models.DateField(blank=True, null=True)

class ElectricityInfo(models.Model):
    resident = models.ForeignKey('ResidentInfo')
    building = models.ForeignKey('BuildingInfo')
    year = models.IntegerField()
    month = models.IntegerField()
    readIn = models.IntegerField(blank=True, null=True)
    usePeriod = models.IntegerField(blank=True, null=True)
    readBefore = models.IntegerField(blank=True, null=True)
    readNow = models.IntegerField(blank=True, null=True)
    capacityBefore = models.IntegerField(blank=True, null=True)
    capacityNow = models.IntegerField(blank=True, null=True)
    basicCharge = models.IntegerField(blank=True, null=True)
    useCharge = models.IntegerField(blank=True, null=True)
    vat = models.IntegerField(blank=True, null=True)
    fundE = models.IntegerField(blank=True, null=True)
    tvLicenseFee = models.IntegerField(blank=True, null=True)
    trimmedFee = models.IntegerField(blank=True, null=True)
    totalFee = models.IntegerField(blank=True, null=True)

class GasInfo(models.Model):
    resident = models.ForeignKey('ResidentInfo')
    building = models.ForeignKey('BuildingInfo')
    type = models.IntegerField()
    year = models.IntegerField()
    month = models.IntegerField()
    readIn = models.IntegerField(blank=True, null=True)
    usePeriod = models.IntegerField(blank=True, null=True)
    readBefore = models.IntegerField(null=True, blank=True)
    readNow = models.IntegerField(null=True, blank=True)
    capacityBefore = models.IntegerField(null=True, blank=True)
    capacityNow = models.IntegerField(null=True, blank=True)
    readBeforeHotWater = models.IntegerField(null=True, blank=True) # bela 1,2,3
    readBeforeHeat = models.IntegerField(null=True, blank=True) # bela 1,2,3
    readNowHotWater = models.IntegerField(null=True, blank=True) # bela 1,2,3
    readNowHeat = models.IntegerField(null=True, blank=True) # bela 1,2,3
    capacityBeforeHotWater = models.IntegerField(null=True, blank=True) # bela 1,2,3
    capacityBeforeHeat = models.IntegerField(null=True, blank=True) # bela 1,2,3
    capacityNowHotWater = models.IntegerField(null=True, blank=True) # bela 1,2,3
    capacityNowHeat = models.IntegerField(null = True, blank=True) # bela 1,2,3
    basicCharge = models.IntegerField(blank=True, null=True) 
    useCharge = models.IntegerField(blank=True, null=True)
    vat = models.IntegerField(blank=True, null=True)
    trimmedFee = models.IntegerField(blank=True, null=True)
    totalFee = models.IntegerField(blank=True, null=True)

class WaterInfo(models.Model):
    resident = models.ForeignKey('ResidentInfo')
    building = models.ForeignKey('BuildingInfo')
    year = models.IntegerField()
    month = models.IntegerField()
    readIn = models.IntegerField(blank=True, null=True)
    usePeriod = models.IntegerField(blank=True, null=True)
    readBefore = models.IntegerField(blank=True, null=True)
    readNow = models.IntegerField(blank=True, null=True)
    capacityBefore = models.IntegerField(blank=True, null=True)
    capacityNow = models.IntegerField(blank=True, null=True)
    basicCharge = models.IntegerField(blank=True, null=True)
    waterSupplyCharge = models.IntegerField(blank=True, null=True)
    sewerageCharge = models.IntegerField(blank=True, null=True)
    waterUseCharge = models.IntegerField(blank=True, null=True)
    trimmedFee = models.IntegerField(blank=True, null=True)
    totalFee = models.IntegerField(blank=True, null=True)

class PaymentInfo(models.Model):
    resident = models.ForeignKey('ResidentInfo')
    building = models.ForeignKey('BuildingInfo')
    noticeCheck = models.BooleanField()
    checked = models.BooleanField()
    year = models.IntegerField()
    month = models.IntegerField()
    number = models.IntegerField()
    totalFee = models.IntegerField()
    amountPaySum = models.IntegerField()
    amountPay = models.IntegerField()
    amountNoPay = models.IntegerField()
    delayFee = models.IntegerField()
    payDate = models.DateField(null=True)
    confirmDate = models.DateField(null=True)
    confirmStatus = models.CharField(max_length=1)
    payStatus = models.IntegerField()
    delayNumber = models.IntegerField()
    accumNumber = models.IntegerField()
    payMsg = models.TextField()
    modifyNumber = models.IntegerField()
    class Meta:
        unique_together = ('resident', 'building', 'year', 'month', 'payStatus')

class PaymentModifyInfo(models.Model):
    payment = models.ForeignKey('PaymentInfo')
    modifyNumber = models.IntegerField()
    year = models.IntegerField()
    month = models.IntegerField()
    payStatus = models.IntegerField()
    payDate = models.DateField(null=True)
    delayNumber = models.IntegerField()
    accumNumber = models.IntegerField()
    amountPaySum = models.IntegerField()
    amountPay = models.IntegerField()
    amountNoPay = models.IntegerField()
    delayFee = models.IntegerField()
    confirmDate = models.DateField(null=True)
    modifyTime = models.DateField(null=True)
    modifyMsg = models.TextField()
    class Meta:
        unique_together = ('payment', 'modifyNumber')


class DepartmentList(models.Model):
    name = models.CharField(max_length = 10)

class PositionList(models.Model):
	number = models.IntegerField()
	name = models.CharField(max_length = 10)

# 시스템 : 연체율
class SettingPayment(models.Model):
	building = models.ForeignKey('BuildingInfo')
	month = models.IntegerField()
	delayRate = models.FloatField()

# 시스템 : 공과금 사용기간
class SettingBill(models.Model):
    building = models.ForeignKey('BuildingInfo')
    type = models.CharField(max_length=13)
    month = models.IntegerField()
    startDate = models.DateField()
    endDate = models.DateField()
    noticeDate = models.DateField()

class SystemSettings(models.Model):
    name = models.CharField(max_length = 20)
    value = models.CharField(max_length = 20)

class AcademicCareer(models.Model):
    user = models.ForeignKey(User)
    period = models.CharField(max_length = 40)
    name = models.CharField(max_length = 20)
    location = models.CharField(max_length = 10)
    major = models.CharField(max_length = 20)
    gpa = models.CharField(max_length = 5)
    maxgpa = models.CharField(max_length = 5)
    etc = models.CharField(max_length = 100)


class WorkCareer(models.Model):
    user = models.ForeignKey(User)
    period = models.CharField(max_length = 40)
    name = models.CharField(max_length = 20)
    position = models.CharField(max_length = 20)
    mission = models.CharField(max_length = 100)

# 표준 고지서
class StandardBill(models.Model):
    type = models.IntegerField()
    year = models.IntegerField()
    month = models.IntegerField()
    building = models.ForeignKey('BuildingInfo', null=True, blank=True)
    room = models.ForeignKey('RoomInfo', null=True, blank=True)
    managerName = models.CharField(max_length = 12)
    inputDate = models.DateField(null=True)
    category = models.IntegerField()
    memo = models.TextField()
    status = models.IntegerField()

class LeaveOwner(models.Model):
    resident = models.ForeignKey('ResidentInfo')
    # outReasen, realOutDate 등은 ResidentInfo에 들어가 있음
    deposit = models.IntegerField(default = 0)
    rent = models.IntegerField(default = 0)
    returnMoney = models.IntegerField(default = 0)
    unpaid = models.IntegerField(default = 0)
    unpaidCollected = models.IntegerField(default = 0)
    unpaidAdded = models.IntegerField(default = 0)
    fee = models.IntegerField(default = 0)
    bankName = models.CharField(max_length = 20, default = '')
    accountNumber = models.CharField(max_length = 50, default = '')
    accountHolder = models.CharField(max_length = 20, default = '')

    # 갑지 완료
    isUnpaidDone = models.BooleanField(default = False)
    isFeeDone = models.BooleanField(default = False)
    isOwnerDone = models.BooleanField(default = False)

    # 을지 완료
    isTenantDone = models.BooleanField(default = False)

    # 임차인확인처리
    isConfirmed = models.BooleanField(default = False)

    def content_file_name(instance, filename):
        return '/'.join(['content', str(instance.pk), filename])

    # 정산서 파일
    ownerFile = models.ForeignKey('LeaveFile', null = True, related_name = "owner")
    tenantFile = models.ForeignKey('LeaveFile', null = True, related_name = "tenant")
 
    feeComment = models.TextField(default = '')
    unpaidComment = models.TextField(default = '')

class LeaveFile(models.Model):
    fileName = models.CharField(max_length = 256, null = True)
    file = models.TextField(null = True)
    uploaded = models.DateTimeField(null = True)

class LeaveConfirm(models.Model):
    leaveOwner = models.ForeignKey('LeaveOwner')
    checked = models.BooleanField(default = False)
    adminuser = models.CharField(max_length = 20, null = True)
    adminuserid = models.IntegerField(default = 0)
    date = models.CharField(max_length = 20, null = True)
    desc = models.CharField(max_length = 200, null = True)

# LeaveOwner에 연결된 Table
class LeaveUnpaidItem(models.Model):
    leaveOwner = models.ForeignKey('LeaveOwner')
    checked = models.BooleanField(default = False)
    accumNumber = models.IntegerField(default = 0)
    amount = models.IntegerField(default = 0)
    amountNoPay = models.IntegerField(default = 0)
    amountPay = models.IntegerField(default = 0)
    amountPaySum = models.IntegerField(default = 0)
    confirmDate = models.CharField(max_length = 20, null = True)
    confirmStatus = models.CharField(max_length = 20, null = True)
    delayFee = models.IntegerField(default = 0)
    delayNumber = models.IntegerField(default = 0)
    expectedDate = models.DateTimeField(null = True)
    isThis = models.IntegerField(default = 0)
    leasePayDate = models.IntegerField(default = 0)
    modifyNumber = models.IntegerField(default = 0)
    month = models.IntegerField(default = 0)
    number = models.IntegerField(default = 0)
    payDate = models.CharField(max_length = 20, null = True)
    payDateDay = models.IntegerField(default = 0)
    payMsg = models.CharField(max_length = 20, null = True)
    payStatus = models.IntegerField(default = 0)
    revisiedAmount = models.IntegerField(default = 0)
    totalFee = models.IntegerField(default = 0)
    # 불필요 and python keyword
    #type = model.CharField(max_length = 20, null = True) 
    year = models.IntegerField(default = 0)
    
# LeaveOwner에 연결된 Table
class LeaveUnpaidAddedItem(models.Model):
    leaveOwner = models.ForeignKey('LeaveOwner')
    checked = models.BooleanField(default = False)
    title = models.CharField(max_length = 20, default = '')
    subType = models.CharField(max_length = 20, null=True)
    month = models.IntegerField(null=True)
    year = models.IntegerField(null=True)
    amount = models.IntegerField(default = 0)
    desc = models.TextField(default = '')

# LeaveOwner에 연결된 Table
class LeaveFeeItem(models.Model):
    leaveOwner = models.ForeignKey('LeaveOwner')
    checked = models.BooleanField(default = False)
    title = models.CharField(max_length = 20, default = '')
    subType = models.CharField(max_length = 20, null=True)
    month = models.IntegerField(null=True)
    year = models.IntegerField(null=True)
    amount = models.IntegerField(default = 0)
    desc = models.TextField(default = '')

# LeaveOwner에 연결된 Table
class LeavePayoff(models.Model):
    leaveOwner = models.ForeignKey('LeaveOwner')
    checked = models.BooleanField(default = False)
    title = models.CharField(max_length = 20, default = '')
    subType = models.CharField(max_length = 20, null=True)
    date = models.CharField(max_length = 20, null=True)
    month = models.IntegerField(null=True)
    year = models.IntegerField(null=True)
    amount = models.IntegerField(default = 0)
    desc = models.TextField(default = '')
   
# LeaveOwner에 연결된 Table
class LeaveRead(models.Model):
    leaveOwner = models.ForeignKey('LeaveOwner')
    checked = models.BooleanField(default = False)
    title = models.CharField(max_length = 20, default = '')
    subType = models.CharField(max_length = 20, null=True)
    month = models.IntegerField(null=True)
    year = models.IntegerField(null=True)
    amount = models.IntegerField(default = 0)
    desc = models.TextField(default = '')

