#!/bin/bash

#SBATCH --account=rrg-gberseth
#SBATCH --time=2:00:00
#SBATCH --job-name=fact
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --gres=gpu:v100l:1
#SBATCH --mem=4G
#SBATCH --array=1-30

targets=('troglitazone_rediscovery' 'isomers_c9h10n2o2pf2cl' 'sitagliptin_mpo' 'median2' 'valsartan_smarts' 'scaffold_hop')

seeds=(1 2 3 4 5)

s=${seeds[$(((SLURM_ARRAY_TASK_ID-1) % 5))]}
echo ${s}

t=${targets[$(((SLURM_ARRAY_TASK_ID-1) / 5))]}
echo ${t}

rsync -a $HOME/projects/def-gberseth/$USER/molecular-rl/ $SLURM_TMPDIR/molecular-rl --exclude=env_lm
echo "moved code to slurm tmpdir"

cd $SLURM_TMPDIR/molecular-rl

python train_our_agent.py oracle=${t} seed=${s} prior_path='saved/nbf/10_1.pt' wandb_log=True wandb_run_name='reinfogced_nbf1_'${s}