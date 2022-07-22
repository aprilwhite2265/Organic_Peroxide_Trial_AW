
Organic peroxide Trial
=======================

 This program takes a list of chemicals and their concentrations and determines if the product is an organic peroxide or not.

Introduction
------------
 This program takes a list of chemicals and their concentrations and determines if the product is an organic peroxide or not.

Installation
------------
 *This program requires CIRpy; to install follow the instructions below.

 Install CIRpy using:
 pip install cirpy

 Alternatively, you can manually download the package and install it using the following command:
 tar -xzvf CIRpy-1.0.2.tar.gz
 cd CIRpy-1.0.2
 python setup.py install

Comments
---------

 Step 1: Gather the list of chemicals and their percent.
 Step 2: Convert the each chemical into it's SMILES.
 Step 3: Check for Hydrogen Peroxide and other peroxides and generate a list including their mass, concentration(mass percent), and the number of OO bonds.
 Step 4: Fix and split all of the recently generated lists.
 Step 5: Use the provided formula to find the Oxygen Availability
 Step 6: Create an if/else statement that will determine if the product is an organic peroxide and by what section it was determined.

Questions
----------

Which of the provided formulated products meet the definition Organic Peroxide under CFR 173.128(a)(4)?
  Product 2
Which of the provided formulated products do not meet the definition?
  Product 1,Product 3, Product 4
Which subsection under CFR 173.128(a)(4) was used to determine whether the product meets or does not meet the definition of an Organic Peroxide?
  Product 1:CFR 173.128(a)(4)(i)
  Product 2:CFR 173.128(a)(4)(ii)
  Product 3:CFR 173.128(a)(4)(i)
  Product 4:CFR 173.128(a)(4)(i)

Tests
-----

TEST 1 (Product 1):
Input: water,benzoyl peroxide,glycerin,Palmitic acid,Carbomer
Output: Please insert the percent of water
Input:65
Output: Please insert the percent of benzoyl peroxide
Input:10
Output: Please insert the percent of glycerin
Input:10
Output: Please insert the percent of Palmitic acid
Input:5
Output: Please insert the percent of Carbomer
Input:5
Output: This product is not an Organic Peroxide

TEST 2 (Product 2):
Input: water,Hydrogen peroxide,Stearic acid,Dicumyl peroxide
Output: Please insert the percent of water
Input:45
Output: Please insert the percent of hydrogen peroxide
Input:1.8
Output: Please insert the percent of stearic acid
Input:15
Output: Please insert the percent of Dicumyl peroxide
Input:9
Output: This product is an organic peroxide(49 CFR 173.128(a)(4)(ii))

TEST 3 (Product 3):
Input: sodium percarbonate,Alcohols, C12-15, ethoxylated,hydrogen peroxide
Output: Please resubmit the list or instead of names, try the CAS number
Input: 497-19-8,64-17-5,7722-84-1
Output: Please resubmit the list or instead of names, try the CAS number
Input:497-19-8,7722-84-1
Output: Please insert the percent of 497-19-8
Input:35
Output: Please insert the percent of 7722-84-1
Input:70
Output: This product is not an Organic peroxides
**NOTE Alcohols, C12-15, ethoxylated is not in the CIRpy database***

TEST 4 (Product 4):
Input: ethanol,hydrogen peroxide,Glycerin,water
Output: Please insert the percent of ethanol
Input:80
Output: Please insert the percent of hydrogen peroxide
Input:1
Output: Please insert the percent of Glycerin
Input:2
Output: Please insert the percent of water:
Input:18
Output: This product is not an Organic peroxide
