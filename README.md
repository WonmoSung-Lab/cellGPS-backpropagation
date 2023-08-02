# backpropagation-cellGPS
improved speed of the cellGPS algorithm using backpropagation

# main/Backpropagation/Speed Test
main code
- Demo - Topas PET data backprop vs numerical grads.ipynb
  - comparision between two algorithms for one simulated data
- Demo - real PET data backprop vs numerical grads.ipynb
  - comparision between two algorithms for one real data (from nature paper)
- Topas PET data backprop vs numerical grads-hyperparameter tuning.ipynb
  - comparision between two algorithms for about 140 simulated data with different hyperparameter settings
- Topas PET data backprop vs numerical grads.ipynb
  - comparision between two algorithms for about 140 simulated data with one hyperparameter settings

# commons
code for algorithms
- loss.py
  - code for the loss function J(a), for the previous cellGPS algorithm
- lossWithGrad.py
  - code for the backpropagation implementation of the loss function J(a)
- optimizers.py
  - code for the wrapper function, single_cellGPS() for easy use
- utils.py
  - utils
 
# data
data for the testing of the algorithms
- Topas - single cell/raw
  - GT: ground truth, LOR: PET list mode data files genereated with TOPAS
- Comparisons.pkl
  - python pickle file generated in 'Topas PET data backprop vs numerical grads.ipynb' for saving result
- helical_real_PET_data.bin
  - helical real data from the nature paper
