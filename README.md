FP Distal vs Proximal

python3 train_data_epoch.py --epochs 60 --lr 0.0001 --train_data /home/priyanka/nist_data --model mobilenet_v2 

 python3 test_dataset_model.py --pth fingermodel_bal_mobilenet_v2_0.0001_50.pth --model mobilenet_v2 --test_data /home/priyanka/own_data 
