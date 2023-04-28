#!/bin/bash

#SBATCH --account=def-gberseth
#SBATCH --time=4:00:00
#SBATCH --job-name=fact
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --gres=gpu:v100l:1
#SBATCH --mem=8G
#SBATCH --array=1-3

rsync -a $HOME/projects/def-gberseth/$USER/CEC-CVPR2021/ $SLURM_TMPDIR/CEC-CVPR2021

cd $SLURM_TMPDIR/CEC-CVPR2021

source env_clfsl/bin/activate
cd data/
tar -xf cifar-100-python.tar.gz
cd ..

seeds=(1 2 5)
seed=${seeds[$((SLURM_ARRAY_TASK_ID-1))]}
echo ${seed}

export WANDB_API_KEY=46d9db79775e2a53e112833075a6bc7a85207c17

# python train_fact.py project@_global_=fact_cifar100 wandb_log=True seed=${seed} wandb_run_name=base_fact_${seed} #&\
# python train.py project/fact_dataset@_global_=cifar100 seed=2 wandb_run_name=cifar &\
# python train.py project/fact_dataset@_global_=cifar100 seed=3 wandb_run_name=cifar
python train.py -project cec -dataset cifar100 -seed ${seed} -wandb_log True -wandb_run_name base_cec_${seed} \
-epochs_base 100 -lr_base 0.002 -lrg 0.0002 -step 20 -gamma 0.5 -gpu 0 -set_no_val \
-model_dir checkpoint/cifar100/base/ft_cos-avg_cos-data_init-start_0/default/session0_max_acc.pth

# a="cifar100"_$(date +%F_%H-%M-%S)
# mkdir $HOME/projects/def-gberseth/$USER/$a
# cp -r $SLURM_TMPDIR/cl-fsl/checkpoint $HOME/projects/def-gberseth/$USER/$a
# cp -r $SLURM_TMPDIR/cl-fsl/wandb $HOME/projects/def-gberseth/$USER/$a
# cp -r $SLURM_TMPDIR/cl-fsl/local_exp $HOME/projects/def-gberseth/$USER/$a