#!/bin/bash

#SBATCH --account=def-gberseth
#SBATCH --time=4:00:00
#SBATCH --job-name=fact
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --gres=gpu:v100l:1
#SBATCH --mem=8G
#SBATCH --array=1-3

rsync -a $HOME/projects/def-gberseth/$USER/cl_fsl_fact/cl-fsl/ $SLURM_TMPDIR/cl-fsl_fact

cd $SLURM_TMPDIR/cl-fsl_fact

source env_clfsl/bin/activate
cd data/
tar -xf cifar-100-python.tar.gz
cd ..

ids=(1 2 5)
dataset_id=${ids[$((SLURM_ARRAY_TASK_ID-1))]}
echo ${dataset_id}

python train_fact.py project@_global_=fact_cifar100_superrandom wandb_log=True seed=1 wandb_run_name=superrandom_fact_${dataset_id} dataset_dir=superrandom_${dataset_id}
# python train.py project/fact_dataset@_global_=cifar100 seed=2 wandb_run_name=cifar &\
# python train.py project/fact_dataset@_global_=cifar100 seed=3 wandb_run_name=cifar

a="cifar100"_$(date +%F_%H-%M-%S)
mkdir $HOME/projects/def-gberseth/$USER/$a
cp -r $SLURM_TMPDIR/cl-fsl/checkpoint $HOME/projects/def-gberseth/$USER/$a
# cp -r $SLURM_TMPDIR/cl-fsl/wandb $HOME/projects/def-gberseth/$USER/$a
# cp -r $SLURM_TMPDIR/cl-fsl/local_exp $HOME/projects/def-gberseth/$USER/$a