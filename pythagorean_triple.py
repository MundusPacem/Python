X = input("Enter the first integer: ")
Y = input("Enter the second integer: ")

#c = sqrt(X**2 + Y**2)
m = 1
n = 0
count = 0

print "\n\tSide A\tSide B\tSide C"
print "\t======\t======\t======"

while True:

    if m == X:
        break

    a = m**2 - n**2
    b = 2*n*m
    c = m**2 +n**2
    
    print "\t%d\t%d\t%d" % (a,b,c)

    m     += 1
    n     += 1
    count += 1

print "\n\tThe number of combinations for max values %d and %d is: %d" \
      % (X,Y,count)



"""
Results
=======
Part B:

Enter the first integer: 100
Enter the second integer: 100

	Side A	Side B	Side C
	======	======	======
	1	0	1
	3	4	5
	5	12	13
	7	24	25
	9	40	41
	11	60	61
	13	84	85
	15	112	113
	17	144	145
	19	180	181
	21	220	221
	23	264	265
	25	312	313
	27	364	365
	29	420	421
	31	480	481
	33	544	545
	35	612	613
	37	684	685
	39	760	761
	41	840	841
	43	924	925
	45	1012	1013
	47	1104	1105
	49	1200	1201
	51	1300	1301
	53	1404	1405
	55	1512	1513
	57	1624	1625
	59	1740	1741
	61	1860	1861
	63	1984	1985
	65	2112	2113
	67	2244	2245
	69	2380	2381
	71	2520	2521
	73	2664	2665
	75	2812	2813
	77	2964	2965
	79	3120	3121
	81	3280	3281
	83	3444	3445
	85	3612	3613
	87	3784	3785
	89	3960	3961
	91	4140	4141
	93	4324	4325
	95	4512	4513
	97	4704	4705
	99	4900	4901
	101	5100	5101
	103	5304	5305
	105	5512	5513
	107	5724	5725
	109	5940	5941
	111	6160	6161
	113	6384	6385
	115	6612	6613
	117	6844	6845
	119	7080	7081
	121	7320	7321
	123	7564	7565
	125	7812	7813
	127	8064	8065
	129	8320	8321
	131	8580	8581
	133	8844	8845
	135	9112	9113
	137	9384	9385
	139	9660	9661
	141	9940	9941
	143	10224	10225
	145	10512	10513
	147	10804	10805
	149	11100	11101
	151	11400	11401
	153	11704	11705
	155	12012	12013
	157	12324	12325
	159	12640	12641
	161	12960	12961
	163	13284	13285
	165	13612	13613
	167	13944	13945
	169	14280	14281
	171	14620	14621
	173	14964	14965
	175	15312	15313
	177	15664	15665
	179	16020	16021
	181	16380	16381
	183	16744	16745
	185	17112	17113
	187	17484	17485
	189	17860	17861
	191	18240	18241
	193	18624	18625
	195	19012	19013
	197	19404	19405

	The number of combinations for max values 100 and 100 is: 99

"""