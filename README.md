# backpropagation-cellGPS
A backpropagation approach to improve the speed of the PEPT-SBSR(cellGPS) algorithm.

---
# Comparision_Helical
Comparision of the previous and current algorithm of reconstruction speed and accuracy with the helical data.

---
# commons
## objFunc.py
The objective function for the PEPT-SBSR algorithm. 
  
## backpropagation.py
Implementing backpropagation to calculate the gradient of the objective function efficiently.
 
## optimizer.py
Wraper for the backpropagation approach of the PEPT-SBSR(cellGPS) algorithm.

---
# data
## Helical_100Bq300s.csv
PET list mode data generated from a simulated Inveon microPET scanner. A single moving point source following a helical trajectory with a radioactivity of 100Bq was recorded for 5 minutes. The helical trajectory had a radius of 2 cm, and had an angular velocity of 6 deg/s.
