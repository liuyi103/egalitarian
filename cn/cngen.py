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

A = [(1,'A1'),(2,'A2'),(3,'A3'),(4,'A9'),(5,'A10'),(6,'A11'),(7,'A28'),(8,'A19'),
         (9,'Ax')]
HLA_A = dict(A)
B = [(1,'B5'),(2,'B7'),(3,'B8'),(4,'B12'),(5,'B13'),(6,'B14'),(7,'B15'),(8,'B16'),
         (9,'B17'),(10,'B18'),(11,'B21'),(12,'B22'),(13,'B27'),(14,'B35'),(15,'B37'),(16,'B40'),(17,'Bx')]

HLA_B = dict(B)
DR = [(1,'DR1'),(2,'DR3'),(3,'DR4'),(4,'DR7'),(5,'DR8'),(6,'DR9'),(7,'DR10'),(8,'DR11'),
         (9,'DR12'),(10,'DR13'),(11,'DR14'),(12,'DR15'),(13,'DR16'),(14,'DRx')]

HLA_DR = dict(DR)
HLA_A_pro = []
HLA_B_pro = []
HLA_DR_pro = []
file_A = file('D:\\newworkspace\\egarlitarian\\cn\\HLA_A.txt','r')
file_B = file('D:\\newworkspace\\egarlitarian\\cn\\HLA_B.txt','r')
file_DR = file('D:\\newworkspace\\egarlitarian\\cn\\HLA_DR.txt','r')
for i in range(10):
    HLA_A_pro.append([i+1,file_A.readline().split()])
    HLA_B_pro.append([i+1,file_B.readline().split()])
    
for j in range(2):
    HLA_DR_pro.append([j+1,file_DR.readline().split()])
    
HLA_A_dict = dict(HLA_A_pro)
HLA_B_dict = dict(HLA_B_pro)
HLA_DR_dict = dict(HLA_DR_pro)

file_CREG= file('D:\\newworkspace\\egarlitarian\\cn\\CREG.txt','r')
A_CREG = []
B_CREG = []
DR_CREG = []
for i in range(1):
    A_CREG.append(file_CREG.readline().split())
for i in range(4):
    B_CREG.append(file_CREG.readline().split())
for i in range(6):
    DR_CREG.append(file_CREG.readline().split())

wait_score = [1.2,2.4,3.6,4.8,6.0]
#patient_file = file('E:\python\patients.txt','w')
#donor_file = file('E:\python\donors.txt','w')
#weight_file = file('E:\python\weight.txt','w')

def generator(number):
    patients = []
    donors = []


    for n in range(number):
        generatePatient(patients)
        generateDonor(donors)

    score =[]

    immue_DR = ['DR4','DR7','A2','A28','B7','B12']
    for i in range(number):
        p_score = []
        for j in range(number):
            if i == j :
                p_score.append(0)
                continue
            else:
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
                elif (patients[i].getHLA_A1()=='A11' or patients[i].getHLA_A2()=='A11') and ((donors[j].getHLA_DR1() == 'DR4' or donors[j].getHLA_DR2() == 'DR4')\
                    or (donors[j].getHLA_DR1() == 'DR8' or donors[j].getHLA_DR2() == 'DR8')):
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
    if random()*100 < 51.27 :
        pa.setGender('male')
    else:
        pa.setGender('female')
        
    a = random()*100 
    if a <40.5:
        pa.setBloodType('O')
    elif 40.5 <= a and a < 73.4:
        pa.setBloodType('A')
    elif 73.4 <= a and a < 92.1:
        pa.setBloodType('B')
    else:
        pa.setBloodType('AB')

    b = random()*100 
    if b <0.9:
        pa.setAge(0)
    elif 0.9 <= b and b < 10.6:
        pa.setAge(1)
    elif 10.6 <= b and b < 36.8:
        pa.setAge(2)
    elif 36.8 <= b and b < 79.8:
        pa.setAge(3)
    else:
        pa.setAge(4)
        
    c = random()*100
    if c <77:
        pa.setPRA('negative')
    elif 77 <= c and c < 94:
        pa.setPRA('low')
    else:
        pa.setPRA('high')

    d = random()*100
    if d <0.65:
        pa.setProvince(1)
    elif 0.65 <= d and d < 4.09:
        pa.setProvince(2)
    elif 4.09 <= d and d < 18.48:
        pa.setProvince(3)
    elif 18.48 <= d and d < 27.65:
        pa.setProvince(4)
    elif 27.65 <= d and d < 29.37:
        pa.setProvince(5)
    elif 29.37 <= d and d < 55.91:
        pa.setProvince(6)
    elif 55.91 <= d and d < 64.09:
        pa.setProvince(7)
    elif 64.09 <= d and d < 81.17:
        pa.setProvince(8)
    elif 81.17 <= d and d < 88.94:
        pa.setProvince(9)
    else: 
        pa.setProvince(10)
    
    e = random()*1000
    for i in range(len(HLA_A_dict[pa.getProvince()])):
        if e <= string.atof(HLA_A_dict[pa.getProvince()][i]):
            pa.setHLA_A1(HLA_A[i+1])
            break
    
    f = random()*1000
    for j in range(len(HLA_B_dict[pa.getProvince()])):
        if f <= string.atof(HLA_B_dict[pa.getProvince()][j]):
            pa.setHLA_B1(HLA_B[j+1])
            break

    g = random()*100
    if pa.getProvince() != 6 and pa.getProvince() != 7:
        for i in range(len(HLA_DR_dict[1])):
            if g <= string.atof(HLA_DR_dict[1][i]):
                pa.setHLA_DR1(HLA_DR[i+1])
                break
    else:
        for i in range(len(HLA_DR_dict[2])):
            if g <= string.atof(HLA_DR_dict[2][i]):
                pa.setHLA_DR1(HLA_DR[i+1])
                break




    h = random()*1000
    for i in range(len(HLA_A_dict[pa.getProvince()])):
        if h <= string.atof(HLA_A_dict[pa.getProvince()][i]):
            pa.setHLA_A2(HLA_A[i+1])
            break
    
    k = random()*1000
    for j in range(len(HLA_B_dict[pa.getProvince()])):
        if k <= string.atof(HLA_B_dict[pa.getProvince()][j]):
            pa.setHLA_B2(HLA_B[j+1])
            break

    l = random()*100
    if pa.getProvince() != 6 and pa.getProvince() != 7:
        for i in range(len(HLA_DR_dict[1])):
            if l <= string.atof(HLA_DR_dict[1][i]):
                pa.setHLA_DR2(HLA_DR[i+1])
                break
    else:
        for i in range(len(HLA_DR_dict[2])):
            if l <= string.atof(HLA_DR_dict[2][i]):
                pa.setHLA_DR2(HLA_DR[i+1])
                break
            
    #patient_file.write(str(pa.getGender()) + ' ' +str(pa.getBloodType())+ ' ' + str(pa.getPRA())+' '+ str(pa.getAge())+ ' '+ str(pa.getProvince())+ ' '\
                      # +str(pa.getWaitYears()) + ' '+str(pa.getHLA_A1())+' ' +str(pa.getHLA_A2())+' '+str(pa.getHLA_B1())+' '+str(pa.getHLA_B2())+' '\
                                                        # +str(pa.getHLA_DR1())+' '+str(pa.getHLA_DR2())+'\n')
    patients.append(pa)


def generateDonor(donors):
    do = Person()
    do.setName('patient')
    
    if random()*100 < 51.27 :
        do.setGender('male')
    else:
        do.setGender('female')
        
    a = random()*100 
    if a <40.5:
        do.setBloodType('O')
    elif 40.5 <= a and a < 73.4:
        do.setBloodType('A')
    elif 73.4 <= a and a < 92.1:
        do.setBloodType('B')
    else:
        do.setBloodType('AB')

    b = random()*100 
    if b <34:
        do.setAge(1)
    elif 34 <= b and b < 78.8:
        do.setAge(2)
    elif 78.8 <= b and b < 98.8:
        do.setAge(3)
    else: 
        do.setAge(4)
        

    d = random()*100
    if d <0.65:
        do.setProvince(1)
    elif 0.65 <= d and d < 4.09:
        do.setProvince(2)
    elif 4.09 <= d and d < 18.48:
        do.setProvince(3)
    elif 18.48 <= d and d < 27.65:
        do.setProvince(4)
    elif 27.65 <= d and d < 29.37:
        do.setProvince(5)
    elif 29.37 <= d and d < 55.91:
        do.setProvince(6)
    elif 55.91 <= d and d < 64.09:
        do.setProvince(7)
    elif 64.09 <= d and d < 81.17:
        do.setProvince(8)
    elif 81.17 <= d and d < 88.94:
        do.setProvince(9)
    else: 
        do.setProvince(10)

    e = random()*1000
    for i in range(len(HLA_A_dict[do.getProvince()])):
        if e <= string.atof(HLA_A_dict[do.getProvince()][i]):
            do.setHLA_A1(HLA_A[i+1])
            break
    
    f = random()*1000
    for j in range(len(HLA_B_dict[do.getProvince()])):
        if f <= string.atof(HLA_B_dict[do.getProvince()][j]):
            do.setHLA_B1(HLA_B[j+1])
            break

    g = random()*100
    if do.getProvince() != 6 and do.getProvince() != 7:
        for i in range(len(HLA_DR_dict[1])):
            if g <= string.atof(HLA_DR_dict[1][i]):
                do.setHLA_DR1(HLA_DR[i+1])
                break
    else:
        for i in range(len(HLA_DR_dict[2])):
            if g <= string.atof(HLA_DR_dict[2][i]):
                do.setHLA_DR1(HLA_DR[i+1])
                break


    h = random()*1000
    for i in range(len(HLA_A_dict[do.getProvince()])):
        if h <= string.atof(HLA_A_dict[do.getProvince()][i]):
            do.setHLA_A2(HLA_A[i+1])
            break
    
    k = random()*1000
    for j in range(len(HLA_B_dict[do.getProvince()])):
        if k <= string.atof(HLA_B_dict[do.getProvince()][j]):
            do.setHLA_B2(HLA_B[j+1])
            break

    l = random()*100
    if do.getProvince() != 6 and do.getProvince() != 7:
        for i in range(len(HLA_DR_dict[1])):
            if l <= string.atof(HLA_DR_dict[1][i]):
                do.setHLA_DR2(HLA_DR[i+1])
                break
    else:
        for i in range(len(HLA_DR_dict[2])):
            if l <= string.atof(HLA_DR_dict[2][i]):
                do.setHLA_DR2(HLA_DR[i+1])
                break
            
    #donor_file.write(str(do.getGender()) + ' ' +str(do.getBloodType())+ ' ' + str(do.getAge())+ ' '+ str(do.getProvince()) + ' '+str(do.getHLA_A1())+' '\
                      # +str(do.getHLA_A2())+' '+str(do.getHLA_B1())+' '+str(do.getHLA_B2())+' '+str(do.getHLA_DR1())+' '+str(do.getHLA_DR2())+'\n')
    donors.append(do)




f=file('output.txt','w')
try:
    f.write(str(generator(int(sys.argv[1]))))
except:
    f.write(str(generator(10)))
f.close()
#patient_file.close()
#donor_file.close()
#weight_file.close()




