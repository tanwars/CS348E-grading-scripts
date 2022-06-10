#!/bin/bash

# mkdir $1
# cp ../../../../Downloads/$1* ./$1

cd ./$1
# unzip $1*

my_data='com_z = jumper.calc_com_whole_body(draw=False)[2]\n        com_vel_z = jumper.calc_com_lin_vel_whole_body()[2]\n        com_vel_z_sq = com_vel_z ** 2 if com_vel_z > 0 else -com_vel_z ** 2\n        print("objective value", -100 * (com_vel_z_sq \/ GRAVITY \/ 2.0 + com_z))\n        time.sleep(0.2)'
sed -i "s/time.sleep(0.2).*/${my_data}/" optimize_jumping_inv.py
sed -i "s/time.sleep(0.2).*/${my_data}/" optimize_jumping_inv_dc.py

cp ../tester.py .
cat optimize_jumping_inv.py tester.py > test_task3.py
cat optimize_jumping_inv_dc.py tester.py > test_task4.py

echo "********************************************************************"
echo "********************************************************************"
echo "\n"
echo "\n"

python humanoid_jumper_inv.py 

echo "********************************************************************"
echo "********************************************************************"
echo "\n"
echo "\n"

# python test_task3.py 1st_trial visualize
python test_task3.py test_trial

echo "********************************************************************"
echo "********************************************************************"
echo "\n"
echo "\n"

# python test_task4.py 1st_trial_dc visualize
python test_task4.py test_trial_dc

echo "********************************************************************"
echo "********************************************************************"