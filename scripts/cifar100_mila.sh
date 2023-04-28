#!/bin/bash

#SBATCH --time=5:00:00
#SBATCH --job-name=fact
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=12
#SBATCH --gres=gpu:1
#SBATCH --mem=32G

rsync -a $HOME/cl-fsl/ $SLURM_TMPDIR/cl-fsl --exclude=env_cfsl

cd $SLURM_TMPDIR/cl-fsl

cd data/
tar -xf cifar-100-python.tar.gz
cd ..

python train.py project/fact_dataset@_global_=cifar100 seed=1 wandb_run_name=cifar &\
python train.py project/fact_dataset@_global_=cifar100 seed=2 wandb_run_name=cifar &\
python train.py project/fact_dataset@_global_=cifar100 seed=3 wandb_run_name=cifar

a="cifar100"_$(date +%F_%H-%M-%S)
mkdir $HOME/$a
cp -r $SLURM_TMPDIR/cl-fsl/checkpoint $HOME/$a
cp -r $SLURM_TMPDIR/cl-fsl/wandb $HOME/$a
cp -r $SLURM_TMPDIR/cl-fsl/local_exp $HOME/$a