import subprocess

conda_path = "~/miniconda3/etc/profile.d/conda.sh"
tempoGAN_path = "/mnt/c/Work/22-04_tempoGAN_2/tensorflow/tempoGAN/tempoGAN.py"

input_file = "/mnt/c/Users/Martin~1/AppData/Local/Temp/houdini_temp/density_low.0016.npz"
model_file = "/mnt/c/Work/22-04_tempoGAN_2/tensorflow/3ddata_gan/test_0000/model_0034.ckpt"

subprocess.run(
    f'wsl bash -c \". {conda_path} && '
    'conda activate tempoGAN && '
    f'python {tempoGAN_path} '
    f'input_file {input_file} model_file {model_file} frame 16\"',
    shell=True
)
