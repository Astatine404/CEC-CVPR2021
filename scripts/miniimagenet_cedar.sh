#!/bin/bash

#SBATCH --account=rrg-gberseth
#SBATCH --time=8:00:00
#SBATCH --job-name=fact
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --gres=gpu:v100l:1
#SBATCH --mem=16G

rsync -a $HOME/projects/def-gberseth/$USER/cl-fsl/ $SLURM_TMPDIR/cl-fsl --exclude=env_cfsl

cd $SLURM_TMPDIR/cl-fsl

cd data/
tar -xf miniimagenet.tar
cd ..

python train_fact.py project@_global_=fact_mini_imagenet seed=1 wandb_run_name=miniimagenet_1 #&\
# python train.py project/fact_dataset@_global_=mini_imagenet seed=2 wandb_run_name=miniimagenet &\
# python train.py project/fact_dataset@_global_=mini_imagenet seed=3 wandb_run_name=miniimagenet

a="mini_imagenet"_$(date +%F_%H-%M-%S)
mkdir $HOME/projects/def-gberseth/$USER/$a
cp -r $SLURM_TMPDIR/cl-fsl/checkpoint $HOME/projects/def-gberseth/$USER/$a
# cp -r $SLURM_TMPDIR/cl-fsl/wandb $HOME/projects/def-gberseth/$USER/$a
# cp -r $SLURM_TMPDIR/cl-fsl/local_exp $HOME/projects/def-gberseth/$USER/$a