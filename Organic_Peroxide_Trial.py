import cirpy

#Gathers Chemicals, percent, and formula#
while True:
	chem_list=input('Please insert the list of chemicals: ')
	p_list=""
	m_formula=""
	chem_list=chem_list.split(',')
	for c in chem_list:
		percent= input("Please insert the percent of "+c+" : ")
		p_list+=percent+","
		formula=cirpy.resolve(c,'smiles')
		m_formula+=str(formula)+','
	m_formula=m_formula.split(',')
	if "None" in m_formula:
		m_formula.remove('None')
		m_formula.remove('')
	p_list=p_list[:-1]
	p_list=p_list.split(',')
	len_chem=len(chem_list)
	len_for=len(m_formula)
	len_for=len_for-1
	if len_for!=len_chem:
		print('Please resubmit the list or instead of names, try the CAS number')
	else:
		break
#checks for peroxides and hydrogen peroxides and makes a list#
OP_list=''
count_oo=''
mass_oo=''
con_oo=''
con_hp='0.0'
i=0
for f in m_formula:
	if "OOC" in f or "COO" in f:
		OP_list+=str(f)+","
		weight=cirpy.resolve(f,'mw')
		mass_oo+=str(weight)+','
		cou=f.count("OO")
		count_oo=str(cou)+','
		con=p_list[i]
		con_oo+=str(con)+','
		i+=1
	elif "OO" in f:
		con=p_list[i]
		con_hp=con_hp.replace("0.0",str(con))
		i+=1
	else:
		i+=1

#Removes last comma and splits list#
if len(OP_list)>=1:
	OP_list=OP_list[:-1]
	mass_oo=mass_oo[:-1]
	count_oo=count_oo[:-1]
	con_oo=con_oo[:-1]
	OP_list=OP_list.split(',')
	count_oo=count_oo.split(',')
	mass_oo=mass_oo.split(',')
	con_oo=con_oo.split(',')
	con_hp=con_hp.split(',')

#Executes formula to solve for Oxygen availability
p1=0.0
cn= len(OP_list)
while cn>0:
	mi=mass_oo[cn-1]
	mi=float(mi)
	ci=con_oo[cn-1]
	ci=float(ci)*.01
	ni=count_oo[cn-1]
	ni=float(ni)
	cn-=1
	p1+=((ni*ci)/mi)
Oa=16*p1


#Determines if the product contains an organic peroxide or not
hydro=con_hp[0]
hydro=float(hydro)
if hydro<=1.0 and Oa>.01:
		print("This product is an organic peroxide(49 CFR 173.128(a)(4)(i))")
elif hydro>1.0 and hydro<7.0 and Oa>.005:
		print("This product is an organic peroxide(49 CFR 173.128(a)(4)(ii))")
else:
	print("This product is not an organic peroxide")
k=input("press Enter to exit")
