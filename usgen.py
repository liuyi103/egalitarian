from random import *
from time import *
import string
import sys

_metaclass_ = type
class Person:
    def setName(self,name):
        self.name = name
        
    def getName(self):
        return self.name
    
    def setGender(self,gender):
        self.gender = gender
        
    def getGender(self):
        return self.gender
  
    def setBloodType(self,bloodtype):
        self.bloodtype = bloodtype
        
    def getBloodType(self):
        return self.bloodtype
     
    def setPRA(self,pra):
        self.pra = pra
        
    def getPRA(self):
        return self.pra

    def setAge(self,age):
        self.age = age
        
    def getAge(self):
        return self.age
    
    def setProvince(self,province):
        self.province = province

    def getProvince(self):
        return self.province

   # def setTravel(self,travel):
    #    self.travel = travel

    #def getTravel(self):
     #   return self.travel
    
    def setRace(self,race):
        self.race = race

    def getRace(self):
        return self.race
    
    def setWaitYears(self, waityears):
        self.waityears = waityears

    def getWaitYears(self):
        return self.waityears
    
    def setHLA_A1(self,hla_a1):
        self.hla_a1 = hla_a1

    def getHLA_A1(self):
        return self.hla_a1

    def setHLA_A2(self,hla_a2):
        self.hla_a2 = hla_a2

    def getHLA_A2(self):
        return self.hla_a2

    def setHLA_B1(self,hla_b1):
        self.hla_b1 = hla_b1

    def getHLA_B1(self):
        return self.hla_b1

    def setHLA_B2(self,hla_b2):
        self.hla_b2 = hla_b2

    def getHLA_B2(self):
        return self.hla_b2
    
    def setHLA_DR1(self,hla_dr1):
        self.hla_dr1 = hla_dr1

    def getHLA_DR1(self):
        return self.hla_dr1

    def setHLA_DR2(self,hla_dr2):
        self.hla_dr2 = hla_dr2

    def getHLA_DR2(self):
        return self.hla_dr2

    def setA_MM(self,A_MM):
        self.A_MM = A_MM
        
    def getA_MM(self):
        return self.A_MM

    def setB_MM(self,B_MM):
        self.B_MM = B_MM
        
    def getB_MM(self):
        return self.B_MM

    def setDR_MM(self,DR_MM):
        self.DR_MM = DR_MM
        
    def getDR_MM(self):
        return self.DR_MM

    def setScore(self,score):
        self.score = score
        
    def getScore(self):
        return self.score

A = [(1,'A1'),(2,'A2'),(3,'A3'),(4,'A9'),(5,'A10'),(6,'A11'),(7,'A19'),(8,'A23'),(9,'A24'),(10,'A25'),(11,'A26'),(12,'A28'),(13,'A29'),(14,'A30'),
         (15,'A31'),(16,'A32'),(17,'A33'),(18,'A34'),(19,'A36'),(20,'A43'),(21,'A66'),(22,'A68'),(23,'A69'),(24,'A74'),(25,'Ax')]
HLA_A = dict(A)
B = [(1,'B5'),(2,'B7'),(3,'B8'),(4,'B12'),(5,'B13'),(6,'B14'),(7,'B15'),(8,'B16'),
         (9,'B17'),(10,'B18'),(11,'B21'),(12,'B22'),(13,'B27'),(14,'B35'),(15,'B37'),(16,'B38'),(17,'B39'),(18,'B40'),(19,'B41'),(20,'B42'),(21,'B44')
     ,(22,'B45'),(23,'B46'),(24,'B47'),(25,'B48'),(26,'B49'),(27,'B50'),(28,'B51'),(29,'B52'),(30,'B53'),(31,'B54'),(32,'B55'),(33,'B56'),(34,'B57')
     ,(35,'B58'),(36,'B59'),(37,'B60'),(38,'B61'),(39,'B62'),(40,'B63'),(41,'B64'),(42,'B65'),(43,'B67'),(44,'B70'),(45,'B71'),(46,'B72'),(47,'B73')
     ,(48,'B75'),(49,'B76'),(50,'B77'),(51,'Bx')]

HLA_B = dict(B)
DR = [(1,'DR1'),(2,'DR2'),(3,'DR3'),(4,'DR4'),(5,'DR5'),(6,'DR6'),(7,'DR7'),(8,'DR8'),
         (9,'DR9'),(10,'DR10'),(11,'DR11'),(12,'DR12'),(13,'DR13'),(14,'DR14'),(15,'DR15'),(16,'DR16'),(17,'DR17'),(18,'DR18'),(19,'DRx')]

HLA_DR = dict(DR)
HLA_A_pro = []
HLA_B_pro = []
HLA_DR_pro = []
HLA_A_D_pro = []
HLA_B_D_pro = []
HLA_DR_D_pro = []
file_A = file('us\\HLA_A1.txt','r')
file_B = file('us\\HLA_B1.txt','r')
file_DR = file('us\\HLA_DR1.txt','r')
file_A_D = file('us\\HLA_A_D.txt','r')
file_B_D = file('us\\HLA_B_D.txt','r')
file_DR_D = file('us\\HLA_DR_D.txt','r')
for i in range(4):
    HLA_A_pro.append([i+1,file_A.readline().split()])
    HLA_B_pro.append([i+1,file_B.readline().split()])
    HLA_DR_pro.append([i+1,file_DR.readline().split()])

for i in range(3):
    HLA_A_D_pro.append([i+1,file_A_D.readline().split()])
    HLA_B_D_pro.append([i+1,file_B_D.readline().split()])
    HLA_DR_D_pro.append([i+1,file_DR_D.readline().split()])
    
HLA_A_dict = dict(HLA_A_pro)
#print len(HLA_A_dict[4])
HLA_B_dict = dict(HLA_B_pro)
#print len(HLA_B_dict[4])
HLA_DR_dict = dict(HLA_DR_pro)
#print len(HLA_DR_dict[4])

HLA_A_D_dict = dict(HLA_A_D_pro)
#print len(HLA_A_D_dict[3])
HLA_B_D_dict = dict(HLA_B_D_pro)
#print len(HLA_B_D_dict[3])
HLA_DR_D_dict = dict(HLA_DR_D_pro)
#print len(HLA_DR_D_dict[3])

file_CREG= file('us\\CREG.txt','r')
A_CREG = []
B_CREG = []
DR_CREG = []
for i in range(4):
    A_CREG.append(file_CREG.readline().split())
for i in range(5):
    B_CREG.append(file_CREG.readline().split())
for i in range(6):
    DR_CREG.append(file_CREG.readline().split())

#print A_CREG
wait_score = [1.2,2.4,3.6,4.8,6.0]
#patient_file = file('patients.txt','w')
#donor_file = file('donors.txt','w')
#weight_file = file('weight.txt','w')

def generator(number):
    patients = []
    donors = []


    for n in range(number):
        x=generatePatient(patients)
        generateDonor(donors,x[0],x[1])

    score =[]

    immue_DR = ['DR4','DR5','DR6','DR7','A2','A28','B7','B12']
    for i in range(number):
        p_score = []
        for j in range(number):
            if i == j :
                p_score.append(0)
                continue
            else:
                #if (patients[i].getTravel() == False or donors[j].getTravel()==False) and patients[i].getProvince() != donors[j].getProvince():
                   # p_score.append(0)
                if patients[i].getBloodType()=='O' and donors[j].getBloodType()!='O': 
                    p_score.append(0)
                    continue
                elif patients[i].getBloodType()=='A' and (donors[j].getBloodType()=='B' or donors[j].getBloodType()=='AB'):
                    p_score.append(0)
                    continue
                elif patients[i].getBloodType()=='B' and (donors[j].getBloodType()=='A' or donors[j].getBloodType()=='AB'):
                    p_score.append(0)
                    continue
            
                if patients[i].getPRA()=='negative':
                    if patients[i].getAge()==0 and donors[j].getAge() != 1:
                        p_score.append(0)
                        continue
                    elif patients[i].getAge()< donors[j].getAge():
                        p_score.append(0)
                        continue
                
                if (patients[i].getHLA_A1()=='A2' or patients[i].getHLA_A2()=='A2') and (donors[j].getHLA_DR1() == 'DR8' or donors[j].getHLA_DR2() == 'DR8'):
                    p_score.append(0)
                    continue
                
                elif (patients[i].getHLA_A1()=='A3' or patients[i].getHLA_A2()=='A3') and ((donors[j].getHLA_DR1() == 'DR2' or donors[j].getHLA_DR2() == 'DR2')):
                    p_score.append(0)
                    continue
                elif (patients[i].getHLA_A1()=='A24' or patients[i].getHLA_A2()=='A24') and ((donors[j].getHLA_DR1() == 'DR4' or donors[j].getHLA_DR2() == 'DR4')\
                    or (donors[j].getHLA_DR1() == 'DR6' or donors[j].getHLA_DR2() == 'DR6')):
                    p_score.append(0)
                    continue
                elif (patients[i].getHLA_A1()=='A11' or patients[i].getHLA_A2()=='A11') and ((donors[j].getHLA_DR1() == 'DR4' or donors[j].getHLA_DR2() == 'DR4')\
                    or (donors[j].getHLA_DR1() == 'DR5' or donors[j].getHLA_DR2() == 'DR5')or (donors[j].getHLA_DR1() == 'DR8' or donors[j].getHLA_DR2() == 'DR8')):
                    p_score.append(0)
                    continue
                elif (patients[i].getHLA_B1()=='B44' or patients[i].getHLA_B2()=='B44') and ((donors[j].getHLA_DR1() == 'DR1' or donors[j].getHLA_DR2() == 'DR1')\
                    or (donors[j].getHLA_DR1() == 'DR3' or donors[j].getHLA_DR2() == 'DR3')or (donors[j].getHLA_DR1() == 'DR5' or donors[j].getHLA_DR2() == 'DR5')\
                                                                                             or (donors[j].getHLA_DR1() == 'DR6' or donors[j].getHLA_DR2() == 'DR6')):
                    p_score.append(0)
                    continue
                elif (patients[i].getHLA_A1()=='DR1' or patients[i].getHLA_A2()=='DR1') and (donors[j].getHLA_A1() in immue_DR or donors[j].getHLA_A1() in immue_DR\
                    or donors[j].getHLA_B1() in immue_DR or donors[j].getHLA_B2() in immue_DR or donors[j].getHLA_DR1() in immue_DR or donors[j].getHLA_DR2() in immue_DR):
                    p_score.append(0)
                    continue
            
                Ap = [patients[i].getHLA_A1(),patients[i].getHLA_A2()]
                Ad = [donors[j].getHLA_A1(),donors[j].getHLA_A2()]
                if Ap == Ad or Ap == Ad.reverse():
                    patients[i].setA_MM([2,0,0])
                elif Ap[0] == Ad[0]:
                    patients[i].setA_MM([1,0,1])
                    for k in range(len(A_CREG)):
                        if Ap[1] in A_CREG[k] and Ad[1] in A_CREG[k]:
                            patients[i].setA_MM([1,1,0])
                            break
                elif Ap[0] == Ad[1]:
                    patients[i].setA_MM([1,0,1])
                    for k in range(len(A_CREG)):
                        if Ap[1] in A_CREG[k] and Ad[0] in A_CREG[k]:
                            patients[i].setA_MM([1,1,0])
                            break
                elif Ap[1] == Ad[0]:
                    patients[i].setA_MM([1,0,1])
                    for k in range(len(A_CREG)):
                        if Ap[0] in A_CREG[k] and Ad[1] in A_CREG[k]:
                            patients[i].setA_MM([1,1,0])
                            break                   
                elif Ap[1] == Ad[1]:
                    patients[i].setA_MM([1,0,1])
                    for k in range(len(A_CREG)):
                        if Ap[0] in A_CREG[k] and Ad[0] in A_CREG[k]:
                            patients[i].setA_MM([1,1,0])
                            break
                else:
                    patients[i].setA_MM([0,0,2])
                    for k in range(len(A_CREG)):
                        if Ap[0] in A_CREG[k] and Ad[0] in A_CREG[k]:
                            patients[i].setA_MM([0,1,1])
                            break
                    if patients[i].getA_MM()== [0,1,1]:
                        for k in range(len(A_CREG)):
                            if Ap[1] in A_CREG[k] and Ad[1] in A_CREG[k]:
                                patients[i].setA_MM([0,2,0])
                                break
                    for k in range(len(A_CREG)):
                        if Ap[0] in A_CREG[k] and Ad[1] in A_CREG[k]:
                            patients[i].setA_MM([0,1,1])
                            break
                    if patients[i].getA_MM()== [0,1,1]:
                        for k in range(len(A_CREG)):
                            if Ap[1] in A_CREG[k] and Ad[0] in A_CREG[k]:
                                patients[i].setA_MM([0,2,0])
                                break
                    for k in range(len(A_CREG)):
                        if Ap[1] in A_CREG[k] and Ad[0] in A_CREG[k]:
                            patients[i].setA_MM([0,1,1])
                            break
                    if patients[i].getA_MM()== [0,1,1]:
                        for k in range(len(A_CREG)):
                            if Ap[0] in A_CREG[k] and Ad[1] in A_CREG[k]:
                                patients[i].setA_MM([0,2,0])
                                break
                    for k in range(len(A_CREG)):
                        if Ap[1] in A_CREG[k] and Ad[1] in A_CREG[k]:
                            patients[i].setA_MM([0,1,1])
                            break
                    if patients[i].getA_MM()== [0,1,1]:
                        for k in range(len(A_CREG)):
                            if Ap[0] in A_CREG[k] and Ad[0] in A_CREG[k]:
                                patients[i].setA_MM([0,2,0])
                                break

                Bp = [patients[i].getHLA_B1(),patients[i].getHLA_B2()]
                Bd = [donors[j].getHLA_A1(),donors[j].getHLA_B2()]
                if Bp == Bd or Bp == Bd.reverse():
                    patients[i].setB_MM([2,0,0])
                elif Bp[0] == Bd[0]:
                    patients[i].setB_MM([1,0,1])
                    for k in range(len(B_CREG)):
                        if Bp[1] in B_CREG[k] and Bd[1] in B_CREG[k]:
                            patients[i].setB_MM([1,1,0])
                            break
                elif Bp[0] == Bd[1]:
                    patients[i].setB_MM([1,0,1])
                    for k in range(len(B_CREG)):
                        if Bp[1] in B_CREG[k] and Bd[0] in B_CREG[k]:
                            patients[i].setB_MM([1,1,0])
                            break
                elif Bp[1] == Bd[0]:
                    patients[i].setB_MM([1,0,1])
                    for k in range(len(B_CREG)):
                        if Bp[0] in B_CREG[k] and Bd[1] in B_CREG[k]:
                            patients[i].setB_MM([1,1,0])
                            break                   
                elif Bp[1] == Bd[1]:
                    patients[i].setB_MM([1,0,1])
                    for k in range(len(B_CREG)):
                        if Bp[0] in B_CREG[k] and Bd[0] in B_CREG[k]:
                            patients[i].setB_MM([1,1,0])
                            break
                else:
                    patients[i].setB_MM([0,0,2])
                    for k in range(len(B_CREG)):
                        if Bp[0] in B_CREG[k] and Bd[0] in B_CREG[k]:
                            patients[i].setB_MM([0,1,1])
                            break
                    if patients[i].getB_MM()== [0,1,1]:
                        for k in range(len(B_CREG)):
                            if Bp[1] in B_CREG[k] and Bd[1] in B_CREG[k]:
                                patients[i].setB_MM([0,2,0])
                                break
                    for k in range(len(B_CREG)):
                        if Bp[0] in B_CREG[k] and Bd[1] in B_CREG[k]:
                            patients[i].setB_MM([0,1,1])
                            break
                    if patients[i].getB_MM()== [0,1,1]:
                        for k in range(len(B_CREG)):
                            if Bp[1] in B_CREG[k] and Bd[0] in B_CREG[k]:
                                patients[i].setB_MM([0,2,0])
                                break
                    for k in range(len(B_CREG)):
                        if Bp[1] in B_CREG[k] and Bd[0] in B_CREG[k]:
                            patients[i].setB_MM([0,1,1])
                            break
                    if patients[i].getB_MM()== [0,1,1]:
                        for k in range(len(B_CREG)):
                            if Bp[0] in B_CREG[k] and Bd[1] in B_CREG[k]:
                                patients[i].setB_MM([0,2,0])
                                break
                    for k in range(len(B_CREG)):
                        if Bp[1] in B_CREG[k] and Bd[1] in B_CREG[k]:
                            patients[i].setB_MM([0,1,1])
                            break
                    if patients[i].getB_MM()== [0,1,1]:
                        for k in range(len(B_CREG)):
                            if Bp[0] in B_CREG[k] and Bd[0] in B_CREG[k]:
                                patients[i].setB_MM([0,2,0])
                                break

                DRp = [patients[i].getHLA_DR1(),patients[i].getHLA_DR2()]
                DRd = [donors[j].getHLA_A1(),donors[j].getHLA_DR2()]
                if DRp == DRd or DRp == DRd.reverse():
                     patients[i].setDR_MM([2,0,0])
                elif DRp[0] == DRd[0]:
                     patients[i].setDR_MM([1,0,1])
                     for k in range(len(DR_CREG)):
                         if DRp[1] in DR_CREG[k] and DRd[1] in DR_CREG[k]:
                            patients[i].setDR_MM([1,1,0])
                            break
                elif DRp[0] == DRd[1]:
                     patients[i].setDR_MM([1,0,1])
                     for k in range(len(DR_CREG)):
                        if DRp[1] in DR_CREG[k] and DRd[0] in DR_CREG[k]:
                            patients[i].setDR_MM([1,1,0])
                            break
                elif DRp[1] == DRd[0]:
                     patients[i].setDR_MM([1,0,1])
                     for k in range(len(DR_CREG)):
                        if DRp[0] in DR_CREG[k] and DRd[1] in DR_CREG[k]:
                            patients[i].setDR_MM([1,1,0])
                            break                   
                elif DRp[1] == DRd[1]:
                     patients[i].setDR_MM([1,0,1])
                     for k in range(len(DR_CREG)):
                        if DRp[0] in DR_CREG[k] and DRd[0] in DR_CREG[k]:
                            patients[i].setDR_MM([1,1,0])
                            break
                else:
                     patients[i].setDR_MM([0,0,2])
                     for k in range(len(DR_CREG)):
                        if DRp[0] in DR_CREG[k] and DRd[0] in DR_CREG[k]:
                            patients[i].setDR_MM([0,1,1])
                            break
                     if patients[i].getDR_MM()== [0,1,1]:
                        for k in range(len(DR_CREG)):
                            if DRp[1] in DR_CREG[k] and DRd[1] in DR_CREG[k]:
                                patients[i].setDR_MM([0,2,0])
                                break
                     for k in range(len(DR_CREG)):
                        if DRp[0] in DR_CREG[k] and DRd[1] in DR_CREG[k]:
                            patients[i].setDR_MM([0,1,1])
                            break
                     if patients[i].getDR_MM()== [0,1,1]:
                        for k in range(len(DR_CREG)):
                            if DRp[1] in DR_CREG[k] and DRd[0] in DR_CREG[k]:
                                patients[i].setDR_MM([0,2,0])
                                break
                     for k in range(len(DR_CREG)):
                        if DRp[1] in DR_CREG[k] and DRd[0] in DR_CREG[k]:
                            patients[i].setDR_MM([0,1,1])
                            break
                     if patients[i].getDR_MM()== [0,1,1]:
                        for k in range(len(DR_CREG)):
                            if DRp[0] in DR_CREG[k] and DRd[1] in DR_CREG[k]:
                                patients[i].setDR_MM([0,2,0])
                                break
                     for k in range(len(DR_CREG)):
                        if DRp[1] in DR_CREG[k] and DRd[1] in DR_CREG[k]:
                            patients[i].setDR_MM([0,1,1])
                            break
                     if patients[i].getDR_MM()== [0,1,1]:
                       for k in range(len(DR_CREG)):
                            if DRp[0] in DR_CREG[k] and DRd[0] in DR_CREG[k]:
                                patients[i].setDR_MM([0,2,0])
                                break

                A_MM = patients[i].getA_MM()
                B_MM = patients[i].getB_MM()
                DR_MM = patients[i].getDR_MM()
                y = patients[i].getWaitYears()
                if           (A_MM == [2,0,0] and B_MM == [2,0,0] and DR_MM == [2,0,0]):
                         p_score.append(10+ wait_score[y])
                elif        (A_MM == [1,1,0] and B_MM == [2,0,0] and DR_MM == [2,0,0]) or\
                        (A_MM == [0,2,0] and B_MM == [2,0,0] and DR_MM == [2,0,0]) or\
                        (A_MM == [2,0,0] and B_MM == [1,1,0] and DR_MM == [2,0,0]) or\
                        (A_MM == [1,1,0] and B_MM == [1,1,0] and DR_MM == [2,0,0]) or\
                        (A_MM == [0,2,0] and B_MM == [1,1,0] and DR_MM == [2,0,0]) or\
                        (A_MM == [2,0,0] and B_MM == [0,2,0] and DR_MM == [2,0,0]) or\
                        (A_MM == [1,1,0] and B_MM == [0,2,0] and DR_MM == [2,0,0]) or\
                        (A_MM == [0,2,0] and B_MM == [0,2,0] and DR_MM == [2,0,0]) or\
                        (A_MM == [2,0,0] and B_MM == [1,0,1] and DR_MM == [2,0,0]) or\
                        (A_MM == [1,1,0] and B_MM == [1,0,1] and DR_MM == [2,0,0]) or\
                        (A_MM == [0,2,0] and B_MM == [1,0,1] and DR_MM == [2,0,0]):
                      p_score.append(8+ wait_score[y])
                 
                elif        (A_MM == [1,0,1] and B_MM == [2,0,0] and DR_MM == [2,0,0]) or\
                        (A_MM == [0,1,1] and B_MM == [2,0,0] and DR_MM == [2,0,0]) or\
                        (A_MM == [0,0,2] and B_MM == [2,0,0] and DR_MM == [2,0,0]):
                      p_score.append(7+ wait_score[y])
                 
                elif        (A_MM == [1,0,1] and B_MM == [1,1,0] and DR_MM == [2,0,0]) or\
                        (A_MM == [0,1,1] and B_MM == [1,1,0] and DR_MM == [2,0,0]) or\
                        (A_MM == [0,0,2] and B_MM == [1,1,0] and DR_MM == [2,0,0]) or\
                        (A_MM == [1,0,1] and B_MM == [0,2,0] and DR_MM == [2,0,0]) or\
                        (A_MM == [0,1,1] and B_MM == [0,2,0] and DR_MM == [2,0,0]) or\
                        (A_MM == [0,0,2] and B_MM == [0,2,0] and DR_MM == [2,0,0]) or\
                        (A_MM == [2,0,0] and B_MM == [2,0,0] and DR_MM == [1,1,0]) or\
                        (A_MM == [1,1,0] and B_MM == [2,0,0] and DR_MM == [1,1,0]) or\
                        (A_MM == [0,2,0] and B_MM == [2,0,0] and DR_MM == [1,1,0]) or\
                        (A_MM == [1,0,1] and B_MM == [2,0,0] and DR_MM == [1,1,0]) or\
                        (A_MM == [0,1,1] and B_MM == [2,0,0] and DR_MM == [1,1,0]) or\
                        (A_MM == [0,0,2] and B_MM == [2,0,0] and DR_MM == [1,1,0]) or\
                        (A_MM == [2,0,0] and B_MM == [1,1,0] and DR_MM == [1,1,0]) or\
                        (A_MM == [1,1,0] and B_MM == [1,1,0] and DR_MM == [1,1,0]) or\
                        (A_MM == [0,2,0] and B_MM == [1,1,0] and DR_MM == [1,1,0]) or\
                        (A_MM == [1,0,1] and B_MM == [1,1,0] and DR_MM == [1,1,0]) or\
                        (A_MM == [0,1,1] and B_MM == [1,1,0] and DR_MM == [1,1,0]) or\
                        (A_MM == [0,0,2] and B_MM == [1,1,0] and DR_MM == [1,1,0]) or\
                        (A_MM == [2,0,0] and B_MM == [0,2,0] and DR_MM == [1,1,0]) or\
                        (A_MM == [1,1,0] and B_MM == [0,2,0] and DR_MM == [1,1,0]) or\
                        (A_MM == [0,2,0] and B_MM == [0,2,0] and DR_MM == [1,1,0]) or\
                        (A_MM == [1,0,1] and B_MM == [0,2,0] and DR_MM == [1,1,0]) or\
                        (A_MM == [0,1,1] and B_MM == [0,2,0] and DR_MM == [1,1,0]) or\
                        (A_MM == [0,0,2] and B_MM == [0,2,0] and DR_MM == [1,1,0]) or\
                        (A_MM == [2,0,0] and B_MM == [2,0,0] and DR_MM == [0,2,0]) or\
                        (A_MM == [1,1,0] and B_MM == [2,0,0] and DR_MM == [0,2,0]) or\
                        (A_MM == [0,2,0] and B_MM == [2,0,0] and DR_MM == [0,2,0]) or\
                        (A_MM == [1,0,1] and B_MM == [2,0,0] and DR_MM == [0,2,0]) or\
                        (A_MM == [0,1,1] and B_MM == [2,0,0] and DR_MM == [0,2,0]) or\
                        (A_MM == [0,0,2] and B_MM == [2,0,0] and DR_MM == [0,2,0]) or\
                        (A_MM == [2,0,0] and B_MM == [1,1,0] and DR_MM == [0,2,0]) or\
                        (A_MM == [1,1,0] and B_MM == [1,1,0] and DR_MM == [0,2,0]) or\
                        (A_MM == [0,2,0] and B_MM == [1,1,0] and DR_MM == [0,2,0]) or\
                        (A_MM == [1,0,1] and B_MM == [1,1,0] and DR_MM == [0,2,0]) or\
                        (A_MM == [0,1,1] and B_MM == [1,1,0] and DR_MM == [0,2,0]) or\
                        (A_MM == [0,0,2] and B_MM == [1,1,0] and DR_MM == [0,2,0]) or\
                        (A_MM == [2,0,0] and B_MM == [0,2,0] and DR_MM == [0,2,0]) or\
                        (A_MM == [1,1,0] and B_MM == [0,2,0] and DR_MM == [0,2,0]) or\
                        (A_MM == [0,2,0] and B_MM == [0,2,0] and DR_MM == [0,2,0]) or\
                        (A_MM == [1,0,1] and B_MM == [0,2,0] and DR_MM == [0,2,0]) or\
                        (A_MM == [0,1,1] and B_MM == [0,2,0] and DR_MM == [0,2,0]) or\
                        (A_MM == [0,0,2] and B_MM == [0,2,0] and DR_MM == [0,2,0]):
                      p_score.append(6+ wait_score[y])
                 
                elif        (A_MM == [1,0,1] and B_MM == [1,0,1] and DR_MM == [2,0,0]) or\
                        (A_MM == [0,1,1] and B_MM == [1,0,1] and DR_MM == [2,0,0]) or\
                        (A_MM == [2,0,0] and B_MM == [0,1,1] and DR_MM == [2,0,0]) or\
                        (A_MM == [1,1,0] and B_MM == [0,1,1] and DR_MM == [2,0,0]) or\
                        (A_MM == [0,2,0] and B_MM == [0,1,1] and DR_MM == [2,0,0]) or\
                        (A_MM == [1,0,1] and B_MM == [0,1,1] and DR_MM == [2,0,0]) or\
                        (A_MM == [0,1,1] and B_MM == [0,1,1] and DR_MM == [2,0,0]) or\
                        (A_MM == [2,0,0] and B_MM == [0,0,2] and DR_MM == [2,0,0]) or\
                        (A_MM == [1,1,0] and B_MM == [0,0,2] and DR_MM == [2,0,0]) or\
                        (A_MM == [0,2,0] and B_MM == [0,0,2] and DR_MM == [2,0,0]) or\
                        (A_MM == [1,0,1] and B_MM == [0,0,2] and DR_MM == [2,0,0]) or\
                        (A_MM == [0,1,1] and B_MM == [0,0,2] and DR_MM == [2,0,0]) or\
                        (A_MM == [2,0,0] and B_MM == [1,0,1] and DR_MM == [1,1,0]) or\
                        (A_MM == [1,1,0] and B_MM == [1,0,1] and DR_MM == [1,1,0]) or\
                        (A_MM == [0,2,0] and B_MM == [1,0,1] and DR_MM == [1,1,0]) or\
                        (A_MM == [1,0,1] and B_MM == [1,0,1] and DR_MM == [1,1,0]) or\
                        (A_MM == [0,1,1] and B_MM == [1,0,1] and DR_MM == [1,1,0]) or\
                        (A_MM == [2,0,0] and B_MM == [0,1,1] and DR_MM == [1,1,0]) or\
                        (A_MM == [1,1,0] and B_MM == [0,1,1] and DR_MM == [1,1,0]) or\
                        (A_MM == [0,2,0] and B_MM == [0,1,1] and DR_MM == [1,1,0]) or\
                        (A_MM == [1,0,1] and B_MM == [0,1,1] and DR_MM == [1,1,0]) or\
                        (A_MM == [0,1,1] and B_MM == [0,1,1] and DR_MM == [1,1,0]) or\
                        (A_MM == [2,0,0] and B_MM == [0,0,2] and DR_MM == [1,1,0]) or\
                        (A_MM == [1,1,0] and B_MM == [0,0,2] and DR_MM == [1,1,0]) or\
                        (A_MM == [0,2,0] and B_MM == [0,0,2] and DR_MM == [1,1,0]) or\
                        (A_MM == [1,0,1] and B_MM == [0,0,2] and DR_MM == [1,1,0]) or\
                        (A_MM == [0,1,1] and B_MM == [0,0,2] and DR_MM == [1,1,0]) or\
                        (A_MM == [2,0,0] and B_MM == [1,0,1] and DR_MM == [0,2,0]) or\
                        (A_MM == [1,1,0] and B_MM == [1,0,1] and DR_MM == [0,2,0]) or\
                        (A_MM == [0,2,0] and B_MM == [1,0,1] and DR_MM == [0,2,0]) or\
                        (A_MM == [1,0,1] and B_MM == [1,0,1] and DR_MM == [0,2,0]) or\
                        (A_MM == [0,1,1] and B_MM == [1,0,1] and DR_MM == [0,2,0]) or\
                        (A_MM == [2,0,0] and B_MM == [0,1,1] and DR_MM == [0,2,0]) or\
                        (A_MM == [1,1,0] and B_MM == [0,1,1] and DR_MM == [0,2,0]) or\
                        (A_MM == [0,2,0] and B_MM == [0,1,1] and DR_MM == [0,2,0]) or\
                        (A_MM == [1,0,1] and B_MM == [0,1,1] and DR_MM == [0,2,0]) or\
                        (A_MM == [0,1,1] and B_MM == [0,1,1] and DR_MM == [0,2,0]) or\
                        (A_MM == [2,0,0] and B_MM == [0,0,2] and DR_MM == [0,2,0]) or\
                        (A_MM == [1,1,0] and B_MM == [0,0,2] and DR_MM == [0,2,0]) or\
                        (A_MM == [0,2,0] and B_MM == [0,0,2] and DR_MM == [0,2,0]) or\
                        (A_MM == [1,0,1] and B_MM == [0,0,2] and DR_MM == [0,2,0]) or\
                        (A_MM == [0,1,1] and B_MM == [0,0,2] and DR_MM == [0,2,0]) or\
                        (A_MM == [2,0,0] and B_MM == [2,0,0] and DR_MM == [1,0,1]) or\
                        (A_MM == [1,1,0] and B_MM == [2,0,0] and DR_MM ==[1,0,1]) or\
                        (A_MM == [0,2,0] and B_MM == [2,0,0] and DR_MM ==[1,0,1]) or\
                        (A_MM == [1,0,1] and B_MM == [2,0,0] and DR_MM == [1,0,1]) or\
                        (A_MM == [0,1,1] and B_MM == [2,0,0] and DR_MM ==[1,0,1]) or\
                        (A_MM == [2,0,0] and B_MM == [1,1,0] and DR_MM ==[1,0,1]) or\
                        (A_MM == [1,1,0] and B_MM == [1,1,0] and DR_MM ==[1,0,1]) or\
                        (A_MM == [0,2,0] and B_MM == [1,1,0] and DR_MM ==[1,0,1]) or\
                        (A_MM == [1,0,1] and B_MM == [1,1,0] and DR_MM ==[1,0,1]) or\
                        (A_MM == [0,1,1] and B_MM == [1,1,0] and DR_MM ==[1,0,1]) or\
                        (A_MM == [2,0,0] and B_MM == [0,2,0] and DR_MM ==[1,0,1]) or\
                        (A_MM == [1,1,0] and B_MM == [0,2,0] and DR_MM ==[1,0,1]) or\
                        (A_MM == [0,2,0] and B_MM == [0,2,0] and DR_MM ==[1,0,1]) or\
                        (A_MM == [1,0,1] and B_MM == [0,2,0] and DR_MM == [1,0,1]) or\
                        (A_MM == [0,1,1] and B_MM == [0,2,0] and DR_MM ==[1,0,1]) or\
                        (A_MM == [2,0,0] and B_MM == [1,0,1] and DR_MM ==[1,0,1]) or\
                        (A_MM == [1,1,0] and B_MM == [1,0,1] and DR_MM ==[1,0,1]) or\
                        (A_MM == [0,2,0] and B_MM == [1,0,1] and DR_MM == [1,0,1]) or\
                        (A_MM == [1,0,1] and B_MM == [1,0,1] and DR_MM == [1,0,1]) or\
                        (A_MM == [0,1,1] and B_MM == [1,0,1] and DR_MM == [1,0,1]) or\
                        (A_MM == [2,0,0] and B_MM == [0,1,1] and DR_MM ==[1,0,1]) or\
                        (A_MM == [1,1,0] and B_MM == [0,1,1] and DR_MM ==[1,0,1]) or\
                        (A_MM == [0,2,0] and B_MM == [0,1,1] and DR_MM ==[1,0,1]) or\
                        (A_MM == [1,0,1] and B_MM == [0,1,1] and DR_MM ==[1,0,1]) or\
                        (A_MM == [0,1,1] and B_MM == [0,1,1] and DR_MM ==[1,0,1]) or\
                        (A_MM == [2,0,0] and B_MM == [2,0,0] and DR_MM == [0,1,1]) or\
                        (A_MM == [1,1,0] and B_MM == [2,0,0] and DR_MM ==[0,1,1]) or\
                        (A_MM == [0,2,0] and B_MM == [2,0,0] and DR_MM ==[0,1,1]) or\
                        (A_MM == [1,0,1] and B_MM == [2,0,0] and DR_MM ==[0,1,1]) or\
                        (A_MM == [0,1,1] and B_MM == [2,0,0] and DR_MM ==[0,1,1]) or\
                        (A_MM == [2,0,0] and B_MM == [1,1,0] and DR_MM ==[0,1,1]) or\
                        (A_MM == [1,1,0] and B_MM == [1,1,0] and DR_MM ==[0,1,1]) or\
                        (A_MM == [0,2,0] and B_MM == [1,1,0] and DR_MM ==[0,1,1]) or\
                        (A_MM == [1,0,1] and B_MM == [1,1,0] and DR_MM ==[0,1,1]) or\
                        (A_MM == [0,1,1] and B_MM == [1,1,0] and DR_MM ==[0,1,1]) or\
                        (A_MM == [2,0,0] and B_MM == [0,2,0] and DR_MM ==[0,1,1]) or\
                        (A_MM == [1,1,0] and B_MM == [0,2,0] and DR_MM ==[0,1,1]) or\
                        (A_MM == [0,2,0] and B_MM == [0,2,0] and DR_MM ==[0,1,1]) or\
                        (A_MM == [1,0,1] and B_MM == [0,2,0] and DR_MM ==[0,1,1]) or\
                        (A_MM == [0,1,1] and B_MM == [0,2,0] and DR_MM ==[0,1,1]) or\
                        (A_MM == [2,0,0] and B_MM == [1,0,1] and DR_MM ==[0,1,1]) or\
                        (A_MM == [1,1,0] and B_MM == [1,0,1] and DR_MM ==[0,1,1]) or\
                        (A_MM == [0,2,0] and B_MM == [1,0,1] and DR_MM ==[0,1,1]) or\
                        (A_MM == [1,0,1] and B_MM == [1,0,1] and DR_MM ==[0,1,1]) or\
                        (A_MM == [0,1,1] and B_MM == [1,0,1] and DR_MM == [0,1,1]) or\
                        (A_MM == [2,0,0] and B_MM == [0,1,1] and DR_MM ==[0,1,1]) or\
                        (A_MM == [1,1,0] and B_MM == [0,1,1] and DR_MM ==[0,1,1]) or\
                        (A_MM == [0,2,0] and B_MM == [0,1,1] and DR_MM ==[0,1,1]) or\
                        (A_MM == [1,0,1] and B_MM == [0,1,1] and DR_MM ==[0,1,1]) or\
                        (A_MM == [0,1,1] and B_MM == [0,1,1] and DR_MM ==[0,1,1]) or\
                        (A_MM == [2,0,0] and B_MM == [2,0,0] and DR_MM == [0,0,2]) or\
                        (A_MM == [1,1,0] and B_MM == [2,0,0] and DR_MM == [0,0,2]) or\
                        (A_MM == [0,2,0] and B_MM == [2,0,0] and DR_MM == [0,0,2]) or\
                        (A_MM == [1,0,1] and B_MM == [2,0,0] and DR_MM == [0,0,2]) or\
                        (A_MM == [0,1,1] and B_MM == [2,0,0] and DR_MM == [0,0,2]) or\
                        (A_MM == [2,0,0] and B_MM == [1,1,0] and DR_MM == [0,0,2]) or\
                        (A_MM == [1,1,0] and B_MM == [1,1,0] and DR_MM == [0,0,2]) or\
                        (A_MM == [0,2,0] and B_MM == [1,1,0] and DR_MM == [0,0,2]) or\
                        (A_MM == [1,0,1] and B_MM == [1,1,0] and DR_MM == [0,0,2]) or\
                        (A_MM == [0,1,1] and B_MM == [1,1,0] and DR_MM == [0,0,2]) or\
                        (A_MM == [2,0,0] and B_MM == [0,2,0] and DR_MM == [0,0,2]) or\
                        (A_MM == [1,1,0] and B_MM == [0,2,0] and DR_MM == [0,0,2]) or\
                        (A_MM == [0,2,0] and B_MM == [0,2,0] and DR_MM == [0,0,2]) or\
                        (A_MM == [1,0,1] and B_MM == [0,2,0] and DR_MM == [0,0,2]) or\
                        (A_MM == [0,1,1] and B_MM == [0,2,0] and DR_MM == [0,0,2]):
                      p_score.append(3+ wait_score[y])
                else:
                      p_score.append(0)
        
        score.append(p_score)
        
    #weight_file.write(str(score))
    return score

    

def generatePatient(patients):
    pa = Person()
    pa.setName('patient')

    pa.setWaitYears(int(random()/2*10))
    if random()*100 < 59.65 :
        pa.setGender('male')
    else:
        pa.setGender('female')
        
    a = random()*100 
    if a <52.28:
        pa.setBloodType('O')
    elif 52.28 <= a and a < 81.1:
        pa.setBloodType('A')
    elif 81.1 <= a and a < 97.22:
        pa.setBloodType('B')
    else:
        pa.setBloodType('AB')

    b = random()*100 
    if b <0.89:
        pa.setAge(0)
    elif 0.89 <= b and b < 10.46:
        pa.setAge(1)
    elif 10.46 <= b and b < 35.95:
        pa.setAge(2)
    elif 35.95 <= b and b < 78.98:
        pa.setAge(3)
    else:
        pa.setAge(4)
        
    c = random()*100
    if c <63:
        pa.setPRA('negative')
    elif 63 <= c and c < 86:
        pa.setPRA('low')
    else:
        pa.setPRA('high')

    d = random()*100
    if d <5.59:
        pa.setProvince(1)
    elif 5.59 <= d and d < 18.33:
        pa.setProvince(2)
    elif 18.33 <= d and d < 28.73:
        pa.setProvince(3)
    elif 28.73 <= d and d < 35.77:
        pa.setProvince(4)
    elif 35.77 <= d and d < 50.95:
        pa.setProvince(5)
    elif 50.95 <= d and d < 54.7:
        pa.setProvince(6)
    elif 54.7 <= d and d < 68.28:
        pa.setProvince(7)
    elif 68.28 <= d and d < 73.87:
        pa.setProvince(8)
    elif 73.87 <= d and d < 81.58:
        pa.setProvince(9)
    elif 81.58 <= d and d< 92.18:
        pa.setProvince(11)
    else: 
        pa.setProvince(11)

    #m = random()
    #if m <= 0.5:
     #   pa.setTravel(True)
    #else:
     #   pa.setTravel(False)

    p = random()*100
    if p <= 37.07:
        pa.setRace(0)
    elif 37.07 <p and p <= 71.19:
        pa.setRace(1)
    elif 71.19 <p and p <= 90.65:
        pa.setRace(2)
    elif 90.65 <p and p <= 98.13:
        pa.setRace(3)
    elif 98.13 <p and p <= 99.29:
        pa.setRace(4)
    elif 99.29 <p and p <= 99.84:
        pa.setRace(5)
    else:
        pa.setRace(6)

    ra = pa.getRace()
    if ra == 0 or ra == 2:
        gene = 2
        e = random()*20795
        f = random()*19939
        g = random()*19661
        h = random()*20795
        k = random()*19939
        l = random()*19661
    elif ra == 1 or ra ==4:
        gene = 1
        e = random()*19948
        f = random()*19960
        g = random()*19747
        h = random()*19948
        k = random()*19960
        l = random()*19747
    elif ra == 3:
        gene = 4
        e = random()*19964
        f = random()*19977
        g = random()*19484
        h = random()*19964
        k = random()*19977
        l = random()*19484
    else:
        gene = 3
        e = random()*19896
        f = random()*19950
        g = random()*19588
        h = random()*19896
        k = random()*19950
        l = random()*19588
  
    for i in range(len(HLA_A_dict[gene])):
        if e <= string.atof(HLA_A_dict[gene][i]):
            pa.setHLA_A1(HLA_A[i+1])
            break

    for j in range(len(HLA_B_dict[gene])):
        if f <= string.atof(HLA_B_dict[gene][j]):
            pa.setHLA_B1(HLA_B[j+1])
            break

    for j in range(len(HLA_DR_dict[gene])):
        if g <= string.atof(HLA_DR_dict[gene][j]):
            pa.setHLA_DR1(HLA_DR[j+1])
            break
        
    for i in range(len(HLA_A_dict[gene])):
        if h <= string.atof(HLA_A_dict[gene][i]):
            pa.setHLA_A2(HLA_A[i+1])
            break
    
    for j in range(len(HLA_B_dict[gene])):
        if k <= string.atof(HLA_B_dict[gene][j]):
            pa.setHLA_B2(HLA_B[j+1])
            break
        
    for j in range(len(HLA_DR_dict[gene])):
        if l <= string.atof(HLA_DR_dict[gene][j]):
            pa.setHLA_DR2(HLA_DR[j+1])
            break
            
    #patient_file.write(str(pa.getGender()) + ' ' +str(pa.getBloodType())+ ' ' + str(pa.getPRA())+' '+ str(pa.getAge())+ ' '+ str(pa.getProvince())+ ' '\
                     #  +str(pa.getRace())+' '+str(pa.getWaitYears()) + ' '+str(pa.getHLA_A1())+' ' +str(pa.getHLA_A2())+' '+str(pa.getHLA_B1())+' '+str(pa.getHLA_B2())+' '\
                                                      #  +str(pa.getHLA_DR1())+' '+str(pa.getHLA_DR2())+'\n')
    patients.append(pa)
    return [pa.getRace(),pa.getProvince()]


def generateDonor(donors,race,region):
    do = Person()
    do.setName('patient')
    do.setProvince(region)
    m = random()
   # if m <= 0.5:
    #    do.setTravel(True)
    #else:
     #   do.setTravel(False)
        
    if random()*100 < 41.17 :
        do.setGender('male')
    else:
        do.setGender('female')
        
    a = random()*100 
    if a <64.12:
        do.setBloodType('O')
    elif 64.12 <= a and a < 90.99:
        do.setBloodType('A')
    elif 90.99 <= a and a < 98.97:
        do.setBloodType('B')
    else:
        do.setBloodType('AB')

    b = random()*100
    if b <0.04:
        do.setAge(0)
    if b <= 0.04 and b <33.89:
        do.setAge(1)
    elif 33.89 <= b and b < 78.52:
        do.setAge(2)
    elif 78.52 <= b and b < 98.74:
        do.setAge(3)
    else: 
        do.setAge(4)
        
    rac = random()
    if rac <=0.9:
        do.setRace(race)
    else:
        p = random()*100
        if p <= 70.49:
            do.setRace(0)
        elif 70.49 <p and p <= 83.12:
            do.setRace(1)
        elif 83.12 <p and p <= 95.54:
            do.setRace(2)
        elif 95.54 <p and p <= 98.29:
            do.setRace(3)
        elif 98.29 <p and p <= 98.89:
            do.setRace(4)
        elif 98.89 <p and p <= 99.42:
            do.setRace(5)
        elif 99.42 <p and p <= 99.92:
            do.setRace(6)
        else:
            do.setRace(7)
    
    ra = do.getRace()
    if ra == 0 or ra == 2:
        gene = 2
        e = random()*19299
        f = random()*19640
        g = random()*19219
        h = random()*19299
        k = random()*19640
        l = random()*19219
    elif ra == 1 or ra ==4:
        gene = 1
        e = random()*19224
        f = random()*19474
        g = random()*19280
        h = random()*19224
        k = random()*19474
        l = random()*19280
    else:
        gene = 3
        e = random()*19396
        f = random()*19595
        g = random()*19145
        h = random()*19396
        k = random()*19595
        l = random()*19145
        
    for i in range(len(HLA_A_D_dict[gene])):
        if e <= string.atof(HLA_A_D_dict[gene][i]):
            do.setHLA_A1(HLA_A[i+1])
            break
    
    for j in range(len(HLA_B_D_dict[gene])):
        if f <= string.atof(HLA_B_D_dict[gene][j]):
            do.setHLA_B1(HLA_B[j+1])
            break

    for j in range(len(HLA_DR_D_dict[gene])):
        if g <= string.atof(HLA_DR_D_dict[gene][j]):
            do.setHLA_DR1(HLA_DR[j+1])
            break

    for i in range(len(HLA_A_D_dict[gene])):
        if h <= string.atof(HLA_A_D_dict[gene][i]):
            do.setHLA_A2(HLA_A[i+1])
            break
    
    for j in range(len(HLA_B_D_dict[gene])):
        if k <= string.atof(HLA_B_D_dict[gene][j]):
            do.setHLA_B2(HLA_B[j+1])
            break

    for j in range(len(HLA_DR_D_dict[gene])):
        if l <= string.atof(HLA_DR_D_dict[gene][j]):
            do.setHLA_DR2(HLA_DR[j+1])
            break
            
   # donor_file.write(str(do.getGender()) + ' ' +str(do.getBloodType())+ ' ' + str(do.getAge())+ ' '+str(do.getRace()) + ' '+str(do.getHLA_A1())+' '\
                  #     +str(do.getHLA_A2())+' '+str(do.getHLA_B1())+' '+str(do.getHLA_B2())+' '+str(do.getHLA_DR1())+' '+str(do.getHLA_DR2())+'\n')
    donors.append(do)




f=file('output.txt','w')
f.write(str(generator(int(sys.argv[1]))))
f.close()
#patient_file.close()
#donor_file.close()
#weight_file.close()




