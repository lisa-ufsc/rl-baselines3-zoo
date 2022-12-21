
import sys
from rl_zoo3.enjoy import enjoy
from automation_script.automatic_commit import AutomaticCommit

sys.argv = ["python3", "--algo", "tqc", "--env", "AntBulletEnv-v0", "-f", "experiments/exploration/seed_814179323/n_steps_4", "-n", "10000", "--load-best", "--no-render", "--progress"]

seeds = [3372438727, 896053610, 2784473964, 2183673577, 1843725486, 814179323, 2594327367, 3632205932, 3203387808, 2619532351]
steps = [128, 64, 32, 16, 8, 4]
envs  = ["AntBulletEnv-v0", "HopperBulletEnv-v0", "HalfCheetahBulletEnv-v0"]
n = 1000000

commands = []
for seed in seeds:
    for step in steps:
        for env in envs:
            commands.append(["python3", "--algo", "tqc", "--env", env, "-f", f"experiments/exploration/seed_{seed}/n_steps_{step}", "--reward-log", f"experiments/exploration/rewards/seed_{seed}/n_steps_{step}/tqc/{env}", "-n", str(n), "--load-best", "--no-render"])

[print(command) for command in commands]

if __name__ == "__main__": 
    for command in commands:
        sys.argv = command[:]
        try:
            enjoy()
            AutomaticCommit(" ".join(command)).update()
        except KeyboardInterrupt as e:
            print(e)
            break
        except:
            print("Algum erro ocorreu!")


import os
pasta = './experiments/exploration/rewards'
for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in arquivos:
        os.rename(os.path.join(diretorio, arquivo), os.path.join(diretorio, "monitor.csv"))
